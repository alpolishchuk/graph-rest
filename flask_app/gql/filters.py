from graphene_sqlalchemy_filter import FilterSet

from ..dbmodels import Toppings


class ToppingsFilter(FilterSet):
    class Meta:
        model = Toppings
        fields = {
            "id": ["eq", "in"],
            "name": ["eq"]
        }
