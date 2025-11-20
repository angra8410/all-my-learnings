# Week 06: Agentic AI Development - Memory, Planning & Deployment

## 👤 Persona
**You are an ML operations veteran and agentic AI architect who demystifies advanced agent patterns and explains deployment in approachable, practical terms. You focus on patterns that work in production, not academic papers. Your goal is to help learners build agents that can remember context, plan multi-step actions, and deploy reliably.**

## 🧠 Chain of Thought Approach
Let's build production-grade agentic AI systems step-by-step:
1. Understand **agent patterns** beyond simple ReAct — when and why to use each
2. Implement **memory systems** that let agents learn and adapt
3. Master **planning patterns** (Tree of Thought, multi-step reasoning)
4. Build **stateful agents** that maintain context across interactions
5. Deploy agents with **minimal infrastructure** that "just works"

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Understand and implement advanced agent patterns (ReAct, Tree of Thought, Plan-and-Execute)
2. Build memory systems for context retention
3. Create agents that can plan multi-step workflows
4. Implement stateful conversational agents
5. Deploy agents with minimal infrastructure (Flask API, containerization basics)
6. Apply the Pareto 80/20 approach to agent architecture and deployment

**Estimated Duration**: 4-5 hours

## 🚀 Why Advanced Agents Matter (Pareto Context)

**Simple agents respond. Advanced agents think, remember, and improve.**

Advanced agent capabilities are critical because:
- ✅ **Memory**: Agents remember past interactions (80% of enterprise use cases need this)
- ✅ **Planning**: Break complex tasks into achievable steps
- ✅ **Deployment**: Get agents into users' hands quickly
- ✅ **State Management**: Handle multi-turn conversations gracefully

**90% of production agent value** comes from memory + planning + reliable deployment.

## 📋 Prerequisites

- Completed Weeks 01-05 (especially Week 05 on agents)
- Understanding of LangChain agents and tools
- Python 3.9+
- Basic Docker knowledge (helpful but not required)
- Flask or FastAPI familiarity (helpful but not required)

## 🎓 Key Concepts

### 1. Agent Patterns (The Essential Three)

#### Pattern 1: ReAct Agent (Review + Extension)
**Use Case**: 80% of agent scenarios

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain import hub

# Create tools
def search_docs(query: str) -> str:
    """Search documentation."""
    return f"Found docs about: {query}"

tools = [
    Tool(name="DocSearch", func=search_docs, 
         description="Search internal documentation")
]

# Agent with memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=5
)

# Multi-turn conversation
response1 = executor.invoke({"input": "Search for authentication docs"})
response2 = executor.invoke({"input": "What did I just ask about?"})
# Agent remembers: "You asked about authentication docs"
```

#### Pattern 2: Plan-and-Execute Agent
**Use Case**: Complex multi-step tasks

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from typing import List, Dict

class PlanAndExecuteAgent:
    """Agent that plans before acting."""
    
    def __init__(self, tools: List[Tool]):
        self.tools = tools
        self.llm = ChatOpenAI(temperature=0)
        self.tool_map = {tool.name: tool for tool in tools}
    
    def plan(self, objective: str) -> List[Dict]:
        """Create step-by-step plan."""
        plan_prompt = f"""Break this objective into 3-5 concrete steps:
        
        Objective: {objective}
        
        Available tools: {', '.join(self.tool_map.keys())}
        
        Return a JSON list of steps:
        [
            {{"step": 1, "action": "tool_name", "input": "...", "reason": "..."}},
            ...
        ]"""
        
        response = self.llm.invoke(plan_prompt)
        
        # Parse plan (simplified)
        import json
        import re
        json_match = re.search(r'\[.*\]', response.content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return []
    
    def execute_step(self, step: Dict) -> str:
        """Execute a single step."""
        tool_name = step["action"]
        tool_input = step["input"]
        
        if tool_name in self.tool_map:
            tool = self.tool_map[tool_name]
            result = tool.run(tool_input)
            return result
        else:
            return f"Error: Tool {tool_name} not found"
    
    def run(self, objective: str) -> Dict:
        """Plan and execute the objective."""
        # 1. Create plan
        print("Planning...")
        plan = self.plan(objective)
        
        # 2. Execute plan
        print(f"Executing {len(plan)} steps...")
        results = []
        
        for step in plan:
            print(f"\nStep {step['step']}: {step['reason']}")
            result = self.execute_step(step)
            results.append({
                "step": step,
                "result": result
            })
            print(f"Result: {result}")
        
        # 3. Synthesize final answer
        synthesis_prompt = f"""Based on these step results, provide a final answer:
        
        Objective: {objective}
        Results: {results}
        
        Final Answer:"""
        
        final_answer = self.llm.invoke(synthesis_prompt)
        
        return {
            "objective": objective,
            "plan": plan,
            "results": results,
            "answer": final_answer.content
        }

# Usage
tools = [
    Tool(name="Search", func=lambda x: "search results", 
         description="Search the web"),
    Tool(name="Calculate", func=lambda x: str(eval(x)), 
         description="Calculate math")
]

agent = PlanAndExecuteAgent(tools=tools)
response = agent.run("Find the population of Tokyo and calculate 10% of it")
```

