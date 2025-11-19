# Project Steps - Week 00: Setup & Tools

## 🎯 Overview

This document outlines incremental tasks that contribute to your capstone project. While Week 00 focuses on environment setup, the infrastructure you build here will be used throughout all four capstone projects.

## 📊 Capstone Projects Reminder

1. **FINANCE**: Loan Default Prediction with ETL, feature store, LLM/ML ensemble
2. **SPORTS**: NFL Draft Sentiment Analysis with social scraping, sentiment model
3. **E-COMMERCE**: Order Management Chatbot with RAG and tool integration
4. **ENTERPRISE**: Salesforce CRM Q&A Assistant with access control

## 🏗️ Week 00 Contributions to Capstone

### Task 1: Project Repository Structure (30 min)

Create a unified repository structure that will house all four capstone projects:

```bash
mkdir -p capstone-projects/{finance,sports,ecommerce,enterprise}
mkdir -p capstone-projects/shared/{utils,data,models,configs}
```

**Directory structure:**
```
capstone-projects/
├── finance/                  # Loan default prediction
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   └── tests/
├── sports/                   # NFL sentiment analysis
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   └── tests/
├── ecommerce/                # Order chatbot
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   └── tests/
├── enterprise/               # Salesforce Q&A
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   └── tests/
└── shared/                   # Shared utilities
    ├── utils/
    ├── data/
    ├── models/
    └── configs/
```

**Deliverable**: Repository structure ready for all capstone projects

---

### Task 2: Shared Configuration Management (20 min)

Create a configuration system that will be used across all projects.

Create `capstone-projects/shared/configs/base_config.py`:

```python
"""
Base configuration for all capstone projects.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BaseConfig:
    """Base configuration class."""
    
    # Project paths
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    DATA_DIR = PROJECT_ROOT / "shared" / "data"
    MODELS_DIR = PROJECT_ROOT / "shared" / "models"
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    
    # Model defaults
    DEFAULT_LLM_MODEL = "gpt-3.5-turbo"
    DEFAULT_TEMPERATURE = 0.7
    DEFAULT_MAX_TOKENS = 500
    
    # Database (to be configured in later weeks)
    DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING", "")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = PROJECT_ROOT / "logs" / "capstone.log"
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        required = ["OPENAI_API_KEY"]
        missing = [key for key in required if not getattr(cls, key)]
        
        if missing:
            raise ValueError(f"Missing required config: {', '.join(missing)}")
        
        return True
```

**Deliverable**: Reusable configuration system for all projects

---

### Task 3: Shared Utility Functions (25 min)

Create common utility functions that will be reused across projects.

Create `capstone-projects/shared/utils/llm_utils.py`:

```python
"""
Shared LLM utility functions for all capstone projects.
"""
import os
from typing import Dict, List, Optional
from openai import OpenAI
import anthropic

class LLMClient:
    """Wrapper for multiple LLM providers."""
    
    def __init__(self, provider: str = "openai", model: Optional[str] = None):
        """
        Initialize LLM client.
        
        Args:
            provider: "openai" or "anthropic"
            model: Model name (uses defaults if not provided)
        """
        self.provider = provider
        
        if provider == "openai":
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = model or "gpt-3.5-turbo"
        elif provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            self.model = model or "claude-3-haiku-20240307"
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def complete(
        self,
        prompt: str,
        system_message: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> Dict:
        """
        Generate completion from prompt.
        
        Args:
            prompt: User prompt
            system_message: Optional system message
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Dict with response, tokens, and metadata
        """
        if self.provider == "openai":
            return self._complete_openai(prompt, system_message, temperature, max_tokens)
        elif self.provider == "anthropic":
            return self._complete_anthropic(prompt, system_message, temperature, max_tokens)
    
    def _complete_openai(self, prompt, system_message, temperature, max_tokens):
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return {
            "response": response.choices[0].message.content,
            "tokens": response.usage.total_tokens,
            "model": self.model,
            "provider": "openai"
        }
    
    def _complete_anthropic(self, prompt, system_message, temperature, max_tokens):
        kwargs = {"max_tokens": max_tokens}
        if system_message:
            kwargs["system"] = system_message
        
        message = self.client.messages.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            **kwargs
        )
        
        return {
            "response": message.content[0].text,
            "tokens": message.usage.input_tokens + message.usage.output_tokens,
            "model": self.model,
            "provider": "anthropic"
        }
```

Create `capstone-projects/shared/utils/data_utils.py`:

```python
"""
Shared data utility functions.
"""
import pandas as pd
from pathlib import Path
from typing import Optional

def load_csv(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Load CSV file with error handling.
    
    Args:
        filepath: Path to CSV file
        **kwargs: Additional arguments for pd.read_csv
        
    Returns:
        DataFrame
    """
    try:
        df = pd.read_csv(filepath, **kwargs)
        print(f"✅ Loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"❌ Error loading {filepath}: {e}")
        raise

def save_csv(df: pd.DataFrame, filepath: str, **kwargs):
    """Save DataFrame to CSV with directory creation."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, **kwargs)
    print(f"✅ Saved {len(df)} rows to {filepath}")
```

**Deliverable**: Reusable utility modules for LLM and data operations

---

### Task 4: Logging Infrastructure (15 min)

Set up logging that will be used for debugging and monitoring.

