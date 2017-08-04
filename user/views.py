from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# for the class 'SignUpView'
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from .forms import CustomUserCreationForm
from firstapp.models import Game, Move


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