#### Pattern 3: Tree of Thought
**Use Case**: Problems requiring exploration of multiple solution paths

```python
from typing import List, Tuple

class TreeOfThoughtAgent:
    """Agent that explores multiple reasoning paths."""
    
    def __init__(self, branching_factor: int = 3):
        self.llm = ChatOpenAI(temperature=0.7)  # Higher temp for diversity
        self.branching_factor = branching_factor
    
    def generate_thoughts(self, prompt: str, n: int = 3) -> List[str]:
        """Generate multiple potential next thoughts."""
        generation_prompt = f"""Given this problem or partial solution:
        
        {prompt}
        
        Generate {n} different next steps or approaches:"""
        
        thoughts = []
        for _ in range(n):
            response = self.llm.invoke(generation_prompt)
            thoughts.append(response.content.strip())
        
        return thoughts
    
    def evaluate_thought(self, thought: str, goal: str) -> float:
        """Evaluate how promising a thought is (0-1 scale)."""
        eval_prompt = f"""Rate how promising this approach is (0.0 to 1.0):
        
        Goal: {goal}
        Approach: {thought}
        
        Return only a number between 0.0 and 1.0:"""
        
        response = self.llm.invoke(eval_prompt)
        
        try:
            score = float(response.content.strip())
            return max(0.0, min(1.0, score))
        except:
            return 0.5
    
    def solve(self, problem: str, max_depth: int = 3) -> Dict:
        """Solve problem using tree of thought."""
        print(f"Problem: {problem}\n")
        
        # Track best path
        best_path = []
        best_score = 0.0
        
        def explore(current_state: str, depth: int, path: List[str]):
            nonlocal best_path, best_score
            
            if depth >= max_depth:
                # Evaluate final state
                score = self.evaluate_thought(current_state, problem)
                if score > best_score:
                    best_score = score
                    best_path = path + [current_state]
                return
            
            # Generate possible next thoughts
            thoughts = self.generate_thoughts(current_state, self.branching_factor)
            
            # Evaluate and explore top thoughts
            scored_thoughts = [
                (t, self.evaluate_thought(t, problem)) 
                for t in thoughts
            ]
            scored_thoughts.sort(key=lambda x: x[1], reverse=True)
            
            # Explore top 2 paths
            for thought, score in scored_thoughts[:2]:
                print(f"{'  ' * depth}Exploring (score={score:.2f}): {thought[:60]}...")
                explore(thought, depth + 1, path + [current_state])
        
        # Start exploration
        explore(problem, 0, [])
        
        # Generate final answer from best path
        final_prompt = f"""Based on this reasoning path, provide the final answer:
        
        Problem: {problem}
        Reasoning Path:
        {chr(10).join(f'{i+1}. {step}' for i, step in enumerate(best_path))}
        
        Final Answer:"""
        
        final_answer = self.llm.invoke(final_prompt)
        
        return {
            "problem": problem,
            "best_path": best_path,
            "best_score": best_score,
            "answer": final_answer.content
        }

# Usage
agent = TreeOfThoughtAgent(branching_factor=3)
result = agent.solve(
    "Design a caching strategy for a high-traffic API",
    max_depth=2
)
print(f"\n\nFinal Answer:\n{result['answer']}")
```

## 🎯 Pareto Principle (80/20 for Advanced Agents)

### 20% of Features That Deliver 80% of Value

#### 1. **Conversation Memory** (Most Critical)

