
import os
from urllib import request, response
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask extensions
login_manager = LoginManager()
db = SQLAlchemy()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)



def create_app():
    app = Flask(__name__)

    # SECURITY 1: Secure secret key
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    if not app.config['SECRET_KEY']:
        raise RuntimeError(
            "SECRET_KEY is missing. Set it in your terminal."
        )

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # SECURITY 2: Secure session cookies
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    # True when running with HTTPS in production
    app.config['SESSION_COOKIE_SECURE'] = (
        os.environ.get('SESSION_COOKIE_SECURE') == '1'
    )

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    login_manager.login_view = 'auth.login'

    # Import User model
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return db.session.get(User, int(user_id))
        except (TypeError, ValueError):
            return None


    # Register Blueprints
    from app.auth import auth
    app.register_blueprint(auth)

    from app.dashboard import dashboard
    app.register_blueprint(dashboard)

    # Create database tables for local development
    with app.app_context():
        db.create_all()

    # Custom error page for too many requests
    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        return render_template('429.html'), 429

    @app.after_request
    def prevent_sensitive_page_caching(response):
        if request.path.startswith(('/dashboard', '/maintenance')):
            response.headers['Cache-Control'] = 'no-store'
        return response

    return app
