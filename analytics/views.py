import datetime
import calendar
from itertools import chain
from django.shortcuts import render
from api.models import Article
from films.models import FilmRating, FilmWatchlist
from serials.models import SerialRating, SerialWatchlist


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


def month(request):
    today = datetime.datetime.now()
    film_votes_month = FilmRating.objects.filter(date__year=today.year,
                                                date__month=today.month)
    film_watchlist_month = FilmWatchlist.objects.filter(date__year=today.year,
                                                       date__month=today.month)
    serial_votes_month = SerialRating.objects.filter(date__year=today.year,
                                                    date__month=today.month)
    serial_watchlist_month = SerialWatchlist.objects.filter(date__year=today.year,
                                                           date__month=today.month)
    articles_month = Article.objects.filter(created_date__year=today.year,
                                           created_date__month=today.month)
    film_votes_countmonth = film_votes_month.count()
    film_watchlist_countmonth = film_watchlist_month.count()
    serial_votes_countmonth = serial_votes_month.count()
    serial_watchlist_countmonth = serial_watchlist_month.count()

    days_in_month = calendar.monthrange(today.year, today.month)[1]
    all_votes = []
    all_watchlist = []
    all_articles = []
    current_days = []
    for i in range(1, days_in_month + 1):
        fvotes = film_votes_month.filter(date__day=i).count()
        svotes = serial_votes_month.filter(date__day=i).count()
        fwatchlist = film_watchlist_month.filter(date__day=i).count()
        swatchlist = serial_watchlist_month.filter(date__day=i).count()
        articles = articles_month.filter(created_date__day=i).count()
        all_votes.append(fvotes + svotes)
        all_watchlist.append(fwatchlist + swatchlist)
        all_articles.append(articles)
        if today.month < 10:
            if i < 10:
                current_days.append(f'{today.year}-0{today.month}-0{i}')
            else:
                current_days.append(f'{today.year}-0{today.month}-{i}')
        else:
            if i < 10:
                current_days.append(f'{today.year}-{today.month}-0{i}')
            else:
                current_days.append(f'{today.year}-{today.month}-{i}')

    all_rate_votes = []
    for i in range(1, 11):
        f_rate_votes = film_votes_month.filter(rate=i).count()
        s_rate_votes = serial_votes_month.filter(rate=i).count()
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

    today_month = today.strftime('%B')

    context = {
        'film_votes_countmonth': film_votes_countmonth,
        'film_watchlist_countmonth': film_watchlist_countmonth,
        'serial_votes_countmonth': serial_votes_countmonth,
        'serial_watchlist_countmonth': serial_watchlist_countmonth,
        'today': today,
        'all_votes': all_votes,
        'all_watchlist': all_watchlist,
        'max_all_votes': max_all_votes,
        'current_days': current_days,
        'all_rate_votes': all_rate_votes,
        'min_all_votes': min_all_votes,
        'sum_rate_votes': sum_rate_votes,
        'sum_all_votes': sum_all_votes,
        'sum_all_watchlist': sum_all_watchlist,
        'sum_all_articles': sum_all_articles,
        'max_all_watchlist': max_all_watchlist,
        'min_all_watchlist': min_all_watchlist,
        'sum_new_things': sum_new_things,
        'today_month': today_month,
    }
    return render(request, 'analytics/month.html', context)