Create `capstone-projects/shared/utils/logging_utils.py`:

```python
"""
Shared logging configuration.
"""
import logging
import sys
from pathlib import Path
from typing import Optional

def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    level: str = "INFO"
) -> logging.Logger:
    """
    Set up logger with file and console handlers.
    
    Args:
        name: Logger name
        log_file: Optional log file path
        level: Logging level
        
    Returns:
        Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    
    return logger
```

**Deliverable**: Centralized logging system

---

### Task 5: Testing Infrastructure (20 min)

Create testing framework that will be used throughout the course.

Create `capstone-projects/shared/tests/test_llm_utils.py`:

```python
"""
Tests for shared LLM utilities.
"""
import pytest
import os
from dotenv import load_dotenv
from shared.utils.llm_utils import LLMClient

load_dotenv()

@pytest.fixture
def openai_client():
    """Create OpenAI client for testing."""
    return LLMClient(provider="openai")

@pytest.fixture
def anthropic_client():
    """Create Anthropic client for testing."""
    return LLMClient(provider="anthropic")

def test_openai_completion(openai_client):
    """Test OpenAI completion."""
    result = openai_client.complete(
        prompt="Say 'test successful'",
        max_tokens=10
    )
    
    assert "response" in result
    assert "tokens" in result
    assert result["provider"] == "openai"
    assert isinstance(result["response"], str)

def test_anthropic_completion(anthropic_client):
    """Test Anthropic completion."""
    result = anthropic_client.complete(
        prompt="Say 'test successful'",
        max_tokens=10
    )
    
    assert "response" in result
    assert "tokens" in result
    assert result["provider"] == "anthropic"
    assert isinstance(result["response"], str)

def test_system_message(openai_client):
    """Test system message integration."""
    result = openai_client.complete(
        prompt="What's your role?",
        system_message="You are a helpful assistant.",
        max_tokens=20
    )
    
    assert len(result["response"]) > 0
```

Create `capstone-projects/pytest.ini`:

```ini
[pytest]
testpaths = shared/tests finance/tests sports/tests ecommerce/tests enterprise/tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

**Deliverable**: Testing framework with example tests

---

### Task 6: CI/CD Pipeline Setup (25 min)

Create GitHub Actions workflow for continuous integration.

Create `.github/workflows/capstone-ci.yml`:

```yaml
name: Capstone Projects CI

on:
  push:
    branches: [ main, develop ]
    paths:
      - 'Data-AI-Course/capstone-projects/**'
  pull_request:
    branches: [ main ]
    paths:
      - 'Data-AI-Course/capstone-projects/**'

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Cache pip packages
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 capstone-projects/ --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 capstone-projects/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Format check with black
      run: |
        pip install black
        black --check capstone-projects/
    
    - name: Run tests
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      run: |
        cd capstone-projects
        pytest --cov=shared --cov-report=term-missing
```

**Deliverable**: Automated CI pipeline for testing and validation

---

### Task 7: Documentation Template (15 min)

Create documentation template for capstone projects.

Create `capstone-projects/TEMPLATE.md`:

```markdown
# [Project Name] - Capstone Project

## 📋 Project Overview

**Domain**: [Finance/Sports/E-commerce/Enterprise]  
**Objective**: [Brief description]  
**Timeline**: Week [X] - Week [Y]

## 🎯 Learning Objectives

1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## 📊 Dataset

**Source**: [Dataset URL or description]  
**Size**: [Number of records]  
**Features**: [Key features]

## 🏗️ Architecture

[High-level architecture diagram or description]

## 🛠️ Tech Stack

- **LLM**: [Model used]
- **Framework**: [LangChain/LlamaIndex]
- **Database**: [Vector DB/SQL]
- **Deployment**: [Platform]

## 📝 Implementation Steps

### Phase 1: Data Preparation
- [ ] Task 1
- [ ] Task 2

### Phase 2: Model Development
- [ ] Task 1
- [ ] Task 2

### Phase 3: Evaluation
- [ ] Task 1
- [ ] Task 2

### Phase 4: Deployment
- [ ] Task 1
- [ ] Task 2

## 🧪 Testing Strategy

[Description of testing approach]

## 🔒 Security Considerations

[Security measures and considerations]

## ✅ Success Criteria

1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

## 📚 Resources

- [Resource 1]
- [Resource 2]
```

**Deliverable**: Standardized documentation template

---

## ✅ Week 00 Checklist for Capstone

- [ ] Capstone project directory structure created
- [ ] Shared configuration system in place
- [ ] Utility functions for LLM operations created
- [ ] Utility functions for data operations created
- [ ] Logging infrastructure set up
- [ ] Testing framework configured
- [ ] CI/CD pipeline created
- [ ] Documentation template ready

## 🎯 Success Metrics

By the end of Week 00, you should have:
- ✅ Organized repository structure for all 4 capstone projects
- ✅ Reusable code modules that will save time in later weeks
- ✅ Testing and CI/CD infrastructure
- ✅ Documentation standards established

## 🚀 Next Week Preview

In Week 01, you'll start building on this foundation:
- Use LLMClient for prompt engineering experiments
- Leverage logging for debugging prompt strategies
- Apply testing to validate prompt templates
- Begin collecting data for capstone projects

---

**Remember**: Good project structure at the beginning saves hours of refactoring later! 🎯
