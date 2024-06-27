from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


from core.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacancy import Vacancy


class Snippet(Base):
    __tablename__ = 'snippets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    requirement: Mapped[str | None] = mapped_column()
    responsibility: Mapped[str | None] = mapped_column()

    # Связь с таблицей вакансий
    vacancy: Mapped["Vacancy"] = relationship(back_populates="snippet")