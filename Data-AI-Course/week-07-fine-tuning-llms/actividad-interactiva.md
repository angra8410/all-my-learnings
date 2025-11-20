# Actividades Interactivas - Week 07: Fine-Tuning LLMs

## 🎯 Objective

Master fine-tuning LLMs through **practical, high-impact exercises** focused on the **Pareto 80/20 principle**: minimal effort, maximal learning.

---

## Exercise 1: Dataset Preparation for Fine-Tuning (30 min)

### 🎯 Objective
Learn to prepare high-quality datasets—the **#1 factor** in fine-tuning success (40% of impact!).

### 📝 Context
You're building a customer support bot for "TechCo" that needs to respond in a friendly, helpful style with company-specific knowledge.

### Steps

1. **Setup**
   ```bash
   mkdir week-07-exercise-1
   cd week-07-exercise-1
   touch training_data.jsonl
   ```

2. **Create Training Data**
   
   Create 20 instruction-response pairs in `training_data.jsonl`. Each line should be valid JSON:
   
   ```json
   {"input": "How do I reset my password?", "output": "Hey there! 😊 No worries, password resets are easy! Here's what to do:\n1. Click 'Forgot Password' on the login page\n2. Enter your email\n3. Check your inbox for the reset link\n4. Create your new password\n\nIf you don't see the email within 5 minutes, check your spam folder. Still stuck? We're here to help!"}
   {"input": "What's your refund policy?", "output": "Great question! We want you to be happy with your purchase. 🎉\n\n• 30-day money-back guarantee\n• Free return shipping\n• Refunds processed within 3-5 business days\n\nJust go to Orders > Select item > Request Refund. Easy peasy!"}
   ```

3. **Data Quality Checklist**
   
   For each example, verify:
   - ✅ Input is a realistic customer question
   - ✅ Output uses consistent tone/style (friendly, helpful, uses emojis)
   - ✅ Output includes specific, actionable information
   - ✅ Covers diverse scenarios (account, billing, products, shipping, etc.)

4. **Validation Script**
   
   Create `validate_data.py`:
   ```python
   import json
   
   def validate_dataset(filepath):
       """Validate JSONL dataset format and quality"""
       with open(filepath, 'r') as f:
           lines = f.readlines()
       
       issues = []
       for i, line in enumerate(lines):
           try:
               data = json.loads(line)
               if 'input' not in data or 'output' not in data:
                   issues.append(f"Line {i+1}: Missing 'input' or 'output' field")
               if len(data['input']) < 10:
                   issues.append(f"Line {i+1}: Input too short")
               if len(data['output']) < 20:
                   issues.append(f"Line {i+1}: Output too short")
           except json.JSONDecodeError:
               issues.append(f"Line {i+1}: Invalid JSON")
       
       if not issues:
           print(f"✅ Dataset valid! {len(lines)} examples ready for fine-tuning.")
       else:
           print("❌ Issues found:")
           for issue in issues:
               print(f"  - {issue}")
   
   validate_dataset('training_data.jsonl')
   ```
   
   Run it:
   ```bash
   python validate_data.py
   ```
   
   **Expected output**: `✅ Dataset valid! 20 examples ready for fine-tuning.`

### 🎓 Key Takeaway
**Quality > Quantity**: 20 excellent examples teach the model more than 200 mediocre ones. Focus on consistency, relevance, and diversity.

### Validation Checklist
- [ ] Created 20+ high-quality instruction-response pairs
- [ ] All examples follow consistent format and style
- [ ] Validation script passes without errors
- [ ] Dataset covers diverse customer scenarios

**Duration**: 30 minutes

---

## Exercise 2: Fine-Tune with LoRA (60 min)

### 🎯 Objective
Execute a complete fine-tuning workflow using **LoRA/PEFT**—the vital technique that makes fine-tuning practical and affordable.

### 📝 Context
Fine-tune a small language model (GPT-2 or distilgpt2) on your customer support dataset from Exercise 1.

### Steps

1. **Setup Environment**
   ```bash
   mkdir week-07-exercise-2
   cd week-07-exercise-2
   
   # Install dependencies
   pip install transformers datasets peft accelerate torch
   ```

