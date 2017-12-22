from itertools import chain
from operator import attrgetter
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Coalesce
from django.db.models import Avg, Func, Count, Q
from django.contrib.auth.models import User
from api.models import Film, Serial
from serials.models import SerialRating, SerialWatchlist
from films.models import FilmRating, FilmWatchlist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


def list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()

    result_list = sorted(
        chain(films, serials),
        key=attrgetter('title'))

    result_list_c = films_c + serials_c

    paginator = Paginator(result_list, per_page=10)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator(paginator.num_pages)

    if request.user.is_authenticated():
        add_film_id = request.GET.get('add_film_id', None)
        del_film_id = request.GET.get('del_film_id', None)
        add_film_watchlist = request.GET.get('add_film_watchlist', None)
        del_film_watchlist = request.GET.get('del_film_watchlist', None)
        add_serial_id = request.GET.get('add_serial_id', None)
        del_serial_id = request.GET.get('del_serial_id', None)
        add_serial_watchlist = request.GET.get('add_serial_watchlist', None)
        del_serial_watchlist = request.GET.get('del_serial_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)

        if request.method == 'GET':
            if add_film_id is not None and rate is not None:
                film = get_object_or_404(Film, id=add_film_id)
                if FilmRating.objects.filter(user=activ_user, film=film).exists():
                    FilmRating.objects.filter(user=activ_user, film=film).update(rate=rate)
                else:
                    FilmRating.objects.create(user=activ_user, film=film, rate=rate)

            if del_film_id is not None and rate is not None:
                film = get_object_or_404(Film, id=del_film_id)
                FilmRating.objects.filter(user=activ_user, film=film, rate=rate).delete()

            if add_film_watchlist is not None:
                film = get_object_or_404(Film, id=add_film_watchlist)
                if FilmWatchlist.objects.filter(user=activ_user, film=film).exists():
                    FilmWatchlist.objects.filter(user=activ_user, film=film).update()
                else:
                    FilmWatchlist.objects.create(user=activ_user, film=film)

            if del_film_watchlist is not None:
                film = get_object_or_404(Film, id=del_film_watchlist)
                FilmWatchlist.objects.filter(user=activ_user, film=film).delete()

            if add_serial_id is not None and rate is not None:
                serial = get_object_or_404(Serial, id=add_serial_id)
                if SerialRating.objects.filter(user=activ_user, serial=serial).exists():
                    SerialRating.objects.filter(user=activ_user, serial=serial).update(rate=rate)
                else:
                    SerialRating.objects.create(user=activ_user, serial=serial, rate=rate)

            if del_serial_id is not None and rate is not None:
                serial = get_object_or_404(Serial, id=del_serial_id)
                SerialRating.objects.filter(user=activ_user, serial=serial, rate=rate).delete()

            if add_serial_watchlist is not None:
                serial = get_object_or_404(Serial, id=add_serial_watchlist)
                if SerialWatchlist.objects.filter(user=activ_user, serial=serial).exists():
                    SerialWatchlist.objects.filter(user=activ_user, serial=serial).update()
                else:
                    SerialWatchlist.objects.create(user=activ_user, serial=serial)

            if del_serial_watchlist is not None:
                serial = get_object_or_404(Serial, id=del_serial_watchlist)
                SerialWatchlist.objects.filter(user=activ_user, serial=serial).delete()

        filmrating = FilmRating.objects.filter(user=activ_user)
        f_id = filmrating.values_list('film__id', flat=True)

        watchlistfilm = FilmWatchlist.objects.filter(user=activ_user)
        watchlist_film_id = watchlistfilm.values_list('film__id', flat=True)

        serialrating = SerialRating.objects.filter(user=activ_user)
        s_id = serialrating.values_list('serial__id', flat=True)

        watchlistserial = SerialWatchlist.objects.filter(user=activ_user)
        watchlist_serial_id = watchlistserial.values_list('serial__id', flat=True)

        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list': result_list,
            'result_list_c': result_list_c,
            'f_id': f_id,
            'watchlist_film_id': watchlist_film_id,
            'filmrating': filmrating,
            's_id': s_id,
            'watchlist_serial_id': watchlist_serial_id,
            'serialrating': serialrating,
        }
    else:
        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list': result_list,
            'result_list_c': result_list_c,
        }
    return render(request, 'list.html', context)


