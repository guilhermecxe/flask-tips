from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    select = SelectField('Select', choices=[], validate_choice=False)
    # validate_choice=False para permitir que escolhas diferentes das pré-selecionadas sejam válidas
    submit = SubmitField('Submit')