from flask import Flask
from application.model import db, load_db
from flask_bootstrap import Bootstrap

app = Flask(__name__)


# create a function that creates a web application
# a web server will run this web application
def create_app():
    app.debug = True
    # secret_key for session
    app.secret_key = 'g3h^rmRd67kWpyqAhUed!5Yz&4mF!R6C@E-#Ug?tHQXH@5Ypw?nM^N5uW+shHR8vD5'
    # set the app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite'

    # initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    # the load_db(db) fuction was used for testing
    with app.test_request_context():
        load_db(db)
    ################################################

    # importing modules here to avoid circular references, register blueprints of routes
    from application.cart import cartbp
    from application.view import viewbp
    from application.admin import adminbp

    # Register Blueprint
    app.register_blueprint(cartbp)
    app.register_blueprint(viewbp)
    app.register_blueprint(adminbp)

    return app
