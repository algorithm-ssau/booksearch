from django.shortcuts import render, redirect
from .models import Book, Author, Review
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.db.models import Q

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        last_review_list = Review.objects.filter(book_id=book_id)[:5]
    except Review.DoesNotExist:
        review_list = None

    to_read_obj = request.user.to_read.filter(id=book_id)
    flag = to_read_obj.exists()
    
    return render(request, 'catalog/book_detail.html', {'book': book, 'last_review_list' : last_review_list, 'flag' : flag})

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

def index(request):
    last_book_list = Book.objects.all()[:5]
    return render(request, 'index.html', {'last_book_list': last_book_list})

def book_comment(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if not request.user.is_authenticated:
        return redirect('login')

    review_obj = Review.objects.filter(Q(custom_user_id=request.user.id) & Q(book_id=book_id))
    flag = review_obj.exists()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.book_id = book_id
        review.custom_user_id = request.user.id
        review.save()
        form.save_m2m()
        return redirect('book_detail', book_id)
    else:
        form = ReviewForm()
    
    return render(request, 'catalog/book_comment.html', {'form' : form, 'flag' : flag, 'book' : book})

def add_to_reading_list(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        request.user.to_read.add(book)
        return redirect('book_detail', book_id)
    return render(request, 'catalog/book_detail.html')

def remove_from_reading_list(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        request.user.to_read.remove(book)
        return redirect('book_detail', book_id)
    return render(request, 'catalog/book_detail.html')
