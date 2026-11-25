
from flask import url_for, redirect
from app.dashboard import dashboard
from app.dashboard.forms import SpaceForm

spaces = []
tints = ["blue", "green", "yellow", "purple"]


@dashboard.route('/house/add', methods=['POST'])
def addSpace():
    form = SpaceForm()

    if form.validate_on_submit():
        spaceName = form.space_name.data
        spaceType = form.space_type.data

        spaceColor = tints[len(spaces) % len(tints)]

        spaces.append({
            "name": spaceName,
            "color": spaceColor,
            "type": spaceType
        })

    return redirect(url_for('dashboard.index'))
