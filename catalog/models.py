from django.db import models
from customauth.models import CustomUser

class Country(models.Model):
    country_name = models.CharField(max_length=30, unique=True)

    class Meta(object):
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(default=None, null=True, blank=True)
    country =  models.ForeignKey(Country, on_delete=models.CASCADE)
    biography = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} ({self.birth_date.year})'

class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genre_name

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    class Meta(object):
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Book(models.Model):
    title = models.CharField(max_length=120)
    original_title = models.CharField(default='', blank=True, max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    annotation = models.TextField(default='', blank=True)
    rewiews = models.ManyToManyField(CustomUser, through='Review')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    RATING_CHOICES = [
        (1, 'Very poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField(default='', blank=True)

    class Meta:
        unique_together = ('book', 'custom_user')

    def __str__(self):
        return f'{self.book}, {self.custom_user}'
