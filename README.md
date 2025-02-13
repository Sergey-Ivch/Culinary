# CulinaryCanvas
### Описание:
Проект CulinaryCanvas предоставляет возможность пользователям публиковать рецепты своих блюд, редактировать их в любое время, ознакамливаться с чужими рецептами,
подписываться на публикации других авторов и добавлять рецепт в список покупок для удобного отслеживания списка продуктов, которые нужно купить для приготовления выбранных блюд.
Оставлять под рецептами оценку в диапазоне от одного до пяти (целое число) и комментарии.
Рецепты делятся на категории, такие как «Легко», «Средне», «Сложно». Добавлять категории может только администратор.
у рецепта присутствует фотография, ингредиенты, описание, название, время приготовления и категория "сложности".
У ингредиента присутствукт название, единица измерения, и количество.

Публиковать и редактировать рецепты, добавлять комментарии и ставить оценки могут только аутентифицированные пользователи.


### Технологический стек:
![Python](https://img.shields.io/badge/Python-3.7-green) ![Django](https://img.shields.io/badge/Django-2.2.19-green) ![Git Bash](https://img.shields.io/badge/Git_Bash-2.40.0-green)


### Библиотеки:
![Django](https://img.shields.io/badge/Django-2.2.19-green) ![Pillow](https://img.shields.io/badge/Pillow-9.5.0-green)
![pytz](https://img.shields.io/badge/pytz-2025.1-green) ![sorl-thumbnail](https://img.shields.io/badge/sorl--thumbnail-12.9.0-green)
![sqlparse](https://img.shields.io/badge/sqlparse-0.4.4-green)



### Модификаторы Django применяемые в проекте:
![Декоратор](https://img.shields.io/badge/@login_required-gray) ![Paginator](https://img.shields.io/badge/Paginator-gray)
![validators](https://img.shields.io/badge/validators-gray) ![context_processors](https://img.shields.io/badge/context_processors-gray)


### Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в папку с файлом manage.py и выполнить миграции:

```
python manage.py makemigrations users
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

Открыть по ссылке:
```
http://127.0.0.1:8000/
```


### Автор
- [Ивченков Сергей](https://github.com/SleekHarpy)