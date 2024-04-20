from django.urls import path
from autentification.views import UserCreationForm

app_name = 'autentification'

urlpatterns = [
    path('auth/register/', UserCreationForm, name='register'),
]