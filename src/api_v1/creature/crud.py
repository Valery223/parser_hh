from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Creature
from api_v1.creature.schemas import (CreatureCreate,
                                     CreatureUpdate,
                                     CreatureUpdatePartial)


async def get_one(db: AsyncSession, name: str)-> Creature | None:
    return await db.get(Creature, name)


async def get_all(db: AsyncSession) -> list[Creature]:
    stmt = select(Creature).order_by(Creature.name)
    result: Result = await db.execute(stmt)
    creatures = result.scalars().all()
    return list(creatures)


async def create(db: AsyncSession, creature_in: CreatureCreate ) -> Creature: 
    creature_model = Creature(**creature_in.model_dump())
    db.add(creature_model)
    await db.commit()
    # await db.refresh(creature_model) # if in psql data maybe rework
    return creature_model  


async def modify(db: AsyncSession,
                 creature: Creature,
                 creature_update: CreatureUpdate | CreatureUpdatePartial,
                 partial: bool = False) -> Creature:
    for key, value in creature_update.model_dump(exclude_unset=partial).items():
        setattr(creature, key, value)
    await db.commit()
    return creature


async def delete(db: AsyncSession,
                 creature: Creature) -> None:
    await db.delete(creature)
    await db.commit()

