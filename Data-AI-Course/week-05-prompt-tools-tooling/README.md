# Week 05: Prompt Tools & Tooling - LangChain Agents & Tool Design

## 👤 Persona
**You are a creative machine learning engineer who loves building intelligent agents and finding hidden patterns in tool interactions. You excel at teaching complex frameworks like LangChain in bite-sized, practical chunks. Your approach emphasizes rapid prototyping and iterative refinement, helping learners build working agents fast.**

## 🧠 Chain of Thought Approach
Let's build intelligent AI agents step-by-step:
1. Understand **why agents** are the next evolution beyond simple LLM calls
2. Learn **LangChain fundamentals** — just the 20% you actually need
3. Master **tool design** — how to give AI superpowers
4. Build **safe, production-ready agents** with proper guardrails
5. Create **composable toolkits** that scale across projects

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Understand agent architectures and when to use them
2. Build LangChain agents with custom tools
3. Design safe, effective tool interfaces
4. Implement ReAct (Reasoning + Acting) pattern
5. Create reusable tool libraries
6. Apply security best practices for agent systems
7. Focus on the Pareto 80/20 — essential tools that solve 80% of problems

**Estimated Duration**: 4-5 hours

## 🚀 Why Agents & Tools Matter (Pareto Context)

**Agents = LLMs + Actions**

Agents are critical because:
- ✅ **Break through knowledge cutoffs**: Search the web, query databases
- ✅ **Automate complex workflows**: Multi-step tasks with decision-making
- ✅ **Integrate external systems**: APIs, tools, services
- ✅ **Deliver real business value**: Beyond text generation

**80% of enterprise AI value** comes from agents that can *act*, not just *respond*.

## 📋 Prerequisites

- Completed Weeks 01-04
- Understanding of prompt engineering and async Python
- Working OpenAI API access
- Python 3.9+
- Basic understanding of APIs and JSON

## 🎓 Key Concepts

### 1. What is an Agent?

**Agent = LLM + Tools + Decision Loop**

```
User Query → [Agent Reasoning] → [Choose Tool] → [Execute Tool] 
          ↑                                           ↓
          └─────────────[Process Result]←────────────┘
```

**Three Types of Agents (Focus on These):**

1. **ReAct Agent**: Reasoning + Acting (most popular)
2. **Function Calling Agent**: Direct function invocation
3. **Conversational Agent**: Maintains conversation history

### 2. The ReAct Pattern (80% of Agents Use This)

**ReAct = Thought → Action → Observation → Repeat**

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub

# Define a simple tool
def calculate_length(text: str) -> int:
    """Calculate the length of text."""
    return len(text)

# Create tool
length_tool = Tool(
    name="TextLength",
    func=calculate_length,
    description="Useful for finding the length of text. Input should be a string."
)

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Get ReAct prompt template
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(
    llm=llm,
    tools=[length_tool],
    prompt=prompt
)

# Create executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[length_tool],
    verbose=True,  # See reasoning process
    max_iterations=5
)

# Run agent
response = agent_executor.invoke({
    "input": "What is the length of the word 'artificial intelligence'?"
})

print(response["output"])

# Agent thinks through:
# Thought: I need to find the length of "artificial intelligence"
# Action: TextLength
# Action Input: "artificial intelligence"
# Observation: 24
# Thought: I now know the final answer
# Final Answer: The length is 24 characters.
```

### 3. Building Custom Tools (The Essential Skill)

**Tool Design Pattern:**

```python
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

# Define tool input schema
class SearchInput(BaseModel):
    """Input for search tool."""
    query: str = Field(description="Search query string")
    max_results: int = Field(default=5, description="Maximum number of results")

class SearchTool(BaseTool):
    """Custom search tool."""
    
    name: str = "web_search"
    description: str = """Useful for finding current information on the internet.
    Input should be a search query string.
    Returns: List of relevant search results."""
    args_schema: Type[BaseModel] = SearchInput
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """Execute the search."""
        # Simplified example - integrate actual search API
        results = self._search_api(query, max_results)
        
        formatted = "\n\n".join([
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['snippet']}"
            for r in results
        ])
        
        return formatted
    
    async def _arun(self, query: str, max_results: int = 5) -> str:
        """Async version."""
        # Implement async search
        return self._run(query, max_results)
    
    def _search_api(self, query: str, max_results: int) -> list:
        """Mock search API call."""
        return [
            {
                "title": f"Result {i}",
                "url": f"https://example.com/{i}",
                "snippet": f"Relevant content for {query}"
            }
            for i in range(max_results)
        ]

# Usage
search_tool = SearchTool()
result = search_tool.run("latest AI developments")
```

## 🎯 Pareto Principle (80/20 for Agents)

### 20% of Tools That Deliver 80% of Value

#### 1. **Search Tool** (Most Requested)
```python
from langchain_community.tools import DuckDuckGoSearchRun

def create_search_tool():
    """Create web search tool."""
    search = DuckDuckGoSearchRun()
    
    return Tool(
        name="WebSearch",
        func=search.run,
        description="""Search the internet for current information.
        Use this when you need up-to-date facts, news, or information
        not in your training data. Input should be a search query."""
    )

