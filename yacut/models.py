import re
from enum import Enum
from random import sample

from sqlalchemy.sql.functions import now

from settings import MAX_SHORT, MAX_URL, MAX_GENERATE, MIN_LENGTH, ALLOWED_CHAR
from yacut import db
from .error_handlers import ApiError, ShortIdGenerateError


class URLMap(db.Model):

    class Items(Enum):
        MAIN = 'main'
        SHORT = 'short'

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL), nullable=False)
    short = db.Column(db.String(MAX_SHORT), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=now())

    def __repr__(self):
        return f'{self.original}'

    @staticmethod
    def get(short_id):
        """Метод получения объекта"""
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def get_unique_short_id():
        """Метод проверки и генерации новой короткой ссылки"""
        short = ''.join(sample(ALLOWED_CHAR, MAX_GENERATE))
        if not URLMap.get(short):
            return short
        raise ShortIdGenerateError('Не удалось сгенерировать короткую ссылку')

    @staticmethod
    def save(**kwargs):
        """Метод сохранения объекта в БД"""
        url = URLMap.from_dict(kwargs)
        db.session.add(url)
        db.session.commit()
        return url

    @staticmethod
    def from_dict(data):
        return URLMap(**data)

    def to_dict(self, url):
        """Метод преобразования объект в словарь"""
        return {
            'url': self.original,
            'short_link': f'{url}{self.short}'
        }

    @classmethod
    def check_attr(cls, value, start, end, pattern, item):
        """Проверка корректности параметра"""
        if (not isinstance(value, str) or not start <= len(value) <= end or
                not re.match(pattern, value)):
            if item == cls.Items.MAIN:
                raise ApiError('Недопустимый url')
            else:
                raise ApiError('Указано недопустимое имя для короткой ссылки')

    @classmethod
    def check_url(cls, value):
        """Проверка корректности входного URL"""
        if not value:
            raise ApiError("\"url\" является обязательным полем!")
        cls.check_attr(
            value, MIN_LENGTH, MAX_URL, r"http(s|)://\w+", cls.Items.MAIN
        )
        return value

    @classmethod
    def check_short_link(cls, value):
        """Проверка короткой ссылки и генерация """
        if not value:
            try:
                return cls.get_unique_short_id()
            except ShortIdGenerateError as error:
                raise ApiError(error)
        cls.check_attr(
            value, MIN_LENGTH, MAX_SHORT, r"^[a-zA-Z0-9_]*$", cls.Items.SHORT
        )
        if URLMap.get(value):
            raise ApiError(f'Имя "{value}" уже занято.')
        return value
