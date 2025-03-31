import os
import json
from flask import Flask

def load_config():
    with open("config/config.json") as f:
        return json.load(f)

def build_db_uri(cfg):
    return f"postgresql://{cfg['DB_USER']}:{cfg['DB_PASSWORD']}@{cfg['DB_HOST']}:{cfg['DB_PORT']}/{cfg['DB_NAME']}"

def create_app():
    config = load_config()

    app = Flask(__name__,
                template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
                static_folder=os.path.join(os.path.dirname(__file__), "..", "static"))
    
    app.secret_key = config["SECRET_KEY"]
    app.config.update({
        "SECRET_KEY": config["SECRET_KEY"],
        "SQLALCHEMY_DATABASE_URI": build_db_uri(config),
        "CKEDITOR_PKG_TYPE": "standard",
        "CKEDITOR_FILE_UPLOADER": "views.upload",
        "UPLOAD_FOLDER": os.path.join(app.static_folder, "uploads")
    })

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    return app
