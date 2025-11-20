# Week 07: Fine-Tuning LLMs

## 👨‍🏫 Your Expert Persona

**You are an applied NLP/AI expert** who specializes in customizing large language models (LLMs) for diverse use cases in industry. You make complex ideas refreshingly approachable and focus on practical, high-impact techniques that deliver results quickly.

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Understand fine-tuning fundamentals** and when it's the right solution
2. **Prepare datasets efficiently** using proven minimal patterns
3. **Implement LoRA/PEFT** for parameter-efficient fine-tuning
4. **Avoid common pitfalls** with "just right" default settings
5. **Execute a complete fine-tuning workflow** with measurable results

**Estimated Duration**: 4-5 hours

---

## 🧠 Chain of Thought: Understanding Fine-Tuning

### Step 1: What is Fine-Tuning and Why It Matters

Fine-tuning adapts a pre-trained LLM to your specific use case by training it on your domain-specific data. Think of it as teaching an already-educated expert your company's specific procedures.

**When to use fine-tuning:**
- ✅ You need consistent style/tone across outputs
- ✅ You have 100+ high-quality examples
- ✅ Prompt engineering hits diminishing returns
- ✅ You need cost reduction on repetitive tasks

**When NOT to fine-tune:**
- ❌ You have <50 examples (use few-shot prompting instead)
- ❌ The task changes frequently (too inflexible)
- ❌ You just need better prompts (cheaper solution)

### Step 2: Core Steps (Pareto 80/20)

The **20% of steps** that deliver **80% of results**:

1. **Data Preparation (30% of effort, 40% of impact)**
   - Format: Input-output pairs in JSON/JSONL
   - Quality > Quantity: 100 great examples > 1000 mediocre ones
   - Balance: Diverse examples covering edge cases

2. **Model Selection (10% of effort, 20% of impact)**
   - Start small: GPT-3.5-turbo, Llama-2-7B, or Mistral-7B
   - Proven models with active communities
   - Consider: inference speed, cost, licensing

3. **Training with LoRA/PEFT (40% of effort, 30% of impact)**
   - Use Parameter-Efficient Fine-Tuning (PEFT)
   - LoRA reduces trainable parameters by 90%+
   - Faster training, lower memory, easier deployment

4. **Evaluation (20% of effort, 10% of impact)**
   - Test on held-out examples
   - Compare: base model vs. fine-tuned model
   - Measure: accuracy, consistency, latency

### Step 3: Minimal Practical Workflow

Here's a **battle-tested, minimal workflow** using Hugging Face:

```python
# Install dependencies
# pip install transformers datasets peft accelerate bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
import torch

# Step 1: Load base model and tokenizer
model_name = "mistralai/Mistral-7B-v0.1"  # or "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,  # Reduce memory usage
    device_map="auto",
    torch_dtype=torch.float16
)

# Step 2: Prepare model for LoRA
model = prepare_model_for_kbit_training(model)

# Step 3: Configure LoRA (these are proven defaults)
lora_config = LoraConfig(
    r=16,                # Rank (higher = more parameters, start with 8-16)
    lora_alpha=32,       # Scaling factor (typically 2x rank)
    target_modules=["q_proj", "v_proj"],  # Which layers to adapt
    lora_dropout=0.05,   # Regularization
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # Typically <1% of total params!

# Step 4: Prepare dataset
def format_instruction(example):
    """Format your data as instruction-response pairs"""
    return f"### Instruction:\n{example['input']}\n\n### Response:\n{example['output']}"

# Load your data (JSONL format: {"input": "...", "output": "..."})
dataset = load_dataset("json", data_files="your_data.jsonl")
dataset = dataset.map(lambda x: {"text": format_instruction(x)})

# Step 5: Training arguments (sensible defaults)
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,           # 3-5 epochs usually sufficient
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,            # LoRA sweet spot
    logging_steps=10,
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

# Step 6: Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"]
)

trainer.train()

# Step 7: Save the LoRA adapter (tiny size!)
model.save_pretrained("./fine-tuned-lora")
tokenizer.save_pretrained("./fine-tuned-lora")
```

### Step 4: Common Pitfalls and Solutions

