from django.shortcuts import render, redirect, get_object_or_404
from api.models import Serial, Category, Article
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from user.models import Profile
from .models import SerialRating, SerialWatchlist
from django.db.models import Avg, Func, Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


def list(request):
    serial_list = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True))
    categories = Category.objects.all()
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    page = request.GET.get('page')
    year = request.GET.get('year')
    category = request.GET.get('category')

    if year:
        serial_list = serial_list.filter(
            Q(year__icontains=year)
            )
    if category:
        serial_list = serial_list.filter(
            Q(category__name__icontains=category)
            )

    paginator = Paginator(serial_list, per_page=10)
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
        activ_profile = get_object_or_404(Profile, user=activ_user)

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
            's_id': s_id,
            'serials': serials,
            'serialrating': serialrating,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
            'categories': categories,
            'latest_article': latest_article,
        }
        return render(request, 'serial/list.html', context)
    else:
        context = {
            'serials': serials,
            'categories': categories,
            'latest_article': latest_article,
        }
        return render(request, 'serial/list.html', context)


def detail(request, pk):
    serial = get_object_or_404(Serial, pk=pk)
    current_serial = Serial.objects.filter(id=serial.id).annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True),
        inwatchlist=Count('serialwatchlist__user', distinct=True))
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    if request.user.is_authenticated():
        add_serial_id = request.GET.get('add_serial_id', None)
        del_serial_id = request.GET.get('del_serial_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist = request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)
        if request.method == 'GET':
            if add_serial_id is not None and rate is not None:
                if SerialRating.objects.filter(user=activ_user, serial=serial).exists():
                    SerialRating.objects.filter(user=activ_user, serial=serial).update(rate=rate)
                else:
                    SerialRating.objects.create(user=activ_user, serial=serial, rate=rate)

            if del_serial_id is not None and rate is not None:
                SerialRating.objects.filter(user=activ_user, serial=serial, rate=rate).delete()

            if add_watchlist is not None:
                if SerialWatchlist.objects.filter(user=activ_user, serial=serial).exists():
                    SerialWatchlist.objects.filter(user=activ_user, serial=serial).update()
                else:
                    SerialWatchlist.objects.create(user=activ_user, serial=serial)

            if del_watchlist is not None:
                serial = get_object_or_404(Serial, id=del_watchlist)
                SerialWatchlist.objects.filter(user=activ_user, serial=serial).delete()

        rating = SerialRating.objects.filter(user=activ_user, serial=serial)
        watchlist = SerialWatchlist.objects.filter(serial=serial, user=activ_user).first()

        context = {
            'serial': serial,
            'rating': rating,
            'current_serial': current_serial,
            'watchlist': watchlist,
            'latest_article': latest_article,
        }
    else:
        context = {
            'serial': serial,
            'current_serial': current_serial,
            'latest_article': latest_article,
        }
    return render(request, 'serial/detail.html', context)


def top_rated(request):
    serial_list = Serial.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0),
        votes=Count('serialrating__user', distinct=True))
    categories = Category.objects.all()
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    page = request.GET.get('page')
    year = request.GET.get('year')
    category = request.GET.get('category')

    if year:
        serial_list = serial_list.filter(
            Q(year__icontains=year)
            )
    if category:
        serial_list = serial_list.filter(
            Q(category__name__icontains=category)
            )

    serial_list = serial_list.order_by('-average_score')[:100]

    paginator = Paginator(serial_list, per_page=100)
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
        activ_profile = get_object_or_404(Profile, user=activ_user)

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
            's_id': s_id,
            'serials': serials,
            'serialrating': serialrating,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
            'latest_article': latest_article,
            'categories': categories,
        }
        return render(request, 'serial/top_rated.html', context)
    else:
        context = {
            'serials': serials,
            'latest_article': latest_article,
            'categories': categories,
        }
        return render(request, 'serial/top_rated.html', context)
