from abc import ABC, abstractmethod
import json
import os


class JSONVacancy(ABC):
    """Абстрактный класс для работы с JSON-файлами вакансий"""

    @abstractmethod
    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, words_del):
        """Метод для удаления ненужных данных из файла"""
        pass

    @abstractmethod
    def vacancy_from_file(self, words_sample):
        """Метод для выборки нужных данных из файла"""
        pass

    @abstractmethod
    def full_data_from_file(self):
        """Метод для получения всех данных из файла"""
        pass


class HHVacancy(JSONVacancy):
    """Класс для работы с вакансиями с сайта HH.ru"""

    def __init__(self, file_name_save='data/suitable_vacancies.json'):
        """Инициализатор класса"""
        self.__file_name_save = file_name_save

    def get_file_name(self):
        return self.__file_name_save

    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        if not stock_list:
            print("Вакансий с такими критериями не найдено")
            return

        try:
            # Загружаем существующие данные, если файл существует
            data = []
            if os.path.exists(self.get_file_name()):
                with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                    data = json.load(file)

            for vacancy in stock_list:
                if vacancy.to_json() not in data:
                    data.append(vacancy.to_json())


            with open(self.get_file_name(), 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except json.JSONDecodeError:
            print("Ошибка: файл поврежден или не в формате JSON.")
        except Exception as e:
            print(f"Ошибка при сохранении вакансий: {e}")

    def delete_vacancy(self, words_del):
        """Метод для удаления ненужных данных из файла"""
        if not os.path.exists(self.get_file_name()):
            return 'Файла с таким названием не существует'

        try:
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)

            filtered_data = [
                vacancy for vacancy in data
                if (words_del != vacancy['city'] and
                    words_del not in vacancy['name'] and
                    words_del not in vacancy['description'])
            ]

            # Сохраняем отфильтрованные данные в файл
            with open(self.get_file_name(), 'w', encoding="utf-8") as file:
                json.dump(filtered_data, file, indent=4, ensure_ascii=False)

            return filtered_data

        except Exception as e:
            return f"Ошибка при удалении вакансий: {e}"

    def vacancy_from_file(self, words_sample):
        """Метод для выборки нужных данных из файла"""
        if not os.path.exists(self.get_file_name()):
            return 'Файла с таким названием не существует'

        try:
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)

            result_data = [
                vacancy for vacancy in data
                if (words_sample in vacancy["description"] or
                    words_sample == vacancy['name'] or
                    words_sample == vacancy['city'])
            ]

            return result_data

        except Exception as e:
            return f"Ошибка при выборке вакансий: {e}"

    def full_data_from_file(self):
        """Метод для получения всех данных из файла"""
        if not os.path.exists(self.get_file_name()):
            return 'Файла с таким названием не существует'

        try:
            with open(self.get_file_name(), 'r', encoding="utf-8") as file:
                data = json.load(file)
            return data

        except Exception as e:
            return f"Ошибка при получении всех данных: {e}"