# Usage in agent
search_tool = create_search_tool()
# Add to agent's toolkit
```

#### 2. **Calculator Tool**
```python
from langchain.tools import Tool
import math
import re

def safe_calculate(expression: str) -> str:
    """Safely evaluate mathematical expressions."""
    # Whitelist allowed operations
    allowed = set("0123456789+-*/()%. ")
    
    if not all(c in allowed for c in expression):
        return "Error: Invalid characters in expression"
    
    try:
        # Safe eval with limited scope
        result = eval(expression, {"__builtins__": {}}, {
            "sqrt": math.sqrt,
            "pow": math.pow,
            "abs": abs
        })
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

calculator_tool = Tool(
    name="Calculator",
    func=safe_calculate,
    description="""Perform mathematical calculations.
    Input should be a valid mathematical expression like '25 * 4' or 'sqrt(16)'.
    Supports: +, -, *, /, sqrt, pow, abs"""
)
```

#### 3. **Database Query Tool**
```python
import sqlite3
from typing import Dict, Any

class DatabaseTool(BaseTool):
    """Safe database query tool."""
    
    name: str = "database_query"
    description: str = """Query the database for information.
    Input should be a natural language question about the data.
    This tool will convert it to SQL and return results."""
    
    def __init__(self, db_path: str):
        super().__init__()
        self.db_path = db_path
        self.llm = ChatOpenAI(temperature=0)
    
    def _run(self, question: str) -> str:
        """Convert question to SQL and execute."""
        # Generate SQL from natural language
        sql = self._generate_sql(question)
        
        # Execute with safety checks
        if not self._is_safe_query(sql):
            return "Error: Query is not safe (must be SELECT only)"
        
        results = self._execute_query(sql)
        return self._format_results(results)
    
    def _generate_sql(self, question: str) -> str:
        """Use LLM to generate SQL."""
        prompt = f"""Convert this question to SQL:
        Question: {question}
        
        Database schema:
        - users (id, name, email, created_at)
        - orders (id, user_id, amount, status, created_at)
        
        Return only the SQL query, no explanation."""
        
        response = self.llm.invoke(prompt)
        return response.content.strip()
    
    def _is_safe_query(self, sql: str) -> bool:
        """Ensure query is read-only."""
        sql_upper = sql.upper().strip()
        dangerous = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE"]
        return sql_upper.startswith("SELECT") and not any(d in sql_upper for d in dangerous)
    
    def _execute_query(self, sql: str) -> list:
        """Execute SQL query."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        finally:
            conn.close()
    
    def _format_results(self, results: list) -> str:
        """Format query results."""
        if not results:
            return "No results found."
        
        return "\n".join([str(row) for row in results[:10]])  # Limit to 10 rows

# Usage
db_tool = DatabaseTool(db_path="./data.db")
```

#### 4. **API Integration Tool**
```python
import requests
from typing import Optional

class APITool(BaseTool):
    """Generic API integration tool."""
    
    name: str = "api_call"
    description: str = """Make API calls to external services.
    Useful for getting data from web services."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        super().__init__()
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    
    def _run(self, endpoint: str, params: Optional[Dict] = None) -> str:
        """Make GET request to API."""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return str(data)
        
        except requests.exceptions.RequestException as e:
            return f"API Error: {str(e)}"
    
    async def _arun(self, endpoint: str, params: Optional[Dict] = None) -> str:
        """Async version."""
        import httpx
        
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            return str(response.json())

# Usage for specific API
weather_tool = APITool(
    base_url="https://api.weather.com/v3",
    api_key="YOUR_API_KEY"
)
```

### 4. Building Complete Agent Systems

**Production-Ready Agent Template:**

```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

class ProductionAgent:
    """Production-ready agent with memory and safety."""
    
    def __init__(self, tools: list, model: str = "gpt-3.5-turbo"):
        self.tools = tools
        self.llm = ChatOpenAI(model=model, temperature=0)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create custom prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to tools.
            
            Guidelines:
            - Use tools when needed to get accurate information
            - Always verify information before responding
            - If unsure, say so - don't make up information
            - Keep responses concise and relevant
            - Cite sources when using tool results"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        # Create agent
        agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create executor
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True,
            max_iterations=5,
            max_execution_time=30,  # Safety timeout
            handle_parsing_errors=True
        )
    
    def run(self, query: str) -> str:
        """Execute agent with query."""
        try:
            response = self.agent_executor.invoke({"input": query})
            return response["output"]
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset(self):
        """Clear conversation memory."""
        self.memory.clear()

# Usage
tools = [
    create_search_tool(),
    calculator_tool,
    # Add more tools as needed
]

agent = ProductionAgent(tools=tools)

# Multi-turn conversation
print(agent.run("What's the current population of Tokyo?"))
print(agent.run("Calculate 10% of that number"))
print(agent.run("What's the weather there?"))
```

### 5. Tool Safety & Validation

**Critical: Always validate tool inputs and outputs**

```python
from typing import Any, Callable
import re

