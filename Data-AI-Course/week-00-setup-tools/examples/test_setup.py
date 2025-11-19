"""
Test script to verify API connectivity and environment setup.
Week 00 - Setup & Tools

Run this after completing environment setup to ensure everything works.
Usage: python test_setup.py
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_imports():
    """Test that all required packages are installed."""
    print("=" * 60)
    print("Testing Package Imports")
    print("=" * 60)
    
    required_packages = [
        ("openai", "OpenAI SDK"),
        ("anthropic", "Anthropic SDK"),
        ("langchain", "LangChain"),
        ("langchain_openai", "LangChain OpenAI"),
        ("llama_index", "LlamaIndex"),
        ("transformers", "HuggingFace Transformers"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("dotenv", "python-dotenv"),
    ]
    
    failed = []
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name:30s} imported successfully")
        except ImportError as e:
            print(f"❌ {name:30s} import failed: {e}")
            failed.append(name)
    
    if failed:
        print(f"\n⚠️  Failed imports: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All packages imported successfully")
    return True


def test_environment():
    """Test environment configuration."""
    print("\n" + "=" * 60)
    print("Testing Environment Variables")
    print("=" * 60)
    
    required_vars = {
        "OPENAI_API_KEY": "OpenAI API",
        "ANTHROPIC_API_KEY": "Anthropic API",
    }
    
    optional_vars = {
        "HUGGINGFACE_API_KEY": "HuggingFace API",
        "LANGCHAIN_API_KEY": "LangChain Tracing",
    }
    
    missing_required = []
    for var, name in required_vars.items():
        value = os.getenv(var)
        if not value or value.startswith("<YOUR_"):
            print(f"❌ {name:30s} not configured")
            missing_required.append(name)
        else:
            masked = value[:8] + "..." + value[-4:] if len(value) > 12 else "***"
            print(f"✅ {name:30s} configured ({masked})")
    
    for var, name in optional_vars.items():
        value = os.getenv(var)
        if value and not value.startswith("<YOUR_"):
            masked = value[:8] + "..." + value[-4:] if len(value) > 12 else "***"
            print(f"✅ {name:30s} configured ({masked})")
        else:
            print(f"⚠️  {name:30s} not configured (optional)")
    
    if missing_required:
        print(f"\n❌ Missing required variables: {', '.join(missing_required)}")
        print("Create .env file with your API keys")
        return False
    
    print("\n✅ All required environment variables configured")
    return True


def test_openai_connection():
    """Test OpenAI API connectivity."""
    print("\n" + "=" * 60)
    print("Testing OpenAI API Connection")
    print("=" * 60)
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key.startswith("<YOUR_"):
        print("⚠️  Skipping (API key not configured)")
        return False
    
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=api_key)
        
        print("Sending test request to OpenAI...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'API test successful' and nothing else"}
            ],
            max_tokens=10,
            temperature=0
        )
        
        result = response.choices[0].message.content
        tokens = response.usage.total_tokens
        
        print(f"✅ OpenAI API working")
        print(f"   Response: {result}")
        print(f"   Tokens used: {tokens}")
        print(f"   Model: {response.model}")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False


def test_anthropic_connection():
    """Test Anthropic API connectivity."""
    print("\n" + "=" * 60)
    print("Testing Anthropic API Connection")
    print("=" * 60)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key or api_key.startswith("<YOUR_"):
        print("⚠️  Skipping (API key not configured)")
        return False
    
    try:
        import anthropic
        
        client = anthropic.Anthropic(api_key=api_key)
        
        print("Sending test request to Anthropic...")
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "Say 'API test successful' and nothing else"}
            ]
        )
        
        result = message.content[0].text
        tokens = message.usage.input_tokens + message.usage.output_tokens
        
        print(f"✅ Anthropic API working")
        print(f"   Response: {result}")
        print(f"   Tokens used: {tokens}")
        print(f"   Model: {message.model}")
        return True
        
    except Exception as e:
        print(f"❌ Anthropic API error: {e}")
        return False


def test_langchain():
    """Test LangChain integration."""
    print("\n" + "=" * 60)
    print("Testing LangChain Integration")
    print("=" * 60)
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key.startswith("<YOUR_"):
        print("⚠️  Skipping (OpenAI API key not configured)")
        return False
    
    try:
        from langchain_openai import ChatOpenAI
        from langchain.prompts import ChatPromptTemplate
        from langchain.schema.output_parser import StrOutputParser
        
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            api_key=api_key,
            max_tokens=10
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "Say 'LangChain test successful' and nothing else")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        print("Testing LangChain chain...")
        result = chain.invoke({})
        
        print(f"✅ LangChain working")
        print(f"   Response: {result}")
        return True
        
    except Exception as e:
        print(f"❌ LangChain error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("AI WORKFLOWS BOOTCAMP - ENVIRONMENT SETUP TEST")
    print("Week 00: Setup & Tools")
    print("=" * 60)
    
    results = {
        "Package Imports": test_imports(),
        "Environment Variables": test_environment(),
        "OpenAI API": test_openai_connection(),
        "Anthropic API": test_anthropic_connection(),
        "LangChain Integration": test_langchain(),
    }
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test:30s} {status}")
    
    passed_count = sum(results.values())
    total_count = len(results)
    
    print("\n" + "=" * 60)
    print(f"Results: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 Congratulations! Your environment is fully configured!")
        print("You're ready to start Week 01: Prompt Engineering")
        return 0
    elif passed_count >= 3:
        print("\n⚠️  Most tests passed. Review failures and fix if needed.")
        print("You can proceed with caution or fix issues first.")
        return 0
    else:
        print("\n❌ Multiple tests failed. Please fix configuration issues.")
        print("Review the README.md and troubleshooting guide.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
