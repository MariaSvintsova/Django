from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
