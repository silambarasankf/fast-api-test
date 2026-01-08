import os
from fastapi import FastAPI
from pydantic import BaseModel

# Load .env file only if it exists (for local development)
# In Azure, environment variables are set via Application Settings
try:
    from dotenv import load_dotenv
    load_dotenv()  # Only loads if .env file exists
except ImportError:
    pass  # python-dotenv not installed, skip

app = FastAPI()

# Example: Access environment variables
# These work both locally (from .env) and in Azure (from Application Settings)
DATABASE_URL = os.environ.get("DATABASE_URL", "default_value")
API_KEY = os.environ.get("API_KEY")
DEBUG_MODE = os.environ.get("DEBUG", "false").lower() == "true"


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI! This is a version 3 update."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/env-check")
def env_check():
    """Check if environment variables are loaded (remove in production)"""
    return {
        "DATABASE_URL": DATABASE_URL[:20] + "..." if DATABASE_URL and len(DATABASE_URL) > 20 else DATABASE_URL,
        "API_KEY": "***SET***" if API_KEY else "NOT SET",
        "DEBUG_MODE": DEBUG_MODE,
        "all_env_vars": list(os.environ.keys())  # Lists all available env var names
    }


@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
