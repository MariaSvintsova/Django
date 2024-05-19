from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from main.models import NULLABLE

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True, verbose_name='Ваш email')
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Фото')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, verbose_name='Ваша страна')
    is_stuff = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_edit_product_description", "Can edit product description"),
            ("can_edit_product_category", "Can edit product category"),
        ]