2. **Create Training Script**
   
   Save as `fine_tune_lora.py`:
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForLanguageModeling
   from peft import LoraConfig, get_peft_model
   from datasets import load_dataset
   import torch
   
   # Configuration (Pareto-optimal defaults)
   MODEL_NAME = "distilgpt2"  # Small, fast for learning
   LORA_R = 8
   LORA_ALPHA = 16
   LORA_DROPOUT = 0.05
   LEARNING_RATE = 2e-4
   NUM_EPOCHS = 3
   BATCH_SIZE = 2
   
   print("🚀 Starting fine-tuning process...")
   
   # 1. Load model and tokenizer
   print("📥 Loading base model...")
   tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
   tokenizer.pad_token = tokenizer.eos_token  # Required for GPT models
   
   model = AutoModelForCausalLM.from_pretrained(
       MODEL_NAME,
       torch_dtype=torch.float32,  # Use float32 for CPU training
   )
   
   # 2. Configure LoRA
   print("⚙️ Configuring LoRA...")
   lora_config = LoraConfig(
       r=LORA_R,
       lora_alpha=LORA_ALPHA,
       target_modules=["c_attn"],  # GPT-2 attention layers
       lora_dropout=LORA_DROPOUT,
       bias="none",
       task_type="CAUSAL_LM"
   )
   
   model = get_peft_model(model, lora_config)
   model.print_trainable_parameters()  # See the magic of PEFT!
   
   # 3. Load and prepare dataset
   print("📊 Loading dataset...")
   dataset = load_dataset("json", data_files="../week-07-exercise-1/training_data.jsonl")
   
   def format_prompt(example):
       """Format as instruction-following prompt"""
       return {
           "text": f"### User: {example['input']}\n### Assistant: {example['output']}"
       }
   
   dataset = dataset.map(format_prompt)
   
   # Tokenize
   def tokenize(example):
       return tokenizer(example["text"], truncation=True, max_length=512, padding="max_length")
   
   tokenized_dataset = dataset.map(tokenize, remove_columns=["input", "output", "text"])
   
   # 4. Training arguments
   print("🎯 Setting up training...")
   training_args = TrainingArguments(
       output_dir="./results",
       num_train_epochs=NUM_EPOCHS,
       per_device_train_batch_size=BATCH_SIZE,
       learning_rate=LEARNING_RATE,
       logging_steps=5,
       save_strategy="epoch",
       report_to="none",  # Disable wandb for simplicity
   )
   
   # 5. Train!
   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=tokenized_dataset["train"],
       data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
   )
   
   print("🏋️ Training started...")
   trainer.train()
   
   # 6. Save the model
   print("💾 Saving fine-tuned model...")
   model.save_pretrained("./fine-tuned-model")
   tokenizer.save_pretrained("./fine-tuned-model")
   
   print("✅ Fine-tuning complete! Model saved to ./fine-tuned-model")
   ```

3. **Run Training**
   ```bash
   python fine_tune_lora.py
   ```
   
   **Expected output**: 
   ```
   trainable params: 294,912 || all params: 82,237,824 || trainable%: 0.3585
   ```
   *(Notice: Only 0.36% of parameters are trained! That's the power of LoRA.)*

4. **Test Your Fine-Tuned Model**
   
   Create `test_model.py`:
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer
   from peft import PeftModel
   import torch
   
   # Load model
   base_model = AutoModelForCausalLM.from_pretrained("distilgpt2")
   tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
   model = PeftModel.from_pretrained(base_model, "./fine-tuned-model")
   
   # Test prompts
   test_prompts = [
       "### User: How long does shipping take?\n### Assistant:",
       "### User: Can I change my order?\n### Assistant:",
       "### User: Do you ship internationally?\n### Assistant:"
   ]
   
   print("🧪 Testing fine-tuned model...\n")
   
   for prompt in test_prompts:
       inputs = tokenizer(prompt, return_tensors="pt")
       outputs = model.generate(
           **inputs,
           max_new_tokens=100,
           temperature=0.7,
           do_sample=True,
           pad_token_id=tokenizer.eos_token_id
       )
       response = tokenizer.decode(outputs[0], skip_special_tokens=True)
       print(f"Prompt: {prompt}")
       print(f"Response: {response}\n")
       print("-" * 50)
   ```
   
   ```bash
   python test_model.py
   ```

