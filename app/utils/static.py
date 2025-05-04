from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

def mount_static(app: FastAPI):
    static_path = Path(__file__).resolve().parents[2] / "static"
    if not static_path.is_dir():
        raise RuntimeError(f"Static directory not found at {static_path}")
    app.mount("/static", StaticFiles(directory=static_path), name="static")
