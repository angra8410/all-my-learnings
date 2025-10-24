"""
FastAPI application with integrated Agent.
This is a complete example combining FastAPI with the agent core.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from datetime import datetime
import sys
import os

# Add parent directory to path to import agent modules
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

app = FastAPI(
    title="Agentic Weather API",
    description="FastAPI application with integrated AI agent for weather queries",
    version="1.0.0"
)


# Pydantic models
class QueryRequest(BaseModel):
    """Request model for agent queries."""
    query: str
    context: Optional[Dict[str, Any]] = None


class QueryResponse(BaseModel):
    """Response model for agent queries."""
    query: str
    result: Dict[str, Any]
    message: str
    status: str
    timestamp: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    timestamp: str
    version: str


# Simple Agent Implementation (inline for this example)
class SimpleAgent:
    """Simplified agent for the FastAPI app."""
    
    def __init__(self):
        self.history = []
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a query and return mock results."""
        query_lower = query.lower()
        
        if "weather" in query_lower or "temperature" in query_lower:
            result = {
                "type": "weather",
                "location": "Madrid",
                "temperature": "25°C",
                "condition": "Sunny",
                "timestamp": datetime.now().isoformat()
            }
            message = "The weather in Madrid is sunny with a temperature of 25°C."
        
        elif "time" in query_lower:
            result = {
                "type": "time",
                "current_time": datetime.now().strftime("%H:%M:%S"),
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            message = f"Current time is {result['current_time']} on {result['date']}."
        
        else:
            result = {"type": "general", "info": "Query processed"}
            message = "I processed your query but don't have specific information about it."
        
        response = {
            "query": query,
            "result": result,
            "message": message,
            "status": "success"
        }
        
        self.history.append(response)
        return response


# Initialize agent
agent = SimpleAgent()


# API Endpoints
@app.get("/", tags=["General"])
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to the Agentic Weather API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "agent_query": "/agent/query",
            "agent_history": "/agent/history"
        }
    }


@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )


@app.post("/agent/query", response_model=QueryResponse, tags=["Agent"])
async def query_agent(request: QueryRequest):
    """
    Send a query to the agent.
    
    Example:
    ```json
    {
        "query": "What's the weather like?"
    }
    ```
    """
    try:
        result = agent.process_query(request.query)
        return QueryResponse(
            query=result["query"],
            result=result["result"],
            message=result["message"],
            status=result["status"],
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/agent/history", tags=["Agent"])
async def get_history():
    """Get agent conversation history."""
    return {
        "history": agent.history,
        "count": len(agent.history),
        "timestamp": datetime.now().isoformat()
    }


@app.delete("/agent/history", tags=["Agent"])
async def clear_history():
    """Clear agent conversation history."""
    agent.history = []
    return {
        "message": "History cleared",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/info", tags=["General"])
async def get_info():
    """Get system information."""
    import platform
    return {
        "python_version": platform.python_version(),
        "system": platform.system(),
        "platform": platform.platform(),
        "api_version": "1.0.0",
        "agent_status": "active"
    }


# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    print("🚀 Agentic Weather API starting...")
    print("📍 Agent initialized and ready")


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    print("👋 Agentic Weather API shutting down...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
