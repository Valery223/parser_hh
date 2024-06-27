from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator
from typing import Optional, Any
import datetime

from errors.validation import ValidationError

class QueryParamsBase(BaseModel):
    page: Optional[int] = Field(0, description="Номер страницы.")
    per_page: Optional[int] = Field(10, description="Количество элементов на странице. Максимум 100.")
    text: Optional[str] = Field(None, description="Текст запроса.")
    search_field: Optional[str] = Field(None, description="Область поиска.")
    experience: Optional[str] = Field(None, description="Опыт работы.")
    employment: Optional[str] = Field(None, description="Тип занятости.")
    schedule: Optional[str] = Field(None, description="График работы.")
    area: Optional[str] = Field(None, description="Регион.")
    metro: Optional[str] = Field(None, description="Метро.")
    professional_role: Optional[str] = Field(None, description="Профессиональная область.")
    industry: Optional[str] = Field(None, description="Индустрия.")
    employer_id: Optional[str] = Field(None, description="Идентификатор работодателя.")
    currency: Optional[str] = Field(None, description="Код валюты.")
    salary: Optional[float] = Field(None, description="Размер заработной платы.")
    label: Optional[str] = Field(None, description="Фильтр по меткам вакансий.")
    only_with_salary: Optional[bool] = Field(False, description="Показывать только вакансии с зарплатой.")
    period: Optional[int] = Field(None, description="Период поиска в днях.")
    date_from: Optional[str] = Field(None, description="Дата начала поиска.")
    date_to: Optional[str] = Field(None, description="Дата окончания поиска.")
    top_lat: Optional[float] = Field(None, description="Верхняя граница широты.")
    bottom_lat: Optional[float] = Field(None, description="Нижняя граница широты.")
    left_lng: Optional[float] = Field(None, description="Левая граница долготы.")
    right_lng: Optional[float] = Field(None, description="Правая граница долготы.")
    order_by: Optional[str] = Field(None, description="Сортировка вакансий.")
    sort_point_lat: Optional[float] = Field(None, description="Широта точки сортировки.")
    sort_point_lng: Optional[float] = Field(None, description="Долгота точки сортировки.")
    clusters: Optional[bool] = Field(False, description="Возвращать ли кластеры.")
    describe_arguments: Optional[bool] = Field(False, description="Возвращать ли описание аргументов.")
    no_magic: Optional[bool] = Field(False, description="Отключение автоматического преобразования запросов.")
    premium: Optional[bool] = Field(False, description="Учет премиум вакансий в сортировке.")
    responses_count_enabled: Optional[bool] = Field(False, description="Включение счетчика откликов.")
    part_time: Optional[str] = Field(None, description="Вакансии для подработки.")
    accept_temporary: Optional[bool] = Field(False, description="Поиск только по временным вакансиям.")
    locale: Optional[str] = Field("RU", description="Идентификатор локали.")
    host: Optional[str] = Field("hh.ru", description="Доменное имя сайта.")

    @model_validator(mode='before')
    def check_dates_or_period(cls, values: dict[str, Any]) -> dict[str, Any]:
        period, date_from, date_to = values.get('period'), values.get('date_from'), values.get('date_to')
        if period is not None and (date_from is not None or date_to is not None):
            raise ValidationError('`period` cannot be used with `date_from` or `date_to`')
        return values



class EmployerBase(BaseModel):
    id: str
    name: str

    

class SalaryBase(BaseModel):
    salary_from: Optional[float]
    salary_to: Optional[float]
    currency: Optional[str]
    gross: Optional[bool]

    model_config = ConfigDict(from_attributes=True)

class Snippet(BaseModel):
    requirement: Optional[str] = None
    responsibility: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class ScheduleBase(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)

class ExperienceBase(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)

class VacancyBase(BaseModel):
    id: str
    
    accept_handicapped: Optional[bool] = None
    accept_incomplete_resumes: Optional[bool] = None
    accept_kids: Optional[bool] = None
    accept_temporary: Optional[bool] = None
    allow_messages: Optional[bool] = None
    alternate_url: Optional[str] = None
    apply_alternate_url: Optional[str] = None
    approved: Optional[bool] = None
    archived: Optional[bool] = None
    code: Optional[str] = None
    description: Optional[str] = None
    has_test: Optional[bool] = None
    premium: Optional[bool] = None
    name: Optional[str] = None
    department: Optional[str] = None
    response_letter_required: Optional[bool] = None
    response_url: Optional[str] = None
    sort_point_distance: Optional[str] = None
    published_at: Optional[datetime.datetime] = None
    created_at: Optional[datetime.datetime] = None
    show_logo_in_search: Optional[bool] = None

    #foreign keys
    area_id: Optional[str] = None
    type_id: Optional[str] = None
    schedule_id: Optional[str] = None
    experience_id: Optional[str] = None
    employer_name: Optional[str] = None
    employment_name: Optional[str] = None
    salary_id: Optional[int] = None
    snippet_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode='before')
    @classmethod
    def extract_area_id(cls, values):
        foreign_keys = {'area':'id', 'type' : 'id', 'schedule': 'id', 'experience' : 'id',
                        'employer': 'name', 'employment': 'name'}
        for k,v in foreign_keys.items():
            obj = values.get(k)
            if obj is not None:
                values[k+'_'+v] = obj.get(v)
        return values

class VacancyCreate(VacancyBase):
    pass

class Vacancy(VacancyBase):
    area: Optional["Area"]
    type_: Optional["Type"]
    employer: Optional["Employer"]
    schedule: Optional["Schedule"]
    employment: Optional["Employment"]
    experience: Optional["Experience"]
    salary: Optional["Salary"]
    snippet: Optional["Snippet"]


class AreaBase(BaseModel):
    id: str
    name: str
    url: str
    
    model_config = ConfigDict(from_attributes=True)

class AreaCreate(AreaBase):
    pass

class Area(AreaBase):
    vacancies: list[Vacancy] = []

class EmployerBase(BaseModel):
    id: str
    name: str
    url: Optional[str]
    alternate_url: Optional[str]
    vacancies_url: Optional[str]
    accredited_it_employer: Optional[bool]
    trusted: bool

    model_config = ConfigDict(from_attributes=True)

class EmployerCreate(EmployerBase):
    pass

class Employer(EmployerBase):
    vacancies: list[Vacancy] = []


class EmploymentBase(BaseModel):
    id: Optional[str]
    name: str
    
    model_config = ConfigDict(from_attributes=True)

class EmploymentCreate(EmploymentBase):
    pass

class Employment(EmploymentBase):
    vacancies: list[Vacancy] = []


class ExperienceBase(BaseModel):
    id: str
    name: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    vacancies: list[Vacancy] = []

class SalaryBase(BaseModel):
    salary_from: Optional[float]
    salary_to: Optional[float]
    currency: Optional[str]
    gross: Optional[bool]

    model_config = ConfigDict(from_attributes=True)

class SalaryCreate(SalaryBase):
    pass

class Salary(SalaryBase):
    vacancy: Vacancy

class ScheduleBase(BaseModel):
    id: str
    name: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    vacancies: list[Vacancy] = []

class SnippetBase(BaseModel):
    requirement: Optional[str]
    responsibility: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class SnippetCreate(SnippetBase):
    pass

class Snippet(SnippetBase):
    vacancy: Vacancy


class TypeBase(BaseModel):
    id: str
    name: Optional[str]
    model_config = ConfigDict(from_attributes=True)

class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    vacancies: list[Vacancy] = []