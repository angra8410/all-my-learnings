#!/usr/bin/env python3
"""
MCP Agent - Model Context Protocol Agent Example

This is a minimal runnable example of an MCP agent that processes prompts
and returns mock responses. This implementation demonstrates the basic
structure and flow of an MCP agent.

Requirements:
    - Python 3.9+
    - No external dependencies required for basic functionality

How to run:
    python agent.py

Expected output:
    The agent will process a few example prompts and display the responses.

Architecture:
    - MCPAgent: Main agent class that coordinates prompt processing
    - LLMMockAdapter: Simulates an LLM response (no real AI model)
    - PromptParser: Parses and validates input prompts
    - ResponseFormatter: Formats the output responses

Future enhancements:
    - Integration with real LLM APIs (OpenAI, Anthropic, etc.)
    - Persistent context management
    - Async processing
    - Error handling and retry logic
"""

import json
from typing import Union, Dict, Any
from datetime import datetime


class LLMMockAdapter:
    """
    Mock LLM adapter that simulates responses from a language model.
    In a real implementation, this would call an actual LLM API.
    """
    
    def __init__(self, model_name: str = "mcp-mock-v1"):
        self.model_name = model_name
    
    def generate_response(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """
        Generate a mock response for the given prompt.
        
        Args:
            prompt (str): The input prompt
            context (dict): Optional context information
            
        Returns:
            str: Generated response (mock)
        """
        # In a real implementation, this would call an LLM API
        # For now, we just echo back with a prefix
        response = f"Respuesta del agente MCP: {prompt}"
        
        if context and context.get("previous_topic"):
            response = f"Basado en el contexto de {context['previous_topic']}, {response}"
        
        return response


class PromptParser:
    """
    Parser for handling different prompt formats.
    Supports both simple strings and structured JSON prompts.
    """
    
    @staticmethod
    def parse(prompt: Union[str, dict]) -> Dict[str, Any]:
        """
        Parse the input prompt and extract relevant information.
        
        Args:
            prompt (str | dict): Input prompt in string or dict format
            
        Returns:
            dict: Parsed prompt with extracted fields
        """
        if isinstance(prompt, str):
            return {
                "prompt_text": prompt,
                "context": {},
                "parameters": {}
            }
        elif isinstance(prompt, dict):
            return {
                "prompt_text": prompt.get("prompt", ""),
                "context": prompt.get("context", {}),
                "parameters": prompt.get("parameters", {})
            }
        else:
            raise ValueError("Prompt must be a string or dictionary")


class ResponseFormatter:
    """
    Formatter for agent responses.
    Can output simple strings or structured JSON responses.
    """
    
    @staticmethod
    def format_simple(response_text: str) -> str:
        """
        Format a simple text response.
        
        Args:
            response_text (str): The response text
            
        Returns:
            str: Formatted response
        """
        return response_text
    
    @staticmethod
    def format_structured(response_text: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a structured JSON response with metadata.
        
        Args:
            response_text (str): The response text
            metadata (dict): Metadata about the response
            
        Returns:
            dict: Structured response
        """
        return {
            "response": response_text,
            "metadata": metadata,
            "status": "success",
            "timestamp": datetime.now().isoformat()
        }


class MCPAgent:
    """
    Main MCP Agent class.
    
    This agent processes prompts following the Model Context Protocol,
    maintains conversation context, and generates appropriate responses.
    
    Usage:
        agent = MCPAgent()
        response = agent.process_prompt("Hello, how are you?")
        print(response)
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize the MCP Agent.
        
        Args:
            config (dict): Optional configuration dictionary
        """
        self.config = config or {}
        self.llm_adapter = LLMMockAdapter(
            model_name=self.config.get("model_name", "mcp-mock-v1")
        )
        self.parser = PromptParser()
        self.formatter = ResponseFormatter()
        self.context = {}
        
    def set_context(self, context: Dict[str, Any]) -> None:
        """
        Set the conversation context for the agent.
        
        Args:
            context (dict): Context information
        """
        self.context.update(context)
    
    def process_prompt(self, prompt: Union[str, dict], structured_output: bool = False) -> Union[str, Dict[str, Any]]:
        """
        Process a prompt and generate a response.
        
        This is the main entry point for the agent. It parses the prompt,
        generates a response using the LLM adapter, and formats the output.
        
        Args:
            prompt (str | dict): Input prompt
            structured_output (bool): If True, return structured JSON response
            
        Returns:
            str | dict: Agent response
        """
        try:
            # Parse the input prompt
            parsed = self.parser.parse(prompt)
            prompt_text = parsed["prompt_text"]
            prompt_context = parsed["context"]
            
            # Merge prompt context with agent context
            full_context = {**self.context, **prompt_context}
            
            # Generate response using LLM adapter
            response_text = self.llm_adapter.generate_response(
                prompt=prompt_text,
                context=full_context
            )
            
            # Format the response
            if structured_output:
                metadata = {
                    "model": self.llm_adapter.model_name,
                    "tokens_used": len(response_text.split()),  # Mock token count
                    "processing_time_ms": 45,  # Mock processing time
                }
                if prompt_context.get("conversation_id"):
                    metadata["conversation_id"] = prompt_context["conversation_id"]
                
                return self.formatter.format_structured(response_text, metadata)
            else:
                return self.formatter.format_simple(response_text)
                
        except Exception as e:
            # In a real implementation, we would have proper error handling
            error_response = {
                "status": "error",
                "error": {
                    "type": type(e).__name__,
                    "message": str(e),
                    "code": "PROCESSING_ERROR"
                }
            }
            return error_response if structured_output else f"Error: {str(e)}"


def main():
    """
    Main function demonstrating the MCP Agent usage.
    """
    print("=" * 60)
    print("MCP Agent - Model Context Protocol Agent Example")
    print("=" * 60)
    print()
    
    # Create an agent instance
    agent = MCPAgent(config={"model_name": "mcp-mock-v1"})
    
    # Example 1: Simple prompt
    print("Example 1: Simple Prompt")
    print("-" * 60)
    prompt1 = "¿Cuál es el significado de la vida?"
    response1 = agent.process_prompt(prompt1)
    print(f"Prompt: {prompt1}")
    print(f"Response: {response1}")
    print()
    
    # Example 2: Structured prompt with context
    print("Example 2: Structured Prompt with Context")
    print("-" * 60)
    prompt2 = {
        "prompt": "Continúa la conversación sobre Python",
        "context": {
            "previous_topic": "Programación en Python",
            "conversation_id": "conv-789"
        }
    }
    response2 = agent.process_prompt(prompt2, structured_output=True)
    print(f"Prompt: {json.dumps(prompt2, indent=2, ensure_ascii=False)}")
    print(f"Response: {json.dumps(response2, indent=2, ensure_ascii=False)}")
    print()
    
    # Example 3: Using set_context
    print("Example 3: Using Context Manager")
    print("-" * 60)
    agent.set_context({"user_id": "user-123", "session": "session-456"})
    prompt3 = "¿Qué es el Model Context Protocol?"
    response3 = agent.process_prompt(prompt3, structured_output=True)
    print(f"Prompt: {prompt3}")
    print(f"Response: {json.dumps(response3, indent=2, ensure_ascii=False)}")
    print()
    
    print("=" * 60)
    print("Agent execution completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
