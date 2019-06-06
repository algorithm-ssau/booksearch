from django.shortcuts import render, redirect
from .models import Book, Author, Review
from .forms import ReviewForm

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        last_review_list = Review.objects.filter(book_id=book_id)[:5]
    except Review.DoesNotExist:
        review_list = None

    if request.user.is_authenticated:
        to_read_obj = request.user.to_read.filter(id=book_id)
        flag = to_read_obj.exists()
    else:
        flag = None

    user_review = get_user_review(request, book_id)
    form = get_comment_form(request, book_id)
    
    return render(request, 'catalog/book_detail.html', {'form' : form, 'book': book, 'last_review_list' : last_review_list, 'flag' : flag, 'user_review' : user_review})

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

    user_review = get_user_review(request, book_id)
    form = get_comment_form(request, book_id)
    
    return render(request, 'catalog/all_reviews.html', {'form' : form, 'book': book, 'review_list' : review_list, 'user_review' : user_review})

def index(request):
    last_book_list = Book.objects.all()[:5]
    return render(request, 'index.html', {'last_book_list': last_book_list})

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

def get_comment_form(request, book_id):
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
    return form

def get_user_review(request, book_id):
    try:
        user_review = Review.objects.get(custom_user_id=request.user.id, book_id=book_id)
    except Review.DoesNotExist:
        user_review = None
    return user_review