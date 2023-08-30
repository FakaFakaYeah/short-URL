# **ShortURL - Сервис по уменьшению пользовательских ссылок**

### Оглавление
<ol>
 <li><a href="#description">Описание проекта</a></li>
 <li><a href="#stack">Используемые технологии</a></li>
 <li><a href="#architecture">Архитектура проекта</a></li>
 <li><a href="#docker">Как запустить проект в Docker?</a></li>
 <li><a href="#start_project">Как развернуть проект локально?</a></li>
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
![](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
---
### Архитектура проекта<a name="architecture"></a>

| Директория   | Описание                                            |
|--------------|-----------------------------------------------------|
| `migrations` | Содержит миграции проекта                           |
| `yacut`      | Файлы проекта  Flask                                |
| `test`       | Директория с тестами проекта                        |
| `infra`      | Файлы для запуска с помощью Docker, настройки Nginx | 

___
### Как запустить проект в Docker?<a name="docker"></a>
* Запустите терминал и клонируйте репозиторий 
    ```
    git clone https://github.com/FakaFakaYeah/short-URL.git
    ```

* Установите Docker по ссылке https://www.docker.com/products/docker-desktop

* Перейдите в директорию с Docker-compose.yaml
    ```
    cd infra
    ```
  
* Создайте .env файл и заполните его

  Шаблон наполнения env файла

  ```
  FLASK_APP=yacut  # Название приложение
  SECRET_KEY= SECRET_SECRET  # Ваш секретный ключ
  DATABASE_URI=postgresql://postgres:postgres@db:5432/postgres  # Данные для подключения к БД,
  можете указать свои
  DB_ENGINE=django.db.backends.postgresql  # указываем, что работаем с postgresql
  DB_NAME=postgres  # имя базы данных
  POSTGRES_USER=postgres  # логин для подключения к базе данных
  POSTGRES_PASSWORD=postgres  # пароль для подключения к БД (установите свой)
  DB_HOST=db  # название сервиса (контейнера)
  DB_PORT=5432  # порт для подключения к БД
  ```
  
* Выполните команду по разворачиванию docker-compose
    ```
    docker-compose up -d
    ```
  
 Будет проведена сборка образа по Dockerfile и запуск проекта в трех контейнерах

* Выполните миграции по следующей команде:
    ```
    docker compose exec yacut flask db upgrade
    ```
  
* Проект будет доступен по следующим адресам:
  ```
  http://localhost/ - главная страница сайта
  http://localhost/api/id - POST метод для генерации короткой ссылки
  http://localhost/api/id/<string:short_id>/ - Получение длинной ссылки по
  короткому id
  ```

---
### Как развернуть проект локально?<a name="start_project"></a>

* Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone https://github.com/FakaFakaYeah/yacut.git
  ```
  
  ```
  cd yacut
  ```

* Создайте и активируйте виртуальное окружение

  Если у вас Linux/macOS

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
  
  Если у вас windows

  ```
  python -m venv venv
  source venv/scripts/activate
  ```

* Установить зависимости из файла requirements.txt:

  ```
  python3 -m pip install --upgrade pip
  ```
  
  ```
  pip install -r requirements.txt
  ```

* Создайте .env файл и заполните его

  Шаблон наполнения env файла
  ```
  FLASK_APP=yacut  # Название приложение
  SECRET_KEY= SECRET_SECRET  # Ваш секретный ключ
  ```

* Выполнить миграции
  ```
  flask db upgrade
  ```

* Запустить проект

  ```
  flask run
  ```

* Проект будет доступен по следующим адресам:
  ```
  http://127.0.0.1:5000/ - главная страница сайта
  http://127.0.0.1:5000/api/id - POST метод для генерации короткой ссылки
  http://127.0.0.1:5000/api/id/<string:short_id>/ - Получение длинной ссылки по
  короткому id
  ```
___
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