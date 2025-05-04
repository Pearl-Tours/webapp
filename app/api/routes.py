from fastapi import APIRouter
from app.api import index  #do not forget to import a new route

router = APIRouter()

#include all sub-routers
router.include_router(index.router)

