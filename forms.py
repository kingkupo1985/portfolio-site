from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=5)])
    email = EmailField('Email', validators=[DataRequired(), Email(message='Please enter a valid email')])
    phone = StringField('Phone Number', validators=[DataRequired(message='Please enter a valid phone')])
    message = CKEditorField('form_message', validators=[DataRequired(message='Please enter a message'), Length(min=50)])
    submit = SubmitField("Send Message")

class MorseCodeForm(FlaskForm):
    morse_code = StringField('English Text', validators=[DataRequired()])
    submit = SubmitField('Encode to Morse Code')

