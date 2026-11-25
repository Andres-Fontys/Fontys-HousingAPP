from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(255))

class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)  # empty if nobody is logged in
    title = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    urgency = db.Column(db.String(10), nullable=False, default="normal")
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="unseen")  # unseen, reviewed, in_progress, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def status_label(self):
        return self.status.replace("_", " ").capitalize()