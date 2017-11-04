from user.models import Profile
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages


def home(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['mat.slisz@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Thanks for your reply')
            return redirect('website_home')

    if request.user.is_authenticated():
        return render(request, "main/home.1.html")
    else:
        return render(request, "main/home.html")
