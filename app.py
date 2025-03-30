from flask import Flask
from backend.database import db, app as db_app
from backend.models import user, question, answer, vote
from backend.routes import register_routes

app = db_app  # Usamos la instancia de app desde database.py

from markdown import markdown

@app.template_filter("markdown")
def markdown_filter(text):
    return markdown(text)

# Registrar rutas
register_routes(app)

@app.route("/")
def home():
    return "Welcome to StudentOverflow!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Tablas verificadas/creadas correctamente.")
    app.run(debug=True)
