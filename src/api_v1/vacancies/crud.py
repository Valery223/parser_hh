from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Type

from core.models import Vacancy, Area
from api_v1.vacancies.shemas import VacancyBase, VacancyCreate, AreaBase, AreaCreate


# async def vacancy_get_one(session: AsyncSession, id: int)-> Vacancy | None:
#     return await session.get(Vacancy, id)

# async def vacancy_get_all(session: AsyncSession) -> list[Vacancy]:
#     stmt = select(Vacancy).order_by(Vacancy.name)
#     result: Result = await session.execute(stmt)
#     vacances = result.scalars().all()
#     return list(vacances)

# async def vacancy_create(session: AsyncSession, vacancy_in: VacancyCreate ) -> Vacancy: 
#     vacancy_model = Vacancy(**vacancy_in.model_dump())
#     session.add(vacancy_model)
#     await session.commit()
#     # await db.refresh(creature_model) # if in psql data maybe rework
#     return vacancy_model

async def get_one(session: AsyncSession, model: Type, key)-> Type | None:
    return await session.get(model, key)

# async def vacancy_get_all(session: AsyncSession) -> list[Area]:
#     stmt = select(Area).order_by(Area.name)
#     result: Result = await session.execute(stmt)
#     areas = result.scalars().all()
#     return list(areas)

async def create(session: AsyncSession, model: Type, scheme_in: Type ) -> Area: 
    in_model = model(**scheme_in.model_dump())
    session.add(in_model)
    await session.commit()
    # await db.refresh(creature_model) # if in psql data maybe rework
    return in_model