from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.creature.schemas import Creature, CreatureCreate, CreatureUpdate, CreatureUpdatePartial
from . import crud
from core.models.db_helper import db_helper
from .dependencies import creature_by_name

router = APIRouter(tags=["Cretures"])

@router.get("/", response_model=list[Creature])
async def get_all(db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.get_all(db)


@router.get("/{name}", response_model=Creature)
async def get_one(creature: Creature =  Depends(creature_by_name) ):
    print("helloo!!!!!!!!!!!!!!!")
    return creature


@router.post("/", response_model=Creature, status_code=status.HTTP_201_CREATED)
async def create(creature_in:CreatureCreate, db: AsyncSession = Depends(db_helper.get_db)):
    return await crud.create(db,creature_in)


@router.put("/{name}")
async def update(
    creature_update: CreatureUpdate,
    creature: Creature = Depends(creature_by_name),
    session: AsyncSession = Depends(db_helper.get_db),
):
    return await crud.modify(
        db=session,
        creature=creature,
        creature_update=creature_update,
    )


@router.patch("/{name}")
async def update_partial(
    creature_update: CreatureUpdatePartial,
    creature: Creature = Depends(creature_by_name),
    session: AsyncSession = Depends(db_helper.get_db),
):
    return await crud.modify(
        db=session,
        creature=creature,
        creature_update=creature_update,
        partial=True
    )

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    creature: Creature = Depends(creature_by_name),
    session: AsyncSession = Depends(db_helper.get_db)
) -> None:
    await crud.delete(db=session,creature=creature)