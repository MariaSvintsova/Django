from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from main.models import Category, Customer


def get_cached_categories():
    if settings.СACHE_ENABLED:
        key = 'category_list'
        categories = cache.get(key)
        if not categories:
            categories = list(Category.objects.all())
            cache.set(key, categories, 60 * 60)
    else:
        categories = list(Category.objects.all())
    return categories

def get_cached_customers_for_dish(dish_pk):
    if settings.СACHE_ENABLED:
        key = f"customer_list{dish_pk}"
        customers_list = cache.get(key)
        if customers_list is None:
            customers_list = Customer.objects.filter(dish_pk=dish_pk)
            cache.set(key, customers_list)
    else:
        customers_list = Customer.objects.filter(dish_pk=dish_pk)

    return customers_list

def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )
