from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from core.models.base import Base

if TYPE_CHECKING:
    from .vacancy import Vacancy

class Type(Base):
    __tablename__ = 'types'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column()

    vacancies: Mapped[list["Vacancy"]] =  relationship(back_populates="type_")
