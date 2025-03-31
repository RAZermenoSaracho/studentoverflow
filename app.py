from config.init_app import create_app, load_config
from config.init_db import ensure_database_exists
from backend.extensions import db, ckeditor, login_manager
from backend.models.user import User
from backend.routes import register_routes  # Asegúrate de tener esta función

config = load_config()
ensure_database_exists(config)

app = create_app()
app.jinja_env.add_extension('jinja2.ext.do')

# Inicializar extensiones
db.init_app(app)
ckeditor.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

register_routes(app)

@app.template_filter("markdown")
def markdown_filter(text):
    from markdown import markdown
    return markdown(text)

@app.route("/")
def home():
    return "Welcome to StudentOverflow!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
