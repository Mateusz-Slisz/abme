from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from .forms import CustomUserCreationForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from .models import Profile
from django.db import transaction
from api.models import Author, Book, Film


@login_required
def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully, login.')
            return redirect('user_home')

    else:
        f = CustomUserCreationForm()

    return render(request, 'user/signup.html', {'form': f})



@login_required
@transaction.atomic
def settings(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated! '))
            return redirect('user_settings')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def settings_films(request):
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
    }
    return render(request, 'user/settings_films.html', context)


@login_required
def settings_books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'user/settings_books.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)

    var = get_object_or_404(Profile, user=user)
    film = var.film.all()

    context = {
        'user': user,
        'film': film,
    }
    return render(request, 'user/profile.html', context)


