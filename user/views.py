from itertools import chain
from operator import attrgetter
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from films.models import FilmRating, FilmWatchlist
from books.models import BookRating, BookWatchlist
from serials.models import SerialRating, SerialWatchlist
from api.models import Serial, Film
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, UserForm


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


@login_required
@transaction.atomic
def settings_password(request):
    return render(request, 'user/settings_password.html')


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

    f_ratings = FilmRating.objects.filter(user=user).order_by('-date')

    context = {
        'user': user,
        'f_ratings': f_ratings,
    }
    return render(request, 'user/profile_films.html', context)


def profile_serials(request, username):
    user = get_object_or_404(User, username=username)
    var = get_object_or_404(Profile, user=user)

    s_ratings = SerialRating.objects.filter(user=user).order_by('-date')

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
    del_film_watchlist = request.GET.get('del_film_watchlist', None)
    del_serial_watchlist = request.GET.get('del_serial_watchlist', None)

    activ_user = get_object_or_404(User, username=request.user)

    if request.method == 'GET':
        if del_film_watchlist is not None:
            film = get_object_or_404(Film, id=del_film_watchlist)
            FilmWatchlist.objects.filter(user=activ_user, film=film).delete()

        if del_serial_watchlist is not None:
            serial = get_object_or_404(Serial, id=del_serial_watchlist)
            SerialWatchlist.objects.filter(user=activ_user, serial=serial).delete()

    watchlist_f = FilmWatchlist.objects.filter(user=activ_user)
    watchlist_s = SerialWatchlist.objects.filter(user=activ_user)
    watchlist_b = BookWatchlist.objects.filter(user=activ_user)

    watchlist_all = sorted(
        chain(watchlist_f, watchlist_s),
        key=attrgetter('date'),
        reverse=True)

    context = {
        'watchlist_all': watchlist_all,
    }
    return render(request, 'user/watchlist.html', context)
