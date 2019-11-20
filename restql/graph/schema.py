import graphene

from graphene_django.types import DjangoObjectType

from restql.pizza.models import Pizza, Toppings
from restql.pizza.forms import PizzaForm, ToppingsForm
from graphene_django.forms.mutation import DjangoModelFormMutation


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza


class ToppingsType(DjangoObjectType):
    class Meta:
        model = Toppings


class PizzaMutation(DjangoModelFormMutation):
    pizza = graphene.Field(PizzaType)

    class Meta:
        form_class = PizzaForm


class ToppingMutation(DjangoModelFormMutation):
    topping = graphene.Field(ToppingsType)

    class Meta:
        form_class = ToppingsForm


class Mutation(graphene.ObjectType):
    pizza_mut = PizzaMutation.Field()
    topping_mut = ToppingMutation.Field()


class Query:
    pizza = graphene.Field(PizzaType, id=graphene.Int(), name=graphene.String(), price=graphene.Float())
    topping = graphene.Field(ToppingsType, id=graphene.Int(), name=graphene.String(), quantity=graphene.Float())
    all_pizzas = graphene.List(PizzaType)
    all_toppings = graphene.List(ToppingsType)

    def resolve_pizza(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Pizza.objects.get(pk=id)

        if name is not None:
            return Pizza.objects.get(name=name)

        return None

    def resolve_topping(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Toppings.objects.get(pk=id)

        if name is not None:
            return Toppings.objects.get(name=name)

        return None

    def resolve_all_pizzas(self, info, **kwargs):
        return Pizza.objects.all()

    def resolve_all_toppings(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Toppings.objects.select_related('pizza').all()
