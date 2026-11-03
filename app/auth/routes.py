from app.auth import auth

@auth.route('/login')
def login():
    return "Login page"

@auth.route('/register')
def register():
    return "Register page"