from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
class UploadForm(FlaskForm):
    description = TextAreaField(
        'Description',
        validators=[
            DataRequired(),
            Length(5, 255,
            message=('Your message is too short.'))
        ]
    )

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'Image Files Only'])
    ])