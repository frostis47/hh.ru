import json


def filter_by_salary(min_salary, vacancies):
    """Метод фильтрации списка вакансий по заработной плате"""
    return [
        vacancy for vacancy in vacancies
        if isinstance(vacancy.salary, dict) and vacancy.salary.get("from", 0) >= min_salary
    ]


class Vacancy:
    def __init__(self, name, city, salary, data_base_hh=None):
        self.name = name
        self.city = city
        self.salary = salary
        self.data_base_hh = data_base_hh
        self.result = []
        if data_base_hh:
            self.__reform_file(data_base_hh)

    def filter_city(self):
        """Возвращает список вакансий в данном городе."""
        return [self]

    def __reform_file(self, data_hh):
        """Метод для обработки JSON-ответа от сайта HH.ru"""
        for item in data_hh.get('items', []):
            salary_info = item.get("salary")
            url = item.get("apply_alternate_url", "")
            description = item.get("responsibility", "")

            if salary_info is None:
                salary = {"from": 0, "to": 0}
            elif salary_info.get("currency") == 'RUR':
                salary = {
                    "from": salary_info.get("from", 0) or 0,
                    "to": salary_info.get("to", 0) or 0
                }
            else:
                continue

            self.result.append({
                "name": item.get("name", "Не указано"),
                "city": item.get("area", {}).get("name", "Не указано"),
                "salary": salary,
                "url": url,
                "description": description,
                "employer": item.get("employer", {}).get("name", "Не указано")
            })

    @classmethod
    def from_dict(cls, vacancy):
        """Создает объект Vacancy из словаря."""
        return cls(
            name=vacancy.get("name", "Не указано"),
            city=vacancy.get("area", {}).get("name", "Не указано"),
            salary=vacancy.get("salary", {"from": 0}),
            data_base_hh=vacancy
        )



if __name__ == "__main__":
    data = {
        "items": [
            {
                "id": "93353083",
                "premium": False,
                "name": "Тестировщик комфорта квартир",
                "area": {
                    "id": "26",
                    "name": "Воронеж"
                },
                "salary": {
                    "from": 350000,
                    "to": 450000,
                    "currency": "RUR"
                },
                "employer": {
                    "name": "Специализированный застройщик BM GROUP"
                },
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
                "schedule": {
                    "id": "flexible",
                    "name": "Гибкий график"
                },
                "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в "
                                  "спальне."
            },
            {
                "id": "92223756",
                "premium": False,
                "name": "Удаленный диспетчер чатов (в Яндекс)",
                "area": {
                    "id": "113",
                    "name": "Москва"
                },
                "employer": {
                    "name": "Яндекс"
                },
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
                "schedule": {
                    "id": "flexible",
                    "name": "Гибкий график"
                },
                "responsibility": "Обрабатывать входящие чаты и поддерживать клиентов."
            }
        ]
    }

    vacancies = [Vacancy.from_dict(item) for item in data["items"]]

    filtered_by_city = [vacancy for vacancy in vacancies if vacancy.city == "Воронеж"]
    print("Вакансии в городе Воронеж:", [vacancy.name for vacancy in filtered_by_city])

    filtered_by_salary = filter_by_salary(70000, vacancies)
    print("Вакансии с зарплатой от 70000:", [vacancy.name for vacancy in filtered_by_salary])
