from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import NULLABLE


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    email = models.EmailField(unique=True, verbose_name='Ваш email')
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Фото')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, verbose_name='Ваша страна')



    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'