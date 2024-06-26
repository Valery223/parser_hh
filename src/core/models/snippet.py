from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


from core.models.base import Base


class Snippet(Base):
    __tablename__ = 'snippets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    requirement: Mapped[str | None] = mapped_column()
    responsibility: Mapped[str | None] = mapped_column()

    # Связь с таблицей вакансий
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), unique=True)
    vacancy = relationship("Vacancy", back_populates="snippet")