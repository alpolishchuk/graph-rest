import graphene as g
from graphene import InputObjectType


class PizzaInputType(InputObjectType):
    """Graphene input for pizzas request"""
    id = g.Int()
    name = g.String()


class CreatePizzaInputType(InputObjectType):
    """Graphene input for create pizza"""
    name = g.String()
    price = g.Float()
    toppings = g.List(g.Int)


class UpdatePizzaInputType(PizzaInputType):
    price = g.Float()
    toppings = g.List(g.Int)
