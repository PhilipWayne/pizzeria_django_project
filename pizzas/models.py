from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Names of pizzas"""
    name = models.CharField(max_length=200)
    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """Names of toppings for pizzas"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name        