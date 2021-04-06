from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField
from wtforms.validators import DataRequired,Length, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField(
        'Description',
        [
            DataRequired(),
            Length(5, 255,
            message=('Your message is too short.'))
        ]
    )

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'Image Files Only'])
    ])