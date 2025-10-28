#!/usr/bin/env python3
"""
Basic unit tests for MCP Agent

Tests the core functionality of the agent including:
- Prompt validation
- Context enrichment
- Response generation
- Error handling

Run with:
    python -m pytest tests/test_agent_basic.py -v
    
Or with unittest:
    python -m unittest tests.test_agent_basic
"""

import unittest
import sys
import os

# Add parent directory to path to import agent module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

from agent import MCPAgent, MockLLM


class TestMockLLM(unittest.TestCase):
    """Test cases for the Mock LLM"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.llm = MockLLM()
    
    def test_llm_initialization(self):
        """Test that LLM initializes correctly"""
        self.assertEqual(self.llm.model_name, "mock-llm-v1")
        self.assertIsNotNone(self.llm.response_templates)
    
    def test_llm_generate_greeting(self):
        """Test LLM generates greeting response"""
        response = self.llm.generate("Hello, how are you?")
        self.assertIn("mcp agent", response.lower())
    
    def test_llm_generate_python(self):
        """Test LLM generates Python-related response"""
        response = self.llm.generate("What is Python?")
        self.assertIn("python", response.lower())
        self.assertIn("programming language", response.lower())
    
    def test_llm_generate_default(self):
        """Test LLM generates default response for unknown prompts"""
        response = self.llm.generate("Random question about something")
        self.assertTrue("mock" in response.lower() or "response" in response.lower())


class TestMCPAgent(unittest.TestCase):
    """Test cases for the MCP Agent"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = MCPAgent()
    
    def test_agent_initialization(self):
        """Test that agent initializes correctly"""
        self.assertIsNotNone(self.agent.llm)
        self.assertEqual(self.agent.version, "0.1-mock")
    
    def test_validate_prompt_valid(self):
        """Test validation of valid prompt"""
        prompt_data = {
            "prompt": "Test prompt",
            "role": "user"
        }
        is_valid, error = self.agent.validate_prompt(prompt_data)
        self.assertTrue(is_valid)
        self.assertIsNone(error)
    
    def test_validate_prompt_missing_field(self):
        """Test validation fails when prompt field is missing"""
        prompt_data = {
            "role": "user"
        }
        is_valid, error = self.agent.validate_prompt(prompt_data)
        self.assertFalse(is_valid)
        self.assertIn("Missing required field", error)
    
    def test_validate_prompt_empty(self):
        """Test validation fails when prompt is empty"""
        prompt_data = {
            "prompt": "",
            "role": "user"
        }
        is_valid, error = self.agent.validate_prompt(prompt_data)
        self.assertFalse(is_valid)
        self.assertIn("non-empty string", error)
    
    def test_validate_prompt_invalid_max_tokens(self):
        """Test validation fails with invalid max_tokens"""
        prompt_data = {
            "prompt": "Test",
            "max_tokens": -5
        }
        is_valid, error = self.agent.validate_prompt(prompt_data)
        self.assertFalse(is_valid)
        self.assertIn("positive integer", error)
    
    def test_enrich_context_no_context(self):
        """Test context enrichment without context"""
        prompt_data = {
            "prompt": "Test prompt"
        }
        enriched = self.agent.enrich_context(prompt_data)
        self.assertEqual(enriched, "Test prompt")
    
    def test_enrich_context_with_context(self):
        """Test context enrichment with context"""
        prompt_data = {
            "prompt": "Follow-up question",
            "context": {
                "previous_question": "What is Python?",
                "previous_answer": "Python is a programming language"
            }
        }
        enriched = self.agent.enrich_context(prompt_data)
        self.assertIn("previous_question", enriched)
        self.assertIn("Follow-up question", enriched)
    
    def test_process_prompt_success(self):
        """Test successful prompt processing"""
        prompt_data = {
            "prompt": "Hello, how are you?",
            "role": "user"
        }
        result = self.agent.process_prompt(prompt_data)
        
        # Check response structure
        self.assertIn("response", result)
        self.assertIn("status", result)
        self.assertIn("metadata", result)
        
        # Check status is success
        self.assertEqual(result["status"], "success")
        
        # Check response is not empty
        self.assertTrue(len(result["response"]) > 0)
        
        # Check metadata
        self.assertIn("model", result["metadata"])
        self.assertIn("tokens_used", result["metadata"])
        self.assertIn("processing_time", result["metadata"])
        self.assertIn("timestamp", result["metadata"])
    
    def test_process_prompt_error_handling(self):
        """Test error handling for invalid prompt"""
        prompt_data = {
            "role": "user"
            # Missing 'prompt' field
        }
        result = self.agent.process_prompt(prompt_data)
        
        # Check that status is error
        self.assertEqual(result["status"], "error")
        
        # Check that error message exists
        self.assertIn("error", result)
        self.assertTrue(len(result["error"]) > 0)
    
    def test_process_prompt_with_parameters(self):
        """Test prompt processing with custom parameters"""
        prompt_data = {
            "prompt": "Test prompt with parameters",
            "role": "user",
            "max_tokens": 100,
            "temperature": 0.5
        }
        result = self.agent.process_prompt(prompt_data)
        
        # Check successful processing
        self.assertEqual(result["status"], "success")
        self.assertTrue(len(result["response"]) > 0)


class TestAgentIntegration(unittest.TestCase):
    """Integration tests for the MCP Agent"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = MCPAgent()
    
    def test_conversation_flow(self):
        """Test multi-turn conversation flow"""
        # First prompt
        prompt1 = {
            "prompt": "What is Python?",
            "role": "user"
        }
        result1 = self.agent.process_prompt(prompt1)
        self.assertEqual(result1["status"], "success")
        
        # Follow-up prompt with context
        prompt2 = {
            "prompt": "Tell me more",
            "role": "user",
            "context": {
                "previous_question": prompt1["prompt"],
                "previous_answer": result1["response"]
            }
        }
        result2 = self.agent.process_prompt(prompt2)
        self.assertEqual(result2["status"], "success")
    
    def test_multiple_prompts_sequence(self):
        """Test processing multiple prompts in sequence"""
        prompts = [
            {"prompt": "Hello"},
            {"prompt": "What is MCP?"},
            {"prompt": "Explain Python"},
        ]
        
        for prompt_data in prompts:
            result = self.agent.process_prompt(prompt_data)
            self.assertEqual(result["status"], "success")
            self.assertTrue(len(result["response"]) > 0)


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestMockLLM))
    suite.addTests(loader.loadTestsFromTestCase(TestMCPAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestAgentIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on results
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    # Run tests when executed directly
    exit_code = run_tests()
    sys.exit(exit_code)
