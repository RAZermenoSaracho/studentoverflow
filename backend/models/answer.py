from backend.extensions import db
from datetime import datetime
from backend.models.vote import Vote

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    votes = db.relationship(Vote, backref='answer', lazy=True)

    images = db.relationship("Image", backref="answer", cascade="all, delete-orphan")

