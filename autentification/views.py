from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from autentification.forms import UserCreationForm, RegisterForm, UserProfileForm


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


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('auth:profile')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            if form.data.get('need_generate', False):
                self.object.set_password(
                    self.object.make_random_password(length=12)
                )
                self.object.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
