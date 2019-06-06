from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('all_authors/', views.all_authors, name='all_authors'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('book/<int:book_id>/all_reviews/', views.all_reviews, name='all_reviews'),
    path('book/<int:book_id>/add_to_reading_list/', views.add_to_reading_list, name='add_to_reading_list'),
    path('book/<int:book_id>/remove_from_reading_list/', views.remove_from_reading_list, name='remove_from_reading_list'),
]
