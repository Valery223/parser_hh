from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi_pagination import Page, add_pagination, paginate

from .shemas import QueryParamsBase, VacancyBase
from core.models import db_helper, Vacancy
from . import service


router = APIRouter(tags=["Vacancies"])


# @router.get("/", response_model=Page[VacancyBase])
# async def get_all(query: Annotated[QueryParamsBase, Depends()],
#                   session: AsyncSession = Depends(db_helper.get_db)):
#     params = query.model_dump(exclude_none = True)
#     vacancies = service.vacancy_get_one(params, session)
    
#     return paginate(vacancies)

@router.get("/")
async def get_all(query: Annotated[QueryParamsBase, Depends()],
                  session: AsyncSession = Depends(db_helper.get_db)):
    params = query.model_dump(exclude_none = True)
    vacancies = await service.vacancy_get_one(params, session)
    return vacancies