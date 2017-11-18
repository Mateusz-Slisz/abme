from django.shortcuts import render, redirect, get_object_or_404
from api.models import Book
from django.contrib.auth.models import User
from user.models import Profile
from .models import BookRating, BookWatchlist
from django.db.models import Avg, Func
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 1)'


def list(request):
    if request.user.is_authenticated():
        add_book_id = request.GET.get('add_book_id', None)
        del_book_id = request.GET.get('del_book_id', None)
        add_watchlist = request.GET.get('add_watchlist', None)
        del_watchlist = request.GET.get('del_watchlist', None)
        rate = request.GET.get('rate', None)
        activ_user = get_object_or_404(User, username=request.user)
        activ_profile = get_object_or_404(Profile, user=activ_user)

        if request.method == 'GET' and add_book_id is not None:
            book = get_object_or_404(Book, id=add_book_id)
            if BookRating.objects.filter(user=activ_user, book=book).exists():
                BookRating.objects.filter(user=activ_user, book=book).update(rate=rate)
            else:
                BookRating.objects.create(user=activ_user, book=book, rate=rate)

        if request.method == 'GET' and del_book_id is not None:
            book = get_object_or_404(Book, id=del_book_id)
            BookRating.objects.filter(user=activ_user, book=book, rate=rate).delete()

        if request.method == 'GET' and add_watchlist is not None:
            book = get_object_or_404(Book, id=add_watchlist)
            if BookWatchlist.objects.filter(user=activ_user, book=book).exists():
                BookWatchlist.objects.filter(user=activ_user, book=book).update()
            else:
                BookWatchlist.objects.create(user=activ_user, book=book)
        
        if request.method == 'GET' and del_watchlist is not None:
            book = get_object_or_404(Book, id=del_watchlist)
            BookWatchlist.objects.filter(user=activ_user, book=book).delete()
        
        book_list = Book.objects.get_queryset().order_by('id').annotate(average_score=Round(Avg('bookrating__rate')))
        
        bookrating = BookRating.objects.filter(user=activ_user)
        b_id = bookrating.values_list('book__id', flat=True)

        watchlist = BookWatchlist.objects.all().filter(user=activ_user)
        watchlist_id = watchlist.values_list('book__id', flat=True)

        page = request.GET.get('page')
        paginator = Paginator(book_list, per_page=10)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator(paginator.num_pages)

        context = {
            'bookrating': bookrating,
            'b_id': b_id,
            'books': books,
            'activ_profile': activ_profile,
            'watchlist_id': watchlist_id,
        }
        return render(request, 'list/book_list.html', context)
    else:
        book_list = Book.objects.get_queryset().order_by('id').annotate(average_score=Round(Avg('bookrating__rate')))

        page = request.GET.get('page')
        paginator = Paginator(book_list, per_page=10)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator(paginator.num_pages)

        context = {
            'books': books,
        }
        return render(request, 'list/book_list.html', context)