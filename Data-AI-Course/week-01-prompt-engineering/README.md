# Week 01: Prompt Engineering Fundamentals

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Understand and apply core prompt engineering principles
2. Design effective prompt templates for different use cases
3. Implement few-shot learning techniques
4. Use chain-of-thought (CoT) prompting for complex reasoning
5. Debug and iterate on prompts systematically
6. Recognize and avoid common prompt pitfalls
7. Measure prompt effectiveness quantitatively

**Estimated Duration**: 4-5 hours

## 🚀 Why Prompt Engineering Matters

Prompt engineering is the highest-leverage skill in AI development. A well-crafted prompt can:
- Achieve 10x better results than a naive prompt
- Replace complex fine-tuning in many cases
- Save thousands of dollars in API costs
- Enable rapid prototyping and iteration

**Think of prompts as the "code" for LLMs** — they need the same rigor as traditional programming.

## 📋 Prerequisites

- Completed Week 00 (environment setup)
- Working OpenAI or Anthropic API access
- Basic understanding of LLM capabilities
- Familiarity with Python

## 🎓 Key Concepts

### 1. The Anatomy of a Good Prompt

A well-structured prompt typically includes:

```
[ROLE] You are a [specific role with relevant expertise]

[CONTEXT] Given this context: [relevant background information]

[TASK] Your task is to [clear, specific instruction]

[FORMAT] Please provide your response in [desired format]

[CONSTRAINTS] Constraints:
- [constraint 1]
- [constraint 2]

[EXAMPLES] Here are examples: [few-shot examples if applicable]
```

### 2. Prompt Engineering Principles

**The 6 P's of Prompt Engineering:**

1. **Persona**: Define who the LLM should be
2. **Purpose**: State the goal clearly
3. **Parameters**: Set constraints and requirements
4. **Patterns**: Use proven prompt templates
5. **Polish**: Iterate and refine
6. **Proof**: Measure and validate results

### 3. Prompt Patterns

#### Pattern 1: Zero-Shot
```python
prompt = "Translate this to French: 'Hello, world!'"
# No examples provided
```

#### Pattern 2: Few-Shot
```python
prompt = """
Translate to French:
English: Good morning
French: Bonjour

English: Thank you
French: Merci

English: Hello, world!
French:"""
# Provides examples to guide the model
```

#### Pattern 3: Chain-of-Thought (CoT)
```python
prompt = """
Question: What is 15% of 240?
Let's think step by step:
1. Convert 15% to decimal: 0.15
2. Multiply: 240 × 0.15 = 36
Answer: 36

Question: What is 23% of 180?
Let's think step by step:"""
# Encourages reasoning process
```

#### Pattern 4: ReAct (Reasoning + Acting)
```python
prompt = """
Thought: I need to find the capital of France
Action: search("capital of France")
Observation: Paris is the capital of France
Thought: I now know the answer
Answer: Paris

Thought: I need to find the population of Tokyo
Action:"""
```

### 4. Temperature and Parameters

**Temperature** (0.0 to 2.0):
- **0.0-0.3**: Deterministic, consistent (good for factual tasks)
- **0.4-0.7**: Balanced creativity and consistency
- **0.8-1.0**: Creative, varied responses
- **1.1-2.0**: Highly creative, less predictable

**Top-p** (nucleus sampling):
- **0.1**: Very focused, conservative
- **0.5**: Moderate diversity
- **0.9-1.0**: Maximum diversity

**Max Tokens**: Controls response length
- Set appropriately for task
- Monitor to control costs

## 🛠️ Prompt Engineering Toolkit

### Essential Techniques

#### 1. System Messages
```python
system_message = """You are an expert Python developer with 10 years of experience.
You write clean, efficient, well-documented code.
You always include error handling and type hints."""
```

#### 2. Delimiters
Use clear delimiters to separate sections:
```python
prompt = """
Text to analyze: \"\"\"
{user_input}
\"\"\"

Task: Extract key entities
"""
```

#### 3. Output Formatting
Request specific formats:
```python
prompt = """
Analyze this text and return JSON:
{
  "sentiment": "positive/negative/neutral",
  "entities": ["entity1", "entity2"],
  "summary": "one-sentence summary"
}
"""
```

#### 4. Constraint Specification
```python
prompt = """
Write a product description.

Constraints:
- Maximum 100 words
- Include 3 key benefits
- Use professional tone
- Avoid technical jargon
- Include a call-to-action
"""
```

## 📊 Prompt Debugging Workflow

### Step 1: Start Simple
Begin with the simplest possible prompt:
```python
prompt = "Summarize this text: {text}"
```

### Step 2: Add Context
```python
prompt = """You are a technical writer.
Summarize this text for a non-technical audience: {text}"""
```

### Step 3: Specify Format
```python
prompt = """You are a technical writer.
Summarize this text in 3 bullet points for a non-technical audience: {text}"""
```

### Step 4: Add Examples (if needed)
```python
prompt = """You are a technical writer.
Summarize text in 3 bullet points for non-technical audience.

Example:
Input: "Machine learning models require large datasets..."
Output:
• AI systems need lots of data to learn
• More data generally means better performance
• Quality of data matters more than quantity

Now summarize: {text}"""
```

