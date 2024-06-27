from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

from typing import  Optional, List

from core.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacancy import Vacancy


class Salary(Base):
    __tablename__ = 'salaries'

    

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    salary_from: Mapped[float | None] = mapped_column(nullable=True)
    salary_to: Mapped[float | None] = mapped_column(nullable=True)
    currency: Mapped[str | None] = mapped_column(nullable=True)
    gross: Mapped[bool | None] = mapped_column(nullable=True)

    vacancy: Mapped["Vacancy"] = relationship(back_populates="salary")