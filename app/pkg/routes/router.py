from pkg.build.application import app, request

from pkg.handlers.handler import *
from pkg.repository.user import *

"""Маршруты API-шки [NEWS] і [USER'a]"""

@app.route("/api/", methods=['GET'])
def homepage():
    """Главная страница"""  
    return home()

@app.route("/api/news", methods=['GET'])
def get_all_news():
    """Отримання усіх новин"""
    return get_all()

@app.route("/api/news/<news_id>", methods=['GET'])
def get_one_news(news_id):
    """Отримання одної новини по [news_id] """
    return get_one(news_id)

@app.route("/api/news-update/<news_id>", methods=['GET', 'UPDATE'])
def update_one_news(news_id):
    """Обновлення одної новини по [news_id] """
    return update_one(news_id)

@app.route("/api/news-delete/<news_id>", methods=['DELETE'])
def delete_one_news(news_id):
    """Видалення одної новини по [news_id] """
    return delete_one(news_id)

####################### USER ##################
data = dict()

@app.route("/login", methods=['GET', 'POST'])
def user_account_login():
    """Аутентифікація і авторизація користувача"""
    data = request.get_json()
    get_user_from_db(data)
    return dict({"response": "Good"})


@app.route("/registration", methods=['GET', 'POST'])
def user_accout_registration():
    """Регістрація користувача"""
    data = request.get_json()
    add_user_to_db(data)
    return dict({"response": "Good"})


def init_routers():
    """Функция стартер остальных методов маршрутизации =)"""
    homepage()