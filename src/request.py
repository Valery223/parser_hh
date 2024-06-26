



import json

def extract_keys(data, parent_key=''):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.append(full_key)
            if isinstance(value, dict):
                keys.extend(extract_keys(value, full_key))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        keys.extend(extract_keys(item, full_key))
    return keys


data = {'items': [{'id': '98906477', 'premium': False, 'name': 'Дегустатор пива', 'department': None, 'has_test': False, 'response_letter_required': True, 'area': {'id': '2760', 'name': 'Бишкек', 'url': 'https://api.hh.ru/areas/2760?locale=RU&host=hh.ru'}, 'salary': {'from': 70000, 'to': None, 'currency': 'KGS', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-06-12T12:21:43+0300', 'created_at': '2024-06-12T12:21:43+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98906477', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/98906477?locale=RU&host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/98906477', 'relations': [], 'employer': {'id': '8636827', 'name': 'ОсОО Балтика', 'url': 'https://api.hh.ru/employers/8636827?locale=RU&host=hh.ru', 'alternate_url': 'https://hh.ru/employer/8636827', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6570954.png', '90': 'https://img.hhcdn.ru/employer-logo/6570953.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/1237630.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=8636827&locale=RU&host=hh.ru', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': None, 'responsibility': 'Заполнение отчетов о качестве и характеристиках каждого образца пива. Участие в <highlighttext>тестировании</highlighttext> и улучшении производственных процессов для обеспечения высокого качества...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '151', 'name': 'Специалист по сертификации'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'employment': {'id': 'part', 'name': 'Частичная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}], 'found': 33637, 'pages': 2000, 'page': 0, 'per_page': 1, 'clusters': None, 'arguments': None, 'fixes': None, 'suggests': None, 'alternate_url': 'https://hh.ru/search/vacancy?accept_temporary=false&enable_snippets=true&items_on_page=1&text=test'}

json_data = json.dumps(data, indent=4)

# Вывод отформатированного JSON
print(json_data)

keys = data.keys()
print(keys)

keys1 = data['items'][0].keys()
print(keys1)
print("\n")
print(extract_keys(data['items'][0]))