from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacancy import Vacancy


class Employment(Base):
    __tablename__ = 'employments'

    id: Mapped[str | None] = mapped_column()
    name: Mapped[str] = mapped_column(primary_key=True)

    # Связь с таблицей вакансий
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="employment")