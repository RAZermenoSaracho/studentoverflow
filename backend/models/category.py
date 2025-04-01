from backend.extensions import db

question_category = db.Table(
    'question_category',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    questions = db.relationship('Question', secondary=question_category, back_populates='categories')