### 🎓 Key Takeaway
**LoRA makes fine-tuning practical**: Train <1% of parameters, 3-5x faster, same results. This is the modern standard for LLM customization.

### Validation Checklist
- [ ] Successfully installed all dependencies
- [ ] Training completed without errors
- [ ] Model shows <1% trainable parameters (LoRA magic!)
- [ ] Fine-tuned model responds in the trained style
- [ ] Understand the complete workflow

**Duration**: 60 minutes

---

## Exercise 3: Compare Base vs. Fine-Tuned Models (30 min)

### 🎯 Objective
**Evaluate impact**: Measure the difference fine-tuning makes through systematic comparison.

### Steps

1. **Create Comparison Script**
   
   Save as `compare_models.py`:
   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
   from peft import PeftModel
   
   print("🔄 Comparing base vs fine-tuned models...\n")
   
   # Load base model
   base_tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
   base_model = AutoModelForCausalLM.from_pretrained("distilgpt2")
   
   # Load fine-tuned model
   ft_base = AutoModelForCausalLM.from_pretrained("distilgpt2")
   ft_model = PeftModel.from_pretrained(ft_base, "./week-07-exercise-2/fine-tuned-model")
   ft_tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
   
   # Test cases
   test_cases = [
       "### User: What's your return policy?\n### Assistant:",
       "### User: How do I track my order?\n### Assistant:",
       "### User: Can I cancel my subscription?\n### Assistant:"
   ]
   
   for i, test_case in enumerate(test_cases):
       print(f"\n{'='*60}")
       print(f"TEST CASE {i+1}: {test_case.split('###')[1].strip()}")
       print(f"{'='*60}")
       
       # Base model response
       base_inputs = base_tokenizer(test_case, return_tensors="pt")
       base_outputs = base_model.generate(
           **base_inputs, 
           max_new_tokens=80,
           temperature=0.7,
           do_sample=True,
           pad_token_id=base_tokenizer.eos_token_id
       )
       base_response = base_tokenizer.decode(base_outputs[0], skip_special_tokens=True)
       
       print(f"\n📊 BASE MODEL:")
       print(base_response)
       
       # Fine-tuned model response
       ft_inputs = ft_tokenizer(test_case, return_tensors="pt")
       ft_outputs = ft_model.generate(
           **ft_inputs,
           max_new_tokens=80,
           temperature=0.7,
           do_sample=True,
           pad_token_id=ft_tokenizer.eos_token_id
       )
       ft_response = ft_tokenizer.decode(ft_outputs[0], skip_special_tokens=True)
       
       print(f"\n✨ FINE-TUNED MODEL:")
       print(ft_response)
   ```

2. **Run Comparison**
   ```bash
   python compare_models.py
   ```

3. **Evaluate Results**
   
   Create an evaluation table in `evaluation_results.md`:
   ```markdown
   # Fine-Tuning Evaluation Results
   
   ## Comparison Metrics
   
   | Criteria | Base Model | Fine-Tuned Model | Winner |
   |----------|-----------|------------------|--------|
   | Follows company style | ❌ No | ✅ Yes | Fine-tuned |
   | Uses friendly tone | ❌ Inconsistent | ✅ Consistent | Fine-tuned |
   | Provides specific info | ❌ Generic | ✅ Specific | Fine-tuned |
   | Stays on topic | ⚠️ Sometimes | ✅ Always | Fine-tuned |
   | Uses emojis appropriately | ❌ No | ✅ Yes | Fine-tuned |
   
   ## Sample Output Comparison
   
   **Prompt**: "What's your return policy?"
   
   **Base Model**: [paste output here]
   **Fine-Tuned Model**: [paste output here]
   
   **Analysis**: [your observations]
   
   ## Conclusion
   
   Fine-tuning improved [list specific improvements]
   ```

### 🎓 Key Takeaway
**Quantify the win**: Fine-tuning should show clear, measurable improvements in style consistency, relevance, and task-specific knowledge.

### Validation Checklist
- [ ] Successfully compared both models on 3+ test cases
- [ ] Documented clear differences in outputs
- [ ] Fine-tuned model shows improved consistency
- [ ] Understand when fine-tuning adds value

**Duration**: 30 minutes

---

## Exercise 4: Troubleshooting Common Issues (40 min)

### 🎯 Objective
Learn to diagnose and fix the **top 3 fine-tuning problems** that catch 80% of learners.

### Scenario-Based Learning

#### Issue 1: Model Overfits (Memorizes Training Data)

**Symptoms**:
- Perfect on training examples
- Poor/nonsensical on new inputs
- Repeats training examples verbatim

**Your Task**: Simulate and fix overfitting

```python
# Create overfitting_simulation.py
from transformers import TrainingArguments

