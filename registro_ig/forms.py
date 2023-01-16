from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,FloatField,SubmitField # crear inputs tipo str
from wtforms.validators import DataRequired,Length,ValidationError


   

class MovementsForm(FlaskForm):
    date = DateField('fecha', validators=[DataRequired(message="la fecha es requerida")])
    concept = StringField('Concepto', validators=[DataRequired(),Length(min=4,message="el concepto es requerido")])
    quantity = FloatField('Cantidad', validators=[DataRequired(message="lacantidad es requerida")])

    submit = SubmitField('Aceptar')

    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida : la fecha introducida es a futuro")