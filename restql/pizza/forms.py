from django import forms

from restql.pizza.models import Pizza, Toppings


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('name', 'price')


class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = ('name', 'quantity')
