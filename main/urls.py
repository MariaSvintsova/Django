from django.urls import path

from main import views
from main.apps import MainConfig
from main.views import DishListView, DishDetailView, contacts, DishCreateView, DishUpdateView, toggle_activity

# app_name = MainConfig.name
app_name = 'main'

urlpatterns = [
    path('', DishListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('create/', DishCreateView.as_view(), name='create_dish'),
    path('edit/<int:pk>/', DishUpdateView.as_view(), name='update_dish'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
