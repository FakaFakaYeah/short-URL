# Сервис по уменьшению пользовательских ссылок

### Оглавление
<ol>
 <li><a href="#description">Описание проекта</a></li>
 <li><a href="#stack">Используемые технологии</a></li>
 <li><a href="#architecture">Архитектура проекта</a></li>
 <li><a href="#start_project">Как развернуть проект локально?</a></li>
 <li><a href="#url">Ссылки проекта</a></li>
 <li><a href="#author">Авторы проекта</a></li>
</ol>

---
### Описание проекта:<a name="description"></a>
Сервис предназначен для уменьшения пользовательских ссылок различной длинны.
Пользователь может предоставить свой вариант короткой ссылки длинной не более 16 символов. Если пользователь не предоставляет свой вариант, за него автоматически генерируется короткая ссылка длинной 6 символов. Дубликаты исключены.

___
### **Используемые технологии**<a name="stack"></a>
![](https://img.shields.io/badge/Python-grey?style=for-the-badge&logo=python&logoColor=yellow)
![](https://img.shields.io/badge/Flask-3CB371?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/SQL_Alchemy-red?style=for-the-badge)
![](https://img.shields.io/badge/Git_Hub-grey?style=for-the-badge&logo=github&logoColor=white)
![](https://img.shields.io/badge/PYTEST-blue?style=for-the-badge&logo=pytest&logoColor=white)
![](https://img.shields.io/badge/ALEMBIC-FFA500?style=for-the-badge)

---
### Архитектура проекта<a name="architecture"></a>

| Директория   | Описание                     |
|--------------|------------------------------|
| `migrations` | Содержит миграции проекта    |
| `yacut`      | Файлы проекта  Flask         |
| `test`       | Директория с тестами проекта |  

---
### Как развернуть проект локально?<a name="start_project"></a>

* Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone https://github.com/FakaFakaYeah/yacut.git
  ```
  
  ```
  cd yacut
  ```

* Cоздать и активировать виртуальное окружение:

  ```
  python3 -m venv venv
  ```

  Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

  Если у вас windows

    ```
    source venv/scripts/activate
    ```

* Установить зависимости из файла requirements.txt:

  ```
  python3 -m pip install --upgrade pip
  ```
  
  ```
  pip install -r requirements.txt
  ```

* Заполнить env файл (на всякий случай в settings.py указаны значения по-умолчанию):

  ```
  в проекте создан шаблон env файла, добавьте вначале точку, заполните значения
  FLASK_APP=yacut
  FLASK_ENV=development
  DATABASE_URI= (база данных с которой будет работать)
  SECRET_KEY= (ваш секретный ключ)
  ```

* Выполнить миграции
  ```
  flask db upgrade
  ```

* Запустить проект

  ```
  flask run
  ```

* Проект будет доступен по следующему адресу:

  ```
  http://127.0.0.1:5000/
  ```

### Ссылки проекта<a name="url"></a>

  ```
  http://127.0.0.1:5000/api/id/ — POST-запрос на создание новой короткой ссылки
  ```
  
  ```
  http://127.0.0.1:5000/api/id/<short_id>/ - GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору. 
  ```

---

### Авторы проекта:<a name="author"></a>
Смирнов Степан
<div>
  <a href="https://github.com/FakaFakaYeah">
    <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/GitHub.png" title="GitHub" alt="Github" width="39" height="39"/>&nbsp
  </a>
  <a href="https://t.me/s_smirnov_work" target="_blank">
      <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp
  </a>
</div>