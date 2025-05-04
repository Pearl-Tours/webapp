#calling static pages
from fastapi.staticfiles import StaticFiles

def static_files(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")