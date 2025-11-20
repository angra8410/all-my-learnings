# Week 03: Building Generative AI Workflows

## 👤 Persona
**You are a pragmatic ML engineer who values efficiency and real-world applicability. You excel at breaking down complex AI workflows into manageable, production-ready components. Your teaching style emphasizes hands-on learning with interactive Python code samples that students can immediately apply to their projects.**

## 🧠 Chain of Thought Approach
Let's build generative AI workflows step-by-step:
1. Understand **why chaining** is essential for complex AI tasks
2. Learn the **core patterns** that make up 90% of production workflows
3. Implement **streaming and caching** for optimal performance
4. Master **multimodal inputs** to handle diverse data types
5. Build **composable pipelines** that scale to production

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Chain multiple LLM calls to solve complex tasks
2. Implement streaming for real-time user experiences
3. Use caching to optimize costs and latency
4. Work with multimodal inputs (text, images, audio)
5. Build production-ready, composable AI workflows
6. Apply the Pareto 80/20 approach to workflow design

**Estimated Duration**: 4-5 hours

## 🚀 Why Workflow Chaining Matters (Pareto Context)

**Single LLM calls solve simple problems. Chained workflows solve real business problems.**

Chaining is critical because:
- ✅ **Complex tasks** need decomposition: "Analyze → Summarize → Translate"
- ✅ **Quality improves** when you specialize each step
- ✅ **Costs decrease** by caching intermediate results
- ✅ **Debugging is easier** when you can inspect each step

**80% of production AI systems use workflow chaining.** Master this, master AI engineering.

## 📋 Prerequisites

