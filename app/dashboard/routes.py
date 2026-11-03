from app.dashboard import dashboard

@dashboard.route('/')
def index():
    return "Dashboard"