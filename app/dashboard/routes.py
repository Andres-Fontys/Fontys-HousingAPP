from flask import render_template
from app.dashboard import dashboard

@dashboard.route('/dashboard')
def index():
    return render_template('dashboard.html')