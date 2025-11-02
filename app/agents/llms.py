from dotenv import load_dotenv
load_dotenv()

import os

# Use browser_use's native ChatOpenAI for full compatibility
from browser_use.llm.openai.chat import ChatOpenAI

# Create LLM instance using browser_use's implementation
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
)