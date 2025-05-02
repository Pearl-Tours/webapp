from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .db.db import init_db

app = FastAPI()

init_db()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="pages")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})