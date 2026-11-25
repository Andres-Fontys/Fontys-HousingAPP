from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class SpaceForm(FlaskForm):

    space_name = StringField(
        "Space name",
        validators=[DataRequired()]
    )

    space_type = SelectField(
        "Space type",
        choices=[
            ("room", "Room"),
            ("shared_space", "Shared Space")
        ],
        validators=[DataRequired()]
    )