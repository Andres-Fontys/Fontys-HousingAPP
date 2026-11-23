from flask import render_template, url_for , redirect, request
from app.dashboard import dashboard

spaces = []

@dashboard.route('/house/add', methods=['POST'])
def addSpace():
    spaceName = request.form['space_name']
    spaces.append(spaceName)
    print(spaceName)
    return redirect(url_for('dashboard.index'))