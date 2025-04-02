from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from backend.extensions import db
from backend.models.question import Question
from backend.models.answer import Answer
from backend.models.image import Image
from backend.models.category import Category
from werkzeug.utils import secure_filename
from sqlalchemy import and_
from werkzeug.security import generate_password_hash
import os
from datetime import datetime
from flask import flash

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def index():
    query = request.args.get("q")
    selected_categories = request.args.getlist("categories")
    
    questions_query = Question.query

    if query:
        questions_query = questions_query.filter(Question.title.ilike(f"%{query}%"))

    if selected_categories:
        questions_query = questions_query.join(Question.categories).filter(
            Category.id.in_(selected_categories)
        )

    questions = questions_query.order_by(Question.created_at.desc()).all()
    all_categories = Category.query.order_by(Category.name).all()

    return render_template(
        "index.html",
        questions=questions,
        all_categories=all_categories,
        selected_categories=selected_categories,
        datetime=datetime
    )

@views_bp.route("/profile", methods=["GET"])
@views_bp.route("/profile/<int:user_id>", methods=["GET"])
@login_required
def profile(user_id=None):
    from backend.models.user import User  # asegúrate de tener esto al principio si no lo has importado

    # Determinar a quién mostrar
    user = User.query.get(user_id) if user_id else current_user

    # Búsqueda de preguntas
    q_query = request.args.get("q")
    if q_query:
        questions = Question.query.filter(
            and_(
                Question.user_id == user.id,
                Question.title.ilike(f"%{q_query}%")
            )
        ).order_by(Question.created_at.desc()).all()
    else:
        questions = Question.query.filter_by(user_id=user.id).order_by(Question.created_at.desc()).all()

    return render_template("profile.html", user=user, questions=questions, datetime=datetime)

@views_bp.route("/profile/update", methods=["POST"])
@login_required
def update_profile():
    new_username = request.form.get("username")
    new_email = request.form.get("email")
    new_password = request.form.get("password")

    if new_username and new_username.strip():
        current_user.username = new_username.strip()

    if new_email and new_email.strip():
        current_user.email = new_email.strip()

    if new_password and new_password.strip():
        current_user.password_hash = generate_password_hash(new_password.strip())

    picture = request.files.get("profile_picture")
    if picture and picture.filename:
        # Eliminar imagen anterior si existe
        if current_user.profile_picture:
            old_path = os.path.join(current_app.config["UPLOAD_FOLDER"], current_user.profile_picture)
            if os.path.exists(old_path) and "default_pp.jpg" not in old_path:
                os.remove(old_path)

        # Guardar nueva imagen
        filename = secure_filename(picture.filename)
        picture.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        current_user.profile_picture = filename

    db.session.commit()
    return redirect(url_for("views.profile"))

@views_bp.route("/question/<int:question_id>", methods=["GET"])
def view_question(question_id):
    question = Question.query.get_or_404(question_id)

    # Ordenar respuestas por cantidad de votos
    sorted_answers = sorted(
        question.answers,
        key=lambda a: sum(v.value for v in a.votes),
        reverse=True
    )
    return render_template("question.html", question=question, answers=sorted_answers, datetime=datetime)

@views_bp.route("/question/<int:question_id>/answer", methods=["POST"])
@login_required
def answer_question(question_id):
    question = Question.query.get_or_404(question_id)
    body = request.form.get("body")
    files = request.files.getlist("images")

    if not body:
        return "El cuerpo de la respuesta es obligatorio", 400

    answer = Answer(body=body, question_id=question.id, user_id=current_user.id)
    db.session.add(answer)
    db.session.flush()

    for file in files:
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            db.session.add(Image(filename=filename, answer_id=answer.id))

    db.session.commit()
    return redirect(url_for("views.view_question", question_id=question_id))

@views_bp.route("/ask", methods=["GET", "POST"])
@login_required
def ask():
    all_categories = Category.query.order_by(Category.name).all()

    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        category_names = request.form.getlist("categories")
        files = request.files.getlist("images")

        if not title or not body or not category_names:
            flash("Todos los campos, incluyendo las categorías, son obligatorios.", "danger")
            return render_template("ask.html", all_categories=all_categories)

        new_question = Question(title=title, body=body, user_id=current_user.id)
        db.session.add(new_question)
        db.session.flush()

        for name in category_names:
            category = Category.query.filter_by(name=name).first()
            if not category:
                category = Category(name=name)
                db.session.add(category)
            new_question.categories.append(category)

        for file in files:
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                db.session.add(Image(filename=filename, question_id=new_question.id))

        db.session.commit()
        return redirect(url_for("views.index"))

    return render_template("ask.html", all_categories=all_categories)

@views_bp.route("/answer/<int:answer_id>/vote", methods=["POST"])
@login_required
def vote_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    value = int(request.form.get("value"))  # 1 o -1

    # Verifica si el usuario ya votó esta respuesta
    existing_vote = next((v for v in answer.votes if v.user_id == current_user.id), None)

    if existing_vote:
        existing_vote.value = value  # actualiza el voto
    else:
        from backend.models.vote import Vote
        vote = Vote(user_id=current_user.id, answer_id=answer.id, value=value)
        db.session.add(vote)

    db.session.commit()
    return redirect(url_for("views.view_question", question_id=answer.question_id))

@views_bp.route('/upload', methods=['POST'], endpoint='upload')
def upload():
    f = request.files.get('upload')
    if not f:
        return "No file", 400

    filename = secure_filename(f.filename)
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
    f.save(upload_path)

    file_url = url_for('static', filename='uploads/' + filename)
    return f"""
    <script type='text/javascript'>
        window.parent.CKEDITOR.tools.callFunction({request.args.get('CKEditorFuncNum')}, '{file_url}', 'Imagen subida correctamente');
    </script>
    """

@views_bp.route("/question/<int:question_id>/edit", methods=["GET", "POST"])
@login_required
def edit_question(question_id):
    question = Question.query.get_or_404(question_id)
    all_categories = Category.query.order_by(Category.name).all()

    if question.user_id != current_user.id:
        return "No autorizado", 403

    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        category_names = request.form.getlist("categories")

        if not title or not body or not category_names:
            flash("Todos los campos, incluyendo las categorías, son obligatorios.", "danger")
            return render_template("edit_question.html", question=question, all_categories=all_categories)

        question.title = title
        question.body = body
        question.categories = []

        for name in category_names:
            category = Category.query.filter_by(name=name).first()
            if not category:
                category = Category(name=name)
                db.session.add(category)
            question.categories.append(category)

        db.session.commit()
        return redirect(url_for("views.view_question", question_id=question.id))

    return render_template("edit_question.html", question=question, all_categories=all_categories)

@views_bp.route("/answer/<int:answer_id>/edit", methods=["GET", "POST"])
@login_required
def edit_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    if answer.user_id != current_user.id:
        return "No autorizado", 403

    if request.method == "POST":
        answer.body = request.form.get("body")
        db.session.commit()
        return redirect(url_for("views.view_question", question_id=answer.question_id))

    return render_template("edit_answer.html", answer=answer)
