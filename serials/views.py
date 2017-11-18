from django.shortcuts import render, redirect, get_object_or_404
from api.models import Serial
from django.contrib.auth.models import User
from user.models import Profile
from .models import SerialRating, SerialWatchlist
from django.db.models import Avg, Func
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 1)'


def list(request):
    if request.user.is_authenticated():
        add_serial_id = request.GET.get('add_serial_id', None)
        del_serial_id = request.GET.get('del_serial_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist= request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)
        activ_profile = get_object_or_404(Profile, user=activ_user)
        
        if request.method == 'GET' and add_serial_id is not None and rate is not None:
            serial = get_object_or_404(Serial, id=add_serial_id)
            if SerialRating.objects.filter(user=activ_user, serial=serial).exists():
                SerialRating.objects.filter(user=activ_user, serial=serial).update(rate=rate)
            else:
                SerialRating.objects.create(user=activ_user, serial=serial, rate=rate)

        if request.method == 'GET' and del_serial_id is not None and rate is not None:
            serial = get_object_or_404(Serial, id=del_serial_id)
            SerialRating.objects.filter(user=activ_user, serial=serial, rate=rate).delete()
        
        if request.method == 'GET' and add_watchlist is not None:
            serial = get_object_or_404(Serial, id=add_watchlist)
            if SerialWatchlist.objects.filter(user=activ_user, serial=serial).exists():
                SerialWatchlist.objects.filter(user=activ_user, serial=serial).update()
            else:
                SerialWatchlist.objects.create(user=activ_user, serial=serial)
        
        if request.method == 'GET' and del_watchlist is not None:
            serial = get_object_or_404(Serial, id=del_watchlist)
            SerialWatchlist.objects.filter(user=activ_user, serial=serial).delete()

        serial_list = Serial.objects.get_queryset().order_by('id').annotate(average_score=Round(Avg('serialrating__rate')))

        serialrating = SerialRating.objects.all().filter(user=activ_user)
        s_id = serialrating.values_list('serial__id', flat=True)

        watchlist = SerialWatchlist.objects.all().filter(user=activ_user)
        watchlist_id = watchlist.values_list('serial__id', flat=True)

        page = request.GET.get('page')
        paginator = Paginator(serial_list, per_page=10)
        try:
            serials = paginator.page(page)
        except PageNotAnInteger:
            serials = paginator.page(1)
        except EmptyPage:
            serials = paginator(paginator.num_pages)

        context = {
            's_id': s_id,
            'serials': serials,
            'serialrating': serialrating,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
        }
        return render(request, 'list/serial_list.html', context)
    else:
        serial_list = Serial.objects.get_queryset().order_by('id').annotate(average_score=Round(Avg('serialrating__rate')))

        page = request.GET.get('page')
        paginator = Paginator(serial_list, per_page=10)
        try:
            serials = paginator.page(page)
        except PageNotAnInteger:
            serials = paginator.page(1)
        except EmptyPage:
            serials = paginator(paginator.num_pages)

        context = {
            'serials': serials,
        }
        return render(request, 'list/serial_list.html', context)