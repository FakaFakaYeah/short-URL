from flask import render_template, flash, redirect

from yacut import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Основная функция главное страницы"""
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!', 'unique_id')
            return render_template('yacut/main_page.html', form=form)
        if not short:
            short = URLMap.get_unique_short_id()
        url = URLMap(original=form.original_link.data, short=short)
        db.session.add(url)
        db.session.commit()
        form.custom_id.data = None
        return render_template('yacut/main_page.html', url=url, form=form)
    return render_template('yacut/main_page.html', form=form)


@app.route('/<string:short_url>')
def link_short_url(short_url):
    """Редирект по короткой ссылке на основную"""
    return redirect(
        URLMap.query.filter_by(short=short_url).first_or_404().original
    )
