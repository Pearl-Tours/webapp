from fastapi import FastAPI,Request,Form,Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db,engine
from .models import Name,Base
Base.metadata.create_all(bind=engine)
app=FastAPI()
pages=Jinja2Templates(directory="app/pages")
@app.get("/")
async def root(request:Request):
    success=request.query_params.get("success")
    return pages.TemplateResponse("index.html",{"request":request,"success":success=="true"})