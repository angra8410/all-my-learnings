# Week 04: Python for AI - Async, Batching & SDK Patterns

## 👤 Persona
**You are a seasoned Python engineer and AI infrastructure specialist who builds scalable, production-grade AI systems. You simplify complex async patterns and SDK design principles into actionable, copy-paste-ready code. Your teaching emphasizes pragmatic solutions that real engineers use in production every day.**

## 🧠 Chain of Thought Approach
Let's build production-ready Python AI code step-by-step:
1. Understand **why async matters** for AI applications (it's about throughput!)
2. Master **batching techniques** that reduce costs by 10x
3. Learn **SDK design patterns** used by OpenAI, Anthropic, and other leaders
4. Apply **packaging best practices** to make code reusable
5. Build **efficient, scalable AI workflows** that handle real production loads

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Write async Python code for concurrent AI API calls
2. Implement batching to optimize throughput and costs
3. Design clean SDK patterns for AI services
4. Package Python AI projects professionally
5. Handle rate limits, retries, and errors gracefully
6. Apply the Pareto 80/20 approach to Python AI engineering

**Estimated Duration**: 4-5 hours

## 🚀 Why These Skills Matter (Pareto Context)

**Async + Batching = 10-100x Performance Improvements**

These Python patterns are critical because:
- ✅ **Async I/O**: Process 100 requests in the time of 1 sequential call
- ✅ **Batching**: Reduce API costs by 50-90% with smart grouping
- ✅ **SDK Patterns**: Write maintainable code that scales from prototype to production
- ✅ **Packaging**: Share and reuse AI components across projects

**80% of production AI performance issues** stem from poor async/batching patterns. Master these, master AI engineering.

## 📋 Prerequisites

- Completed Weeks 01-03
- Python 3.9+ (async/await support)
- Understanding of basic Python functions and classes
- Working OpenAI or similar AI API access
- Familiarity with pip and virtual environments

## 🎓 Key Concepts

### 1. Async I/O: The Foundation (Learn This First)

**Synchronous vs. Asynchronous:**

```python
import time
from openai import OpenAI

client = OpenAI()

# ❌ SLOW: Sequential (3 seconds for 3 calls)
def sync_calls():
    start = time.time()
    
    responses = []
    for i in range(3):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Say hello {i}"}]
        )
        responses.append(response.choices[0].message.content)
    
    print(f"Sync took: {time.time() - start:.2f}s")
    return responses

# ✅ FAST: Concurrent (1 second for 3 calls)
import asyncio
from openai import AsyncOpenAI

async_client = AsyncOpenAI()

async def async_calls():
    start = time.time()
    
    async def single_call(i):
        response = await async_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Say hello {i}"}]
        )
        return response.choices[0].message.content
    
    # Run all 3 calls concurrently
    responses = await asyncio.gather(
        single_call(0),
        single_call(1),
        single_call(2)
    )
    
    print(f"Async took: {time.time() - start:.2f}s")
    return responses

# Run async version
# asyncio.run(async_calls())
```

**Key Insight**: Async doesn't make individual calls faster, but allows you to do many things at once while waiting for I/O.

### 2. Batching: The Cost Optimizer

**Three Essential Batching Patterns:**

#### Pattern 1: Simple Batch Processing
```python
from typing import List, Dict
import asyncio

class BatchProcessor:
    """Process items in batches for efficiency."""
    
    def __init__(self, batch_size: int = 10):
        self.batch_size = batch_size
        self.client = AsyncOpenAI()
    
    def create_batches(self, items: List[str]) -> List[List[str]]:
        """Split items into batches."""
        return [
            items[i:i + self.batch_size] 
            for i in range(0, len(items), self.batch_size)
        ]
    
    async def process_item(self, item: str) -> Dict[str, str]:
        """Process a single item."""
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize: {item}"}],
            max_tokens=50
        )
        return {
            "input": item,
            "output": response.choices[0].message.content
        }
    
    async def process_batch(self, batch: List[str]) -> List[Dict[str, str]]:
        """Process a batch concurrently."""
        tasks = [self.process_item(item) for item in batch]
        return await asyncio.gather(*tasks)
    
    async def process_all(self, items: List[str]) -> List[Dict[str, str]]:
        """Process all items in batches."""
        batches = self.create_batches(items)
        results = []
        
        for i, batch in enumerate(batches):
            print(f"Processing batch {i+1}/{len(batches)}...")
            batch_results = await self.process_batch(batch)
            results.extend(batch_results)
            
            # Rate limiting: small delay between batches
            if i < len(batches) - 1:
                await asyncio.sleep(0.5)
        
        return results

# Usage
async def main():
    processor = BatchProcessor(batch_size=5)
    items = [f"Document {i}" for i in range(25)]
    results = await processor.process_all(items)
    print(f"Processed {len(results)} items")

# asyncio.run(main())
```

#### Pattern 2: Adaptive Batch Sizing
```python
class AdaptiveBatchProcessor:
    """Automatically adjust batch size based on performance."""
    
    def __init__(self, initial_batch_size: int = 10):
        self.batch_size = initial_batch_size
        self.client = AsyncOpenAI()
        self.metrics = []
    
    async def process_batch_with_timing(self, batch: List[str]) -> tuple:
        """Process batch and measure performance."""
        start = time.time()
        
        tasks = [self._process_one(item) for item in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        duration = time.time() - start
        success_count = sum(1 for r in results if not isinstance(r, Exception))
        
        self.metrics.append({
            "batch_size": len(batch),
            "duration": duration,
            "success_rate": success_count / len(batch),
            "items_per_second": len(batch) / duration
        })
        
        return results, duration
    
    async def _process_one(self, item: str) -> str:
        """Process single item."""
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": item}],
            max_tokens=30
        )
        return response.choices[0].message.content
    
    def adjust_batch_size(self):
        """Adjust batch size based on recent performance."""
        if len(self.metrics) < 3:
            return
        
        recent = self.metrics[-3:]
        avg_success = sum(m["success_rate"] for m in recent) / 3
        
        # If success rate drops, reduce batch size
        if avg_success < 0.9:
            self.batch_size = max(1, int(self.batch_size * 0.7))
            print(f"Reduced batch size to {self.batch_size}")
        # If consistently successful, try increasing
        elif avg_success >= 0.98 and self.batch_size < 50:
            self.batch_size = int(self.batch_size * 1.3)
            print(f"Increased batch size to {self.batch_size}")
    
    async def process_adaptive(self, items: List[str]) -> List[str]:
        """Process with adaptive batching."""
        results = []
        i = 0
        
        while i < len(items):
            batch = items[i:i + self.batch_size]
            batch_results, _ = await self.process_batch_with_timing(batch)
            results.extend(batch_results)
            
            i += len(batch)
            self.adjust_batch_size()
        
        return results

# Usage provides automatic optimization
processor = AdaptiveBatchProcessor()
# await processor.process_adaptive(large_item_list)
```

#### Pattern 3: Smart Embedding Batching
```python
class EmbeddingBatcher:
    """Efficient batching for embeddings (OpenAI supports up to 2048 inputs)."""
    
    def __init__(self):
        self.client = OpenAI()  # Sync client for embeddings
    
    def batch_embeddings(self, texts: List[str], batch_size: int = 100) -> List[List[float]]:
        """Generate embeddings in optimal batches."""
        all_embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            # Single API call for entire batch
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=batch
            )
            
            # Extract embeddings in correct order
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
            
            print(f"Generated {len(batch_embeddings)} embeddings (batch {i//batch_size + 1})")
        
        return all_embeddings

# Usage: Much more efficient than one-at-a-time
batcher = EmbeddingBatcher()
texts = [f"Text {i}" for i in range(1000)]
embeddings = batcher.batch_embeddings(texts, batch_size=100)
# Result: 10 API calls instead of 1000!
```

## 🎯 Pareto Principle (80/20 for Python AI)

### 20% of Patterns That Deliver 80% of Value

#### 1. **Rate Limiting** (Most Critical)
```python
import asyncio
from datetime import datetime, timedelta
from collections import deque

class RateLimiter:
    """Simple but effective rate limiter."""
    
    def __init__(self, calls_per_minute: int = 60):
        self.calls_per_minute = calls_per_minute
        self.calls = deque()
    
    async def acquire(self):
        """Wait if necessary to respect rate limit."""
        now = datetime.now()
        
        # Remove calls older than 1 minute
        while self.calls and self.calls[0] < now - timedelta(minutes=1):
            self.calls.popleft()
        
        # If at limit, wait
        if len(self.calls) >= self.calls_per_minute:
            sleep_time = (self.calls[0] + timedelta(minutes=1) - now).total_seconds()
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
            await self.acquire()  # Recursive check
        
        self.calls.append(now)

class RateLimitedClient:
    """API client with built-in rate limiting."""
    
    def __init__(self, calls_per_minute: int = 60):
        self.client = AsyncOpenAI()
        self.limiter = RateLimiter(calls_per_minute)
    
    async def create_completion(self, **kwargs):
        """Rate-limited completion."""
        await self.limiter.acquire()
        return await self.client.chat.completions.create(**kwargs)

# Usage: Never hit rate limits again
client = RateLimitedClient(calls_per_minute=50)
# await client.create_completion(...)
```

#### 2. **Retry with Exponential Backoff**
```python
import random

class RetryClient:
    """Client with smart retry logic."""
    
    def __init__(self, max_retries: int = 3):
        self.client = AsyncOpenAI()
        self.max_retries = max_retries
    
    async def create_with_retry(self, **kwargs):
        """Create completion with exponential backoff retry."""
        last_exception = None
        
        for attempt in range(self.max_retries):
            try:
                return await self.client.chat.completions.create(**kwargs)
            
            except Exception as e:
                last_exception = e
                
                # Don't retry on certain errors
                if "invalid" in str(e).lower():
                    raise
                
                if attempt < self.max_retries - 1:
                    # Exponential backoff with jitter
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"Retry {attempt + 1}/{self.max_retries} after {wait_time:.2f}s")
                    await asyncio.sleep(wait_time)
        
        raise last_exception

# Usage: Handles transient failures automatically
client = RetryClient(max_retries=3)
# response = await client.create_with_retry(model="gpt-3.5-turbo", messages=[...])
```

#### 3. **Connection Pooling**
```python
from typing import Optional
import httpx

class PooledClient:
    """Use connection pooling for better performance."""
    
    def __init__(self):
        # httpx client with connection pooling
        self._http_client: Optional[httpx.AsyncClient] = None
        self.client = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        self._http_client = httpx.AsyncClient(
            limits=httpx.Limits(
                max_keepalive_connections=20,
                max_connections=100
            )
        )
        self.client = AsyncOpenAI(http_client=self._http_client)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup."""
        if self._http_client:
            await self._http_client.aclose()
    
    async def create_completion(self, **kwargs):
        """Create completion using pooled connection."""
        return await self.client.chat.completions.create(**kwargs)

# Usage: Reuse connections for better performance
async def main():
    async with PooledClient() as client:
        # All requests reuse connections from pool
        tasks = [
            client.create_completion(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Hello {i}"}]
            )
            for i in range(20)
        ]
        results = await asyncio.gather(*tasks)

# Connection pooling provides 20-30% latency reduction
```

### 3. SDK Design Patterns

**Build Clean, Reusable AI SDKs:**

```python
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class ModelType(Enum):
    """Supported models."""
    GPT_35_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo-preview"

@dataclass
class CompletionConfig:
    """Configuration for completions."""
    model: ModelType = ModelType.GPT_35_TURBO
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    top_p: float = 1.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to API parameters."""
        params = {
            "model": self.model.value,
            "temperature": self.temperature,
            "top_p": self.top_p
        }
        if self.max_tokens:
            params["max_tokens"] = self.max_tokens
        return params

class AIClient:
    """Clean SDK interface for AI operations."""
    
    def __init__(self, api_key: Optional[str] = None, config: Optional[CompletionConfig] = None):
        """Initialize client with optional configuration."""
        self.client = AsyncOpenAI(api_key=api_key)
        self.config = config or CompletionConfig()
        self._rate_limiter = RateLimiter(calls_per_minute=60)
    
    async def complete(
        self, 
        prompt: str, 
        system: Optional[str] = None,
        config: Optional[CompletionConfig] = None
    ) -> str:
        """High-level completion method."""
        await self._rate_limiter.acquire()
        
        cfg = config or self.config
        messages = []
        
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = await self.client.chat.completions.create(
            messages=messages,
            **cfg.to_dict()
        )
        
        return response.choices[0].message.content
    
    async def batch_complete(
        self, 
        prompts: List[str],
        system: Optional[str] = None,
        batch_size: int = 10
    ) -> List[str]:
        """Batch completion with automatic batching."""
        results = []
        
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i + batch_size]
            tasks = [self.complete(p, system) for p in batch]
            batch_results = await asyncio.gather(*tasks)
            results.extend(batch_results)
        
        return results
    
    async def stream_complete(self, prompt: str, system: Optional[str] = None):
        """Stream completion for real-time UX."""
        await self._rate_limiter.acquire()
        
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        stream = await self.client.chat.completions.create(
            messages=messages,
            stream=True,
            **self.config.to_dict()
        )
        
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

# Usage: Clean, intuitive API
async def example():
    # Initialize with configuration
    config = CompletionConfig(
        model=ModelType.GPT_35_TURBO,
        temperature=0.5,
        max_tokens=100
    )
    
    client = AIClient(config=config)
    
    # Single completion
    result = await client.complete("What is AI?")
    
    # Batch completion
    prompts = [f"Explain {topic}" for topic in ["AI", "ML", "DL"]]
    results = await client.batch_complete(prompts)
    
    # Streaming
    async for token in client.stream_complete("Write a story"):
        print(token, end="", flush=True)

# Clean SDK makes code maintainable and testable
```

### 4. Packaging Best Practices

**Project Structure:**
```
ai-toolkit/
├── src/
│   └── ai_toolkit/
│       ├── __init__.py
│       ├── client.py
│       ├── batch.py
│       ├── rate_limit.py
│       └── utils.py
├── tests/
│   ├── test_client.py
│   └── test_batch.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

**pyproject.toml:**
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "ai-toolkit"
version = "0.1.0"
description = "Production-ready AI utilities"
authors = [{name = "Your Name", email = "you@example.com"}]
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "openai>=1.0.0",
    "httpx>=0.25.0",
    "asyncio>=3.4.3",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]
```

**__init__.py:**
```python
"""AI Toolkit - Production-ready AI utilities."""

from .client import AIClient, CompletionConfig, ModelType
from .batch import BatchProcessor
from .rate_limit import RateLimiter

__version__ = "0.1.0"

__all__ = [
    "AIClient",
    "CompletionConfig",
    "ModelType",
    "BatchProcessor",
    "RateLimiter",
]
```

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Forgetting await
❌ **Problem**: `result = async_function()` returns a coroutine, not the result
✅ **Solution**: `result = await async_function()`

### Pitfall 2: Blocking in Async Functions
❌ **Problem**: Using `time.sleep()` blocks the event loop
✅ **Solution**: Use `await asyncio.sleep()`

### Pitfall 3: Not Handling Exceptions in asyncio.gather
❌ **Problem**: One failure crashes all concurrent tasks
✅ **Solution**: Use `return_exceptions=True`:
```python
results = await asyncio.gather(*tasks, return_exceptions=True)
```

### Pitfall 4: Unbounded Concurrency
❌ **Problem**: Starting 10,000 concurrent requests
✅ **Solution**: Use semaphores:
```python
semaphore = asyncio.Semaphore(10)  # Max 10 concurrent

async def limited_call(item):
    async with semaphore:
        return await process(item)
```

## 🎯 Week 04 Project Component

Build a **High-Performance AI Batch Processor**:

**Requirements**:
1. Async processing with configurable concurrency
2. Automatic batching with adaptive sizing
3. Rate limiting and retry logic
4. Clean SDK interface
5. Comprehensive error handling
6. Performance metrics and logging
7. Package as installable Python module

See `project-steps.md` for detailed implementation guide.

## 📚 Further Reading (Vital Resources Only)

### Must-Read
- [Real Python: Async IO](https://realpython.com/async-io-python/)
- [Python Packaging Guide](https://packaging.python.org/)
- [OpenAI Python Library](https://github.com/openai/openai-python)

### Nice-to-Have
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Poetry for Packaging](https://python-poetry.org/)

## ✅ Success Criteria

By the end of Week 04, you should be able to:
- [x] Write async functions and use await correctly
- [x] Process batches of AI requests efficiently
- [x] Implement rate limiting and retries
- [x] Design clean SDK interfaces
- [x] Package Python projects professionally
- [x] Handle errors gracefully in async code
- [x] Measure and optimize performance
- [x] Use connection pooling for efficiency

## 🏁 Quick Start Checklist

Before starting exercises:
- [ ] Install packages: `pip install openai httpx asyncio pytest-asyncio`
- [ ] Review async/await basics
- [ ] Test OpenAI API key with simple async call
- [ ] Set up project structure for packaging

---

**Next Steps**:
1. Complete hands-on exercises in `actividad-interactiva.md`
2. Build your High-Performance Batch Processor in `project-steps.md`
3. Focus on **async + batching** — these are the **20% that deliver 80%** of performance gains!

🚀 **Remember**: Async isn't about speed, it's about throughput. Batch aggressively, rate limit proactively, and always measure performance!
