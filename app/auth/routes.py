from flask import render_template,url_for,redirect
from app.auth import auth
from app import db
from app.models import User
from app.auth.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

@auth.route('/')
def home():
    return redirect( url_for('auth.login'))

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        check_password = check_password_hash(user.password,form.password.data)
        if check_password:
            login_user(user)
            return redirect(url_for('dashboard.index'))
           

    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('dashboard'))
    return render_template('register.html',form=form)

# @auth.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect('login.html')

