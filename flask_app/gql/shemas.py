import graphene as g
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterableConnectionField
from graphene.types.resolver import dict_or_attr_resolver, dict_resolver

from .filters import ToppingsFilter
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

    @classmethod
    def get_query(cls, info, data=None):
        query = Pizza.query.outerjoin(Toppings, Toppings.pizza_id == Pizza.id)
        if data.id:
            query = query.filter(Pizza.id == data.id)
        if data.name:
            query = query.filter(Pizza.name == data.name)
        return query.all()


class ToppingsModelObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Toppings


class ToppingsConnection(relay.Connection):
    class Meta:
        node = ToppingsModelObjectType

    total_count = g.Int()

    def resolve_total_count(info, *args):
        return info.length


class ToppingsFilterableConnection(FilterableConnectionField):
    def __init__(self):
        super().__init__(ToppingsConnection, filters=ToppingsFilter())
