from backend.routes.auth import auth_bp
from backend.routes.views import views_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(views_bp)
