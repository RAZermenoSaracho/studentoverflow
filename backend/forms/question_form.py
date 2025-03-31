from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    body = CKEditorField('Detalles', validators=[DataRequired()])
    submit = SubmitField('Publicar pregunta')
