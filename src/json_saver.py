import json
import os.path

from src.base_json_saver import BaseJsonSaver
from src.vacancy import Vacancy


class JSONSaver(BaseJsonSaver):
    """Класс для сохранения, добавления и изменения вакансий в json-файле"""

    def __init__(self, file_saver: str = "data/filtered_vacancies.json"):
        """Констркутор, инициализирует путь до файла (для работы с ним)"""
        self.__file_saver = file_saver
        if not os.path.exists(file_saver):
            with open(file_saver, "w") as file:
                json.dump([], file)

    def load_info_json(self):
        """Метод получения данных из файла"""
        with open(self.__file_saver, encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file

    def add_vacancy(self, vacancy: Vacancy):
        """Метод добавления вакансий в файл json"""
        old_vacancies = self.load_info_json()
        dict_vacancy = vacancy.to_dict()
        if dict_vacancy not in old_vacancies:
            print("такая вакансия уже есть")
            return
        old_vacancies.append(dict_vacancy)
        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        """Метод удаления вакансий из файла json"""
        old_vacancies: object = self.load_info_json()
        dict_vacancy = vacancy.to_dict()

        if dict_vacancy in old_vacancies:
            old_vacancies.remove(dict_vacancy)
            with open(self.__file_saver, "w", encoding="utf-8") as file:
                json.dump(old_vacancies, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100000 - 130000",
                      "Требования: опыт работы от 3 лет...")

    json_saver = JSONSaver("../data/filtered_vacancies.json")
    json_saver.add_vacancy(vacancy)
