from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# This is part of the Library flask login, allow us to save sessions.

login_manager = LoginManager()


# We are usign SQLAlchemy to control our database
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # This Part of the Code is the key that firm the cookies and sessions.
    app.config['SECRET_KEY'] = '1234'
    
    # This part configurate the database we are using the library SQLALCHEMY and we are working in SQLITE
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    # From Lines 22 to 26 just create our Database
    db.init_app(app)
    
    from app.models import User

    with app.app_context():
        db.create_all()
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

# This just connect our folder auth,dashboard,etc with the app is part of Flask Blueprint a form to work in modules.
    from app.auth import auth
    app.register_blueprint(auth)
    
    from app.dashboard import dashboard
    app.register_blueprint(dashboard)

    return app