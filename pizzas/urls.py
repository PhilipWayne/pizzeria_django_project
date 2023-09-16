"""Defines URL patterns for pizzeria"""
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # List of pizzas
    path('pizzas', views.pizzas, name='pizzas'),
    # Content of the pizza
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza_toppings'),
]