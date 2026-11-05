from flask import render_template,url_for,redirect
from app.auth import auth

@auth.route('/')
def home():
    return redirect( url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register')
def register():
    return render_template('register.html')