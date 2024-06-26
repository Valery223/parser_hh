from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacancy import Vacancy


class Schedule(Base):
    __tablename__ = 'schedules'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column()

    # Связь с таблицей вакансий
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="schedule")