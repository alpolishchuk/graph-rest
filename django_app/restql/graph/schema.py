import graphene
import graphene_django_optimizer as gql_optimizer
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.types import DjangoObjectType

from restql.pizza.forms import PizzaForm, ToppingForm
from restql.pizza.models import Pizza, Toppings


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        interfaces = (graphene.relay.Node,)


class ToppingType(DjangoObjectType):
    class Meta:
        model = Toppings
        interfaces = (graphene.relay.Node,)


class PizzaMutation(DjangoModelFormMutation):
    pizza = graphene.Field(PizzaType)

    class Meta:
        form_class = PizzaForm


class ToppingMutation(DjangoModelFormMutation):
    topping = graphene.Field(ToppingType)

    class Meta:
        form_class = ToppingForm


class Mutation(graphene.ObjectType):
    pizza_mut = PizzaMutation.Field()
    topping_mut = ToppingMutation.Field()


class Query:
    pizza = graphene.relay.Node.Field(PizzaType)
    all_pizzas = graphene.List(PizzaType)
    get_pizza = graphene.Field(PizzaType, id=graphene.Int(), name=graphene.String(), price=graphene.Float())

    topping = graphene.relay.Node.Field(ToppingType)
    get_topping = graphene.Field(ToppingType, id=graphene.Int(), name=graphene.String(), quantity=graphene.Float())
    all_toppings = graphene.List(ToppingType)

    pizzas_optimized = graphene.List(PizzaType)
    toppings_optimized = graphene.List(ToppingType)

    def resolve_get_pizza(self, info, **kwargs):
        pizza_id = kwargs.get('id')
        name = kwargs.get('name')
        price = kwargs.get('price')

        if pizza_id is not None:
            return Pizza.objects.get(id=pizza_id)

        if name is not None:
            return Pizza.objects.last()

        if price is not None:
            return Pizza.objects.filter(price=price).first()

        return None

    def resolve_get_topping(self, info, **kwargs):
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

    def resolve_pizzas_optimized(self, info, **kwargs):
        return gql_optimizer.query(Pizza.objects.all(), info)

    def resolve_toppings_optimized(self, info, **kwargs):
        return gql_optimizer.query(Toppings.objects.select_related('pizza').all(), info)
