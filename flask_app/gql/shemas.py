import graphene as g
from graphene import ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene.types.resolver import dict_or_attr_resolver, dict_resolver

from ..dbmodels import Pizza, Toppings


class DictResolveObjectType(ObjectType):
    class Meta:
        default_resolver = dict_resolver

    float_field = g.Float()
    int_field = g.Int()
    text_field = g.String()


class AttrResolveObjectType(ObjectType):
    class Meta:
        default_resolver = dict_or_attr_resolver

    float_attr = g.Float()
    int_attr = g.Int()
    text_attr = g.String()


class PizzaModelObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Pizza

    toppings_count = g.Int()

    def resolve_toppings_count(self, *args):
        return len(self.toppings)


class ToppingsModelObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Toppings
