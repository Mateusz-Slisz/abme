from django.shortcuts import render, get_object_or_404
import datetime
import json
from films.models import FilmRating, FilmWatchlist
from serials.models import SerialRating, SerialWatchlist
from itertools import chain


def main(request):
    today = datetime.datetime.now()
    film_votes_year = FilmRating.objects.filter(date__year=today.year)
    serial_votes_year = SerialRating.objects.filter(date__year=today.year)
    film_votes_countyear = film_votes_year.count()
    serial_votes_countyear = serial_votes_year.count()

    all_votes = []
    current_months = []
    for i in range(1, 13):
        fvotes = film_votes_year.filter(date__month=i).count()
        svotes = serial_votes_year.filter(date__month=i).count()
        all_votes.append(fvotes + svotes)
        if i < 10:
            current_months.append(f'{today.year}-0{i}')
        else:
            current_months.append(f'{today.year}-{i}')

    all_rate_votes = []
    for i in range(1, 11):
        f_rate_votes = film_votes_year.filter(rate=i).count()
        s_rate_votes = serial_votes_year.filter(rate=i).count()
        all_rate_votes.append(f_rate_votes + s_rate_votes)

    max_all_votes = max(all_votes)

    context = {
        'film_votes_countyear': film_votes_countyear,
        'serial_votes_countyear': serial_votes_countyear,
        'today': today,
        'all_votes': all_votes,
        'max_all_votes': max_all_votes,
        'current_months': current_months,
        'all_rate_votes': all_rate_votes,

    }
    return render(request, 'analytics/main.html', context)
