#!/usr/bin/env python3
"""
Basic unit tests for the MCP Agent.

These tests verify the basic functionality of the agent including:
- Prompt processing
- Response generation
- Context management
- Input validation

Run tests with:
    python -m pytest tests/test_agent_basic.py -v

Or from the MCP-Agent directory:
    python -m pytest tests/ -v
"""

import sys
import os

# Add the examples directory to the path so we can import the agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

import json
from agent import MCPAgent, LLMMockAdapter, PromptParser, ResponseFormatter


class TestLLMMockAdapter:
    """Test the LLM Mock Adapter"""
    
    def test_adapter_initialization(self):
        """Test that the adapter initializes correctly"""
        adapter = LLMMockAdapter()
        assert adapter.model_name == "mcp-mock-v1"
    
    def test_adapter_custom_model_name(self):
        """Test adapter with custom model name"""
        adapter = LLMMockAdapter(model_name="custom-model")
        assert adapter.model_name == "custom-model"
    
    def test_generate_response_simple(self):
        """Test simple response generation"""
        adapter = LLMMockAdapter()
        response = adapter.generate_response("Hello")
        assert "Respuesta del agente MCP:" in response
        assert "Hello" in response
    
    def test_generate_response_with_context(self):
        """Test response generation with context"""
        adapter = LLMMockAdapter()
        context = {"previous_topic": "Python"}
        response = adapter.generate_response("Continue", context=context)
        assert "Python" in response
        assert "Continue" in response


class TestPromptParser:
    """Test the Prompt Parser"""
    
    def test_parse_string_prompt(self):
        """Test parsing a simple string prompt"""
        parser = PromptParser()
        result = parser.parse("Test prompt")
        
        assert result["prompt_text"] == "Test prompt"
        assert result["context"] == {}
        assert result["parameters"] == {}
    
    def test_parse_dict_prompt(self):
        """Test parsing a structured dictionary prompt"""
        parser = PromptParser()
        prompt = {
            "prompt": "Test question",
            "context": {"user": "test_user"},
            "parameters": {"max_tokens": 100}
        }
        result = parser.parse(prompt)
        
        assert result["prompt_text"] == "Test question"
        assert result["context"]["user"] == "test_user"
        assert result["parameters"]["max_tokens"] == 100
    
    def test_parse_invalid_type(self):
        """Test that invalid prompt types raise an error"""
        parser = PromptParser()
        try:
            parser.parse(12345)  # Invalid type
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "must be a string or dictionary" in str(e)


class TestResponseFormatter:
    """Test the Response Formatter"""
    
    def test_format_simple(self):
        """Test simple text formatting"""
        formatter = ResponseFormatter()
        result = formatter.format_simple("Simple response")
        assert result == "Simple response"
    
    def test_format_structured(self):
        """Test structured JSON formatting"""
        formatter = ResponseFormatter()
        metadata = {"model": "test-model", "tokens": 10}
        result = formatter.format_structured("Structured response", metadata)
        
        assert result["response"] == "Structured response"
        assert result["metadata"]["model"] == "test-model"
        assert result["metadata"]["tokens"] == 10
        assert result["status"] == "success"
        assert "timestamp" in result


