from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import agent

app = FastAPI(
    title="UK-Bot Browser Agent API",
    description="Browser automation agent powered by browser_use",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include agent router
app.include_router(agent.router, prefix="/api/v1", tags=["agent"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "UK-Bot Browser Agent API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoint": "/api/v1/agent"
    }

