from pydantic import BaseModel, Field, model_validator
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

    class Config:
        orm_mode = True

class EmployerBase(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

class VacancyBase(BaseModel):
    id: str
    name: str
    area: AreaBase
    employer: EmployerBase

    class Config:
        orm_mode = True