from django.shortcuts import render, redirect, get_object_or_404
from api.models import Film
from django.contrib.auth.models import User
from user.models import Profile

# Create your views here.

def list(request):
    add_film_id = request.GET.get('add_film_id', None)
    del_film_id = request.GET.get('del_film_id', None)
    activ_user = get_object_or_404(User, username=request.user)
    activ_profile = get_object_or_404(Profile, user=activ_user)

    if request.method == 'GET' and add_film_id is not None:
        film = get_object_or_404(Film, id=add_film_id)
        activ_profile.film.add(film)
        
        context = {
            'film': film,
        }
        
    if request.method == 'GET' and del_film_id is not None:
        film = get_object_or_404(Film, id=del_film_id)
        activ_profile.film.remove(film)

    p_films = activ_profile.film.all()
    films = Film.objects.all()

    context = {
        'films': films,
        'p_films': p_films,
        'activ_profile': activ_profile,
    }
    return render(request, 'list/film_list.html', context)