# BAD: Overfitting configuration
bad_config = TrainingArguments(
    output_dir="./overfit_model",
    num_train_epochs=20,      # TOO MANY epochs
    learning_rate=5e-4,        # TOO HIGH learning rate
    per_device_train_batch_size=1,
    # No regularization!
)

# GOOD: Preventing overfitting
good_config = TrainingArguments(
    output_dir="./good_model",
    num_train_epochs=3,        # ✅ Reasonable
    learning_rate=2e-4,        # ✅ LoRA sweet spot
    per_device_train_batch_size=2,
    weight_decay=0.01,         # ✅ Regularization
    # Add evaluation to detect overfitting early
    evaluation_strategy="epoch"
)

print("❌ Overfitting Config:")
print(f"  Epochs: {bad_config.num_train_epochs}")
print(f"  LR: {bad_config.learning_rate}")
print(f"  Regularization: None")

print("\n✅ Good Config:")
print(f"  Epochs: {good_config.num_train_epochs}")
print(f"  LR: {good_config.learning_rate}")
print(f"  Weight Decay: {good_config.weight_decay}")
```

**Exercise**: 
1. List 3 ways to prevent overfitting
2. Explain why each works

#### Issue 2: Out of Memory (OOM)

**Symptoms**:
- Training crashes with CUDA OOM error
- Process killed

**Your Task**: Create a memory-efficient configuration

```python
# memory_efficient_config.py

print("🧠 Memory Optimization Strategies\n")

strategies = {
    "1. Use 8-bit quantization": {
        "code": "load_in_8bit=True",
        "savings": "~4x memory reduction"
    },
    "2. Reduce batch size": {
        "code": "per_device_train_batch_size=1",
        "savings": "Linear reduction"
    },
    "3. Gradient accumulation": {
        "code": "gradient_accumulation_steps=4",
        "savings": "Simulates larger batch without memory cost"
    },
    "4. Use gradient checkpointing": {
        "code": "gradient_checkpointing=True",
        "savings": "~30% memory reduction (slower training)"
    },
    "5. Use smaller model": {
        "code": "model_name='distilgpt2' instead of 'gpt2-xl'",
        "savings": "Depends on model size"
    }
}

for strategy, details in strategies.items():
    print(f"{strategy}")
    print(f"  Code: {details['code']}")
    print(f"  Impact: {details['savings']}\n")

# Create the most memory-efficient config
print("🔧 Ultra Memory-Efficient Config:")
print("""
from transformers import AutoModelForCausalLM, TrainingArguments

model = AutoModelForCausalLM.from_pretrained(
    "distilgpt2",              # Smallest viable model
    load_in_8bit=True,         # 8-bit quantization
)

args = TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,   # Effective batch size = 8
    gradient_checkpointing=True,
    fp16=True,                       # Use mixed precision
)
""")
```

**Exercise**:
1. Rank these strategies by effectiveness
2. When would you use each?

#### Issue 3: Model "Forgets" General Knowledge

**Symptoms**:
- Model great at your task
- Fails at basic general knowledge
- Lost capabilities it had before

**Your Task**: Implement catastrophic forgetting prevention

```python
# prevent_forgetting.py

print("🛡️ Preventing Catastrophic Forgetting\n")

print("Strategy 1: Use LoRA (BEST)")
print("  ✅ Only adapts small subset of weights")
print("  ✅ Base model unchanged")
print("  ✅ Can easily switch between tasks")

