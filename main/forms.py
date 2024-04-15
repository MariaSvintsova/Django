from django import forms
from django.urls import reverse_lazy

from main.models import Dish, Customer


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'description', 'category', 'photo', 'price', 'birthday')
        success_url = reverse_lazy('main:detail_list')

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

