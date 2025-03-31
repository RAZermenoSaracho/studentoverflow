from backend.extensions import db

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answers.id"), nullable=True)
