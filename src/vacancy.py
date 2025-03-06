class Vacancy:
    """Класс создания вакансии с параметрами"""
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__snippet", "__salary")

    def __init__(
        self,
        name: str,
        url: str,
        salary: str | None | dict = None,
        snippet: str = "Не указан"

    ):
        """Конструктор инициализации объекта класса Vacancy (вакансия работника)"""
        self.__name = name
        self.__url = url
        self.__snippet = snippet if snippet else "Не указан"
        self.__salary = self.__validate(salary)

        self.__list_vacancies.append(self)

    @staticmethod
    def __validate(salary):
        """Метод валидации зарплаты"""
        if isinstance(salary, dict):
            # Убеждаемся, что ключи 'from' и 'to' присутствуют
            from_salary = salary["from"] if salary["from"] else 0
            to_salary = salary["to"] if salary["to"] else 0
            return {"from": from_salary, "to": to_salary}
        else:
            # Если тип данных неожиданный, возвращаем значения по умолчанию
            return {"from": 0, "to": 0}

    def __ge__(self, other):
        """Метод сравнения вакансий по зарплате (верхний порог)"""
        self_salary_to = self.__salary.get("to", 0)
        other_salary_to = other.__salary.get("to", 0)
        return self_salary_to >= other_salary_to


    def __lt__(self, other):
        return (self.salary['from'], self.salary['to']) < (other.salary['from'], other.salary['to'])

    def __str__(self):
        name = self.name
        url = self.url
        salary_from = self.salary["from"]
        salary_to= self.salary["to"]
        snippet = self.snippet

        if salary_from and salary_to:
            salary_info = f"Зарплата от: {salary_from} до: {salary_to}"
        elif not salary_to:
            salary_info = f"Зарплата от: {salary_from}"
        elif not salary_from:
            salary_info = f"Зарплата до: {salary_to}"
        else:
            salary_info = f"Зарплата не указана"

        return (f"Вакансия: {name}\n"
                f"Ссылка: {url}\n"
                f"Требования: {snippet}\n"
                f"{salary_info}\n")

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancy_data in list_vacancies:
            # Валидируем зарплату
            salary = cls.__validate(vacancy_data.get("salary"))

            snippet = vacancy_data.get("snippet", "Не указан")

            if isinstance(snippet, dict):
                snippet = snippet.get("requirement", "")

            # Создаем экземпляр вакансии
            instance = cls(
                name=vacancy_data.get("name"),
                url=vacancy_data.get("alternate_url"),
                salary=salary,
                snippet=snippet,
            )
        return cls.__list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies["salary"].get("from", 0) >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)

    @classmethod
    def list_vacancies(cls):
        """Метод для получения всех вакансий"""
        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def snippet(self):
        return self.__snippet

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "snippet": self.snippet,
        }

if __name__ == "__main__":
    Vacancy.clear_list()
    vacancy_data_list = [
        {
            "name": "Python Developer",
            "url": "https://hh.ru/vacancy/123456",
            "salary": "100000-150000",
            "snippet": "Требования: опыт работы от 3 лет..."
        },
        {
            "name": "Senior Python Developer",
            "url": "https://hh.ru/vacancy/654321",
            "salary": "150000-200000",
            "snippet": "Требования: опыт работы от 5 лет..."
        },
        {
            "name": "Junior Python Developer",
            "url": "https://hh.ru/vacancy/234567",
            "salary": None,
            "snippet": "Требования: опыт работы от 1 года..."
        },
    ]

    Vacancy.cast_to_object_list(vacancy_data_list)

    Vacancy.filtered_salary(0, 150000)
    print(Vacancy.list_vacancies())