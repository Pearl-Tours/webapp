from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils.template import templates

router = APIRouter(prefix="", tags=["/"])

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})