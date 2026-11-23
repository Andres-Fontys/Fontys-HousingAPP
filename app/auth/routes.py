

from flask import render_template, url_for, redirect, flash
from app.auth import auth
from app import db
from app.models import User
from app.auth.forms import RegisterForm, LoginForm

from flask_login import login_user, logout_user, login_required

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from sqlalchemy import or_



# HOME - Redirect to login
@auth.route('/')
def home():
    return redirect(url_for('auth.login'))


# LOGIN - Username OR Email + Password


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # TEMPORARY: Check form validation
    if form.is_submitted() and not form.validate():
        print("Login validation errors:", form.errors)

    if form.validate_on_submit():
        identifier = form.username.data.strip()

        # Find user by username OR email
        user = User.query.filter(
            or_(
                User.username == identifier,
                User.email == identifier
            )
        ).first()

        # Verify hashed password
        if user and check_password_hash(
            user.password,
            form.password.data
        ):
            login_user(user)

            flash(
                "Login successful! Welcome to RoomSync.",
                "success"
            )

            return redirect(url_for('dashboard.index'))

        flash(
            "Invalid username/email or password.",
            "danger"
        )

    return render_template('login.html', form=form)


# REGISTER - Create new account
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        # Hash password before storing
        hashed_password = generate_password_hash(
            form.password.data
        )

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash(
            "Account created successfully! Please log in.",
            "success"
        )

        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


# LOGOUT - End user session
@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()

    flash(
        "You have successfully logged out.",
        "success"
    )

    return redirect(url_for('auth.login'))
