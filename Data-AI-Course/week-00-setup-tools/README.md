# Week 00: Setup & Tools — AI-Powered Workflows Bootcamp

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Set up a complete Python development environment for AI/ML workflows
2. Configure API access to LLM providers (OpenAI, Anthropic, HuggingFace)
3. Understand and use key AI tooling: LangChain, LlamaIndex, OpenAI SDK
4. Create reproducible development environments with virtual environments and Docker
5. Establish best practices for secrets management and version control
6. Build and run your first LLM-powered application

**Estimated Duration**: 3-4 hours

## 🚀 Why This Matters

A properly configured development environment is the foundation of all AI work. This module saves you hours of troubleshooting and establishes professional workflows from day one. Every tool you'll install serves a specific purpose in modern AI development.

## 📋 Prerequisites

Before starting, ensure you have:
- Basic Python knowledge (variables, functions, imports)
- Familiarity with command line/terminal
- Git installed on your system
- A code editor (VS Code recommended)
- Internet connection for API access

## 🛠️ Technology Stack Overview

### Core Tools
- **Python 3.9+**: Primary programming language
- **pip/uv**: Package management
- **virtualenv/venv**: Environment isolation
- **Git**: Version control
- **Docker**: Containerization (optional but recommended)

### AI/ML Libraries
- **OpenAI SDK**: GPT models access
- **Anthropic SDK**: Claude models access
- **LangChain**: LLM orchestration framework
- **LlamaIndex**: Data framework for LLM applications
- **HuggingFace Transformers**: Open-source models

### Supporting Tools
- **python-dotenv**: Environment variable management
- **requests**: HTTP client
- **jupyter**: Interactive notebooks
- **pytest**: Testing framework

## 📦 Installation Guide

### Step 1: Verify Python Installation (5 min)

```bash
# Check Python version (must be 3.9+)
python --version
# or
python3 --version

# Check pip
pip --version
```

**If Python is not installed or version < 3.9:**
- **macOS**: `brew install python@3.11`
- **Ubuntu/Debian**: `sudo apt update && sudo apt install python3.11 python3.11-venv`
- **Windows**: Download from https://www.python.org/downloads/

### Step 2: Create Project Structure (10 min)

```bash
# Create main project directory
mkdir ai-workflows-bootcamp
cd ai-workflows-bootcamp

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Verify activation (should show path to venv)
which python
```

### Step 3: Install Core Dependencies (10 min)

Create `requirements.txt`:

```text
# LLM SDKs
openai==1.12.0
anthropic==0.18.1
langchain==0.1.9
langchain-openai==0.0.5
langchain-community==0.0.20
llama-index==0.10.11
transformers==4.38.0

# Data & Utilities
python-dotenv==1.0.1
requests==2.31.0
pandas==2.2.0
numpy==1.26.4

# Development
jupyter==1.0.0
ipykernel==6.29.2
pytest==8.0.0
black==24.2.0
flake8==7.0.0

# Vector Databases (for later weeks)
faiss-cpu==1.7.4
chromadb==0.4.22
```

Install all dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure API Keys (15 min)

Create `.env` file in project root:

```bash
# DO NOT COMMIT THIS FILE TO GIT
# Add .env to your .gitignore

# OpenAI
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_ORG_ID=<YOUR_ORG_ID>  # Optional

# Anthropic
ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>

# HuggingFace
HUGGINGFACE_API_KEY=<YOUR_HF_TOKEN>

# Other
LANGCHAIN_API_KEY=<YOUR_LANGCHAIN_KEY>  # Optional for tracing
LANGCHAIN_TRACING_V2=false
```

**Getting API Keys:**
- OpenAI: https://platform.openai.com/api-keys
- Anthropic: https://console.anthropic.com/
- HuggingFace: https://huggingface.co/settings/tokens

Create `.env.example` (safe to commit):

```bash
# Template for environment variables
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
HUGGINGFACE_API_KEY=<YOUR_HF_TOKEN>
```

### Step 5: Create .gitignore (5 min)

Create `.gitignore`:

```gitignore
# Virtual Environment
venv/
env/
.venv/

# Environment Variables
.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter
.ipynb_checkpoints
*.ipynb_checkpoints/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# Data
data/*.csv
data/*.json
!data/sample_*.csv

# Models (large files)
models/
*.pkl
*.h5
*.pt
*.bin

# Logs
*.log
logs/
```

### Step 6: Test API Connectivity (15 min)

Create `test_setup.py`:

