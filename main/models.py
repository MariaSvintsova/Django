from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Что это?')
    description = models.TextField(max_length=100, **NULLABLE, verbose_name='Хмм')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Чтото определенное')
    photo = models.ImageField(upload_to='items', **NULLABLE, verbose_name='Фото')
    price = models.IntegerField(verbose_name='цена за единицу')
    birthday = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Предметы'

class Customer(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='блюдо')


    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатели'