from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pathlib import Path

def static_files(app: FastAPI) -> None:
   
    static_dir = Path(__file__).parent.parent.parent / "static"
    
    # Validate directory exists
    if not static_dir.exists():
        raise FileNotFoundError(
            f"Static directory not found at: {static_dir}\n"
            "Create a 'static' folder in your project root."
        )
    
    app.mount("/static", StaticFiles(directory=static_dir), name="static")