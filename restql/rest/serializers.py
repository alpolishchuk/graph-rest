from rest_framework import serializers
from restql.pizza.models import Pizza, Toppings


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'


class ToppingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toppings
        fields = '__all__'
