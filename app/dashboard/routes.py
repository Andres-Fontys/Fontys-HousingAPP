
from flask import render_template
from flask_login import login_required
from app.dashboard import dashboard


@dashboard.route('/dashboard')
@login_required
def index():
    return render_template('dashboard.html')
