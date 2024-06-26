from sqlalchemy import  ForeignKey, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from .base import Base

# Определяем модель для таблицы вакансий
class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[str] = mapped_column(primary_key=True)
    premium: Mapped[bool] = mapped_column()
    name: Mapped[str] = mapped_column()
    department: Mapped[str] = mapped_column(nullable=True)
    has_test: Mapped[bool] = mapped_column()
    response_letter_required: Mapped[bool] = mapped_column()
    area_id: Mapped[str] = mapped_column(ForeignKey('areas.id'))
    salary: Mapped[dict] = mapped_column(JSON, nullable=True)
    type: Mapped[dict] = mapped_column(JSON)
    address: Mapped[dict] = mapped_column(JSON, nullable=True)
    response_url: Mapped[str] = mapped_column(nullable=True)
    sort_point_distance: Mapped[str] = mapped_column(nullable=True)
    published_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    archived: Mapped[bool] = mapped_column()
    apply_alternate_url: Mapped[str] = mapped_column()
    show_logo_in_search: Mapped[bool] = mapped_column(nullable=True)
    insider_interview: Mapped[dict] = mapped_column(JSON, nullable=True)
    url: Mapped[str] = mapped_column()
    alternate_url: Mapped[str] = mapped_column()
    relations: Mapped[list] = mapped_column(JSON)
    employer_id: Mapped[str] = mapped_column(ForeignKey('employers.id'))
    snippet: Mapped[dict] = mapped_column(JSON, nullable=True)
    contacts: Mapped[dict] = mapped_column(JSON, nullable=True)
    schedule: Mapped[dict] = mapped_column(JSON)
    working_days: Mapped[list] = mapped_column(JSON)
    working_time_intervals: Mapped[list] = mapped_column(JSON)
    working_time_modes: Mapped[list] = mapped_column(JSON)
    accept_temporary: Mapped[bool] = mapped_column()
    professional_roles: Mapped[list] = mapped_column(JSON)
    accept_incomplete_resumes: Mapped[bool] = mapped_column()
    experience: Mapped[dict] = mapped_column(JSON)
    employment: Mapped[dict] = mapped_column(JSON)
    adv_response_url: Mapped[str] = mapped_column(nullable=True)
    is_adv_vacancy: Mapped[bool] = mapped_column()
    adv_context: Mapped[dict] = mapped_column(JSON, nullable=True)

    # Связи с другими таблицами
    area = relationship("Area")
    employer = relationship("Employer")