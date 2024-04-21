from django.contrib import admin

from autentification.models import User


# Register your models here.
@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'avatar', 'phone_number', 'country')

