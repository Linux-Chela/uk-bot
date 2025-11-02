from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.graph import browser_use_agent_streaming

router = APIRouter()


class AgentRequest(BaseModel):
    """Request model for agent endpoint."""
    query: str


class AgentResponse(BaseModel):
    """Response model for agent endpoint."""
    result: str


@router.post("/agent", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    """
    Run the browser automation agent and return the result.
    
    Args:
        request: AgentRequest containing the task query
        
    Returns:
        AgentResponse with the result from the agent
    """
    try:
        # Run the browser agent (without verbose output for API)
        result = await browser_use_agent_streaming(request.query, verbose=False)
        
        return AgentResponse(
            result=result or "No result"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