def film_list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()
    result_list_c = films_c + serials_c

    paginator = Paginator(films, per_page=10)
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator(paginator.num_pages)

    if request.user.is_authenticated():
        add_film_id = request.GET.get('add_film_id', None)
        del_film_id = request.GET.get('del_film_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist = request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)

        if request.method == 'GET':
            if add_film_id is not None and rate is not None:
                film = get_object_or_404(Film, id=add_film_id)
                if FilmRating.objects.filter(user=activ_user, film=film).exists():
                    FilmRating.objects.filter(user=activ_user, film=film).update(rate=rate)
                else:
                    FilmRating.objects.create(user=activ_user, film=film, rate=rate)

            if del_film_id is not None and rate is not None:
                film = get_object_or_404(Film, id=del_film_id)
                FilmRating.objects.filter(user=activ_user, film=film, rate=rate).delete()

            if add_watchlist is not None:
                film = get_object_or_404(Film, id=add_watchlist)
                if FilmWatchlist.objects.filter(user=activ_user, film=film).exists():
                    FilmWatchlist.objects.filter(user=activ_user, film=film).update()
                else:
                    FilmWatchlist.objects.create(user=activ_user, film=film)

            if del_watchlist is not None:
                film = get_object_or_404(Film, id=del_watchlist)
                FilmWatchlist.objects.filter(user=activ_user, film=film).delete()

        filmrating = FilmRating.objects.filter(user=activ_user)
        f_id = filmrating.values_list('film__id', flat=True)

        watchlist = FilmWatchlist.objects.filter(user=activ_user)
        watchlist_id = watchlist.values_list('film__id', flat=True)

        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list_c': result_list_c,
            'f_id': f_id,
            'filmrating': filmrating,
            'watchlist_id': watchlist_id,
        }
    else:
        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list_c': result_list_c,
        }

    return render(request, 'film_list.html', context)


def serial_list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()
    result_list_c = films_c + serials_c

    paginator = Paginator(serials, per_page=10)
    try:
        serials = paginator.page(page)
    except PageNotAnInteger:
        serials = paginator.page(1)
    except EmptyPage:
        serials = paginator(paginator.num_pages)

    if request.user.is_authenticated():
        add_serial_id = request.GET.get('add_serial_id', None)
        del_serial_id = request.GET.get('del_serial_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist = request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)

        if request.method == 'GET':
            if add_serial_id is not None and rate is not None:
                serial = get_object_or_404(Serial, id=add_serial_id)
                if SerialRating.objects.filter(user=activ_user, serial=serial).exists():
                    SerialRating.objects.filter(user=activ_user, serial=serial).update(rate=rate)
                else:
                    SerialRating.objects.create(user=activ_user, serial=serial, rate=rate)

            if del_serial_id is not None and rate is not None:
                serial = get_object_or_404(Serial, id=del_serial_id)
                SerialRating.objects.filter(user=activ_user, serial=serial, rate=rate).delete()

            if add_watchlist is not None:
                serial = get_object_or_404(Serial, id=add_watchlist)
                if SerialWatchlist.objects.filter(user=activ_user, serial=serial).exists():
                    SerialWatchlist.objects.filter(user=activ_user, serial=serial).update()
                else:
                    SerialWatchlist.objects.create(user=activ_user, serial=serial)

            if del_watchlist is not None:
                serial = get_object_or_404(Serial, id=del_watchlist)
                SerialWatchlist.objects.filter(user=activ_user, serial=serial).delete()

        serialrating = SerialRating.objects.filter(user=activ_user)
        s_id = serialrating.values_list('serial__id', flat=True)

        watchlist = SerialWatchlist.objects.filter(user=activ_user)
        watchlist_id = watchlist.values_list('serial__id', flat=True)

        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list_c': result_list_c,
            's_id': s_id,
            'serialrating': serialrating,
            'watchlist_id': watchlist_id,
        }
    else:
        context = {
            'serials': serials,
            'films': films,
            'serials_c': serials_c,
            'films_c': films_c,
            'result_list_c': result_list_c,
        }
    return render(request, 'serial_list.html', context)
