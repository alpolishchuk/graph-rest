import graphene as g
from graphene import relay
from collections import namedtuple
from typing import Optional

from graphene_sqlalchemy import SQLAlchemyConnectionField
from .inputs import PizzaInputType
from .shemas import (
    DictResolveObjectType, AttrResolveObjectType, PizzaModelObjectType, ToppingsModelObjectType, ToppingsConnection,
    ToppingsFilterableConnection
)
from .mutation import CreatePizza, UpdatePizza


class Query(g.ObjectType):
    node = relay.Node.Field()

    dict_object = g.Field(DictResolveObjectType)
    attr_object = g.Field(AttrResolveObjectType)
    all_toppings = g.List(ToppingsModelObjectType)
    all_pizzas = g.List(PizzaModelObjectType, data=PizzaInputType())
    all_toppings_connection = SQLAlchemyConnectionField(ToppingsConnection)
    filterable_toppings_connection = ToppingsFilterableConnection()

    def resolve_dict_object(self, info: g.ResolveInfo, **kwargs):
        return {
            "float_field": 1.0,
            "int_field": 2,
            "text_field": "Some Text",
        }

    def resolve_attr_object(self, info: g.ResolveInfo, **kwargs):
        Graph = namedtuple("Graph", ["float_attr", "int_attr", "text_attr"])
        return Graph(float_attr=2.0, int_attr=1, text_attr="Test2")

    def resolve_all_toppings(self, info: g.ResolveInfo, **kwargs):
        return ToppingsModelObjectType.get_query(info, **kwargs)

    def resolve_all_pizzas(self, info: g.ResolveInfo, data: Optional[PizzaInputType] = None, **kwargs):
        return PizzaModelObjectType.get_query(info, data, **kwargs)


class Mutation(g.ObjectType):
    create_pizza = CreatePizza.Field()
    update_pizza = UpdatePizza.Field()
