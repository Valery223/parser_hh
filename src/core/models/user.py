from sqlalchemy import String
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(32), primary_key=True)
    hash: Mapped[str]
    
    
    