import requests
from bs4 import BeautifulSoup
import re

def get_subheadings(url):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все теги <h3> и извлекаем их текст
        h3_tags = soup.find_all('h3')
        subheadings = [tag.get_text() for tag in h3_tags]

        return subheadings
    else:
        # Выводим сообщение об ошибке, если запрос не удался
        print(f"Error {response.status_code}: Unable to fetch the page content.")
        return None

# Пример использования
url = 'http://www.columbia.edu/~fdc/sample.html'
result = get_subheadings(url)

if result:
    print(result)