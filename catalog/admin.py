from django.contrib import admin
from .models import Country, Author, Genre, Category, Book, Review

admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)
