import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_SECRET')


MAX_URL = 256  # Максимальная длинна оригинальной ссылки
MAX_SHORT = 16  # Максимальная длинна короткой ссылки
MIN_LENGTH = 1  # Минимальная длинна для ссылок
MAX_GENERATE = 6  # Максимальная длинна короткой ссылки при генерации
