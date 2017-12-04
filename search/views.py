from itertools import chain
from operator import attrgetter
from django.shortcuts import render
from django.db.models import Avg, Func, Count, Q
from api.models import Film, Serial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


def list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Round(Avg('filmrating__rate')),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Round(Avg('serialrating__rate')),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()

    result_list = sorted(
        chain(films, serials),
        key=attrgetter('title'))

    result_list_c = films_c + serials_c

    paginator = Paginator(result_list, per_page=10)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator(paginator.num_pages)

    context = {
        'serials': serials,
        'films': films,
        'serials_c': serials_c,
        'films_c': films_c,
        'result_list': result_list,
        'result_list_c': result_list_c,
    }

    return render(request, 'list.html', context)


def film_list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Round(Avg('filmrating__rate')),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Round(Avg('serialrating__rate')),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()
    result_list_c = films_c + serials_c

    paginator = Paginator(films, per_page=10)
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator(paginator.num_pages)

    context = {
        'serials': serials,
        'films': films,
        'serials_c': serials_c,
        'films_c': films_c,
        'result_list_c': result_list_c,
    }

    return render(request, 'film_list.html', context)


def serial_list(request):
    films = Film.objects.get_queryset().annotate(
        average_score=Round(Avg('filmrating__rate')),
        votes=Count('filmrating__user', distinct=True))

    serials = Serial.objects.get_queryset().order_by('id').annotate(
        average_score=Round(Avg('serialrating__rate')),
        votes=Count('serialrating__user', distinct=True))

    keywords = request.GET.get('q')
    page = request.GET.get('page')

    if keywords:
        films = films.filter(
            Q(title__icontains=keywords)
        )
        serials = serials.filter(
            Q(title__icontains=keywords)
        )

    films_c = films.count()
    serials_c = serials.count()
    result_list_c = films_c + serials_c

    paginator = Paginator(serials, per_page=10)
    try:
        serials = paginator.page(page)
    except PageNotAnInteger:
        serials = paginator.page(1)
    except EmptyPage:
        serials = paginator(paginator.num_pages)

    context = {
        'serials': serials,
        'films': films,
        'serials_c': serials_c,
        'films_c': films_c,
        'result_list_c': result_list_c,
    }

    return render(request, 'serial_list.html', context)
