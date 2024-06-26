from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Creature

from . import crud

async def creature_by_name(
        name: Annotated[str, Path()],
        session: AsyncSession = Depends(db_helper.get_db)
) -> Creature:
    print("helloo2!!!!!!!!!!!!!!!")
    creature =  await crud.get_one(session, name)
    if creature is not None:
        return creature
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Creature {name} not found",
    )
