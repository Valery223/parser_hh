from fastapi import APIRouter

from .vacancies.views import  router as vacancie_router

router = APIRouter()
router.include_router(router=vacancie_router, prefix="/vacancies")