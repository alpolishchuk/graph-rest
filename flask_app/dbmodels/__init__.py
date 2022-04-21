from ..appinit import db


class Pizza(db.Model):
    __tablename__ = "pizza_pizza"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False, server_default='')
    price = db.Column(db.Float, nullable=False, server_default="100.0")
    toppings = db.relationship("Toppings")


class Toppings(db.Model):
    __tablename__ = "pizza_toppings"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    pizza = db.relationship("Pizza")
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza_pizza.id'), primary_key=True)
    name = db.Column(db.Text, nullable=False, server_default='')
    quantity = db.Column(db.Float, nullable=False, server_default="0")
