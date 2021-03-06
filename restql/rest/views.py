from rest_framework import viewsets

from restql.pizza.models import Toppings, Pizza
from restql.rest.serializers import PizzaSerializer, ToppingsSerializer


class PizzaView(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class ToppingsView(viewsets.ModelViewSet):
    serializer_class = ToppingsSerializer
    queryset = Toppings.objects.all()
