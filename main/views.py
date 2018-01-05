from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from serials.models import SerialRating
from films.models import FilmRating
from user.forms import CustomUserCreationForm
from api.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully, login.')
            return redirect('website_login')
    else:
        signup_form = CustomUserCreationForm()

    if request.user.is_authenticated():
        activ_user = get_object_or_404(User, username=request.user)
        user_film_vote = FilmRating.objects.filter(user=activ_user)
        user_serial_vote = SerialRating.objects.filter(user=activ_user)
        articles_queryset = Article.objects.get_queryset()
        articles = articles_queryset.order_by('-created_date')
        latest_article = articles.first()

        page = request.GET.get('page')


        paginator = Paginator(articles, per_page=4)

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator(paginator.num_pages)

        context = {
            'user_film_vote': user_film_vote,
            'user_serial_vote': user_serial_vote,
            'articles': articles,
            'latest_article': latest_article,
        }
        return render(request, "main/home.1.html", context)
    else:
        return render(request, "main/home.html", {'signup_form': signup_form})
