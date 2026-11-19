
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from app.models import User


# REGISTRATION FORM
class RegisterForm(FlaskForm):

    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=80)
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    submit = SubmitField('Register')

    # Check if username already exists
    def validate_username(self, username):
        value = username.data.strip()

        if '@' in value:
            raise ValidationError(
                "Username cannot contain @. Please choose another."
            )

        existing_user = User.query.filter_by(
            username=value
        ).first()

        if existing_user:
            raise ValidationError(
                "That username already exists. Please choose another."
            )

    # Check if email already exists
    def validate_email(self, email):
        existing_user = User.query.filter_by(
            email=email.data
        ).first()

        if existing_user:
            raise ValidationError(
                "That email is already registered."
            )


# LOGIN FORM

class LoginForm(FlaskForm):

    username_or_email = StringField(
        'Username or Email',
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Login')
