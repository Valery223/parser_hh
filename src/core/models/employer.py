from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


class Employer(Base):
    __tablename__ = 'employers'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    alternate_url: Mapped[str] = mapped_column()
    logo_urls: Mapped[dict] = mapped_column(JSON)
    vacancies_url: Mapped[str] = mapped_column()
    accredited_it_employer: Mapped[bool] = mapped_column()
    trusted: Mapped[bool] = mapped_column()

    # Связь с таблицей вакансий
    vacancies = relationship("Vacancy", back_populates="employer")