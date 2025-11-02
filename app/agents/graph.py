"""
Browser agent implementation with streaming support.

This module provides browser automation using browser_use library
with support for both streaming and non-streaming execution.
"""

import asyncio
from browser_use import Agent as Ag 

# Handle both relative and absolute imports
try:
    from .llms import llm  # When imported as a module
except ImportError:
    from llms import llm  # When run directly


async def browser_use_agent(instructions: str) -> str:
    """
    Run browser automation agent without streaming.
    
    Args:
        instructions: Task description for the agent
        
    Returns:
        Final result from the agent execution
    """
    agent = Ag( 
        task=instructions, 
        llm=llm, 
        use_vision=False,
    )
    result = await agent.run() 
    return result.final_result() 


async def browser_use_agent_streaming(instructions: str, verbose: bool = True) -> str:
    """
    Run browser automation agent with live streaming updates.
    
    Args:
        instructions: Task description for the agent
        verbose: Whether to print streaming updates
        
    Returns:
        Final result from the agent execution
    """
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"🤖 Starting Agent: {instructions}")
        print(f"{'='*60}\n")
    
    step_count = [0]
    
    async def on_step_start(agent):
        step_count[0] += 1
        if verbose:
            print(f"📍 Step {step_count[0]}")
            print(f"   Status: Processing...")
    
    async def on_step_end(agent):
        if verbose:
            print(f"   ✓ Step {step_count[0]} completed\n")
    
    agent = Ag(
        task=instructions,
        llm=llm,
        use_vision=False,
    )
    
    result = await agent.run(
        max_steps=100,
        on_step_start=on_step_start,
        on_step_end=on_step_end
    )
    
    final_result = result.final_result() if result else "No result"
    
    if verbose:
        print(f"{'='*60}")
        print(f"✅ Completed in {step_count[0]} steps")
        print(f"{'='*60}\n")
    
    return final_result


# For LangGraph integration - example structure
async def create_multi_agent_graph():
    """
    Create a LangGraph multi-agent system.
    
    This is a placeholder for your LangGraph implementation.
    You can add multiple agents with different roles here.
    """
    # TODO: Implement LangGraph workflow
    # from langgraph.graph import StateGraph
    # workflow = StateGraph(YourState)
    # workflow.add_node("researcher", researcher_agent)
    # workflow.add_node("browser", browser_use_agent)
    # ...
    pass


# Test the agent when run directly
if __name__ == "__main__":
    print("🧪 Testing browser agent (clean version)...\n")
    
    # Test task
    print("="*60)
    print("TEST: Simple website visit")
    print("="*60)
    test_task = "Go to example.com and tell me the page title"
    result = asyncio.run(browser_use_agent_streaming(test_task))
    print(f"🎯 Result: {result}\n")
