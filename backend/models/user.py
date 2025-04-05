from backend.extensions import db
from datetime import datetime
from backend.models.vote import Vote
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    questions = db.relationship('Question', backref='author', lazy=True)
    answers = db.relationship('Answer', backref='author', lazy=True)
    votes = db.relationship(Vote, backref='voter', lazy=True)
    profile_picture = db.Column(db.String(256), nullable=True)

    @property
    def points(self):
        a_votes = sum(v.value for a in self.answers for v in a.votes)
        return a_votes

    @property
    def rank(self):
        from backend.models.user import User
        users = User.query.all()
        ranked = sorted(users, key=lambda u: u.points, reverse=True)
        for i, u in enumerate(ranked, start=1):
            if u.id == self.id:
                return i
        return None