class TestMCPAgent:
    """Test the main MCP Agent"""
    
    def test_agent_initialization(self):
        """Test that the agent initializes correctly"""
        agent = MCPAgent()
        assert agent.llm_adapter is not None
        assert agent.parser is not None
        assert agent.formatter is not None
        assert agent.context == {}
    
    def test_agent_custom_config(self):
        """Test agent initialization with custom config"""
        config = {"model_name": "custom-model"}
        agent = MCPAgent(config=config)
        assert agent.llm_adapter.model_name == "custom-model"
    
    def test_set_context(self):
        """Test setting agent context"""
        agent = MCPAgent()
        agent.set_context({"user_id": "123", "session": "abc"})
        assert agent.context["user_id"] == "123"
        assert agent.context["session"] == "abc"
    
    def test_process_simple_prompt(self):
        """Test processing a simple string prompt"""
        agent = MCPAgent()
        response = agent.process_prompt("¿Cuál es el significado de la vida?")
        
        assert isinstance(response, str)
        assert "¿Cuál es el significado de la vida?" in response
        assert "Respuesta del agente MCP:" in response
    
    def test_process_structured_prompt(self):
        """Test processing a structured prompt"""
        agent = MCPAgent()
        prompt = {
            "prompt": "Test question",
            "context": {"conversation_id": "conv-123"}
        }
        response = agent.process_prompt(prompt, structured_output=True)
        
        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "response" in response
        assert "metadata" in response
        assert response["metadata"]["conversation_id"] == "conv-123"
    
    def test_process_prompt_with_context(self):
        """Test that agent context is used in processing"""
        agent = MCPAgent()
        agent.set_context({"previous_topic": "MCP"})
        
        prompt = {
            "prompt": "Continue the conversation",
            "context": {}
        }
        response = agent.process_prompt(prompt, structured_output=True)
        
        assert isinstance(response, dict)
        assert "MCP" in response["response"]
    
    def test_multiple_prompts(self):
        """Test processing multiple prompts in sequence"""
        agent = MCPAgent()
        
        response1 = agent.process_prompt("First prompt")
        response2 = agent.process_prompt("Second prompt")
        
        assert isinstance(response1, str)
        assert isinstance(response2, str)
        assert "First prompt" in response1
        assert "Second prompt" in response2
    
    def test_error_handling(self):
        """Test that errors are handled gracefully"""
        agent = MCPAgent()
        # This should not crash even with unusual input
        response = agent.process_prompt("", structured_output=True)
        assert isinstance(response, dict)


def test_agent_example_scenario():
    """
    Integration test: Full example scenario
    
    This test simulates a complete interaction with the agent,
    as described in the specification.
    """
    # Initialize agent
    agent = MCPAgent(config={"model_name": "mcp-mock-v1"})
    
    # Set initial context
    agent.set_context({"user_id": "test-user-001", "session": "test-session"})
    
    # Process a simple prompt
    response1 = agent.process_prompt("¿Qué es el Model Context Protocol?")
    assert isinstance(response1, str)
    assert len(response1) > 0
    
    # Process a structured prompt
    structured_prompt = {
        "prompt": "Explica más sobre MCP",
        "context": {
            "conversation_id": "conv-001",
            "previous_topic": "Model Context Protocol"
        },
        "parameters": {
            "max_tokens": 100
        }
    }
    response2 = agent.process_prompt(structured_prompt, structured_output=True)
    
    assert isinstance(response2, dict)
    assert response2["status"] == "success"
    assert "response" in response2
    assert "metadata" in response2
    assert response2["metadata"]["conversation_id"] == "conv-001"
    
    print("✅ Integration test passed successfully!")


if __name__ == "__main__":
    """
    Run tests directly without pytest (basic test runner)
    """
    import traceback
    
    print("=" * 60)
    print("Running MCP Agent Basic Tests")
    print("=" * 60)
    print()
    
    test_classes = [
        TestLLMMockAdapter,
        TestPromptParser,
        TestResponseFormatter,
        TestMCPAgent
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for test_class in test_classes:
        print(f"\n{test_class.__name__}")
        print("-" * 60)
        
        test_instance = test_class()
        test_methods = [method for method in dir(test_instance) if method.startswith("test_")]
        
        for method_name in test_methods:
            total_tests += 1
            try:
                method = getattr(test_instance, method_name)
                method()
                print(f"  ✅ {method_name}")
                passed_tests += 1
            except Exception as e:
                print(f"  ❌ {method_name}: {str(e)}")
                traceback.print_exc()
                failed_tests += 1
    
    # Run integration test
    print("\n" + "=" * 60)
    print("Integration Test")
    print("-" * 60)
    total_tests += 1
    try:
        test_agent_example_scenario()
        passed_tests += 1
    except Exception as e:
        print(f"❌ Integration test failed: {str(e)}")
        traceback.print_exc()
        failed_tests += 1
    
    print("\n" + "=" * 60)
    print(f"Test Summary: {passed_tests}/{total_tests} passed, {failed_tests} failed")
    print("=" * 60)
    
    sys.exit(0 if failed_tests == 0 else 1)
