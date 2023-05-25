from http import HTTPStatus

from flask import jsonify, request

from yacut import app
from .error_handlers import ApiError
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url():
    """Метод создания короткой ссылки"""
    data = request.get_json()
    if not data:
        raise ApiError('Отсутствует тело запроса')
    original = URLMap.check_url(data.get('url'))
    short = URLMap.check_short_link(data.get('custom_id'))
    return jsonify(
        URLMap.save(original=original, short=short).to_dict(request.host_url)
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/')
def get_original_link(short_id):
    """Получение полной ссылки по короткому id"""
    url = URLMap.get(short_id)
    if not url:
        raise ApiError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify(url=url.original), HTTPStatus.OK