- Completed Week 01 (prompt engineering) and Week 02 (RAG)
- Working OpenAI or Anthropic API access
- Python 3.9+
- Understanding of async/await (we'll cover basics)
- Familiarity with JSON structures

## 🎓 Key Concepts

### 1. Sequential vs. Parallel Chains

**Sequential Chain**: Output of step N → Input of step N+1
```
Input → [Step 1] → [Step 2] → [Step 3] → Final Output
```

**Parallel Chain**: Multiple independent steps
```
Input → [Step 1A] ↘
     → [Step 1B] → [Combine] → Final Output
     → [Step 1C] ↗
```

### 2. The Four Essential Chain Patterns (Learn These First)

#### Pattern 1: Sequential Processing Chain
**Use Case**: Multi-step transformations

```python
from openai import OpenAI
from typing import Dict, Any

client = OpenAI()

class SequentialChain:
    """Chain LLM calls sequentially."""
    
    def __init__(self):
        self.client = OpenAI()
        self.history = []  # Track all steps
    
    def call_llm(self, prompt: str, system: str = None) -> str:
        """Single LLM call."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    
    def run(self, input_text: str) -> Dict[str, Any]:
        """Execute multi-step workflow."""
        # Step 1: Extract key information
        step1_prompt = f"Extract the main topics from this text:\n\n{input_text}"
        topics = self.call_llm(step1_prompt, "You extract key topics concisely.")
        self.history.append({"step": 1, "output": topics})
        
        # Step 2: Summarize each topic
        step2_prompt = f"Summarize each of these topics in one sentence:\n\n{topics}"
        summaries = self.call_llm(step2_prompt, "You write clear, concise summaries.")
        self.history.append({"step": 2, "output": summaries})
        
        # Step 3: Create action items
        step3_prompt = f"Based on these summaries, create 3 action items:\n\n{summaries}"
        actions = self.call_llm(step3_prompt, "You create practical action items.")
        self.history.append({"step": 3, "output": actions})
        
        return {
            "input": input_text,
            "topics": topics,
            "summaries": summaries,
            "actions": actions,
            "history": self.history
        }

# Usage
chain = SequentialChain()
result = chain.run("Long meeting transcript text here...")
print(result["actions"])
```

#### Pattern 2: Map-Reduce Chain
**Use Case**: Process multiple items, then combine

```python
import asyncio
from typing import List

class MapReduceChain:
    """Process items in parallel, then combine results."""
    
    def __init__(self):
        self.client = OpenAI()
    
    async def map_async(self, items: List[str], prompt_template: str) -> List[str]:
        """Process multiple items in parallel (MAP phase)."""
        async def process_one(item: str) -> str:
            prompt = prompt_template.format(item=item)
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )
            return response.choices[0].message.content
        
        # Process all items concurrently
        results = await asyncio.gather(*[process_one(item) for item in items])
        return results
    
    def reduce(self, results: List[str]) -> str:
        """Combine results (REDUCE phase)."""
        combined = "\n\n".join([f"Section {i+1}:\n{r}" for i, r in enumerate(results)])
        
        reduce_prompt = f"""Synthesize these sections into a cohesive summary:

{combined}

Final Summary:"""
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": reduce_prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    
    async def run(self, items: List[str]) -> str:
        """Execute map-reduce workflow."""
        # Map: Process each item
        map_results = await self.map_async(
            items, 
            prompt_template="Summarize this document in 2-3 sentences:\n\n{item}"
        )
        
        # Reduce: Combine all results
        final_result = self.reduce(map_results)
        return final_result

# Usage
async def main():
    chain = MapReduceChain()
    documents = ["Doc 1 text...", "Doc 2 text...", "Doc 3 text..."]
    summary = await chain.run(documents)
    print(summary)

# Run
# asyncio.run(main())
```

#### Pattern 3: Router Chain
**Use Case**: Route to different handlers based on input

```python
from enum import Enum
from typing import Callable, Dict

class TaskType(Enum):
    SUMMARIZE = "summarize"
    TRANSLATE = "translate"
    ANALYZE = "analyze"
    EXTRACT = "extract"

class RouterChain:
    """Route inputs to appropriate specialized handlers."""
    
    def __init__(self):
        self.client = OpenAI()
        self.handlers: Dict[TaskType, Callable] = {
            TaskType.SUMMARIZE: self._handle_summarize,
            TaskType.TRANSLATE: self._handle_translate,
            TaskType.ANALYZE: self._handle_analyze,
            TaskType.EXTRACT: self._handle_extract,
        }
    
    def classify_intent(self, user_input: str) -> TaskType:
        """Determine what the user wants to do."""
        prompt = f"""Classify this request into ONE category:
- summarize: User wants a summary
- translate: User wants translation
- analyze: User wants analysis
- extract: User wants to extract information

Request: {user_input}

Category (one word):"""
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        
        intent = response.choices[0].message.content.strip().lower()
        return TaskType(intent)
    
    def _handle_summarize(self, text: str) -> str:
        """Specialized summarization handler."""
        # Optimized for summaries
        return self._call_llm(f"Summarize concisely:\n\n{text}", temperature=0.3)
    
    def _handle_translate(self, text: str) -> str:
        """Specialized translation handler."""
        # Extract target language and translate
        return self._call_llm(f"Translate this:\n\n{text}", temperature=0.1)
    
    def _handle_analyze(self, text: str) -> str:
        """Specialized analysis handler."""
        # Deep analysis with reasoning
        return self._call_llm(
            f"Analyze this text step by step:\n\n{text}", 
            temperature=0.5
        )
    
    def _handle_extract(self, text: str) -> str:
        """Specialized extraction handler."""
        return self._call_llm(
            f"Extract key facts as JSON:\n\n{text}", 
            temperature=0.0
        )
    
    def _call_llm(self, prompt: str, temperature: float = 0.7) -> str:
        """Helper method for LLM calls."""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    
    def route(self, user_input: str, content: str) -> Dict[str, Any]:
        """Main routing logic."""
        # 1. Classify intent
        task_type = self.classify_intent(user_input)
        
        # 2. Route to appropriate handler
        handler = self.handlers[task_type]
        result = handler(content)
        
        return {
            "task_type": task_type.value,
            "result": result
        }

# Usage
router = RouterChain()
output = router.route(
    user_input="Can you summarize this for me?",
    content="Long document text..."
)
print(f"Task: {output['task_type']}")
print(f"Result: {output['result']}")
```

#### Pattern 4: Validation Chain
**Use Case**: Generate → Validate → Regenerate loop

```python
class ValidationChain:
    """Generate content, validate it, regenerate if needed."""
    
    def __init__(self, max_attempts: int = 3):
        self.client = OpenAI()
        self.max_attempts = max_attempts
    
    def generate(self, prompt: str) -> str:
        """Generate initial content."""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    
    def validate(self, content: str, criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Validate generated content against criteria."""
        validation_prompt = f"""Check if this content meets these criteria:
Criteria: {criteria}

Content: {content}

Respond in JSON format:
{{
    "valid": true/false,
    "issues": ["issue 1", "issue 2", ...],
    "suggestions": ["suggestion 1", ...]
}}"""
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": validation_prompt}],
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        
        import json
        return json.loads(response.choices[0].message.content)
    
    def run(self, prompt: str, validation_criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Generate with validation loop."""
        for attempt in range(self.max_attempts):
            # Generate
            content = self.generate(prompt)
            
            # Validate
            validation = self.validate(content, validation_criteria)
            
            if validation["valid"]:
                return {
                    "success": True,
                    "content": content,
                    "attempts": attempt + 1
                }
            
            # If not valid and not last attempt, add feedback to prompt
            if attempt < self.max_attempts - 1:
                prompt = f"""{prompt}

Previous attempt had these issues:
{validation['issues']}

Suggestions:
{validation['suggestions']}

Please try again:"""
        
        # Max attempts reached
        return {
            "success": False,
            "content": content,
            "attempts": self.max_attempts,
            "final_issues": validation["issues"]
        }

# Usage
chain = ValidationChain(max_attempts=3)
result = chain.run(
    prompt="Write a product description for wireless headphones",
    validation_criteria={
        "length": "100-150 words",
        "tone": "professional",
        "includes": ["battery life", "sound quality", "comfort"]
    }
)
print(result)
```

## 🎯 Pareto Principle (80/20 for Workflows)

### 20% of Patterns That Deliver 80% of Value

1. **Sequential Chain** (40% of use cases)
   - Document processing pipelines
   - Content transformation workflows
   - Report generation

2. **Map-Reduce** (30% of use cases)
   - Batch processing
   - Multi-document analysis
   - Parallel summarization

3. **Router Chain** (20% of use cases)
   - Chatbots with multiple intents
   - Dynamic task handling
   - User intent classification

4. **Validation Chain** (10% of use cases)
   - Quality-critical outputs
   - Regulated industries
   - Content moderation

### 3. Streaming for Real-Time UX

**Why Stream?** Users expect real-time feedback, not 30-second waits.

```python
from openai import OpenAI

class StreamingWorkflow:
    """Workflow with streaming support."""
    
    def __init__(self):
        self.client = OpenAI()
    
    def stream_response(self, prompt: str):
        """Stream LLM response token by token."""
        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True,  # Enable streaming
            temperature=0.7
        )
        
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                print(token, end="", flush=True)  # Real-time output
        
        return full_response
    
    def multi_step_stream(self, input_text: str):
        """Stream each step of a multi-step workflow."""
        print("Step 1: Extracting topics...")
        topics = self.stream_response(f"Extract main topics:\n\n{input_text}")
        
        print("\n\nStep 2: Creating summary...")
        summary = self.stream_response(f"Summarize:\n\n{topics}")
        
        print("\n\nStep 3: Generating actions...")
        actions = self.stream_response(f"Create action items:\n\n{summary}")
        
        return {
            "topics": topics,
            "summary": summary,
            "actions": actions
        }

# Usage gives users real-time feedback at each step
workflow = StreamingWorkflow()
result = workflow.multi_step_stream("Long document...")
```

**Pareto Insight**: Streaming improves perceived performance by 3-5x even when actual processing time is the same.

### 4. Caching for Cost & Performance

**Critical for Production**: Caching reduces costs by 60-80% for repeated queries.

```python
from functools import lru_cache
import hashlib
import json
from typing import Any, Dict

class CachedWorkflow:
    """Workflow with intelligent caching."""
    
    def __init__(self, cache_size: int = 1000):
        self.client = OpenAI()
        self.cache_size = cache_size
    
    def _hash_prompt(self, prompt: str, params: Dict[str, Any]) -> str:
        """Create hash for caching."""
        cache_key = f"{prompt}_{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(cache_key.encode()).hexdigest()
    
    @lru_cache(maxsize=1000)
    def cached_call(self, prompt: str, temperature: float = 0.7, 
                   model: str = "gpt-3.5-turbo") -> str:
        """LLM call with caching."""
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    
    def run_with_cache(self, input_text: str) -> Dict[str, str]:
        """Multi-step workflow with caching."""
        # Each step is cached independently
        topics = self.cached_call(
            f"Extract topics:\n\n{input_text}",
            temperature=0.3  # Low temp for deterministic caching
        )
        
        summary = self.cached_call(
            f"Summarize:\n\n{topics}",
            temperature=0.3
        )
        
        return {
            "topics": topics,
            "summary": summary
        }

# Usage
workflow = CachedWorkflow()

# First call: Makes API requests
result1 = workflow.run_with_cache("Document 1")

# Second call with same input: Uses cache (instant, $0 cost)
result2 = workflow.run_with_cache("Document 1")
```

**Cache Strategy (Pareto 80/20)**:
- ✅ **DO cache**: Deterministic steps (extraction, classification)
- ✅ **DO cache**: Common queries (FAQs, repeated documents)
- ❌ **DON'T cache**: Creative generation (stories, unique content)
- ❌ **DON'T cache**: User-specific responses

### 5. Multimodal Workflows

**Handle text + images + audio in unified workflows.**

```python
from openai import OpenAI
import base64

class MultimodalWorkflow:
    """Workflow supporting multiple input modalities."""
    
    def __init__(self):
        self.client = OpenAI()
    
    def encode_image(self, image_path: str) -> str:
        """Convert image to base64."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def analyze_image_and_text(self, image_path: str, text_query: str) -> str:
        """Analyze image with text context."""
        base64_image = self.encode_image(image_path)
        
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text_query
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    def document_to_insights(self, image_path: str) -> Dict[str, str]:
        """Multi-step analysis of document image."""
        # Step 1: Extract text
        extracted = self.analyze_image_and_text(
            image_path,
            "Extract all text from this document."
        )
        
        # Step 2: Analyze content
        analysis = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Analyze this text:\n\n{extracted}"}
            ]
        ).choices[0].message.content
        
        return {
            "extracted_text": extracted,
            "analysis": analysis
        }

# Usage
workflow = MultimodalWorkflow()
result = workflow.document_to_insights("invoice.jpg")
```

## 🛠️ Production-Ready Workflow Patterns

### Pattern: Error Recovery Chain

```python
class ResilientWorkflow:
    """Workflow with comprehensive error handling."""
    
    def __init__(self, max_retries: int = 3):
        self.client = OpenAI()
        self.max_retries = max_retries
    
    def call_with_retry(self, prompt: str, step_name: str) -> str:
        """Call LLM with exponential backoff retry."""
        import time
        
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    timeout=30  # 30 second timeout
                )
                return response.choices[0].message.content
            
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise Exception(f"Failed {step_name} after {self.max_retries} attempts: {e}")
                
                # Exponential backoff
                wait_time = 2 ** attempt
                print(f"Retry {step_name} in {wait_time}s...")
                time.sleep(wait_time)
        
        return ""
    
    def run_safe(self, input_text: str) -> Dict[str, Any]:
        """Execute workflow with error recovery."""
        try:
            topics = self.call_with_retry(
                f"Extract topics:\n\n{input_text}",
                "topic_extraction"
            )
            
            summary = self.call_with_retry(
                f"Summarize:\n\n{topics}",
                "summarization"
            )
            
            return {
                "success": True,
                "topics": topics,
                "summary": summary
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "topics": None,
                "summary": None
            }

# Usage
workflow = ResilientWorkflow()
result = workflow.run_safe("Document text...")
```

### Pattern: Workflow Observability

```python
import time
from typing import List, Dict, Any

class ObservableWorkflow:
    """Workflow with logging and metrics."""
    
    def __init__(self):
        self.client = OpenAI()
        self.metrics: List[Dict[str, Any]] = []
    
    def _log_step(self, step_name: str, duration: float, 
                  tokens_used: int, cost: float):
        """Log step metrics."""
        self.metrics.append({
            "step": step_name,
            "duration_seconds": duration,
            "tokens": tokens_used,
            "cost_usd": cost,
            "timestamp": time.time()
        })
    
    def _call_and_measure(self, prompt: str, step_name: str) -> str:
        """Call LLM and measure performance."""
        start = time.time()
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        duration = time.time() - start
        tokens = response.usage.total_tokens
        cost = tokens * 0.000002  # Approximate cost
        
        self._log_step(step_name, duration, tokens, cost)
        
        return response.choices[0].message.content
    
    def run_observed(self, input_text: str) -> Dict[str, Any]:
        """Execute workflow with full observability."""
        topics = self._call_and_measure(
            f"Extract topics:\n\n{input_text}",
            "extract_topics"
        )
        
        summary = self._call_and_measure(
            f"Summarize:\n\n{topics}",
            "summarize"
        )
        
        # Calculate totals
        total_duration = sum(m["duration_seconds"] for m in self.metrics)
        total_tokens = sum(m["tokens"] for m in self.metrics)
        total_cost = sum(m["cost_usd"] for m in self.metrics)
        
        return {
            "results": {
                "topics": topics,
                "summary": summary
            },
            "performance": {
                "total_duration": total_duration,
                "total_tokens": total_tokens,
                "total_cost": total_cost,
                "steps": self.metrics
            }
        }

# Usage
workflow = ObservableWorkflow()
result = workflow.run_observed("Document...")
print(f"Total cost: ${result['performance']['total_cost']:.4f}")
print(f"Total time: {result['performance']['total_duration']:.2f}s")
```

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Over-Chaining
❌ **Problem**: 10-step chains are slow and expensive
✅ **Solution**: Aim for 2-4 steps maximum; combine steps when possible

### Pitfall 2: No Error Handling
❌ **Problem**: One failed step breaks entire workflow
✅ **Solution**: Add try-catch, retries, and fallbacks at each step

### Pitfall 3: Ignoring Latency
❌ **Problem**: Users wait 60+ seconds for results
✅ **Solution**: Use streaming, show progress, parallelize when possible

### Pitfall 4: Cache Everything
❌ **Problem**: Stale or inappropriate cached responses
✅ **Solution**: Cache only deterministic, reusable steps

## 🎯 Week 03 Project Component

Build a **Multi-Step Document Processor** that chains workflows:

**Requirements**:
1. Implement 3+ chain patterns (sequential, map-reduce, router)
2. Add streaming for user feedback
3. Implement caching for common operations
4. Include error handling and retries
5. Log performance metrics
6. Handle at least one multimodal input type

See `project-steps.md` for detailed implementation guide.

## 📚 Further Reading (Vital Resources Only)

### Must-Read
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/)
- [OpenAI Streaming Guide](https://platform.openai.com/docs/api-reference/streaming)
- [Async Python Tutorial](https://realpython.com/async-io-python/)

### Nice-to-Have
- [Building Production LLM Apps](https://www.anthropic.com/index/building-effective-agents)

## ✅ Success Criteria

By the end of Week 03, you should be able to:
- [x] Build sequential multi-step chains
- [x] Implement map-reduce for parallel processing
- [x] Create router chains for intent classification
- [x] Add streaming to any workflow
- [x] Implement effective caching strategies
- [x] Handle errors gracefully with retries
- [x] Log and monitor workflow performance
- [x] Work with multimodal inputs (text + images)

## 🏁 Quick Start Checklist

Before starting exercises:
- [ ] Review Week 01 (prompt patterns) and Week 02 (RAG)
- [ ] Install required packages: `pip install openai asyncio`
- [ ] Test async/await with simple examples
- [ ] Set up logging for workflow debugging

---

**Next Steps**:
1. Complete hands-on exercises in `actividad-interactiva.md`
2. Build your Multi-Step Document Processor in `project-steps.md`
3. Focus on the **20% of patterns** (sequential, map-reduce, router) that handle **80% of use cases**!

🚀 **Remember**: Great workflows are simple workflows. Chain only when necessary, cache aggressively, and always show progress to users!