### Step 5: Iterate and Measure
Test with multiple examples and measure:
- Accuracy/correctness
- Consistency across inputs
- Response time
- Token usage/cost

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Vague Instructions
❌ **Bad**: "Tell me about AI"
✅ **Good**: "Explain artificial intelligence in 3 paragraphs for a business audience, focusing on practical applications in retail"

### Pitfall 2: Too Many Tasks
❌ **Bad**: "Analyze sentiment, extract entities, translate to Spanish, and summarize"
✅ **Good**: Break into separate prompts or use chain-of-thought

### Pitfall 3: Ambiguous Format
❌ **Bad**: "List the main points"
✅ **Good**: "List exactly 5 main points as a numbered list"

### Pitfall 4: Missing Context
❌ **Bad**: "Is this good?" (without providing "this")
✅ **Good**: Include all necessary context in the prompt

### Pitfall 5: Ignoring Token Limits
❌ **Bad**: Sending entire documents without considering limits
✅ **Good**: Chunk content appropriately or summarize first

## 🎯 Best Practices

### 1. Be Specific and Clear
```python
# Vague
prompt = "Write code"

# Specific
prompt = "Write a Python function that takes a list of integers and returns the sum of even numbers. Include type hints, docstring, and error handling for empty lists."
```

### 2. Use Examples Strategically
- 0-shot: Simple, well-defined tasks
- 1-3 shot: Moderate complexity, style matching
- 3-5 shot: Complex tasks, specific format requirements
- 5+ shot: Rarely needed, may confuse model

### 3. Iterate Systematically
1. Baseline prompt
2. Add role/persona
3. Add examples
4. Specify format
5. Add constraints
6. Test edge cases

### 4. Version Control Your Prompts
```python
# v1.0 - Basic
prompt_v1 = "Summarize: {text}"

# v1.1 - Added context
prompt_v11 = "As a technical writer, summarize: {text}"

# v1.2 - Added constraints
prompt_v12 = "As a technical writer, summarize in 100 words: {text}"
```

### 5. Measure Performance
Track metrics:
- Response relevance (human eval or automated)
- Task completion rate
- Consistency (same input → similar output)
- Cost per request
- Latency

## 🔧 Advanced Techniques

### Self-Consistency
Run the same prompt multiple times and take majority vote:
```python
responses = [llm(prompt) for _ in range(5)]
# Choose most common response
```

### Generated Knowledge
Have the model generate relevant knowledge first:
```python
prompt = """
First, list key facts about {topic}.
Then, using those facts, answer: {question}
"""
```

### Prompt Chaining
Break complex tasks into steps:
```python
step1 = llm("Extract key facts from: {text}")
step2 = llm(f"Analyze these facts: {step1}")
step3 = llm(f"Create recommendation based on: {step2}")
```

### Meta-Prompting
Have the LLM improve the prompt:
```python
meta_prompt = """
I want to ask an AI to {task}.
Suggest an optimized prompt that would work well.
"""
```

## 📚 Prompt Template Library

### Template 1: Structured Extraction
```python
EXTRACTION_TEMPLATE = """
Extract the following information from the text below.
Return as JSON with these keys: {keys}

Text: \"\"\"
{text}
\"\"\"

JSON:"""
```

### Template 2: Classification
```python
CLASSIFICATION_TEMPLATE = """
Classify the following {item_type} into one of these categories: {categories}

{item_type}: {content}

Category:"""
```

### Template 3: Transformation
```python
TRANSFORMATION_TEMPLATE = """
Convert the following {input_format} to {output_format}:

Input: {content}

Output:"""
```

### Template 4: Generation
```python
GENERATION_TEMPLATE = """
Generate a {output_type} with the following characteristics:
{characteristics}

{output_type}:"""
```

## 🎯 Pareto Principle (20/80 Rule)

### 20% of Concepts (Learn These First)
1. **Clear, specific instructions** - Most important factor
2. **Role/persona specification** - Sets context and expertise level
3. **Output format specification** - Ensures usable results

### 80% of Practice (Do This)
1. **Write 10+ prompts** for different tasks
2. **Compare zero-shot vs few-shot** on same task
3. **Iterate systematically** - measure each change

## 🚀 Week 01 Project Component

This week, you'll create a **Prompt Testing Framework** that you'll use throughout the course and in your capstone projects. This framework will:

- Store prompt templates
- Track prompt versions
- Measure performance metrics
- Compare prompt variations
- Log results for analysis

See `project-steps.md` for detailed implementation.

## 📖 Further Reading

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Prompt Engineering Guide (promptingguide.ai)](https://www.promptingguide.ai/)
- [LangChain Prompt Templates](https://python.langchain.com/docs/modules/model_io/prompts/)

## ✅ Success Criteria

By the end of Week 01, you should be able to:
- [ ] Write effective prompts for common tasks
- [ ] Apply few-shot learning appropriately
- [ ] Debug prompts systematically
- [ ] Measure prompt performance
- [ ] Choose appropriate parameters (temperature, etc.)
- [ ] Recognize and avoid common pitfalls

---

**Next**: Complete the exercises in `actividad-interactiva.md` to practice these concepts hands-on! 🚀
