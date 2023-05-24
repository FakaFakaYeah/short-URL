# Проект сервис YaCut.

> Сервис по уменьшению размера ссылок

### Используемые технологии:
* Python 3.7
* Flask 2.0
* Jinja2 3.0
* SQLAlchemy 1.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/FakaFakaYeah/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Заполнить env файл (на всякий случай в settings.py указаны значения по-умолчанию):

```
в проект созда шаблон env файла, добавьте вначале точку, заполните значения
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI= (база данных с которой будет работать)
SECRET_KEY= (ваш секретный ключ)
```

Выполнить миграции
```
flask db upgrade
```

Запустить проект можно командой

```
flask run
```

Проект будет доступен по следующему адресу:

```
http://127.0.0.1:5000/
```

В проекте доступно открытое API со следующими эндпоинтами

```
http://127.0.0.1:5000/api/id/ — POST-запрос на создание новой короткой ссылки
```

```
http://127.0.0.1:5000/api/id/<short_id>/ - GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору. 
```