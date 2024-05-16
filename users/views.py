import random
import string

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from config import settings
from users.forms import UserProfileForm, UserRegisterForm, PasswordResetForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_success')
    object = None

    def get_success_url(self):
        return reverse_lazy('users:register_success')

    # def form_valid(self, form):
    #     user = form.save()
    #
    #     user_email = user.email
    #     send_mail(
    #         "Подтверждение регистрации",
    #         "Добро пожаловать! Вы успешно зарегистрированы.",
    #         settings.EMAIL_HOST_USER,
    #         recipient_list=[user_email],
    #         fail_silently=False,
    #     )
    #
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         user = form.save()
    #         user_email = user.email
    #         send_mail(
    #             "Подтверждение регистрации",
    #             "Добро пожаловать! Вы успешно зарегистрированы.",
    #             settings.EMAIL_HOST_USER,
    #             recipient_list=[user_email],
    #             fail_silently=False,
    #         )
    #         return redirect(self.get_success_url())
    #     else:
    #         return self.form_invalid(form)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = None
    #     return context


def registration_success(request):
    return render(request, 'users/register_success.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

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


class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

class LogoutView(AuthLogoutView):
    next_page = "users:login"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'email' in request.POST and not request.POST.get('password'):
            # Перенаправляем запрос в PasswordResetView
            return PasswordResetView.as_view()(request)
        return super().post(request, *args, **kwargs)

class PasswordResetView(View):
    form_class = PasswordResetForm
    def get(self, request):
        return render(request, 'users/password_reset.html')

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            user.password = make_password(new_password)
            user.save()

            send_mail(
                'Восстановление пароля',
                f'Ваш новый пароль: {new_password}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, 'users/password_reset_done.html')
        except User.DoesNotExist:
            return render(request, 'users/password_reset.html', {'error': 'Пользователь с таким email не найден.'})
