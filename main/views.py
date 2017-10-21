from user.models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated():
        return render(request, "main/home.html")
    else:
        return render(request, "main/home.html")
