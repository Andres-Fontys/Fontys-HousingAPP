
from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required
from app import db
from app.models import MaintenanceRequest
from app.dashboard import dashboard
from app.dashboard.space import SpaceForm , spaces


@dashboard.route('/dashboard')
@login_required
def index():
    requests = (
        MaintenanceRequest.query
        .filter_by(user_id=current_user.id)
        .order_by(MaintenanceRequest.created_at.desc())
        .all()
    )
    return render_template('dashboard.html', requests=requests,  form=SpaceForm() , spaces=spaces)


@dashboard.route('/maintenance/new', methods=['GET', 'POST'])
@login_required
def new_request():
    if request.method == 'POST':
        category = request.form.get('category', '')
        if category == 'Other':
            category = request.form.get('category_other', '').strip() or 'Other'

        db.session.add(MaintenanceRequest(
            user_id=current_user.id,
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
@login_required
def request_detail(request_id):
    maintenance_request = MaintenanceRequest.query.get_or_404(request_id)

    if maintenance_request.user_id != current_user.id:
        abort(403)

    return render_template('request_detail.html', r=maintenance_request)