print("\nStrategy 2: Mix in general examples")
general_examples = [
    {"input": "What is the capital of France?", "output": "Paris"},
    {"input": "Explain photosynthesis", "output": "Plants convert light to energy..."},
]
print(f"  Add 10-20% general knowledge examples to training set")

print("\nStrategy 3: Lower learning rate")
print("  ✅ 2e-4 for LoRA (vs 1e-5 for full fine-tuning)")
print("  ✅ Gentler updates preserve more base knowledge")

print("\nStrategy 4: Fewer epochs")
print("  ✅ 3 epochs usually sufficient")
print("  ✅ More epochs = more forgetting risk")
```

**Exercise**:
Write a checklist for your fine-tuning workflow that prevents these issues.

### 🎓 Key Takeaway
**Know the top issues before they happen**: 80% of fine-tuning problems come from overfitting, memory, or forgetting. Prevention is easier than cure.

### Validation Checklist
- [ ] Understand symptoms of each issue
- [ ] Can implement solutions for each problem
- [ ] Created personal troubleshooting checklist
- [ ] Feel confident debugging fine-tuning runs

**Duration**: 40 minutes

---

## Exercise 5: Mini-Project - Domain-Specific Fine-Tuning (60 min)

### 🎯 Objective
**Apply everything**: Execute a complete fine-tuning project for a real-world use case.

### Your Mission
Choose ONE domain and fine-tune a model:

**Option A: Medical Q&A Assistant**
- Style: Professional, empathetic, includes disclaimers
- Task: Answer common health questions

**Option B: Code Documentation Generator**
- Style: Clear, technical, includes examples
- Task: Generate docstrings from function signatures

**Option C: Social Media Content Creator**
- Style: Casual, engaging, uses trending language
- Task: Create posts from topic briefs

### Steps

1. **Dataset Creation (20 min)**
   - Create 30 examples minimum in your chosen domain
   - Ensure variety and quality
   - Include edge cases

2. **Fine-Tuning (20 min)**
   - Use LoRA configuration from Exercise 2
   - Adjust hyperparameters if needed
   - Monitor training loss

3. **Evaluation (15 min)**
   - Test on 5 unseen examples
   - Compare to base model
   - Document improvements

4. **Documentation (5 min)**
   - What worked well?
   - What would you improve?
   - When would you use this in production?

### Deliverables

Create a `mini_project_report.md`:

```markdown
# Fine-Tuning Mini-Project Report

## Domain: [Your Choice]

## Dataset
- Number of examples: __
- Format: [describe]
- Key characteristics: [list]

## Training Configuration
- Base model: __
- LoRA rank: __
- Learning rate: __
- Epochs: __
- Training time: __

## Results
[Paste 3 example outputs]

## Evaluation
[Compare with base model]

## Learnings
1. __
2. __
3. __

## Production Readiness
Would I deploy this? [Yes/No, explain]
What would I improve? [list]
```

### 🎓 Key Takeaway
**End-to-end mastery**: You now know the complete workflow from dataset → training → evaluation → deployment decisions.

### Validation Checklist
- [ ] Created domain-specific dataset (30+ examples)
- [ ] Successfully fine-tuned model
- [ ] Evaluated improvements quantitatively
- [ ] Documented complete project
- [ ] Identified next steps for production

**Duration**: 60 minutes

---

## 📋 Final Checklist

- [ ] **Exercise 1**: Dataset preparation ✅
- [ ] **Exercise 2**: LoRA fine-tuning ✅
- [ ] **Exercise 3**: Model comparison ✅
- [ ] **Exercise 4**: Troubleshooting ✅
- [ ] **Exercise 5**: Mini-project ✅

**Total Time**: ~3.5 hours (Pareto-optimized for maximum learning!)

---

## 🎉 Congratulations!

You've mastered the **vital 20%** of fine-tuning that delivers **80% of results**:

✅ High-quality dataset preparation  
✅ LoRA/PEFT implementation  
✅ Evaluation and comparison  
✅ Troubleshooting common issues  
✅ End-to-end project execution  

**Next Steps**:
1. Review `project-steps.md` for capstone integration
2. Track progress in `progreso.md`
3. Check evaluation criteria in `retroalimentacion.md`

**You're now equipped to fine-tune LLMs in production environments!** 🚀
