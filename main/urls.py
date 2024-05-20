from django.urls import path
from django.views.decorators.cache import cache_page

from main import views
from main.apps import MainConfig
from main.views import DishListView, DishDetailView, contacts, DishCreateView, DishUpdateView, toggle_activity, \
    DishUpdateCategoryView, DishUpdateDescriptionView

# app_name = MainConfig.name
app_name = 'main'

urlpatterns = [
    path('', cache_page(60)(DishListView.as_view()), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('dish/<int:pk>/', cache_page(60)(DishDetailView.as_view()), name='dish_detail'),
    path('create/', DishCreateView.as_view(), name='create_dish'),
    path('edit/<int:pk>/', DishUpdateView.as_view(), name='update_dish'),
    path('activity/<int:pk>/', cache_page(60)(toggle_activity), name='toggle_activity'),
    path('dish/<int:pk>/edit_description/', DishUpdateDescriptionView.as_view(), name='edit_dish_description'),
    path('dish/<int:pk>/edit_category/', DishUpdateCategoryView.as_view(), name='edit_dish_category'),
]

