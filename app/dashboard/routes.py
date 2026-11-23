from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import MaintenanceRequest
from app.dashboard import dashboard


@dashboard.route('/dashboard')
@login_required
def index():
    requests = MaintenanceRequest.query.order_by(MaintenanceRequest.created_at.desc()).all()
    return render_template('dashboard.html', requests=requests)


@dashboard.route('/maintenance/new', methods=['GET', 'POST'])
def new_request():
    if request.method == 'POST':
        category = request.form.get('category', '')
        if category == 'Other':
            category = request.form.get('category_other', '').strip() or 'Other'

        db.session.add(MaintenanceRequest(
            user_id=current_user.id if current_user.is_authenticated else None,
            title=request.form.get('title', '').strip(),
            location=request.form.get('location', '').strip(),
            category=category,
            urgency=request.form.get('urgency', 'normal'),
            description=request.form.get('description', '').strip(),
        ))
        db.session.commit()
        return redirect(url_for('dashboard.index'))

    return render_template('new_request.html')


@dashboard.route('/maintenance/<int:request_id>')
def request_detail(request_id):
    maintenance_request = MaintenanceRequest.query.get_or_404(request_id)
    return render_template('request_detail.html', r=maintenance_request)
