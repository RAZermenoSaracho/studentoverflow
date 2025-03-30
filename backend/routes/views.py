from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from backend.database import db
from backend.models.user import User
from backend.models.question import Question
from backend.models.answer import Answer

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def index():
    query = request.args.get("q")
    if query:
        questions = Question.query.filter(Question.title.ilike(f"%{query}%")).all()
    else:
        questions = Question.query.order_by(Question.created_at.desc()).all()
    return render_template("index.html", questions=questions)

@views_bp.route("/profile", methods=["GET"])
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@views_bp.route("/profile/update", methods=["POST"])
@login_required
def update_profile():
    current_user.username = request.form.get("username")
    current_user.email = request.form.get("email")
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
    return render_template("question.html", question=question, answers=sorted_answers)

@views_bp.route("/question/<int:question_id>/answer", methods=["POST"])
@login_required
def answer_question(question_id):
    question = Question.query.get_or_404(question_id)
    body = request.form.get("body")
    answer = Answer(body=body, question_id=question.id, user_id=current_user.id)
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for("views.view_question", question_id=question_id))

@views_bp.route("/ask", methods=["GET", "POST"])
@login_required
def ask():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        if not title or not body:
            return "Faltan campos", 400

        new_question = Question(title=title, body=body, user_id=current_user.id)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for("views.index"))

    return render_template("ask.html")

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

