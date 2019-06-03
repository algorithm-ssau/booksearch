from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        help_text='30 characters or less. Letters, digits and one hyphen between them only',
        validators=[
            validators.RegexValidator(
                r'^[A-Za-z0-9]+(-[A-Za-z0-9]+)?$',
                'Letters, digits and one hyphen between them only allowed', 'invalid',
            ),
        ],
        error_messages={
            'unique': 'This username is already taken'
        }
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    to_read = models.ManyToManyField('catalog.Book', blank=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
