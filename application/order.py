from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, IntegerField
from wtforms.validators import InputRequired, email


# form used for checkout
class CheckoutForm(FlaskForm):
    first_name = StringField("Your first name", validators=[InputRequired()])
    last_name = StringField("Your surname", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    street = StringField("Your address", validators=[InputRequired()])
    suburb = StringField("Your suburb", validators=[InputRequired()])
    state = StringField("Your State", validators=[InputRequired()])
    zip = IntegerField("Your Postal Code", validators=[InputRequired()])
    card = IntegerField("Credit Card Number", validators=[InputRequired()])
    expiry = IntegerField("Expiry xxxx", validators=[InputRequired()])
    cvs = IntegerField("CSV", validators=[InputRequired()])
    card_name = StringField("Credit Card Name", validators=[InputRequired()])

    submit = SubmitField("Finalise Purchase")
