from django.shortcuts import render, get_object_or_404
from api.models import Film, Category, Article
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from user.models import Profile
from django.db.models import Avg, Func, Count, Q
from .models import FilmRating, FilmWatchlist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


def list(request):
    film_list = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True))
    categories = Category.objects.all()
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    page = request.GET.get('page')
    year = request.GET.get('year')
    category = request.GET.get('category')

    if year:
        film_list = film_list.filter(
            Q(year__icontains=year)
            )
    if category:
        film_list = film_list.filter(
            Q(category__name__icontains=category)
            )

    paginator = Paginator(film_list, per_page=10)
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
        activ_profile = get_object_or_404(Profile, user=activ_user)

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
            'f_id': f_id,
            'films': films,
            'filmrating': filmrating,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
            'categories': categories,
            'latest_article': latest_article,
        }
        return render(request, 'film/list.html', context)
    else:
        context = {
            'films': films,
            'categories': categories,
            'latest_article': latest_article,
        }
        return render(request, 'film/list.html', context)


def detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    current_film = Film.objects.filter(id=film.id).annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True),
        inwatchlist=Count('filmwatchlist__user', distinct=True))
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    if request.user.is_authenticated():
        add_film_id = request.GET.get('add_film_id', None)
        del_film_id = request.GET.get('del_film_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist = request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)

        if request.method == 'GET':
            if add_film_id is not None and rate is not None:
                if FilmRating.objects.filter(user=activ_user, film=film).exists():
                    FilmRating.objects.filter(user=activ_user, film=film).update(rate=rate)
                else:
                    FilmRating.objects.create(user=activ_user, film=film, rate=rate)

            if del_film_id is not None and rate is not None:
                FilmRating.objects.filter(user=activ_user, film=film, rate=rate).delete()

            if add_watchlist is not None:
                if FilmWatchlist.objects.filter(user=activ_user, film=film).exists():
                    FilmWatchlist.objects.filter(user=activ_user, film=film).update()
                else:
                    FilmWatchlist.objects.create(user=activ_user, film=film)

            if del_watchlist is not None:
                FilmWatchlist.objects.filter(user=activ_user, film=film).delete()

        rating = FilmRating.objects.filter(user=activ_user, film=film)
        watchlist = FilmWatchlist.objects.filter(film=film, user=activ_user).first()

        context = {
            'film': film,
            'rating': rating,
            'current_film': current_film,
            'watchlist': watchlist,
            'latest_article': latest_article,
        }
    else:
        context = {
            'film': film,
            'current_film': current_film,
            'latest_article': latest_article,
        }
    return render(request, 'film/detail.html', context)


def top_rated(request):
    film_list = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0),
        votes=Count('filmrating__user', distinct=True)).filter(votes__gte=10)
    categories = Category.objects.all()
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    page = request.GET.get('page')
    year = request.GET.get('year')
    category = request.GET.get('category')

    if year:
        film_list = film_list.filter(
            Q(year__icontains=year)
            )
    if category:
        film_list = film_list.filter(
            Q(category__name__icontains=category)
            )

    film_list = film_list.order_by('-average_score')[:100]

    paginator = Paginator(film_list, per_page=100)
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
        activ_profile = get_object_or_404(Profile, user=activ_user)

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
            'f_id': f_id,
            'films': films,
            'filmrating': filmrating,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
            'latest_article': latest_article,
            'categories': categories,
        }
        return render(request, 'film/top_rated.html', context)
    else:
        context = {
            'films': films,
            'latest_article': latest_article,
            'categories': categories,
        }
        return render(request, 'film/top_rated.html', context)
