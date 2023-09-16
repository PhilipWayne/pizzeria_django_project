from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Pizza

def index(request):
    """The home page for pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    "Shows a pizza and its toppings"
    pizza = get_object_or_404(Pizza, id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

    



