from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from app.models import User

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
    
    # This Function check if the username is already taken, and ask to choose a different one
        
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        
        if existing_user_username:
            raise ValidationError(
                "That username already exist. Please Choose a different one"
            )
            
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()

        if existing_user_email:
            raise ValidationError("That email is already registered.")

class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        
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
            DataRequired()
        ]
    )

    submit = SubmitField('Login')
