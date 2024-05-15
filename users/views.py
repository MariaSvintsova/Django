
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail

from config import settings
from users.forms import UserProfileForm, UserRegisterForm
from config.settings import EMAIL_HOST_USER
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_success')
    object = None

    def get_success_url(self):
        return reverse_lazy('users:register_success')


    def form_valid(self, form):
        user = form.save()

        user_email = user.email
        send_mail(
            "Подтверждение регистрации",
            "Добро пожаловать! Вы успешно зарегистрированы.",
            settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
            fail_silently=False,
        )

        return super().form_valid(form)

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


# def