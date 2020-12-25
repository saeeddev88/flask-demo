from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.validators import DataRequired, EqualTo


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    family = StringField("Family", validators=[DataRequired()])
    age = IntegerField("Age",
                       validators=[
                           validators.required(),
                           validators.NumberRange(min=1, max=100)
                       ])
