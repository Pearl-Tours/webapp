# app/main.py
from fastapi import FastAPI
from app.api.routes import router as api_router
from app.utils.static import mount_static

app = FastAPI()

# Include API routes
app.include_router(api_router)

# Mount static files
mount_static(app)