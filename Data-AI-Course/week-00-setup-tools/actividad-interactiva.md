# Actividades Interactivas - Week 00: Setup & Tools

## 🎯 Objective

Complete the development environment setup and validate functionality through hands-on exercises that prepare you for AI workflow development.

---

## Exercise 1: Environment Setup & Verification (30 min)

### Objective
Install and configure Python environment with all necessary tools.

### Steps

1. **Verify Python Installation**
   ```bash
   python3 --version
   ```
   ✅ Expected output: Python 3.9.x or higher
   
   Your version: _______________________________

2. **Create Project Directory**
   ```bash
   mkdir ai-workflows-bootcamp
   cd ai-workflows-bootcamp
   ```
   ✅ Directory created successfully

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   ✅ Check: `ls venv/` should show bin/, lib/, etc.

4. **Activate Virtual Environment**
   ```bash
   # macOS/Linux
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```
   ✅ Prompt should show `(venv)` prefix
   
   Your prompt after activation: _______________________________

5. **Upgrade pip**
   ```bash
   pip install --upgrade pip
   pip --version
   ```
   Your pip version: _______________________________

### Verification
```bash
# Verify virtual environment is active
which python
```

Expected: Path should include `venv`  
Your output: _______________________________

**Checklist:**
- [ ] Python 3.9+ installed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] pip upgraded

**Duration**: 30 minutes

---

## Exercise 2: Install Dependencies (25 min)

### Objective
Install all required Python packages for AI development.

### Steps

1. **Create requirements.txt**
   
   Create file `requirements.txt` with content:
   ```text
   openai==1.12.0
   anthropic==0.18.1
   langchain==0.1.9
   langchain-openai==0.0.5
   langchain-community==0.0.20
   llama-index==0.10.11
   transformers==4.38.0
   python-dotenv==1.0.1
   requests==2.31.0
   pandas==2.2.0
   numpy==1.26.4
   jupyter==1.0.0
   pytest==8.0.0
   black==24.2.0
   flake8==7.0.0
   faiss-cpu==1.7.4
   ```

2. **Install All Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   ✅ This may take 3-5 minutes
   
   Installation successful? [ ] Yes [ ] No

3. **Verify Installations**
   ```bash
   pip list | grep openai
   pip list | grep langchain
   pip list | grep anthropic
   ```
   
   Number of packages installed: _______________________________

4. **Test Imports**
   ```bash
   python -c "import openai; import langchain; import anthropic; print('✅ All imports successful')"
   ```
   
   Output: _______________________________

### Verification
- [ ] requirements.txt created
- [ ] All packages installed without errors
- [ ] Test imports successful
- [ ] No warning messages about conflicts

**Duration**: 25 minutes

---

## Exercise 3: Configure API Keys (20 min)

### Objective
Set up secure API access to LLM providers.

### Steps

1. **Create .env File**
   ```bash
   touch .env
   ```
   
   Add the following content to `.env`:
   ```bash
   OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
   ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
   HUGGINGFACE_API_KEY=<YOUR_HF_TOKEN>
   ```

2. **Get OpenAI API Key**
   - Visit: https://platform.openai.com/api-keys
   - Create new API key
   - Copy and paste into .env
   
   ✅ OpenAI key obtained? [ ] Yes [ ] No

3. **Get Anthropic API Key**
   - Visit: https://console.anthropic.com/
   - Create API key
   - Copy and paste into .env
   
   ✅ Anthropic key obtained? [ ] Yes [ ] No

4. **Create .env.example (Template)**
   ```bash
   cat > .env.example << 'EOF'
   # Template for environment variables
   OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
   ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>
   HUGGINGFACE_API_KEY=<YOUR_HF_TOKEN>
   EOF
   ```

5. **Create .gitignore**
   ```bash
   cat > .gitignore << 'EOF'
   venv/
   .env
   __pycache__/
   *.pyc
   .ipynb_checkpoints/
   data/*.csv
   *.log
   EOF
   ```

### Verification
```bash
# Test that .env is readable
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✅ .env loaded' if os.getenv('OPENAI_API_KEY') else '❌ Keys not found')"
```

Expected output: _______________________________

**Checklist:**
- [ ] .env file created with keys
- [ ] .env.example template created
- [ ] .gitignore configured
- [ ] Keys verified with test command

**Duration**: 20 minutes

---

