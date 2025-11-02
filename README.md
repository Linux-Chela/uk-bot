# UK-Bot Browser Agent API

A simple FastAPI application with browser automation powered by browser_use.

## 🚀 Quick Start

```bash
# 1. Setup
make install
source venv/bin/activate

# 2. Configure
cp .env.example .env
# Edit .env and add your OPEN_API_KEY

# 3. Run
make dev
```

## 📝 API Usage

**Single Endpoint:** `POST /api/v1/agent`

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Go to example.com and tell me the page title"}'
```

**Response:**
```json
{"result": "The page title of example.com is 'Example Domain'."}
```

## 📚 Documentation

- API Docs: http://localhost:8000/docs
- Full Guide: See `API_GUIDE.md`

## Project Structure

```
UK-bot/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration and settings
│   ├── routers/
│   │   ├── __init__.py
│   │   └── agent.py         # Agent API endpoints
│   └── agents/
│       ├── __init__.py
│       └── graph.py         # LangGraph multi-agent implementation
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment variables
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 4. Run the Application

```bash
# Option 1: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using Python
python -m app.main
```

### 5. Access the API

- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative Documentation (ReDoc)**: http://localhost:8000/redoc
- **Root Endpoint**: http://localhost:8000/
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Main Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `GET /api/v1/agent/status` - Get agent system status
- `POST /api/v1/agent` - Run the multi-agent system

### Example Request

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Your query here",
    "session_id": "optional-session-id",
    "config": {}
  }'
```

### Example Response

```json
{
  "result": "Agent response",
  "session_id": "optional-session-id",
  "metadata": {
    "status": "success",
    "message": "Agent execution completed"
  }
}
```

## Next Steps

1. **Implement LangGraph Multi-Agent System**:
   - Define agent nodes in `app/agents/graph.py`
   - Create agent logic and state transitions
   - Configure agent interactions and workflow

2. **Integrate with API**:
   - Update `app/routers/agent.py` to use the agent graph
   - Add proper error handling and logging
   - Implement session management if needed

3. **Add Additional Features**:
   - Database integration for persistence
   - Authentication and authorization
   - Rate limiting
   - Caching
   - Monitoring and observability

## Development

### Project Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation using Python type hints
- **LangGraph**: Framework for building multi-agent systems
- **LangChain**: LLM application framework

### Environment Variables

- `API_HOST`: API host (default: 0.0.0.0)
- `API_PORT`: API port (default: 8000)
- `API_RELOAD`: Enable auto-reload (default: True)
- `OPENAI_API_KEY`: OpenAI API key for LLM integration

## License

MIT

