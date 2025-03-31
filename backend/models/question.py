from backend.extensions import db
from datetime import datetime
from backend.models.vote import Vote

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)
    votes = db.relationship(Vote, backref='question', lazy=True)

    images = db.relationship("Image", backref="question", cascade="all, delete-orphan")