## Exercise 4: Test API Connectivity (30 min)

### Objective
Verify that API keys work and you can connect to LLM providers.

### Steps

1. **Create test_setup.py**
   
   Create file `test_setup.py` with the following content:
   ```python
   import os
   from dotenv import load_dotenv
   from openai import OpenAI
   
   load_dotenv()
   
   def test_openai():
       client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
       response = client.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[{"role": "user", "content": "Say 'test successful'"}],
           max_tokens=10
       )
       return response.choices[0].message.content
   
   def test_anthropic():
       import anthropic
       client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
       message = client.messages.create(
           model="claude-3-haiku-20240307",
           max_tokens=10,
           messages=[{"role": "user", "content": "Say 'test successful'"}]
       )
       return message.content[0].text
   
   if __name__ == "__main__":
       print("Testing OpenAI...")
       print(f"OpenAI: {test_openai()}")
       print("\nTesting Anthropic...")
       print(f"Anthropic: {test_anthropic()}")
       print("\n✅ All tests passed!")
   ```

2. **Run Test Script**
   ```bash
   python test_setup.py
   ```
   
   OpenAI response: _______________________________
   
   Anthropic response: _______________________________

3. **Check API Usage**
   - Visit: https://platform.openai.com/usage
   - Verify that test call appears
   
   ✅ Usage recorded? [ ] Yes [ ] No

### Verification
- [ ] test_setup.py created and runs without errors
- [ ] OpenAI API responds correctly
- [ ] Anthropic API responds correctly
- [ ] API usage shows in dashboards

**Duration**: 30 minutes

---

## Exercise 5: Build Your First LLM App (35 min)

### Objective
Create a simple interactive chat application using OpenAI.

### Steps

1. **Create hello_llm.py**
   ```python
   import os
   from dotenv import load_dotenv
   from openai import OpenAI
   
   load_dotenv()
   
   def chat(prompt: str) -> str:
       client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
       response = client.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": prompt}
           ],
           temperature=0.7,
           max_tokens=200
       )
       return response.choices[0].message.content
   
   def main():
       print("Simple LLM Chat - Type 'quit' to exit")
       print("=" * 50)
       
       while True:
           user_input = input("\nYou: ").strip()
           if user_input.lower() in ['quit', 'exit']:
               break
           if user_input:
               response = chat(user_input)
               print(f"\nAssistant: {response}")
   
   if __name__ == "__main__":
       main()
   ```

2. **Run the Chat App**
   ```bash
   python hello_llm.py
   ```

3. **Test with Different Prompts**
   
   Try these prompts and record responses:
   
   **Prompt 1**: "What is prompt engineering?"
   Response: _______________________________
   _______________________________
   
   **Prompt 2**: "Explain machine learning in one sentence"
   Response: _______________________________
   _______________________________
   
   **Prompt 3**: "Generate a Python function to calculate factorial"
   Response: _______________________________
   _______________________________

4. **Experiment with Parameters**
   
   Modify `temperature` to 0.0 and test:
   ```python
   temperature=0.0  # More deterministic
   ```
   
   How did responses change? _______________________________
   
   Modify `temperature` to 1.5:
   ```python
   temperature=1.5  # More creative
   ```
   
   How did responses change? _______________________________

### Verification
- [ ] hello_llm.py created and runs
- [ ] Successfully had conversation with LLM
- [ ] Tested at least 3 different prompts
- [ ] Experimented with temperature parameter

**Duration**: 35 minutes

---

## Exercise 6: LangChain Quick Start (30 min)

### Objective
Use LangChain to build a more structured LLM application.

### Steps

1. **Create langchain_intro.py**
   ```python
   import os
   from dotenv import load_dotenv
   from langchain_openai import ChatOpenAI
   from langchain.prompts import ChatPromptTemplate
   from langchain.schema.output_parser import StrOutputParser
   
   load_dotenv()
   
   # Initialize model
   llm = ChatOpenAI(
       model="gpt-3.5-turbo",
       temperature=0.7,
       api_key=os.getenv("OPENAI_API_KEY")
   )
   
   # Create prompt template
   prompt = ChatPromptTemplate.from_messages([
       ("system", "You are a {role}. Answer concisely."),
       ("user", "{question}")
   ])
   
   # Create chain
   chain = prompt | llm | StrOutputParser()
   
   # Test the chain
   result = chain.invoke({
       "role": "Python expert",
       "question": "What is a decorator?"
   })
   
   print(f"Response: {result}")
   ```