class SafeToolWrapper:
    """Wrap tools with safety checks."""
    
    def __init__(self, tool: BaseTool, max_output_length: int = 5000):
        self.tool = tool
        self.max_output_length = max_output_length
    
    def _validate_input(self, input_str: str) -> bool:
        """Validate tool input."""
        # Check for common injection patterns
        dangerous_patterns = [
            r";\s*rm\s+-rf",  # Shell injection
            r"DROP\s+TABLE",   # SQL injection
            r"eval\(",         # Code injection
            r"exec\(",
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, input_str, re.IGNORECASE):
                return False
        
        return True
    
    def _sanitize_output(self, output: str) -> str:
        """Sanitize tool output."""
        # Truncate if too long
        if len(output) > self.max_output_length:
            output = output[:self.max_output_length] + "... (truncated)"
        
        # Remove potential PII patterns (simplified)
        output = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', output)  # SSN
        output = re.sub(r'\b\d{16}\b', '[CARD]', output)  # Credit card
        
        return output
    
    def run(self, input_str: str) -> str:
        """Run tool with safety checks."""
        if not self._validate_input(input_str):
            return "Error: Input validation failed"
        
        try:
            output = self.tool.run(input_str)
            return self._sanitize_output(output)
        except Exception as e:
            return f"Tool execution error: {str(e)}"

# Usage
safe_search = SafeToolWrapper(search_tool)
result = safe_search.run("malicious; rm -rf /")  # Blocked
```

### 6. Tool Composition & Toolkits

**Build Reusable Tool Libraries:**

```python
from langchain.agents import Tool
from typing import List

class StandardToolkit:
    """Standard set of safe, useful tools."""
    
    @staticmethod
    def get_basic_tools() -> List[Tool]:
        """Get basic tool set for most agents."""
        return [
            create_search_tool(),
            calculator_tool,
            Tool(
                name="StringOperations",
                func=lambda x: x.upper(),
                description="Convert text to uppercase"
            ),
        ]
    
    @staticmethod
    def get_data_tools(db_path: str) -> List[Tool]:
        """Get data analysis tools."""
        return [
            DatabaseTool(db_path=db_path),
            calculator_tool,
        ]
    
    @staticmethod
    def get_web_tools(api_key: str) -> List[Tool]:
        """Get web interaction tools."""
        return [
            create_search_tool(),
            APITool(base_url="https://api.example.com", api_key=api_key),
        ]

# Usage: Compose toolkits for different scenarios
basic_agent = ProductionAgent(tools=StandardToolkit.get_basic_tools())
data_agent = ProductionAgent(tools=StandardToolkit.get_data_tools("./data.db"))
```

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Tool Description Too Vague
❌ **Bad**: "Useful tool for doing things"
✅ **Good**: "Calculate mathematical expressions. Input: '25 * 4'. Returns: numeric result"

### Pitfall 2: No Input Validation
❌ **Problem**: Agent can execute arbitrary code
✅ **Solution**: Whitelist allowed operations, validate all inputs

### Pitfall 3: Infinite Loops
❌ **Problem**: Agent keeps calling same tool repeatedly
✅ **Solution**: Set `max_iterations=5` in AgentExecutor

### Pitfall 4: Exposing Sensitive Data
❌ **Problem**: Tool returns PII, credentials, etc.
✅ **Solution**: Sanitize outputs, redact sensitive patterns

## 🎯 Week 05 Project Component

Build a **Multi-Tool AI Assistant**:

**Requirements**:
1. ReAct agent with 4+ custom tools
2. Web search capability
3. Database query tool (safe, read-only)
4. Calculator/math tool
5. At least one API integration
6. Conversation memory
7. Input/output validation
8. Error handling and timeouts
9. Comprehensive logging

See `project-steps.md` for detailed implementation guide.

## 📚 Further Reading (Vital Resources Only)

### Must-Read
- [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

### Nice-to-Have
- [LangChain Tools](https://python.langchain.com/docs/integrations/tools/)
- [Building Safe Agents](https://www.anthropic.com/index/building-effective-agents)

## ✅ Success Criteria

By the end of Week 05, you should be able to:
- [x] Explain the ReAct pattern and when to use it
- [x] Build LangChain agents with custom tools
- [x] Design safe, effective tool interfaces
- [x] Implement tool input/output validation
- [x] Create multi-tool agents with memory
- [x] Handle errors and timeouts gracefully
- [x] Build reusable tool libraries
- [x] Apply security best practices

## 🏁 Quick Start Checklist

Before starting exercises:
- [ ] Install: `pip install langchain langchain-openai langchain-community duckduckgo-search`
- [ ] Review ReAct pattern
- [ ] Test simple tool creation
- [ ] Understand agent safety considerations

---

**Next Steps**:
1. Complete hands-on exercises in `actividad-interactiva.md`
2. Build your Multi-Tool AI Assistant in `project-steps.md`
3. Focus on **search, calculator, and database tools** — the **20% that solve 80%** of use cases!

🚀 **Remember**: Tools are superpowers for LLMs. Design them clearly, validate rigorously, and always prioritize safety!