```python
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain_openai import ChatOpenAI

class MemoryStrategies:
    """Different memory strategies for different needs."""
    
    @staticmethod
    def buffer_memory(max_messages: int = 10):
        """Simple buffer - stores last N messages."""
        return ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="output",
            input_key="input",
            max_token_limit=max_messages * 200  # Approximate
        )
    
    @staticmethod
    def summary_memory():
        """Summarizes old conversations - better for long interactions."""
        llm = ChatOpenAI(temperature=0)
        return ConversationSummaryMemory(
            llm=llm,
            memory_key="chat_history",
            return_messages=True
        )
    
    @staticmethod
    def combined_memory():
        """Hybrid: recent buffer + older summaries."""
        from langchain.memory import CombinedMemory
        
        buffer = ConversationBufferMemory(
            memory_key="recent_history",
            return_messages=True,
            input_key="input"
        )
        
        summary = ConversationSummaryMemory(
            llm=ChatOpenAI(temperature=0),
            memory_key="summary",
            input_key="input"
        )
        
        return CombinedMemory(memories=[buffer, summary])

# Usage: Choose based on conversation length
# Short conversations (<10 turns): buffer_memory()
# Long conversations: summary_memory()
# Very long: combined_memory()
```

#### 2. **Persistent State Storage**

```python
import json
from typing import Dict, Any
from datetime import datetime

class AgentStateManager:
    """Manage agent state across sessions."""
    
    def __init__(self, storage_path: str = "./agent_state.json"):
        self.storage_path = storage_path
        self.state = self._load_state()
    
    def _load_state(self) -> Dict[str, Any]:
        """Load state from disk."""
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "conversations": {},
                "preferences": {},
                "metadata": {}
            }
    
    def save_state(self):
        """Persist state to disk."""
        with open(self.storage_path, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def save_conversation(self, user_id: str, messages: List[Dict]):
        """Save conversation for a user."""
        if user_id not in self.state["conversations"]:
            self.state["conversations"][user_id] = []
        
        self.state["conversations"][user_id].append({
            "timestamp": datetime.now().isoformat(),
            "messages": messages
        })
        
        # Keep only last 5 conversations
        self.state["conversations"][user_id] = \
            self.state["conversations"][user_id][-5:]
        
        self.save_state()
    
    def get_user_context(self, user_id: str) -> str:
        """Get relevant context for user."""
        if user_id not in self.state["conversations"]:
            return "No previous context."
        
        recent = self.state["conversations"][user_id][-1]
        summary = f"Last interaction: {recent['timestamp']}\n"
        summary += f"Last message: {recent['messages'][-1]['content'][:100]}"
        
        return summary
    
    def set_preference(self, user_id: str, key: str, value: Any):
        """Store user preference."""
        if user_id not in self.state["preferences"]:
            self.state["preferences"][user_id] = {}
        
        self.state["preferences"][user_id][key] = value
        self.save_state()
    
    def get_preference(self, user_id: str, key: str, default=None):
        """Get user preference."""
        return self.state["preferences"].get(user_id, {}).get(key, default)

# Usage
state_manager = AgentStateManager()

# Save conversation
state_manager.save_conversation("user123", [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"}
])

# Restore context
context = state_manager.get_user_context("user123")
```

#### 3. **Agent Observability**

```python
import logging
from datetime import datetime
from typing import Dict, List

class AgentLogger:
    """Production logging for agents."""
    
    def __init__(self, log_file: str = "agent.log"):
        self.logger = logging.getLogger("AgentLogger")
        self.logger.setLevel(logging.INFO)
        
        # File handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
        self.metrics = []
    
    def log_interaction(self, user_id: str, query: str, response: str, 
                       tools_used: List[str], duration: float):
        """Log agent interaction."""
        self.logger.info(f"""
        User: {user_id}
        Query: {query[:100]}
        Response: {response[:100]}
        Tools: {', '.join(tools_used)}
        Duration: {duration:.2f}s
        """)
        
        self.metrics.append({
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "tools_used": len(tools_used),
            "duration": duration,
            "success": True
        })
    
    def log_error(self, user_id: str, query: str, error: str):
        """Log error."""
        self.logger.error(f"""
        User: {user_id}
        Query: {query[:100]}
        Error: {error}
        """)
        
        self.metrics.append({
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "success": False,
            "error": error
        })
    
    def get_metrics_summary(self) -> Dict:
        """Get summary metrics."""
        if not self.metrics:
            return {}
        
        total = len(self.metrics)
        successful = sum(1 for m in self.metrics if m.get("success", False))
        avg_duration = sum(m.get("duration", 0) for m in self.metrics) / total
        
        return {
            "total_interactions": total,
            "success_rate": successful / total,
            "avg_duration_seconds": avg_duration
        }

# Usage
logger = AgentLogger()
logger.log_interaction("user123", "What's the weather?", "It's sunny", 
                      ["WeatherTool"], 1.23)
print(logger.get_metrics_summary())
```

