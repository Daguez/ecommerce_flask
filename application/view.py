from flask import render_template, Blueprint, url_for, redirect, session, flash, request
# used for debugging
# from sqlalchemy.exc import SQLAlchemyError

from application.model import Item, Order_Details, Order
from .order import CheckoutForm
from application.model import db

# view Blueprint
viewbp = Blueprint('view', __name__)


@viewbp.route("/")
@viewbp.route("/index")
@viewbp.route("/home")
@viewbp.route("/index.html")
def index():
    items = Item.query.all()
    token = request.values.get('token')
    if token == "contact":
        flash('Your message have been send. We will answer your query within two business days.')
    return render_template("index.html", index=True, bottom=True, items=items)


@viewbp.route("/item/<int:itemid>/")
def item(itemid):
    thisitem = Item.query.filter(Item.id == itemid)
    return render_template("item.html", thisitem=thisitem)


@viewbp.route("/about")
@viewbp.route("/about.html")
def about():
    return render_template("about.html", about=True)


@viewbp.route("/contact")
@viewbp.route("/contact.html")
def contact():
    return render_template("contact.html", contact=True)


@viewbp.route("/cat1")
@viewbp.route("/cat1.html")
@viewbp.route("/Cat1.html")
def cat1():
    items = Item.query.filter(Item.category == 1)
    return render_template("cat1.html", bottom=True, items=items)


@viewbp.route("/cat2")
@viewbp.route("/cat2.html")
@viewbp.route("/Cat2.html")
def cat2():
    items = Item.query.filter(Item.category == 2)
    return render_template("cat2.html", bottom=True, items=items)


@viewbp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        total = request.values.get('totalprice')
        token = request.values.get('token')
        print("Total:", total)
        if form.validate_on_submit():
            order.payment = True
            order.orderSent = True
            order.first_name = form.first_name.data
            order.last_name = form.last_name.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.street = form.street.data
            order.suburb = form.suburb.data
            order.state = form.state.data
            order.zip = form.zip.data
            order.card = form.card.data
            order.expiry = form.expiry.data
            order.card_CVS = form.cvs.data
            order.card_name = form.card_name.data
            # Calculate cost again
            totalcost = 0
            for item in order.items:
                totalcost = totalcost + item.price
                totalprice = totalcost
                order.orderCost = totalcost
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! your order will be dispatched soon...')
                return redirect(url_for('view.index'))
            except:
                return 'There was an issue completing your order'
        if token == "check":
            flash("Some entry are invalid")

    return render_template('checkout.html', form=form, bottom=True, totalprice=total)
