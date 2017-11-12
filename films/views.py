from django.shortcuts import render, redirect, get_object_or_404
from api.models import Film
from django.contrib.auth.models import User
from user.models import Profile
from .models import FilmRating
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def list(request):
    if request.user.is_authenticated():
        add_film_id = request.GET.get('add_film_id', None)
        del_film_id = request.GET.get('del_film_id', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)
        activ_profile = get_object_or_404(Profile, user=activ_user)
        
        if request.method == 'GET' and add_film_id is not None:
            film = get_object_or_404(Film, id=add_film_id)
            activ_profile.film.add(film)

            if FilmRating.objects.filter(user=activ_user, film=film).exists():
                filmuser = FilmRating.objects.filter(user=activ_user, film=film)
                filmuser.update(rate=rate)
            else:
                FilmRating.objects.create(user=activ_user, film=film, rate=rate)

        if request.method == 'GET' and del_film_id is not None:
            film = get_object_or_404(Film, id=del_film_id)
            activ_profile.film.remove(film)
            FilmRating.objects.filter(user=activ_user, film=film, rate=rate).delete()

        p_films = activ_profile.film.all()
        film_list = Film.objects.all().annotate(average_score=Avg('filmrating__rate'))

        filmrating = FilmRating.objects.all().filter(user=activ_user)
        f_title = filmrating.values_list('film__title', flat=True)
        f_id = filmrating.values_list('film__id', flat=True)
        
        page = request.GET.get('page')
        paginator = Paginator(film_list, per_page=10)
        try:
            films = paginator.page(page)
        except PageNotAnInteger:
            films = paginator.page(1)
        except EmptyPage:
            films = paginator(paginator.num_pages)

        context = {
            'f_title': f_title,
            'f_id': f_id,
            'films': films,
            'p_films': p_films,
            'filmrating': filmrating,
            'activ_profile': activ_profile,
        }
        return render(request, 'list/film_list.html', context)
    else:
        films = Film.objects.all().annotate(average_score=Avg('filmrating__rate'))

        context = {
            'films': films,
        }
        return render(request, 'list/film_list.html', context)