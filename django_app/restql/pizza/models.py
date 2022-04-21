from django.db import models


class Pizza(models.Model):

    name = models.TextField()
    price = models.FloatField(default=100.0)


class Toppings(models.Model):

    pizza = models.ForeignKey(to=Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    quantity = models.FloatField(default=0.0)
