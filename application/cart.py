from flask import render_template, request, session, flash, redirect, url_for
from flask import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from .model import Item, Order
from application.model import db

# Cart Blueprint
cartbp = Blueprint('cart', __name__, static_folder="static", template_folder="cart/templates")


@cartbp.route('/cart')
@cartbp.route('/cart.html')
def cart(methods=['POST', 'GET']):
    item_id = request.values.get('item_id')
    # token is used to go back to the original page
    token = request.values.get('token')
    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])

        # order will be None if order_id stale
    else:
        # there is no order

        order = None

    # create new order if needed
    if order is None:
        order = Order(payment=False, orderSent=False, first_name='', last_name='', street='', card=123,
                      card_CVS=111, card_name='', orderCost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    totalprice = 0
    if order is not None:
        print("here")
        # Calculating the total price of the basket
        for item in order.items:
            totalprice = totalprice + item.price
            print("totalprice=",totalprice)
    # are we adding an item?
    if item_id is not None:
        item = Item.query.get(item_id)
        if item not in order.items:
            try:
                order.items.append(item)
                db.session.commit()
                #print("order.items", order.items)
            except SQLAlchemyError as e:
                #print("hello")
                print(str(e))
                return 'There is a problem'
            totalprice = 0
            if order is not None:
                print("here")
                # Calculating the total price of the basket
                for item in order.items:
                    totalprice = totalprice + item.price
                    print("totalprice=", totalprice)
            # where did we come from cat1: Category 1 page; cat2: Category 2 page; index: index page
            if token == "cat1":
                flash('Item have been added to the basket.')
                return redirect(url_for('view.cat1'))
            elif token == "cat2":
                flash('Item have been added to the basket.')
                return redirect(url_for('view.cat2'))
            elif token == "index":
                flash('Item have been added to the basket.')
                return redirect(url_for('view.index'))
            elif token == "cart":
                return redirect(url_for('cart.cart'))
        else:
            flash('This is already in your basket.')
            print('item already in basket')
            if token == "cat1":
                return redirect(url_for('view.cat1'))
            elif token == "cat2":
                return redirect(url_for('view.cat2'))
            elif token == "index":
                return redirect(url_for('view.index'))
            elif token == "cart":
                return redirect(url_for('cart.cart'))

    return render_template("cart.html", order=order, totalprice=totalprice)


@cartbp.route('/deleteitem', methods=['POST'])
def deleteitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        item_to_delete = Item.query.get(id)
        try:
            order.items.remove(item_to_delete)
            db.session.commit()
            return redirect(url_for('cart.cart'))
        # for debuging purpose
        except SQLAlchemyError as e:
            print("Sqlalchemy Error:", str(e))
            return 'Problem deleting item from order'
    return redirect(url_for('cart.cart'))


@cartbp.route('/emptycart')
def emptycart():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('view.index'))
