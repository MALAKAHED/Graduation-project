from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_meal, name='add_meal'),
    path('list/', views.meal_list, name='meal_list'),
    path('update/<int:pk>/', views.update_meal, name='update_meal'),
    path('delete/<int:pk>/', views.delete_meal, name='delete_meal'),
]
