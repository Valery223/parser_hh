from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(20)]
    hash: str
    

class UserCreate(UserBase):
    pass

class User(UserBase):
    pass