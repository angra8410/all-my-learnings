"""Simple FastAPI application for Docker example."""

from fastapi import FastAPI

app = FastAPI(title="Docker Example API")

@app.get("/")
def read_root():
    return {"message": "Hello from Docker!", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "docker-example"}

@app.get("/info")
def get_info():
    import platform
    return {
        "python_version": platform.python_version(),
        "system": platform.system(),
        "platform": platform.platform()
    }
