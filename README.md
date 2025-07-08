Установить и активировать виртуальную среду


```
    python -m venv venv
    venv/Scripts/activate
```

Установка пакетов на новой машине:

```
pip install -r requirements.txt
```

Создаем базу данных и делаем миграцию
```
python manage.py makemigrations
python manage.py migrate
```
Создаем супер пользователя
```
python manage.py createsuperuser
```

Запускаем проект
```
python manage.py runserver
```
