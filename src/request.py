import requests


def parsing(params: dict, url = "https://api.hh.ru/vacancies", ):
    # Заголовки запроса с токеном авторизации
    headers = {
        'User-Agent': 'my-app/0.0.1'
        # "Authorization": "Bearer YOUR_OAUTH_TOKEN"
    }

    response = requests.get(url, params=params, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        vacancies = response.json()
        print(vacancies['found'])
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")


