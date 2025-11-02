# FastAPI Integration Guide

## ✅ What's Working

Your browser agent with **live streaming** is working perfectly! 

```bash
python app/agents/graph.py
```

Output:
```
============================================================
🤖 Starting Agent: Go to Google and search...
============================================================

📍 Step 1
   Status: Processing...
   ✓ Step 1 completed

📍 Step 2
   Status: Processing...
   ✓ Step 2 completed
...
```

## 🔧 Integrate with FastAPI

### Option 1: Simple Non-Streaming Endpoint

Update `app/routers/agent.py`:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.agents.graph import browser_use_agent

router = APIRouter()

class AgentRequest(BaseModel):
    query: str
    session_id: Optional[str] = None

class AgentResponse(BaseModel):
    result: str
    session_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

@router.post("/agent", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    """Run the browser agent and return the result."""
    try:
        # Run the agent
        result = await browser_use_agent(request.query)
        
        return AgentResponse(
            result=result or "No result",
            session_id=request.session_id,
            metadata={"status": "success"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

Test it:
```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Go to Google and search for FastAPI"}'
```

### Option 2: Streaming Endpoint (Server-Sent Events)

For real-time updates in the API:

```python
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.agents.graph import browser_use_agent_streaming
import asyncio
import json

@router.post("/agent/stream")
async def stream_agent(request: AgentRequest):
    """Stream agent updates in real-time."""
    
    async def generate():
        """Generate server-sent events."""
        # Track steps
        step_count = [0]
        
        # Callbacks that yield events
        async def on_step_start(agent):
            step_count[0] += 1
            event = {
                "type": "step_start",
                "step": step_count[0],
                "status": "processing"
            }
            yield f"data: {json.dumps(event)}\n\n"
        
        async def on_step_end(agent):
            event = {
                "type": "step_end",
                "step": step_count[0],
                "status": "completed"
            }
            yield f"data: {json.dumps(event)}\n\n"
        
        # Create and run agent
        from browser_use import Agent as Ag
        from app.agents.llms import llm
        
        agent = Ag(
            task=request.query,
            llm=llm,
            use_vision=False,
        )
        
        # Start event
        yield f"data: {json.dumps({'type': 'start', 'query': request.query})}\n\n"
        
        try:
            result = await agent.run(
                max_steps=100,
                on_step_start=on_step_start,
                on_step_end=on_step_end
            )
            
            # Final result
            final = result.final_result() if result else "No result"
            yield f"data: {json.dumps({'type': 'complete', 'result': final})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
```

Test with JavaScript:
```javascript
const eventSource = new EventSource('http://localhost:8000/api/v1/agent/stream');

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Update:', data);
    
    if (data.type === 'complete') {
        console.log('Final result:', data.result);
        eventSource.close();
    }
};
```

### Option 3: WebSocket (Real-time Bi-directional)

Add WebSocket support in `app/main.py`:

```python
from fastapi import WebSocket
from app.agents.graph import browser_use_agent

@app.websocket("/ws/agent")
async def websocket_agent(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive query
            data = await websocket.receive_json()
            query = data.get("query")
            
            # Send start message
            await websocket.send_json({"type": "start", "query": query})
            
            # Run agent with callbacks
            step_count = [0]
            
            async def on_step_start(agent):
                step_count[0] += 1
                await websocket.send_json({
                    "type": "step",
                    "step": step_count[0],
                    "status": "processing"
                })
            
            async def on_step_end(agent):
                await websocket.send_json({
                    "type": "step",
                    "step": step_count[0],
                    "status": "completed"
                })
            
            from browser_use import Agent as Ag
            from app.agents.llms import llm
            
            agent = Ag(task=query, llm=llm, use_vision=False)
            result = await agent.run(
                max_steps=100,
                on_step_start=on_step_start,
                on_step_end=on_step_end
            )
            
            # Send final result
            await websocket.send_json({
                "type": "complete",
                "result": result.final_result() if result else "No result"
            })
            
    except Exception as e:
        await websocket.send_json({"type": "error", "error": str(e)})
    finally:
        await websocket.close()
```

Test with Python client:
```python
import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/agent"
    async with websockets.connect(uri) as websocket:
        # Send query
        await websocket.send(json.dumps({
            "query": "Search Google for FastAPI"
        }))
        
        # Receive updates
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            print(data)
            
            if data["type"] == "complete":
                break

asyncio.run(test_websocket())
```

## 🚀 Quick Start

1. **Start the server:**
```bash
cd /Users/vijay/Desktop/UK-bot
source venv/bin/activate
make dev
```

2. **Test the endpoint:**
Visit http://localhost:8000/docs

3. **Make a request:**
```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Your task here"}'
```

## 📝 Files

- **`app/agents/graph.py`** - Browser agent with streaming ✅
- **`app/agents/llms.py`** - LLM wrapper ✅
- **`app/routers/agent.py`** - FastAPI endpoints (ready to update)
- **`app/main.py`** - FastAPI app

## 🎯 Next Steps

1. Choose your integration option (simple, SSE, or WebSocket)
2. Update `app/routers/agent.py` with your chosen implementation
3. Test with the FastAPI docs at `/docs`
4. Build your LangGraph multi-agent system on top!

Your foundation is solid! 🎉

