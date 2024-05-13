from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True, verbose_name='Ваш email')
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Фото')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, verbose_name='Ваша страна')
    is_stuff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
