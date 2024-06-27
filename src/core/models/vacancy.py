from sqlalchemy import  ForeignKey, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
import datetime

from .base import Base

if TYPE_CHECKING:
    from .area import Area
    from .salary import Salary
    from .type_ import Type
    from .employer import Employer
    from .snippet import Snippet
    from .schedule import Schedule
    from .employment import Employment
    from .experience import Experience

# Определяем модель для таблицы вакансий
class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[str] = mapped_column(primary_key=True)
    accept_handicapped: Mapped[bool | None] = mapped_column()
    accept_incomplete_resumes: Mapped[bool | None] = mapped_column()
    accept_kids: Mapped[bool | None] = mapped_column()
    accept_temporary: Mapped[bool | None] = mapped_column()
    allow_messages: Mapped[bool | None] = mapped_column()
    alternate_url: Mapped[str | None] = mapped_column()
    apply_alternate_url: Mapped[str| None] = mapped_column()
    approved: Mapped[bool | None] = mapped_column()
    archived: Mapped[bool | None] = mapped_column()
    code: Mapped[str | None] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    has_test: Mapped[bool | None] = mapped_column()
    premium: Mapped[bool | None] = mapped_column()
    name: Mapped[str | None] = mapped_column()
    department: Mapped[str | None]  = mapped_column(nullable=True)
    response_letter_required: Mapped[bool | None] = mapped_column()
    response_url: Mapped[str | None] = mapped_column(nullable=True)
    sort_point_distance: Mapped[str | None] = mapped_column(nullable=True)
    published_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    show_logo_in_search: Mapped[bool | None] = mapped_column(nullable=True)


    #foreignKeys
    area_id: Mapped[str | None] = mapped_column(ForeignKey('areas.id'))
    type_id: Mapped[str | None] = mapped_column(ForeignKey('types.id'))
    employment_name: Mapped[str | None] = mapped_column(ForeignKey("employments.name"))
    schedule_id: Mapped[str | None] = mapped_column(ForeignKey('schedules.id'))
    experience_id: Mapped[str | None] = mapped_column(ForeignKey("experiences.id"))
    employer_name: Mapped[str | None] = mapped_column(ForeignKey("employers.name"))
    salary_id: Mapped[int | None] = mapped_column(ForeignKey("salaries.id"))
    snippet_id: Mapped[int | None] = mapped_column(ForeignKey("snippets.id"))

    area: Mapped["Area"] = relationship(back_populates="vacancies")
    type_: Mapped["Type"] = relationship(back_populates="vacancies")
    employer: Mapped["Employer"] = relationship(back_populates="vacancies")
    schedule: Mapped["Schedule"] = relationship(back_populates="vacancies")
    employment: Mapped["Employment"] = relationship(back_populates="vacancies")
    experience: Mapped["Experience"] = relationship(back_populates="vacancies")

    salary: Mapped["Salary"] = relationship(back_populates="vacancy", foreign_keys=[salary_id])
    snippet: Mapped["Snippet"] = relationship(back_populates="vacancy", foreign_keys=[snippet_id])
    
