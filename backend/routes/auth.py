from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from backend.extensions import db
from backend.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for("auth.signup"))

        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash("El nombre de usuario o correo ya está en uso", "warning")
            return redirect(url_for("auth.signup"))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, profile_picture="default_pp.jpg")
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('views.index'))

    return render_template("signup.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("El correo no está registrado", "warning")
            return redirect(url_for("auth.login"))

        if not check_password_hash(user.password_hash, password):
            flash("Contraseña incorrecta", "warning")
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("views.index"))

    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
