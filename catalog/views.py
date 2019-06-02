from django.shortcuts import render
from .models import Book, Author, Review

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        last_review_list = Review.objects.filter(book_id=book_id)[:5]
    except Review.DoesNotExist:
        review_list = None
    return render(request, 'catalog/book_detail.html', {'book': book, 'last_review_list' : last_review_list})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    try:
        book_list = Book.objects.filter(author_id=author_id)
    except Book.DoesNotExist:
        review_list = None
    return render(request, 'catalog/author_detail.html', {'author': author, 'book_list': book_list})

def all_books(request):
    book_list = Book.objects.all()
    return render(request, 'catalog/all_books.html', {'book_list': book_list})

def all_authors(request):
    author_list = Author.objects.all()
    return render(request, 'catalog/all_authors.html', {'author_list': author_list})

def all_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        review_list = Review.objects.filter(book_id=book_id)
    except Review.DoesNotExist:
        review_list = None
    return render(request, 'catalog/all_reviews.html', {'book': book, 'review_list' : review_list})
