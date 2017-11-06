from django.shortcuts import render, redirect, get_object_or_404
from api.models import Book
from django.contrib.auth.models import User
from user.models import Profile
from .models import BookRating

# Create your views here.

def list(request):
    if request.user.is_authenticated():
        add_book_id = request.GET.get('add_book_id', None)
        del_book_id = request.GET.get('del_book_id', None)
        activ_user = get_object_or_404(User, username=request.user)
        activ_profile = get_object_or_404(Profile, user=activ_user)

        if request.method == 'GET' and add_book_id is not None:
            book = get_object_or_404(Book, id=add_book_id)
            activ_profile.book.add(book)

            if BookRating.objects.filter(user=activ_user, book=book).exists():
                bookuser = BookRating.objects.filter(user=activ_user, book=book)
                bookuser.update(rate=1)
            else:
                BookRating.objects.create(user=activ_user, book=book, rate=1)

        if request.method == 'GET' and del_book_id is not None:
            book = get_object_or_404(Book, id=del_book_id)
            activ_profile.book.remove(book)
            BookRating.objects.filter(user=activ_user, book=book, rate=1).delete()

        p_books = activ_profile.book.all()
        books = Book.objects.all()
        bookrating = BookRating.objects.filter(user=activ_user)
        b = bookrating.values_list('book__title', flat=True)

        context = {
            'bookrating': bookrating,
            'b': b,
            'books': books,
            'p_books': p_books,
            'activ_profile': activ_profile,
        }
        return render(request, 'list/book_list.html', context)
    else:
        books = Book.objects.all()

        context = {
            'books': books,
        }
        return render(request, 'list/book_list.html', context)