import re
from datetime import datetime
from enum import Enum
from random import sample
from string import digits, ascii_letters

from settings import MAX_SHORT, MAX_URL, MAX_GENERATE, MIN_LENGTH
from yacut import db
from .error_handlers import ApiError


class URLMap(db.Model):

    class Items(Enum):
        MAIN = 'main'
        SHORT = 'short'

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL), nullable=False)
    short = db.Column(db.String(MAX_SHORT), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return f'{self.original}'

    @staticmethod
    def get_unique_short_id():
        """Метод проверки и генерации новой короткой ссылки"""
        short = ''
        while not short:
            preview_short = ''.join(
                sample(f'{digits}{ascii_letters}', MAX_GENERATE)
            )
            if not URLMap.query.filter_by(short=preview_short).first():
                short = preview_short
        return short

    def to_dict(self):
        """Метод преобразования объект в словарь"""
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    @staticmethod
    def check_data(data):
        """Проверка входного словаря Data"""
        if not data:
            raise ApiError('Отсутствует тело запроса')
        if not data.get('url'):
            raise ApiError("\"url\" является обязательным полем!")
        for key in data:
            if key not in ('url', 'custom_id'):
                raise ApiError('Неверные входные данные')

    @classmethod
    def check_attr(cls, value, start, end, pattern, item):
        """Проверка корректности параметра"""
        if (not isinstance(value, str) or not start <= len(value) <= end
                or not re.match(pattern, value)):
            if item == cls.Items.MAIN:
                raise ApiError('Недопустимый url')
            else:
                raise ApiError(f'Указано недопустимое имя для короткой ссылки')

    @classmethod
    def check_url(cls, value):
        """Проверка корректности входного URL"""
        cls.check_attr(
            value, MIN_LENGTH, MAX_URL, r"http(s|)://\w+", cls.Items.MAIN
        )
        return value

    @classmethod
    def check_short_link(cls, value):
        """Проверка короткой ссылки и генерация """
        if not value:
            return cls.get_unique_short_id()
        cls.check_attr(
            value, MIN_LENGTH, MAX_SHORT, r"^[a-zA-Z0-9_]*$", cls.Items.SHORT
        )
        if URLMap.query.filter_by(short=value).first():
            raise ApiError(f'Имя "{value}" уже занято.')
        return value

    def get_new_link(self):
        """Возврат короткой ссылки"""
        return f'http://localhost/{self.short}'
