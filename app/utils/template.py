from fastapi.templating import Jinja2Templates
from pathlib import Path

templates_dir = Path(__file__).parent.parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))
