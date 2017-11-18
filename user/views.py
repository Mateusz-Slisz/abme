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
from api.models import Author, Book, Film, Serial
from films.models import FilmRating, FilmWatchlist
from books.models import BookRating, BookWatchlist
from serials.models import SerialRating, SerialWatchlist


@login_required
def home(request):
    activ_user = get_object_or_404(User, username=request.user)
    activ_profile = get_object_or_404(Profile, user=activ_user)

    context = {
        'activ_profile': activ_profile,
    }
    return render(request, 'user/home.html', context)


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

    activ_user = get_object_or_404(User, username=request.user)
    activ_profile = get_object_or_404(Profile, user=activ_user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'activ_profile': activ_profile,
    }

    return render(request, 'user/settings.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    var = get_object_or_404(Profile, user=user)
    full_name = user.first_name + " " + user.last_name

    f_ratings = FilmRating.objects.filter(user=user).order_by('-rate')[0:8]
    b_ratings = BookRating.objects.filter(user=user).order_by('-rate')[0:8]
    s_ratings = SerialRating.objects.filter(user=user).order_by('-rate')[0:8]

    context = {
        'user': user,
        'full_name': full_name,
        'f_ratings': f_ratings,
        'b_ratings': b_ratings,
        's_ratings': s_ratings,
    }
    return render(request, 'user/profile.html', context)

def profile_films(request, username):
    user = get_object_or_404(User, username=username)
    var = get_object_or_404(Profile, user=user)

    f_ratings = FilmRating.objects.filter(user=user).order_by('-id')

    context = {
        'user': user,
        'f_ratings': f_ratings,
    }
    return render(request, 'user/profile_films.html', context)

def profile_serials(request, username):
    user = get_object_or_404(User, username=username)
    var = get_object_or_404(Profile, user=user)

    s_ratings = SerialRating.objects.filter(user=user).order_by('-id')

    context = {
        'user': user,
        's_ratings': s_ratings,
    }
    return render(request, 'user/profile_serials.html', context)

def profile_books(request, username):
    user = get_object_or_404(User, username=username)
    var = get_object_or_404(Profile, user=user)

    b_ratings = BookRating.objects.filter(user=user).order_by('-id')

    context = {
        'user': user,
        'b_ratings': b_ratings,
    }
    return render(request, 'user/profile_books.html', context)

@login_required
def watchlist(request):

    activ_user = get_object_or_404(User, username=request.user)
    activ_profile = get_object_or_404(Profile, user=activ_user)

    watchlist_f = FilmWatchlist.objects.filter(user=activ_user)
    watchlist_s = SerialWatchlist.objects.filter(user=activ_user)
    watchlist_b = BookWatchlist.objects.filter(user=activ_user)


    context = {
        'watchlist_f': watchlist_f,
        'watchlist_s': watchlist_s,
        'watchlist_b': watchlist_b,
    }
    return render(request, 'user/watchlist.html', context)
