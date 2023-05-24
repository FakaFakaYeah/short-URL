from http import HTTPStatus

from flask import render_template, jsonify

from yacut import db, app


class ApiError(Exception):

    def __init__(self, message, code=HTTPStatus.BAD_REQUEST):
        super().__init__()
        self.message = message
        self.code = code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(ApiError)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    return render_template('error/404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    db.session.rollback()
    return render_template('error/500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
