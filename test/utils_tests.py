import json

data = '''{
    "items": [
        {
            "id": "93353083",
            "premium": false,
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
            "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне."
        },
        {
            "id": "92223756",
            "premium": false,
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
}'''


vacancy_data = json.loads(data)


for item in vacancy_data['items']:
    job_title = item['name']
    location = item['area']['name']
    employer_name = item['employer']['name']
    apply_url = item['apply_alternate_url']
    responsibilities = item.get('responsibility', 'Нет информации о обязанностях')

    # Вывод информации
    print(f"Название вакансии: {job_title}")
    print(f"Местоположение: {location}")
    print(f"Работодатель: {employer_name}")
    print(f"Ссылка для подачи заявки: {apply_url}")
    print(f"Обязанности: {responsibilities}")
    print("-" * 40)
