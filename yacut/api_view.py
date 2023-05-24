from http import HTTPStatus

from flask import jsonify, request

from yacut import db, app
from .error_handlers import ApiError
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url():
    """Метод создания короткой ссылки"""
    data = request.get_json()
    URLMap.check_data(data)
    original = URLMap.check_url(data.get('url'))
    short = URLMap.check_short_link(data.get('custom_id'))
    url = URLMap(original=original, short=short)
    db.session.add(url)
    db.session.commit()
    return jsonify(
        url=url.original, short_link=url.get_new_link()
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/')
def get_original_link(short_id):
    """Получение полной ссылки по короткому id"""
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise ApiError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify(url=url.original), HTTPStatus.OK
