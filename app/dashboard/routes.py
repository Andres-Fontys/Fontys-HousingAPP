from flask import render_template
from app.dashboard import dashboard



@dashboard.route('/dashboard')
def index():

    return render_template('dashboard.html')

@dashboard.route('/maintenance/new')
def new_request():
    return render_template('new_request.html')