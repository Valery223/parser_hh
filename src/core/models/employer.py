from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


class Employer(Base):
    __tablename__ = 'employers'

    id: Mapped[str | None] = mapped_column()
    name: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str | None] = mapped_column()
    alternate_url: Mapped[str | None] = mapped_column()
    vacancies_url: Mapped[str | None] = mapped_column()
    accredited_it_employer: Mapped[bool | None] = mapped_column()
    trusted: Mapped[bool] = mapped_column()

    # Связь с таблицей вакансий
    vacancies = relationship("Vacancy", back_populates="employer")