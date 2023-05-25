from flask import render_template, flash, redirect

from yacut import app
from .error_handlers import ShortIdGenerateError
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Основная функция главное страницы"""
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            try:
                short = URLMap.get_unique_short_id()
            except ShortIdGenerateError as error:
                flash(str(error), 'unique_id')
                return render_template('yacut/main_page.html', form=form)
        else:
            if URLMap.get(short):
                flash(f'Имя {short} уже занято!', 'unique_id')
                return render_template('yacut/main_page.html', form=form)
        form.custom_id.data = None
        return render_template(
            'yacut/main_page.html', form=form,
            url=URLMap.save(original=form.original_link.data, short=short)
        )
    return render_template('yacut/main_page.html', form=form)


@app.route('/<string:short_url>')
def link_short_url(short_url):
    """Редирект по короткой ссылке на основную"""
    return redirect(
        URLMap.query.filter_by(short=short_url).first_or_404().original
    )
