from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


# Three Class: Order; Item (products); Order_Details Using an association_proxy, the goal was to be able to
# Implement a quantity function for the basket by addressing the quantity Column in Order_Details


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    payment = db.Column(db.Boolean, default=False)
    orderSent = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    street = db.Column(db.String())
    suburb = db.Column(db.String(20))
    state = db.Column(db.String())
    zip = db.Column(db.Integer)
    card = db.Column(db.Integer)
    expiry = db.Column(db.Integer)
    card_name = db.Column(db.String)
    card_CVS = db.Column(db.Integer)
    orderCost = db.Column(db.Float)
    ordered_items = db.relationship(
        "Order_Details", cascade="all, delete-orphan", backref=db.backref("order")
    )
    items = association_proxy('ordered_items', 'item', creator=lambda v: Order_Details(item=v))

    def __repr__(self):
        str = "Id: {}, payment: {}, ordersent: {}, Cost: {}, Street: {}, Firstname: {}, lastname: {}, Card: {}, Item: {}\n"
        str = str.format(self.id, self.payment, self.orderSent, self.orderCost, self.street, self.first_name,
                         self.last_name, self.card,
                         self.items)
        return str


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer)
    name = db.Column(db.String(100))
    description = db.Column(db.String(800))
    itemShort = db.Column(db.String(100))
    image = db.Column(db.String(60))
    price = db.Column(db.Float)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Category: {}, ShortDes: {}\n"
        str = str.format(self.id, self.name, self.description, self.image, self.price, self.category,
                         self.itemShort)
        return str


class Order_Details(db.Model):
    __tablename__ = 'order_details'
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    quantity = db.Column(db.Integer, default=1)

    def __init__(self, order=None, item=None, quantity=1):
        self.order = order
        self.item = item
        self.quantity = quantity

    item = db.relationship(Item)


def load_db(db):
    # Drop and re-create all the tables (For testing)
    # db.drop_all()
    db.create_all()
