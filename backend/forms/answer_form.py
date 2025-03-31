from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm):
    body = CKEditorField('Respuesta', validators=[DataRequired()])
    submit = SubmitField('Responder')
