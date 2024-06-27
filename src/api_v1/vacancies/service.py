import requests

from sqlalchemy import select
from sqlalchemy.engine import Result

from core.models import Area, Type, Salary, Vacancy, Employer, Snippet, Schedule, Experience, Employment
from .shemas import AreaCreate, TypeCreate, SalaryCreate, EmployerCreate, SnippetCreate, ScheduleCreate, ExperienceCreate, EmploymentCreate, VacancyCreate

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
    vacancy_arr = []
    
    response = await parsing(params = params)
    if response.status_code == 200:
        vacancies = response.json()
        for vac in vacancies['items']:
            vacancy = await add_vacancy(session, vac)
        # vacancy = await add_vacancy(session, vacancies['items'][0])
            vacancy_arr.append(vacancy)
        
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
    
    return vacancy_arr

async def add_vacancy(session, vacancy_data):

    vacancy = await crud.get_one(session= session, model=Vacancy, key = vacancy_data['id'])

    if not vacancy:
        vacancy = VacancyCreate(**vacancy_data)

        area_data = vacancy_data['area']
        if area_data is not None:
            area = await crud.get_one(session= session, model=Area, key = area_data['id'])
            if area is None:
                area = AreaCreate(id=area_data['id'], name=area_data['name'], url=area_data['url'])
                await crud.create(session=session, model=Area, scheme_in = area)
            
            vacancy.area_id = area.id

        type_data = vacancy_data['type']
        if type_data is not None:
            type_ = await crud.get_one(session = session, model=Type, key =type_data['id'])
            if type_ is None:
                type_ = TypeCreate(id=type_data['id'], name=type_data['name'])
                await crud.create(session=session, model=Type, scheme_in=type_)

            vacancy.type_id = type_.id

        salary_data = vacancy_data['salary']
        if salary_data is not None:
            # salary в любом случае создаем(если не None)
            salary = SalaryCreate(salary_from =  salary_data['from'], salary_to= salary_data['to'],
                                currency = salary_data['currency'], gross = salary_data['gross'])
            salary = await crud.create(session=session, model=Salary, scheme_in=salary)

            vacancy.salary_id = salary.id

        employer_data = vacancy_data['employer']
        if employer_data is not None:
            employer = await crud.get_one(session= session, model = Employer, key = employer_data['name'])
            if not employer:
                employer = EmployerCreate(id = employer_data['id'], name = employer_data['name'],
                                          url = employer_data['url'], alternate_url= employer_data['alternate_url'],
                                          vacancies_url=employer_data['vacancies_url'], trusted= employer_data["trusted"],
                                          accredited_it_employer=employer_data['accredited_it_employer'])
                await crud.create(session=session, model=Employer, scheme_in=employer)

            vacancy.employer_name = employer.name

        snippet_data = vacancy_data['snippet']
        if snippet_data is not None:
            # snippet в любом случае создаем(если не None)
            snippet = SnippetCreate(requirement=snippet_data['requirement'], responsibility=snippet_data['responsibility'])
            snippet = await crud.create(session=session, model=Snippet, scheme_in=snippet)
        
            vacancy.snippet_id = snippet.id

        schedule_data = vacancy_data['schedule']
        if schedule_data is not None:
            schedule = await crud.get_one(session= session, model = Schedule, key = schedule_data['id'])
            if schedule is None:
                schedule = ScheduleCreate(id = schedule_data['id'], name = schedule_data['name'])
                await crud.create(session= session, model = Schedule, scheme_in= schedule)
        
            vacancy.schedule_id = schedule.id

        experience_data = vacancy_data['experience']
        if experience_data is not None:
            experience = await crud.get_one(session= session, model = Experience, key = experience_data['id'])
            if experience is None:
                experience = ExperienceCreate(id = experience_data['id'], name = experience_data['name'])
                await crud.create(session= session, model = Experience, scheme_in= experience)
        
            vacancy.experience_id = experience.id

        employment_data = vacancy_data['employment']
        if employment_data is not None:
            employment = await crud.get_one(session= session, model = Employment, key = employment_data['id'])
            if employment is None:
                employment = EmploymentCreate(id = employment_data['id'], name = employment_data['id'])
                await crud.create(session= session, model = Employment, scheme_in= employment)

            vacancy.employment_name = employment.name

        vacancy = await crud.create(session= session, model = Vacancy, scheme_in = vacancy)

    return vacancy