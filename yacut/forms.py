from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MAX_URL, MAX_SHORT, MIN_LENGTH


class URLMapForm(FlaskForm):

    original_link = URLField(
        'Укажите вашу ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(MIN_LENGTH, MAX_URL),
            URL(message='Неправильный формат URL')
        ]
    )
    custom_id = StringField(
        'Укажите короткий идентификатор',
        validators=[
            Optional(), Length(MIN_LENGTH, MAX_SHORT),
            Regexp(r'^[a-zA-Z0-9_]*$', message='Латинские буквы и цифры')
        ]
    )
    submit = SubmitField('Создать')