2. **Run LangChain Example**
   ```bash
   python langchain_intro.py
   ```
   
   Response received: _______________________________
   _______________________________

3. **Modify for Different Roles**
   
   Test with different roles:
   
   **Role**: "Data scientist"
   **Question**: "What is overfitting?"
   Response: _______________________________
   
   **Role**: "DevOps engineer"
   **Question**: "What is CI/CD?"
   Response: _______________________________

4. **Add Output Formatting**
   
   Modify the system prompt to include formatting:
   ```python
   ("system", "You are a {role}. Answer in bullet points with exactly 3 points."),
   ```
   
   Did the output format change? _______________________________

### Verification
- [ ] LangChain application runs successfully
- [ ] Tested with at least 3 different roles
- [ ] Experimented with prompt templates
- [ ] Output formatting works as expected

**Duration**: 30 minutes

---

## Exercise 7: Docker Containerization (Optional, 40 min)

### Objective
Create a containerized version of your development environment.

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   RUN apt-get update && apt-get install -y git && \
       rm -rf /var/lib/apt/lists/*
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   CMD ["python", "test_setup.py"]
   ```

2. **Create docker-compose.yml**
   ```yaml
   version: '3.8'
   
   services:
     ai-app:
       build: .
       volumes:
         - .:/app
       env_file:
         - .env
       stdin_open: true
       tty: true
   ```

3. **Build Docker Image**
   ```bash
   docker-compose build
   ```
   
   Build successful? [ ] Yes [ ] No
   Build time: _______________________________

4. **Run Tests in Container**
   ```bash
   docker-compose run --rm ai-app python test_setup.py
   ```
   
   Tests passed in container? [ ] Yes [ ] No

5. **Run Interactive Chat in Container**
   ```bash
   docker-compose run --rm ai-app python hello_llm.py
   ```
   
   Chat works in container? [ ] Yes [ ] No

### Verification
- [ ] Dockerfile created
- [ ] docker-compose.yml created
- [ ] Image builds successfully
- [ ] All tests pass in container
- [ ] Applications run in container

**Duration**: 40 minutes

---

## Exercise 8: Project Structure & Git Setup (25 min)

### Objective
Organize your project and initialize version control.

### Steps

1. **Create Project Structure**
   ```bash
   mkdir -p examples/week-00
   mkdir -p data
   mkdir -p notebooks
   mkdir -p tests
   mkdir -p docs
   ```

2. **Move Files to Appropriate Locations**
   ```bash
   mv hello_llm.py examples/week-00/
   mv langchain_intro.py examples/week-00/
   mv test_setup.py tests/
   ```

3. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git status
   ```
   
   Number of files to be committed: _______________________________

4. **Verify .gitignore is Working**
   ```bash
   git status | grep .env
   ```
   
   .env should NOT appear in git status
   ✅ Verified? [ ] Yes [ ] No

5. **Create First Commit**
   ```bash
   git commit -m "Initial setup: Week 00 complete with working LLM apps"
   ```
   
   Commit hash: _______________________________

6. **Create README.md**
   ```bash
   cat > README.md << 'EOF'
   # AI Workflows Bootcamp
   
   16-week course on AI-powered workflows and automation.
   
   ## Setup
   1. Create virtual environment: `python3 -m venv venv`
   2. Activate: `source venv/bin/activate`
   3. Install: `pip install -r requirements.txt`
   4. Configure: Copy `.env.example` to `.env` and add keys
   5. Test: `python tests/test_setup.py`
   
   ## Structure
   - `examples/` - Code examples by week
   - `data/` - Datasets (gitignored)
   - `notebooks/` - Jupyter notebooks
   - `tests/` - Test files
   EOF
   ```

### Verification
- [ ] Project structure created
- [ ] Files organized properly
- [ ] Git repository initialized
- [ ] .gitignore working correctly
- [ ] First commit created
- [ ] README.md created

**Duration**: 25 minutes

---

## 🏆 Bonus Challenge: Multi-Provider Chat (45 min)

### Objective
Build an application that can switch between OpenAI and Anthropic.

### Task
Create `multi_provider_chat.py` that:
- Allows user to choose provider (OpenAI or Anthropic)
- Uses the same prompt with different providers
- Compares response quality and speed
- Tracks token usage

### Starter Code
```python
import os
import time
from dotenv import load_dotenv
from openai import OpenAI
import anthropic

load_dotenv()

def chat_openai(prompt: str) -> dict:
    start = time.time()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    elapsed = time.time() - start
    
    return {
        "provider": "OpenAI",
        "response": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
        "time": elapsed
    }

def chat_anthropic(prompt: str) -> dict:
    start = time.time()
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )
    
    elapsed = time.time() - start
    
    return {
        "provider": "Anthropic",
        "response": message.content[0].text,
        "tokens": message.usage.input_tokens + message.usage.output_tokens,
        "time": elapsed
    }

def main():
    prompt = input("Enter your prompt: ")
    
    print("\n" + "=" * 60)
    print("Testing with both providers...")
    print("=" * 60)
    
    # Test OpenAI
    openai_result = chat_openai(prompt)
    print(f"\n{openai_result['provider']}:")
    print(f"Response: {openai_result['response']}")
    print(f"Tokens: {openai_result['tokens']}")
    print(f"Time: {openai_result['time']:.2f}s")
    
    # Test Anthropic
    anthropic_result = chat_anthropic(prompt)
    print(f"\n{anthropic_result['provider']}:")
    print(f"Response: {anthropic_result['response']}")
    print(f"Tokens: {anthropic_result['tokens']}")
    print(f"Time: {anthropic_result['time']:.2f}s")

if __name__ == "__main__":
    main()
```

### Test Cases
Test with these prompts and record results:

**Prompt 1**: "Explain quantum computing in simple terms"
- OpenAI time: _____ Tokens: _____ Quality (1-5): _____
- Anthropic time: _____ Tokens: _____ Quality (1-5): _____

**Prompt 2**: "Write a Python function to reverse a string"
- OpenAI time: _____ Tokens: _____ Quality (1-5): _____
- Anthropic time: _____ Tokens: _____ Quality (1-5): _____

### Verification
- [ ] Application compares both providers
- [ ] Tracks token usage
- [ ] Measures response time
- [ ] Tested with multiple prompts
- [ ] Documented differences

---

## 📋 Final Checklist

Before moving to Week 01, confirm:

### Environment Setup
- [ ] Python 3.9+ installed and verified
- [ ] Virtual environment created and activated
- [ ] All dependencies installed from requirements.txt
- [ ] No import errors

### API Configuration
- [ ] OpenAI API key configured
- [ ] Anthropic API key configured
- [ ] .env file created and working
- [ ] .gitignore configured correctly
- [ ] API connectivity tested successfully

### Applications Built
- [ ] hello_llm.py working
- [ ] test_setup.py passing all tests
- [ ] LangChain example running
- [ ] At least one bonus challenge attempted

### Project Organization
- [ ] Project structure created
- [ ] Git repository initialized
- [ ] Files properly organized
- [ ] README.md created
- [ ] First commit made

### Docker (Optional)
- [ ] Dockerfile created
- [ ] Docker image builds successfully
- [ ] Applications run in container

---

## 💡 Troubleshooting Tips

**Issue**: Virtual environment not activating
**Fix**: Check Python installation, try `python -m venv venv` instead

**Issue**: API key errors
**Fix**: Ensure no quotes around keys in .env, verify keys are valid

**Issue**: Import errors after installing packages
**Fix**: Deactivate and reactivate venv, or reinstall with `pip install --force-reinstall`

**Issue**: Docker build fails
**Fix**: Ensure Docker is running: `docker info`

---

## 🎯 Expected Outcomes

After completing these exercises, you should have:

1. ✅ Fully functional Python development environment
2. ✅ Working API connections to OpenAI and Anthropic
3. ✅ 2-3 working LLM applications
4. ✅ Understanding of environment management
5. ✅ Git repository with clean commit history
6. ✅ Optional: Containerized development environment

**Total Time**: 3-4 hours (without Docker), 4-5 hours (with Docker)

---

## 🚀 Next Steps

Proceed to **Week 01: Prompt Engineering Fundamentals** where you'll learn:
- Advanced prompting techniques
- Prompt templates and patterns
- Few-shot learning
- Chain-of-thought prompting
- Prompt debugging strategies

**Remember**: A solid foundation makes everything else easier! 🎯
