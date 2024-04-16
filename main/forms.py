from django import forms
from django.urls import reverse_lazy

from main.models import Dish, Customer

class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DishForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'description', 'category', 'photo', 'price', 'birthday')
        success_url = reverse_lazy('main:detail_list')

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError(f'Название не должно содержать запрещенное слово: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(f'Описание не должно содержать запрещенное слово: {word}')
        return description


class CustomerForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        wrong_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in cleaned_data:
            if word in wrong_words:
                raise forms.ValidationError('Вы использовали запрещенные слова')

        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        wrong_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in cleaned_data:
            if word in wrong_words:
                raise forms.ValidationError('Вы использовали запрещенные слова')

        return cleaned_data