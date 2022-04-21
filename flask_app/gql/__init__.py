import graphene as g
from .shemas import DictResolveObjectType, AttrResolveObjectType, PizzaModelObjectType
from collections import namedtuple


class Query(g.ObjectType):
    dict_object = g.Field(DictResolveObjectType)
    attr_object = g.Field(AttrResolveObjectType)
    all_pizzas = g.List(PizzaModelObjectType)

    def resolve_dict_object(self, info: g.ResolveInfo, **kwargs):
        return {
            "float_field": 1.0,
            "int_field": 2,
            "text_field": "Some Text",
        }

    def resolve_attr_object(self, info: g.ResolveInfo, **kwargs):
        Graph = namedtuple("Graph", ["float_attr", "int_attr", "text_attr"])
        return Graph(float_attr=2.0, int_attr=1, text_attr="Test2")

    def resolve_all_pizzas(self, info: g.ResolveInfo, **kwargs):
        from ..dbmodels import Pizza
        return Pizza.query.all()


class Mutation(g.ObjectType):
    ...
