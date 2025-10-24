"""
Agent Core - Simple implementation of an AI agent.
This is a minimal agent that can process queries and use tools.
"""

from typing import List, Dict, Any, Callable
from dataclasses import dataclass
import json


@dataclass
class Tool:
    """Represents a tool that the agent can use."""
    name: str
    description: str
    function: Callable


class AgentCore:
    """
    Core agent implementation.
    
    This agent can:
    - Process natural language queries
    - Select appropriate tools
    - Execute tools
    - Generate responses
    """
    
    def __init__(self, tools: List[Tool] = None):
        """Initialize the agent with available tools."""
        self.tools = tools or []
        self.conversation_history = []
    
    def add_tool(self, tool: Tool):
        """Add a new tool to the agent."""
        self.tools.append(tool)
        print(f"✅ Tool added: {tool.name}")
    
    def list_tools(self) -> List[str]:
        """List all available tools."""
        return [f"{tool.name}: {tool.description}" for tool in self.tools]
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query.
        
        Steps:
        1. Analyze the query
        2. Select appropriate tool
        3. Execute tool
        4. Generate response
        """
        print(f"\n🤔 Processing query: {query}")
        
        # Step 1: Analyze query (simplified - in real agent, use LLM)
        analysis = self._analyze_query(query)
        
        # Step 2: Select tool
        selected_tool = self._select_tool(analysis)
        
        # Step 3: Execute tool
        if selected_tool:
            tool_result = self._execute_tool(selected_tool, analysis)
        else:
            tool_result = {"error": "No suitable tool found"}
        
        # Step 4: Generate response
        response = self._generate_response(query, tool_result)
        
        # Save to history
        self.conversation_history.append({
            "query": query,
            "response": response
        })
        
        return response
    
    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze the query to understand intent."""
        query_lower = query.lower()
        
        analysis = {
            "original_query": query,
            "keywords": query_lower.split(),
            "intent": "unknown"
        }
        
        # Simple keyword matching (in real agent, use NLU)
        if any(word in query_lower for word in ["weather", "temperature", "clima"]):
            analysis["intent"] = "weather"
        elif any(word in query_lower for word in ["time", "hora", "clock"]):
            analysis["intent"] = "time"
        elif any(word in query_lower for word in ["calculate", "math", "calcular"]):
            analysis["intent"] = "calculator"
        
        return analysis
    
    def _select_tool(self, analysis: Dict[str, Any]) -> Tool:
        """Select the most appropriate tool based on analysis."""
        intent = analysis["intent"]
        
        for tool in self.tools:
            if intent in tool.name.lower():
                print(f"🔧 Selected tool: {tool.name}")
                return tool
        
        print("⚠️  No tool selected")
        return None
    
    def _execute_tool(self, tool: Tool, analysis: Dict[str, Any]) -> Any:
        """Execute the selected tool."""
        try:
            print(f"⚙️  Executing tool: {tool.name}")
            result = tool.function(analysis)
            print(f"✅ Tool execution successful")
            return result
        except Exception as e:
            print(f"❌ Tool execution failed: {e}")
            return {"error": str(e)}
    
    def _generate_response(self, query: str, tool_result: Any) -> Dict[str, Any]:
        """Generate a natural language response."""
        if isinstance(tool_result, dict) and "error" in tool_result:
            message = f"I couldn't process your query: {tool_result['error']}"
        else:
            message = f"Based on your query, here's what I found: {tool_result}"
        
        return {
            "query": query,
            "result": tool_result,
            "message": message,
            "status": "success" if "error" not in str(tool_result) else "error"
        }
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Get conversation history."""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        print("🗑️  History cleared")


# Example usage
if __name__ == "__main__":
    # Create agent
    agent = AgentCore()
    
    # Define some example tools
    def weather_tool(analysis):
        """Mock weather tool."""
        return {
            "temperature": "25°C",
            "condition": "Sunny",
            "location": "Madrid"
        }
    
    def time_tool(analysis):
        """Mock time tool."""
        from datetime import datetime
        return {
            "current_time": datetime.now().strftime("%H:%M:%S"),
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    
    # Add tools to agent
    agent.add_tool(Tool(
        name="weather",
        description="Get weather information",
        function=weather_tool
    ))
    
    agent.add_tool(Tool(
        name="time",
        description="Get current time",
        function=time_tool
    ))
    
    # Test the agent
    print("\n" + "="*50)
    print("🤖 Agent Core Demo")
    print("="*50)
    
    print("\n📋 Available tools:")
    for tool_info in agent.list_tools():
        print(f"  • {tool_info}")
    
    # Process some queries
    queries = [
        "What's the weather like?",
        "What time is it?",
        "Tell me about the climate"
    ]
    
    for query in queries:
        response = agent.process_query(query)
        print(f"\n💬 Response: {response['message']}")
    
    print("\n" + "="*50)
    print("📚 Conversation History:")
    for i, entry in enumerate(agent.get_history(), 1):
        print(f"\n{i}. Q: {entry['query']}")
        print(f"   A: {entry['response']['message']}")