### 2. Deployment Patterns (Getting Agents Live)

#### Pattern 1: Flask API (Simplest, 80% of Use Cases)

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for web clients

# Initialize agent
agent = ProductionAgent(tools=StandardToolkit.get_basic_tools())
state_manager = AgentStateManager()
logger = AgentLogger()

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint."""
    try:
        data = request.json
        user_id = data.get('user_id', 'anonymous')
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "Message required"}), 400
        
        # Get user context
        context = state_manager.get_user_context(user_id)
        
        # Run agent
        import time
        start = time.time()
        
        response = agent.run(message)
        
        duration = time.time() - start
        
        # Log interaction
        logger.log_interaction(user_id, message, response, 
                             ["agent"], duration)
        
        # Save conversation
        state_manager.save_conversation(user_id, [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ])
        
        return jsonify({
            "response": response,
            "user_id": user_id,
            "duration": duration
        }), 200
    
    except Exception as e:
        logger.log_error(user_id, message, str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    """Reset conversation for user."""
    user_id = request.json.get('user_id', 'anonymous')
    agent.reset()
    return jsonify({"message": "Conversation reset"}), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    """Get agent metrics."""
    return jsonify(logger.get_metrics_summary()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# Deploy: python app.py
# Test: curl -X POST http://localhost:5000/chat \
#   -H "Content-Type: application/json" \
#   -d '{"user_id": "test", "message": "Hello"}'
```

#### Pattern 2: Docker Containerization

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Run
CMD ["python", "app.py"]
```

**requirements.txt:**
```
flask==3.0.0
flask-cors==4.0.0
langchain==0.1.0
langchain-openai==0.0.2
openai==1.10.0
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  agent-api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./agent_state.json:/app/agent_state.json
      - ./agent.log:/app/agent.log
    restart: unless-stopped
```

**Deploy:**
```bash
# Build and run
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop
docker-compose down
```

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Memory Bloat
❌ **Problem**: Storing entire conversation history
✅ **Solution**: Use summary memory or sliding window

### Pitfall 2: No Error Recovery
❌ **Problem**: Agent crashes on tool failure
✅ **Solution**: Wrap tools in try-catch, return error messages

### Pitfall 3: Synchronous Blocking
❌ **Problem**: API waits for slow agent operations
✅ **Solution**: Use async endpoints or task queues (Celery)

### Pitfall 4: No Rate Limiting
❌ **Problem**: Agent overwhelms external APIs
✅ **Solution**: Implement rate limiting at tool level

## 🎯 Week 06 Project Component

Build a **Production-Ready Conversational Agent API**:

**Requirements**:
1. Implement one advanced agent pattern (Plan-and-Execute or Tree of Thought)
2. Add conversation memory (buffer or summary)
3. Implement persistent state storage
4. Build Flask API with /chat, /reset, /metrics endpoints
5. Add comprehensive logging
6. Containerize with Docker
7. Include health checks and error handling
8. Document API with examples

See `project-steps.md` for detailed implementation guide.

## 📚 Further Reading (Vital Resources Only)

### Must-Read
- [LangChain Memory Documentation](https://python.langchain.com/docs/modules/memory/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Tutorial](https://docs.docker.com/get-started/)

### Nice-to-Have
- [Tree of Thoughts Paper](https://arxiv.org/abs/2305.10601)
- [Agent Architectures](https://lilianweng.github.io/posts/2023-06-23-agent/)

## ✅ Success Criteria

By the end of Week 06, you should be able to:
- [x] Implement Plan-and-Execute and Tree of Thought patterns
- [x] Build agents with conversation memory
- [x] Create persistent state management
- [x] Deploy agents as Flask APIs
- [x] Containerize with Docker
- [x] Implement comprehensive logging
- [x] Handle errors gracefully
- [x] Monitor agent performance

## 🏁 Quick Start Checklist

Before starting exercises:
- [ ] Install: `pip install flask flask-cors docker`
- [ ] Review Week 05 agent patterns
- [ ] Test Docker installation: `docker --version`
- [ ] Set up project structure for Flask app

---

**Next Steps**:
1. Complete hands-on exercises in `actividad-interactiva.md`
2. Build your Production Agent API in `project-steps.md`
3. Focus on **memory + Flask deployment** — the **20% that gets 80%** of agents into production!

🚀 **Remember**: Great agents remember context, plan ahead, and deploy reliably. Start simple with Flask, add complexity only as needed!
