from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.attrs = {'class': 'form-control'}
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter description'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Choose category'})
        self.fields['photo'].widget.attrs.update({'placeholder': 'Upload photo'})
        self.fields['birthday'].widget.attrs.update({'placeholder': 'Enter birthday'})


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

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


        self.helper.attrs = {'class': 'form-control'}
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter title'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter description'})
