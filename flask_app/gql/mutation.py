import graphene as g
from graphene import Mutation
from contextlib import suppress

from .shemas import PizzaModelObjectType
from .inputs import CreatePizzaInputType, UpdatePizzaInputType
from ..models import PizzaModel
from ..dbmodels import Pizza, Toppings
from ..appinit import db

from logging import getLogger

logger = getLogger(__name__)


class CreatePizza(Mutation):
    Output = PizzaModelObjectType

    class Arguments:
        data = CreatePizzaInputType(required=True)

    def mutate(self, info: g.ResolveInfo, data: CreatePizzaInputType, **kwargs) -> Pizza:
        pizza_data = PizzaModel(data)
        pizza_data.validate()
        toppings_data = data.pop('toppings', None)
        if toppings_data:
            toppings = Toppings.query.filter(Toppings.id.in_(toppings_data)).all()

        try:
            pizza = Pizza(**data)
            db.session.add(pizza)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        with suppress(Exception):
            for topping in toppings:
                topping.pizza_id = pizza.id
            db.session.commit()

        return Pizza.query.filter(Pizza.id == pizza.id).one_or_none()


class UpdatePizza(Mutation):
    Output = PizzaModelObjectType

    class Arguments:
        data = UpdatePizzaInputType(required=True)

    def mutate(self, info: g.ResolveInfo, data: UpdatePizzaInputType, **kwargs) -> Pizza:
        pizza_id = data.pop('id', None)
        if not pizza_id:
            raise Exception("Please provide pizza id to update")

        pizza_data = PizzaModel(data)
        pizza_data.validate()

        toppings_data = data.pop('toppings', None)
        Toppings.query.filter(Toppings.pizza_id == pizza_id).update({"pizza_id": None}, synchronize_session="fetch")
        if toppings_data:
            toppings = Toppings.query.filter(Toppings.id.in_(toppings_data)).all()

        try:
            Pizza.query.filter(Pizza.id == pizza_id).update(data, synchronize_session="fetch")
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        with suppress(Exception):
            for topping in toppings:
                topping.pizza_id = pizza_id
            db.session.commit()

        return Pizza.query.filter(Pizza.id == pizza_id).one_or_none()
