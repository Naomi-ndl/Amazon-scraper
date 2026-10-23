
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

APP_DIR = BASE_DIR / "app"
DATA_DIR = BASE_DIR / "data"
EXPORTS_DIR = BASE_DIR / "exports"

DATA_DIR.mkdir(exist_ok=True)
EXPORTS_DIR.mkdir(exist_ok=True)