| Pitfall | Solution |
|---------|----------|
| **Overfitting** (model memorizes training data) | • Reduce epochs (try 2-3)<br>• Add more diverse examples<br>• Increase LoRA dropout to 0.1 |
| **Catastrophic forgetting** (model loses general knowledge) | • Keep learning rate low (2e-4 to 5e-4)<br>• Use LoRA instead of full fine-tuning<br>• Mix in general examples (10-20%) |
| **Poor convergence** (loss doesn't decrease) | • Check data format consistency<br>• Increase learning rate slightly<br>• Verify tokenization works correctly |
| **Out of memory** | • Enable 8-bit loading<br>• Reduce batch size<br>• Use gradient checkpointing<br>• Try smaller base model |

### Step 5: "Just Right" Default Settings

Start with these **proven configurations**:

```python
# LoRA Configuration
lora_r = 8           # Start here, increase if underfitting
lora_alpha = 16      # 2x rank is standard
lora_dropout = 0.05  # Light regularization

# Training Configuration
learning_rate = 2e-4      # LoRA sweet spot
num_epochs = 3            # Usually sufficient
batch_size = 4            # Adjust based on GPU memory
warmup_steps = 100        # Gentle learning rate warmup
weight_decay = 0.01       # Prevent overfitting

# Evaluation
eval_steps = 50           # Check progress frequently
save_total_limit = 2      # Keep only best 2 checkpoints
```

---

## 🎯 Pareto Principle (20/80 Focus)

### The Vital 20% (Master These)

1. **High-Quality Data Preparation**
   - 100-500 well-formatted examples > 10,000 messy ones
   - Consistent format: instruction → response
   - Representative of real use cases

2. **LoRA/PEFT Over Full Fine-Tuning**
   - 90%+ reduction in trainable parameters
   - 3-5x faster training
   - Easier to experiment and iterate

3. **Sensible Defaults First**
   - Don't tweak hyperparameters initially
   - Use proven configurations from above
   - Optimize only if results are poor

### The Impactful 80% (Practice These)

1. **Rapid Experimentation Loop**
   - Prepare small dataset (100 examples) → fine-tune → evaluate → iterate
   - Each iteration: 1-2 hours max
   - Quick feedback = faster learning

2. **Evaluation-Driven Improvement**
   - Compare outputs: base vs. fine-tuned
   - Measure what matters: accuracy, consistency, tone
   - Use real test cases from production

3. **Incremental Data Growth**
   - Start: 100 examples
   - Works well: add 200 more
   - Diminishing returns: stop at 500-1000

---

## 🛠️ Tools & Technologies

**Primary Stack:**
- **Hugging Face Transformers**: Industry-standard library
- **PEFT (Parameter-Efficient Fine-Tuning)**: LoRA and QLoRA
- **Datasets**: Data loading and processing
- **Accelerate**: Distributed training made easy

**Supporting Tools:**
- **Weights & Biases**: Track experiments (optional but recommended)
- **bitsandbytes**: 8-bit quantization for memory efficiency
- **TRL (Transformer Reinforcement Learning)**: For instruction-tuning

**Alternative Platforms (No-Code Options):**
- OpenAI Fine-Tuning API (easiest, proprietary)
- Anthropic Claude Fine-Tuning (in beta)
- Anyscale Endpoints (managed infrastructure)

---

## 📝 Hands-On Exercise: Fine-Tune a Small LLM

**Objective**: Fine-tune a small model on a toy dataset and compare results.

**Task**: Create a customer service chatbot that responds in a specific company style.

**Dataset** (create 20 examples like this):
```json
{"input": "How do I return an item?", "output": "Hey there! 😊 Returns are super easy! Just visit your Orders page..."}
{"input": "What's your shipping policy?", "output": "Great question! We offer free shipping on orders over $50..."}
```

**Steps**:
1. Prepare 20 instruction-response pairs in JSONL format
2. Use the code template above with `gpt2` (small, fast for learning)
3. Fine-tune for 3 epochs (should take 5-10 minutes on CPU)
4. Test with prompts: "How long does delivery take?"
5. Compare: base GPT-2 vs. your fine-tuned version

**Success Criteria**:
- Fine-tuned model adopts your style/tone
- Responses are coherent and relevant
- You understand the workflow end-to-end

---

## 📚 Resources

See `resources.md` for:
- Hugging Face fine-tuning guides
- PEFT documentation and examples
- Curated datasets for practice
- Community tutorials and case studies

---

## ✅ Success Criteria

- [ ] Understand when to use fine-tuning vs. prompting
- [ ] Can prepare a dataset in correct format
- [ ] Successfully run a LoRA fine-tuning workflow
- [ ] Evaluate and compare base vs. fine-tuned models
- [ ] Know how to troubleshoot common issues
- [ ] Complete the hands-on exercise

**Track your progress in `progreso.md`**

---

## 🚀 Next Steps

1. Complete the **hands-on exercise** above
2. Work through **interactive activities** in `actividad-interactiva.md`
3. Apply fine-tuning to your **capstone project** (see `project-steps.md`)
4. Review **evaluation criteria** in `retroalimentacion.md`

---

**Ready to fine-tune?** The vital few techniques you'll learn this week are used daily in production AI systems. Let's build mastery through practice! 💪
