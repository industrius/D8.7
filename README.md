D8.7 Домашнее задание
Добавить страницу в мои закладки
В качестве закрепления нового модуля дополните сигналами проект таск-менеджера на Django и подключите страницу с кэшированием. Также в коде есть ошибка, которую надо поправить. Например, когда была одна задача с единственной категорией и у задачи переключили категорию, счётчик в соответствующей категории останется равен 1. Подумайте, как это можно исправить. Проверьте, как ведёт себя проект при таких угловых случаях и внесите необходимые изменения.

Везде, где есть счётчики задач в категориях, замените их на значения в объекте вместо прямых подсчётов.
Сделайте новый счётчик задач по приоритетам:
Каждый раз, когда создаётся задача по сигналу post_save, вы обновляете счётчик приоритетов. Всего у вас будет столько же объектов, сколько приоритетов в базе.
Счётчики приоритетов можно просто привязать к классу TodoItem и обрабатывать без дополнительных many2many связей.
Выводите счётчики на основной странице index, где мы выводили счётчики задач с категориями.
Запустите ваш проект на Heroku. Не забудьте подключить кэширование, как мы это делали в модуле.
Создайте пользователя-администратора в проекте с логином pws_admin и паролем sf_password.
Добавьте view с кэшированием — это страница, на которой будет только текущее число и дата (datetime.now). Страница (и дата на ней) должна кэшироваться на 5 минут. Это значит, что при первом доступе на этой странице сохраняется дата, но в ближайшие 5 минут от этого она не изменяется.
Ссылку на ваш код в виде проекта на github и ссылку на деплой на Heroku приложите в ответе.


Для проверки задания локально:

1. Создать новый катог виртуального окружения:

python -m venv <Имя каталога виртуального окружения>

2. Стянуть репозиторий к себе, распаковать в каталог проекта - <Имя каталога проекта> и скопировать его в каталог виртуального окружения - <Имя каталога виртуального окружения>.

3. Активировать виртуальное окружение!

4. Перейти в каталог проекта:

cd <Имя каталога проекта>

5. Установить зависимости из requirements.txt:

pip install -r requirements.txt

6. Выполнить миграции для создания БД:

python manage.py migrate

7. Запустить сервер:

python manage.py runserver

8. Открыть URL:

http://127.0.0.1:8000/
