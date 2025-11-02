# UK-Bot Browser Agent API

## ✅ Your Simple API is Ready!

One endpoint that runs browser automation tasks and returns results.

## 🚀 Start the Server

```bash
cd /Users/vijay/Desktop/UK-bot
source venv/bin/activate
make dev
```

Or:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📝 API Endpoint

**Single Endpoint:** `POST /api/v1/agent`

### Request Format

```json
{
  "query": "Your task description here"
}
```

### Response Format

```json
{
  "result": "The result from the agent"
}
```

## 🧪 Test Examples

### Example 1: Get Page Title

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Go to example.com and tell me the page title"}'
```

**Response:**
```json
{
  "result": "The page title of example.com is 'Example Domain'."
}
```

### Example 2: UK Gov Website

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Go to https://www.gov.uk/book-driving-test and tell me what you see"}'
```

### Example 3: Search Task

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Go to Google and search for FastAPI tutorial. Give me the first result title."}'
```

## 🌐 Using in Your Application

### Python

```python
import requests

url = "http://localhost:8000/api/v1/agent"
payload = {
    "query": "Go to example.com and tell me the page title"
}

response = requests.post(url, json=payload)
result = response.json()
print(result["result"])
```

### JavaScript/Node.js

```javascript
const response = await fetch('http://localhost:8000/api/v1/agent', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    query: 'Go to example.com and tell me the page title'
  })
});

const data = await response.json();
console.log(data.result);
```

### cURL

```bash
curl -X POST "http://localhost:8000/api/v1/agent" \
  -H "Content-Type: application/json" \
  -d '{"query": "Your task here"}'
```

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **Root Info**: http://localhost:8000/

## 🎯 What the Agent Can Do

- ✅ Navigate to any website
- ✅ Extract page content, titles, text
- ✅ Click buttons and interact with elements
- ✅ Fill forms
- ✅ Perform searches
- ✅ Scroll and navigate pages
- ✅ Return extracted information

## 📁 Project Structure

```
UK-bot/
├── app/
│   ├── main.py                  # FastAPI app (simplified)
│   ├── routers/
│   │   └── agent.py            # Single agent endpoint
│   └── agents/
│       ├── llms.py             # LLM configuration
│       └── graph.py      # Browser agent logic
├── requirements.txt
├── Makefile
└── .env
```

## 🔧 Configuration

Edit `.env` file:
```bash
OPEN_API_KEY=your_openai_api_key_here
```

## 🚨 Error Handling

If the agent fails, the API returns:
```json
{
  "detail": "Error message here"
}
```

With HTTP status code 500.

## 🎉 That's It!

Your API is now:
- ✅ Clean and simple
- ✅ One endpoint only
- ✅ Ready for production
- ✅ Easy to integrate

Just send a POST request with your task and get the result!

