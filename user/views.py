from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# for the class 'SignUpView'
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from .forms import CustomUserCreationForm, ProfileForm, UserForm
from firstapp.models import Game, Move
from django.contrib.auth.models import User
from .models import Profile
from django.db import transaction

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


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user/profile.html')



@login_required
@transaction.atomic
def settings(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
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