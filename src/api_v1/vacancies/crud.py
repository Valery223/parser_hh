from core.models import Area, Vacancy, Employer
import datetime

def add_vacancy(session, vacancy_data):
    area_data = vacancy_data['area']
    employer_data = vacancy_data['employer']
    
    area = session.query(Area).filter_by(id=area_data['id']).first()
    if not area:
        area = Area(id=area_data['id'], name=area_data['name'], url=area_data['url'])
        session.add(area)

    employer = session.query(Employer).filter_by(id=employer_data['id']).first()
    if not employer:
        employer = Employer(
            id=employer_data['id'], 
            name=employer_data['name'], 
            url=employer_data['url'], 
            alternate_url=employer_data['alternate_url'],
            logo_urls=employer_data['logo_urls'], 
            vacancies_url=employer_data['vacancies_url'],
            accredited_it_employer=employer_data['accredited_it_employer'],
            trusted=employer_data['trusted']
        )
        session.add(employer)
    
    vacancy = session.query(Vacancy).filter_by(id=vacancy['id']).first()
    if not vacancy:
        vacancy = Vacancy(
            id=vacancy_data['id'],
            premium=vacancy_data['premium'],
            name=vacancy_data['name'],
            department=vacancy_data['department'],
            has_test=vacancy_data['has_test'],
            response_letter_required=vacancy_data['response_letter_required'],
            area=area,
            salary=vacancy_data['salary'],
            type=vacancy_data['type'],
            address=vacancy_data['address'],
            response_url=vacancy_data['response_url'],
            sort_point_distance=vacancy_data['sort_point_distance'],
            published_at=datetime.datetime.fromisoformat(vacancy_data['published_at']),
            created_at=datetime.datetime.fromisoformat(vacancy_data['created_at']),
            archived=vacancy_data['archived'],
            apply_alternate_url=vacancy_data['apply_alternate_url'],
            show_logo_in_search=vacancy_data['show_logo_in_search'],
            insider_interview=vacancy_data['insider_interview'],
            url=vacancy_data['url'],
            alternate_url=vacancy_data['alternate_url'],
            relations=vacancy_data['relations'],
            employer=employer,
            snippet=vacancy_data['snippet'],
            contacts=vacancy_data['contacts'],
            schedule=vacancy_data['schedule'],
            working_days=vacancy_data['working_days'],
            working_time_intervals=vacancy_data['working_time_intervals'],
            working_time_modes=vacancy_data['working_time_modes'],
            accept_temporary=vacancy_data['accept_temporary'],
            professional_roles=vacancy_data['professional_roles'],
            accept_incomplete_resumes=vacancy_data['accept_incomplete_resumes'],
            experience=vacancy_data['experience'],
            employment=vacancy_data['employment'],
            adv_response_url=vacancy_data['adv_response_url'],
            is_adv_vacancy=vacancy_data['is_adv_vacancy'],
            adv_context=vacancy_data['adv_context']
        )
    
        session.add(vacancy)
    session.commit()