from backend.database import db, app
from backend.models import user, question, answer, vote

with app.app_context():
    db.create_all()
    print("Base de datos creada con éxito.")