```python
"""
Test script to verify API connectivity and environment setup.
Run: python test_setup.py
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test that all required packages are installed."""
    print("✓ Testing imports...")
    try:
        import openai
        import anthropic
        import langchain
        import llama_index
        import transformers
        print("✅ All packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_openai_connection():
    """Test OpenAI API connectivity."""
    print("\n✓ Testing OpenAI API...")
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "<YOUR_OPENAI_API_KEY>":
        print("⚠️  OpenAI API key not configured")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        # Simple test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API test successful'"}],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ OpenAI API working: {result}")
        return True
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False

def test_anthropic_connection():
    """Test Anthropic API connectivity."""
    print("\n✓ Testing Anthropic API...")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key or api_key == "<YOUR_ANTHROPIC_API_KEY>":
        print("⚠️  Anthropic API key not configured")
        return False
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=10,
            messages=[{"role": "user", "content": "Say 'API test successful'"}]
        )
        
        result = message.content[0].text
        print(f"✅ Anthropic API working: {result}")
        return True
    except Exception as e:
        print(f"❌ Anthropic API error: {e}")
        return False

def test_environment():
    """Test environment configuration."""
    print("\n✓ Testing environment...")
    
    required_vars = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
    ]
    
    missing = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith("<YOUR_"):
            missing.append(var)
    
    if missing:
        print(f"⚠️  Missing or not configured: {', '.join(missing)}")
        return False
    
    print("✅ All required environment variables configured")
    return True

def main():
    """Run all tests."""
    print("=" * 60)
    print("AI Workflows Bootcamp - Environment Setup Test")
    print("=" * 60)
    
    results = {
        "Imports": test_imports(),
        "Environment": test_environment(),
        "OpenAI": test_openai_connection(),
        "Anthropic": test_anthropic_connection(),
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for test, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test}: {status}")
    
    all_passed = all(results.values())
    print("\n" + ("🎉 All tests passed!" if all_passed else "⚠️  Some tests failed"))
    print("=" * 60)

if __name__ == "__main__":
    main()
```

Run the test:

```bash
python test_setup.py
```

### Step 7: Your First LLM Application (20 min)

Create `hello_llm.py`:

```python
"""
Your first LLM application - A simple prompt-response example.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def chat_with_gpt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Send a prompt to GPT and return the response.
    
    Args:
        prompt: The user's question or instruction
        model: OpenAI model to use
        
    Returns:
        Model's response as string
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content

def main():
    """Interactive chat loop."""
    print("=" * 60)
    print("Simple LLM Chat - Type 'quit' to exit")
    print("=" * 60)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        try:
            response = chat_with_gpt(user_input)
            print(f"\nAssistant: {response}")
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
```

Run it:

```bash
python hello_llm.py
```

### Step 8: Docker Setup (Optional, 20 min)

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 aiuser && \
    chown -R aiuser:aiuser /app

USER aiuser

# Default command
CMD ["python", "-c", "print('AI Workflows container ready!')"]
```

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  ai-app:
    build: .
    container_name: ai-workflows-app
    volumes:
      - .:/app
      - ./data:/app/data
    env_file:
      - .env
    stdin_open: true
    tty: true
    command: /bin/bash
```

Build and run:

```bash
# Build image
docker-compose build

# Run container
docker-compose run --rm ai-app python test_setup.py
```

## 📊 Project Structure

After setup, your project should look like:

```
ai-workflows-bootcamp/
├── venv/                   # Virtual environment (gitignored)
├── examples/               # Code examples
│   └── week-00/
├── data/                   # Datasets (gitignored)
├── notebooks/              # Jupyter notebooks
├── tests/                  # Test files
├── .env                    # Environment variables (gitignored)
├── .env.example            # Template for .env
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose config
├── test_setup.py           # Setup verification script
└── hello_llm.py            # First LLM application
```

## 🎓 Key Concepts

### Virtual Environments
Isolate project dependencies to avoid conflicts. Each project gets its own Python packages.

### Environment Variables
Store sensitive data (API keys) outside of code. Never commit secrets to Git.

### API Rate Limits
Most LLM providers have rate limits:
- OpenAI: Varies by tier (check dashboard)
- Anthropic: Based on usage tier
- Monitor usage to avoid unexpected costs

### Token Economy
LLMs charge by tokens (roughly 4 characters = 1 token):
- Input tokens: Your prompt
- Output tokens: Model's response
- Different models have different pricing

## 💡 Best Practices

1. **Always use virtual environments** - Keep dependencies isolated
2. **Never commit API keys** - Use .env files and .gitignore
3. **Pin dependency versions** - Ensure reproducibility
4. **Test your setup** - Run test_setup.py after configuration
5. **Monitor API usage** - Set up billing alerts
6. **Use version control** - Commit code regularly (but not secrets!)
7. **Document your environment** - Keep requirements.txt updated

## 🔧 Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError`
**Solution**: Ensure virtual environment is activated and dependencies installed

**Problem**: API key errors
**Solution**: Verify .env file exists and keys are correct (no quotes needed)

**Problem**: SSL certificate errors
**Solution**: Update certifi: `pip install --upgrade certifi`

**Problem**: Docker build fails
**Solution**: Ensure Docker daemon is running: `docker info`

## 🚀 Next Steps

Once you've completed this setup:

1. ✅ Verify all tests pass in `test_setup.py`
2. ✅ Successfully run `hello_llm.py`
3. ✅ Commit your code (excluding .env!)
4. ✅ Proceed to **Week 01: Prompt Engineering Fundamentals**

## 📚 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Docker for Beginners](https://docker-curriculum.com/)

## 🎯 Pareto Principle (20/80 Rule)

### 20% of Concepts (Core Fundamentals)
1. **Virtual environments** - Foundation of Python project management
2. **API key management** - Essential for security and functionality
3. **Basic LLM API calls** - The building block of all AI workflows

### 80% of Practice (Hands-on Application)
1. Set up environment from scratch multiple times until automatic
2. Build 3-5 simple LLM applications with different prompts
3. Practice debugging API errors and connectivity issues

---

**Congratulations! 🎉** You now have a professional-grade development environment for AI workflows. You're ready to start building intelligent applications!
