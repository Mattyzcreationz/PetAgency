from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional
# Adding pet forms
class addPet(FlaskForm):
    name = StringField(
        'Pet Name', 
        validators=[InputRequired()]    
    )

    species = SelectField(
        'Species', 
        choices =[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
    )
    
    photo_url=StringField(
        'Photo URl', 
        validators=[Optional(), URL()]
    )

    age = IntergerField(
        'Age',
        validators = [Optional(), NumberRange(min=0, max=30)], 
    )
    notes = TextAreaField(
        'Comments',
        validators=[Optional(), Length(min=10)],
    )

class editPet(FlaskForm):
    photo_url = StringField(
        'Photo Url', 
        validators=[Optional(), URL()],
    )
    available = BooleanField('Avaliable?')

    