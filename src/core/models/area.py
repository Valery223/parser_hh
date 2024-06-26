from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


class Area(Base):
    __tablename__ = 'areas'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()

    # Связь с таблицей вакансий
    vacancies = relationship("Vacancy", back_populates="area")