from flask import Flask

def create_app():
    app = Flask(__name__)

    # This Part of the Code is the key that firm the cookies
    app.config['SECRET_KEY'] = '1234'

    # We are working with blueprints this part conect everything.
    from app.auth.routes import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app