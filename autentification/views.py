from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from autentification.forms import UserCreationForm, RegisterForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('auth:register_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_email = form.cleaned_data['email']
        send_mail(
            "Подтверждение регистрации",
            "Добро пожаловать! Вы успешно зарегистрированы.",
            "mariasvintsova@gmail.com",
            [user_email],
            fail_silently=False,
        )
        print(user_email)
        return response


def registration_success(request):
    return render(request, 'auth/register_success.html')