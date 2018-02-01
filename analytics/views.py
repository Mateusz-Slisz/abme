from django.shortcuts import render, get_object_or_404
import datetime
from api.models import Article
from films.models import FilmRating, FilmWatchlist
from serials.models import SerialRating, SerialWatchlist
from itertools import chain


def main(request):
    today = datetime.datetime.now()
    film_votes_year = FilmRating.objects.filter(date__year=today.year)
    film_watchlist_year = FilmWatchlist.objects.filter(date__year=today.year)
    serial_votes_year = SerialRating.objects.filter(date__year=today.year)
    serial_watchlist_year = SerialWatchlist.objects.filter(date__year=today.year)
    articles_year = Article.objects.filter(created_date__year=today.year)
    film_votes_countyear = film_votes_year.count()
    film_watchlist_countyear = film_watchlist_year.count()
    serial_votes_countyear = serial_votes_year.count()
    serial_watchlist_countyear = serial_watchlist_year.count()

    all_votes = []
    all_watchlist = []
    all_articles = []
    current_months = []
    for i in range(1, 13):
        fvotes = film_votes_year.filter(date__month=i).count()
        svotes = serial_votes_year.filter(date__month=i).count()
        fwatchlist = film_watchlist_year.filter(date__month=i).count()
        swatchlist = serial_watchlist_year.filter(date__month=i).count()
        articles = articles_year.filter(created_date__month=i).count()
        all_votes.append(fvotes + svotes)
        all_watchlist.append(fwatchlist + swatchlist)
        all_articles.append(articles)
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
    min_all_votes = min(all_votes)
    max_all_watchlist = max(all_watchlist)
    min_all_watchlist = min(all_watchlist)
    sum_rate_votes = sum(all_rate_votes)
    sum_all_votes = sum(all_votes)
    sum_all_watchlist = sum(all_watchlist)
    sum_all_articles = sum(all_articles)
    sum_new_things = sum_all_votes + sum_all_watchlist + sum_all_articles

    context = {
        'film_votes_countyear': film_votes_countyear,
        'film_watchlist_countyear': film_watchlist_countyear,
        'serial_votes_countyear': serial_votes_countyear,
        'serial_watchlist_countyear': serial_watchlist_countyear,
        'today': today,
        'all_votes': all_votes,
        'all_watchlist': all_watchlist,
        'max_all_votes': max_all_votes,
        'current_months': current_months,
        'all_rate_votes': all_rate_votes,
        'min_all_votes': min_all_votes,
        'sum_rate_votes': sum_rate_votes,
        'sum_all_votes': sum_all_votes,
        'sum_all_watchlist': sum_all_watchlist,
        'sum_all_articles': sum_all_articles,
        'max_all_watchlist': max_all_watchlist,
        'min_all_watchlist': min_all_watchlist,
        'sum_new_things': sum_new_things,
    }
    return render(request, 'analytics/main.html', context)
