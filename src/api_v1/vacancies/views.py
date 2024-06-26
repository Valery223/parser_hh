from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi_pagination import Page, add_pagination, paginate

from .shemas import QueryParamsBase, VacancyBase
from core.models import db_helper, Vacancy
from request import parsing


router = APIRouter(tags=["Vacancies"])


@router.get("/", response_model=Page[VacancyBase])
async def get_all(query: Annotated[QueryParamsBase, Depends()],
                  db: AsyncSession = Depends(db_helper.get_db)):
    parsing(query.model_dump(exclude_none = True))
    
    vacancies = db.query(Vacancy).all()
    return paginate(vacancies)