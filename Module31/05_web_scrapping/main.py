# TODO здесь писать код
"""Импортируем необходимые библиотеки"""
from bs4 import BeautifulSoup
import requests


"""Функция для получения списка подзаголовков"""
def get_subheadings(url):
    """Отправляем GET-запрос к указанному URL"""
    response = requests.get(url)

    """Определяем тип контента"""
    content_type = response.headers.get('content-type')

    """Проверяем, является ли контент HTML"""
    if 'text/html' in content_type:
        """Инициализируем объект BeautifulSoup для парсинга HTML"""
        soup = BeautifulSoup(response.content, 'html.parser')

        """Находим все теги <h3> на странице"""
        subheadings = soup.find_all('h3')

        """Создаем список заголовков и добавляем каждый в список"""
        subheadings_list = [subheading.text.strip() for subheading in subheadings]

        return subheadings_list
    else:
        return None


"""URL адрес веб-страницы для тестирования"""
url = 'https://example.com/sample-web-page'

"""Вызываем функцию для получения списка подзаголовков"""
result = get_subheadings(url)

"""Выводим результат"""
print(result)