from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

from typing import  Optional, List

from core.models.base import Base


class Salary(Base):
    __tablename__ = 'salaries'

    

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    salary_from: Mapped[float | None] = mapped_column(nullable=True)
    salary_to: Mapped[float | None] = mapped_column(nullable=True)
    currency: Mapped[str | None] = mapped_column(nullable=True)
    gross: Mapped[bool | None] = mapped_column(nullable=True)

    # PrimaryKeyConstraint('salary_from', 'salary_to', 'currency', 'gross', name="mytable_pk"),
    

    # Связь с таблицей вакансий
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), unique=True)
    vacancy = relationship("Vacancy", back_populates="salary")