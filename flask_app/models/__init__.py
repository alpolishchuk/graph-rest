from schematics.models import Model
from schematics.types import FloatType, StringType, ListType, IntType


class PizzaModel(Model):
    """Schematics model for pizza"""

    id = IntType()
    name = StringType(required=True)
    price = FloatType(required=True)
    toppings = ListType(IntType)

    class Options:
        """Options class for PizzaModel."""

        serialize_when_none = False
