"""FastAPI app for docker-compose example."""

from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="Agentic API with Redis")

@app.get("/")
def read_root():
    return {
        "message": "Agentic API running with docker-compose",
        "env": os.getenv("APP_ENV", "development"),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
