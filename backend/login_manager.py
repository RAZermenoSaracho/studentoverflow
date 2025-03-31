from flask_login import LoginManager

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from backend.models.user import User  # Importación diferida
    return User.query.get(int(user_id))
