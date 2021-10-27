def home():
    """Главный обработчик маршрутy "/api/" """
    return "Hello world"

def get_all():
    """Обработчик маршрутy "/api/news" """
    return "All pages"

def get_one(news_one):
    """Обработчик маршруту "/api/news/<news_id>" """
    return news_one

def update_one(id):
    """Обработчик маршруту "/api/news-update/<news_id>" """
    pass

def delete_one(id):
    """Обработчик маршруту "/api/news-delete/<news_id>" """
    pass