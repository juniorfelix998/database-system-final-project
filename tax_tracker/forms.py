from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional

class CompanyForm(FlaskForm):
    name = StringField('Company Name', validators=[DataRequired()])
    industry = StringField('Industry', validators=[Optional()])
    submit = SubmitField('Add Company')

class TaxRecordForm(FlaskForm):
    company_id = SelectField('Company', coerce=int, validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    payment_date = DateField('Payment Date', validators=[Optional()])
    status = SelectField('Status', choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid')
    due_date = SelectField('Due Date', choices=[], validators=[DataRequired()])
    submit = SubmitField('Save')
