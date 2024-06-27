import requests

from sqlalchemy import select
from sqlalchemy.engine import Result

from core.models import Area, Type, Salary, Vacancy, Employer, Snippet
from .shemas import AreaCreate, TypeCreate, SalaryCreate, EmployerCreate, SnippetCreate

from . import crud
# from .crud import vacancy_get_one, vacancy_create, area_get_one, area_create

async def parsing(params: dict, url = "https://api.hh.ru/vacancies"):
    # Заголовки запроса с токеном авторизации
    headers = {
        'User-Agent': 'my-app/0.0.1'
        # "Authorization": "Bearer YOUR_OAUTH_TOKEN"
    }
    return requests.get(url, params=params, headers=headers)

async def vacancy_get_one(params: dict, session):
    response = await parsing(params = params)
    print("----------------------hello2\n\n\n")

    if response.status_code == 200:
        print("----------------------hello3\n\n\n")
        vacancies = response.json()
        print(vacancies['items'][0])
        await add_vacancy(session, vacancies['items'][0])
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
    

async def add_vacancy(session, vacancy_data):

    vacancy = await crud.get_one(session= session, model=Vacancy, key = vacancy_data['id'])

    if not vacancy:
        area_data = vacancy_data['area']
        if area_data is not None:
            area = await crud.get_one(session= session, model=Area, key = area_data['id'])
            if not area:
                area = AreaCreate(id=area_data['id'], name=area_data['name'], url=area_data['url'])
                await crud.create(session=session, model=Area, scheme_in = area)

        type_data = vacancy_data['type']
        if type_data is not None:
            type_ = await crud.get_one(session = session, model=Type, key =type_data['id'])
            if not type_:
                type_ = TypeCreate(id=type_data['id'], name=type_data['name'])
                await crud.create(session=session, model=Type, scheme_in=type_)
        
        salary_data = vacancy_data['salary']
        if salary_data is not None:
            # salary в любом случае создаем(если не None)
            salary = SalaryCreate(salary_from =  salary_data['from'], salary_to= salary_data['to'],
                                currency = salary_data['currency'], gross = salary_data['gross'])
            await crud.create(session=session, model=Salary, scheme_in=salary)

        employer_data = vacancy_data['employer']
        if employer_data is not None:
            employer = await crud.get_one(session= session, model = Employer, key = employer_data['name'])
            if not employer:
                employer = EmployerCreate(id = employer_data['id'], name = employer_data['name'],
                                          url = employer_data['url'], alternate_url= employer_data['alternate_url'],
                                          vacancies_url=employer_data['vacancies_url'], trusted= employer_data["trusted"],
                                          accredited_it_employer=employer_data['accredited_it_employer'])
                await crud.create(session=session, model=Employer, scheme_in=employer)
        
        snippet_data = vacancy_data['snippet']
        if snippet_data is not None:
            # snippet в любом случае создаем(если не None)
            snippet = SnippetCreate(requirement=snippet_data['requirement'], responsibility=snippet_data['responsibility'])
            await crud.create(session=session, model=Snippet, scheme_in=snippet)
        

    # employer = session.query(Employer).filter_by(id=employer_data['id']).first()
    # if not employer:
    #     employer = Employer(
    #         id=employer_data['id'], 
    #         name=employer_data['name'], 
    #         url=employer_data['url'], 
    #         alternate_url=employer_data['alternate_url'],
    #         logo_urls=employer_data['logo_urls'], 
    #         vacancies_url=employer_data['vacancies_url'],
    #         accredited_it_employer=employer_data['accredited_it_employer'],
    #         trusted=employer_data['trusted']
    #     )
    #     session.add(employer)
    
    # vacancy = vacancy_get_one(session,id=vacancy['id'])
    # if not vacancy:
    #     vacancy = Vacancy(
    #         id=vacancy_data['id'],
    #         premium=vacancy_data['premium'],
    #         name=vacancy_data['name'],
    #         department=vacancy_data['department'],
    #         has_test=vacancy_data['has_test'],
    #         response_letter_required=vacancy_data['response_letter_required'],
    #         area=area,
    #         salary=vacancy_data['salary'],
    #         type=vacancy_data['type'],
    #         address=vacancy_data['address'],
    #         response_url=vacancy_data['response_url'],
    #         sort_point_distance=vacancy_data['sort_point_distance'],
    #         published_at=datetime.datetime.fromisoformat(vacancy_data['published_at']),
    #         created_at=datetime.datetime.fromisoformat(vacancy_data['created_at']),
    #         archived=vacancy_data['archived'],
    #         apply_alternate_url=vacancy_data['apply_alternate_url'],
    #         show_logo_in_search=vacancy_data['show_logo_in_search'],
    #         insider_interview=vacancy_data['insider_interview'],
    #         url=vacancy_data['url'],
    #         alternate_url=vacancy_data['alternate_url'],
    #         relations=vacancy_data['relations'],
    #         employer=employer,
    #         snippet=vacancy_data['snippet'],
    #         contacts=vacancy_data['contacts'],
    #         schedule=vacancy_data['schedule'],
    #         working_days=vacancy_data['working_days'],
    #         working_time_intervals=vacancy_data['working_time_intervals'],
    #         working_time_modes=vacancy_data['working_time_modes'],
    #         accept_temporary=vacancy_data['accept_temporary'],
    #         professional_roles=vacancy_data['professional_roles'],
    #         accept_incomplete_resumes=vacancy_data['accept_incomplete_resumes'],
    #         experience=vacancy_data['experience'],
    #         employment=vacancy_data['employment'],
    #         adv_response_url=vacancy_data['adv_response_url'],
    #         is_adv_vacancy=vacancy_data['is_adv_vacancy'],
    #         adv_context=vacancy_data['adv_context']
    #     )

    #     vacancy_create(vacancy)
