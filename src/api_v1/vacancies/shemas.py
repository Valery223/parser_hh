from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Optional, Any

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


class AreaBase(BaseModel):
    id: str
    name: str
    url: str
    
    model_config = ConfigDict(from_attributes=True)

class EmployerBase(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)

class Salary(BaseModel):
    from_: Optional[int] = None 
    to: Optional[int] = None
    currency: Optional[str] = None
    gross: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

class Snippet(BaseModel):
    requirement: Optional[str] = None
    responsibility: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class VacancyBase(BaseModel):
    id: str
    premium: Optional[bool] = None
    name: Optional[str] = None
    department: Optional[str] = None
    has_test: Optional[bool] = None
    response_letter_required: Optional[bool] = None
    area: Optional[AreaBase] = None
    salary: Optional[Salary] = None
    type: Optional[dict] = None
    address: Optional[dict] = None
    response_url: Optional[str] = None
    published_at: Optional[str] = None
    created_at: Optional[str] = None
    archived: Optional[bool] = None
    apply_alternate_url: Optional[str] = None
    show_logo_in_search: Optional[bool] = None
    insider_interview: Optional[bool] = None
    url: Optional[str] = None
    alternate_url: Optional[str] = None
    snippet: Optional[Snippet] = None
    employer: Optional[EmployerBase] = None
    schedule: Optional[dict] = None
    professional_roles: Optional[list] = None
    experience: Optional[dict] = None
    employment: Optional[dict] = None

    model_config = ConfigDict(from_attributes=True)

class VacancyCreate(VacancyBase):
    pass

class AreaCreate(AreaBase):
    pass