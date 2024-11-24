import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle_error(response):
    """Обработка ошибок при выполнении запроса."""
    if response.status_code != 200:
        logger.error(f"Ошибка при запросе: {response.status_code} - {response.text}")
        return False
    return True


def get_data(response):
    """Получение данных из ответа."""
    return response.json().get('items', [])


class HH:
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Инициализация объекта для отправки GET-запросов."""
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword, max_pages=20):
        """Метод отправки GET-запроса на сайт Head Hunter."""
        self.params['text'] = keyword
        while self.params['page'] < max_pages:
            response = requests.get(self._url, headers=self._headers, params=self.params)
            if handle_error(response):
                vacancies = get_data(response)
                self.vacancies.extend(vacancies)
                if not vacancies:
                    break
                self.params['page'] += 1
            else:
                break



if __name__ == "__main__":
    hh_parser = HH()
    hh_parser.load_vacancies('Python Developer')
    logger.info(f"Найдено вакансий: {len(hh_parser.vacancies)}")
