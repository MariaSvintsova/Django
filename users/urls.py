from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import RegisterView, registration_success, ProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register_success/', registration_success, name='register_success'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]