from pydantic import BaseModel, ConfigDict

class CreatureBase(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

class CreatureCreate(CreatureBase):
    pass

class CreatureUpdate(CreatureCreate):
    pass

class CreatureUpdatePartial(CreatureCreate):
    
    name: str | None = None
    country: str | None = None
    area: str | None = None
    description: str | None = None
    aka: str | None = None

class Creature(CreatureBase):
    model_config = ConfigDict(from_attributes=True)