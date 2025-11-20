# Week 08: Evaluating AI

## 👨‍💼 Your Expert Persona

**You are an AI product lead** who believes robust evaluation equals trustworthy AI. You balance statistical rigor with business impact, always asking "what metric actually matters for this use case?" You make complex evaluation concepts accessible and actionable.

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Understand why evaluation** determines AI project success or failure
2. **Select the right metrics** for different AI tasks (classification, regression, generation, etc.)
3. **Implement evaluation pipelines** in Python with real datasets
4. **Interpret metrics** in business context—not just numbers, but decisions
5. **Avoid common evaluation pitfalls** that mislead teams

**Estimated Duration**: 4-5 hours

---

## 🧠 Chain of Thought: Understanding AI Evaluation

### Step 1: Why Evaluation Determines Success

**The harsh reality**: 70% of AI projects fail—not due to bad models, but bad evaluation.

Think of evaluation as your AI system's **report card**. Without it:
- ❌ You can't prove ROI to stakeholders
- ❌ You don't know if model updates improve or degrade performance
- ❌ You can't catch failures before users do
- ❌ You waste resources on the wrong optimization targets

**Evaluation is not optional—it's the foundation of trustworthy AI.**

### Step 2: The Top Metrics (Pareto 80/20)

The **20% of metrics** you'll use **80% of the time**:

#### For Classification Tasks (e.g., spam detection, fraud detection)

| Metric | When to Use | Formula | What It Means |
|--------|-------------|---------|---------------|
| **Accuracy** | Balanced classes | (TP + TN) / Total | % of correct predictions |
| **Precision** | False positives costly | TP / (TP + FP) | Of predicted positives, % actually positive |
| **Recall** | False negatives costly | TP / (TP + FN) | Of actual positives, % we caught |
| **F1 Score** | Balance precision/recall | 2 × (P × R) / (P + R) | Harmonic mean of P and R |

**Real-world examples**:
- **Spam filter**: High precision (avoid flagging real emails)
- **Cancer screening**: High recall (catch all possible cases)
- **Fraud detection**: F1 score (balance both false alarms and missed fraud)

#### For Regression Tasks (e.g., price prediction, demand forecasting)

| Metric | When to Use | Formula | What It Means |
|--------|-------------|---------|---------------|
| **MAE** | Easy to interpret | Σ\|actual - predicted\| / n | Average absolute error |
| **RMSE** | Penalize large errors | √(Σ(actual - predicted)² / n) | Root mean squared error |
| **R² Score** | Explain variance | 1 - (SS_res / SS_tot) | % of variance explained |

#### For Generative AI (e.g., chatbots, content generation)

| Metric | When to Use | What It Measures |
|--------|-------------|------------------|
| **BLEU** | Translation, summarization | N-gram overlap with reference |
| **ROUGE** | Summarization | Recall-oriented overlap |
| **Perplexity** | Language models | How "surprised" model is |
| **Human Eval** | Nuanced quality | Real user ratings |

### Step 3: Decision Chart for Metric Selection

```
START: What's your AI task?
│
├─ Classification (cat/dog, spam/ham)
│  │
│  ├─ Classes balanced? ───Yes───> Accuracy
│  │
│  └─ Classes imbalanced?
│     │
│     ├─ False Positives costly? ───> Precision
│     ├─ False Negatives costly? ───> Recall
│     └─ Both matter equally? ────> F1 Score
│
├─ Regression (predict price, temperature)
│  │
│  ├─ Need interpretability? ───> MAE
│  ├─ Large errors critical? ───> RMSE
│  └─ Explain variance? ────────> R²
│
└─ Generation (text, images)
   │
   ├─ Translation/Summary? ─────> BLEU/ROUGE
   ├─ Language quality? ────────> Perplexity
   └─ Subjective quality? ──────> Human Evaluation
```

### Step 4: Hands-On Evaluation in Python

Here's a **minimal, reusable evaluation framework**:

```python
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

class AIEvaluator:
    """
    Universal AI evaluation toolkit following Pareto 80/20 principle.
    Covers the vital few metrics for most use cases.
    """
    
    def __init__(self, task_type='classification'):
        """
        Args:
            task_type: 'classification', 'regression', or 'generation'
        """
        self.task_type = task_type
        self.results = {}
    
    # ===== CLASSIFICATION METRICS =====
    
    def evaluate_classification(self, y_true, y_pred, labels=None):
        """
        Evaluate classification model with all key metrics.
        
        Args:
            y_true: Ground truth labels
            y_pred: Predicted labels
            labels: Class names for readable output
        
        Returns:
            dict: All relevant metrics
        """
        self.results = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0)
        }
        
        # Confusion matrix for deeper insights
        cm = confusion_matrix(y_true, y_pred)
        self.results['confusion_matrix'] = cm
        
        return self.results
    
    def plot_confusion_matrix(self, labels=None):
        """Visualize confusion matrix"""
        if 'confusion_matrix' not in self.results:
            raise ValueError("Run evaluate_classification first!")
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.results['confusion_matrix'], annot=True, fmt='d', 
                    cmap='Blues', xticklabels=labels, yticklabels=labels)
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.title('Confusion Matrix')
        plt.show()
    
    # ===== REGRESSION METRICS =====
    
    def evaluate_regression(self, y_true, y_pred):
        """
        Evaluate regression model with key metrics.
        
        Args:
            y_true: Ground truth values
            y_pred: Predicted values
        
        Returns:
            dict: All relevant metrics
        """
        self.results = {
            'mae': mean_absolute_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
            'r2_score': r2_score(y_true, y_pred)
        }
        
        # Prediction error distribution
        errors = y_true - y_pred
        self.results['mean_error'] = np.mean(errors)
        self.results['std_error'] = np.std(errors)
        
        return self.results
    
    def plot_regression_results(self, y_true, y_pred):
        """Visualize regression predictions"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Actual vs Predicted
        axes[0].scatter(y_true, y_pred, alpha=0.5)
        axes[0].plot([y_true.min(), y_true.max()], 
                     [y_true.min(), y_true.max()], 'r--', lw=2)
        axes[0].set_xlabel('Actual Values')
        axes[0].set_ylabel('Predicted Values')
        axes[0].set_title('Actual vs Predicted')
        
        # Residuals
        residuals = y_true - y_pred
        axes[1].scatter(y_pred, residuals, alpha=0.5)
        axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
        axes[1].set_xlabel('Predicted Values')
        axes[1].set_ylabel('Residuals')
        axes[1].set_title('Residual Plot')
        
        plt.tight_layout()
        plt.show()
    
    # ===== REPORTING =====
    
    def print_report(self):
        """Print readable evaluation report"""
        print("\n" + "="*50)
        print(f"📊 EVALUATION REPORT ({self.task_type.upper()})")
        print("="*50 + "\n")
        
        for metric, value in self.results.items():
            if metric != 'confusion_matrix':
                if isinstance(value, float):
                    print(f"{metric.upper():15} : {value:.4f}")
                else:
                    print(f"{metric.upper():15} : {value}")
        
        print("\n" + "="*50)

# ===== USAGE EXAMPLE =====

if __name__ == "__main__":
    # Example: Classification
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    
    # Load data
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Evaluate
    evaluator = AIEvaluator(task_type='classification')
    results = evaluator.evaluate_classification(y_test, y_pred, 
                                                labels=['setosa', 'versicolor', 'virginica'])
    evaluator.print_report()
    evaluator.plot_confusion_matrix(labels=['setosa', 'versicolor', 'virginica'])
```

### Step 5: Common Pitfalls & Solutions

| Pitfall | Why It's Bad | Solution |
|---------|--------------|----------|
| **Using accuracy on imbalanced data** | 95% spam → predict "spam" always = 95% accuracy but useless | Use F1, precision, recall instead |
| **Not using a held-out test set** | Overestimate performance (model saw test data during training) | Always split: train (60%), validation (20%), test (20%) |
| **Ignoring business context** | "95% accuracy!" but the 5% errors cost millions | Map metrics to business outcomes ($ cost per error) |
| **Cherry-picking metrics** | Only report metrics that look good | Report all relevant metrics, discuss tradeoffs |
| **Single-point evaluation** | Evaluate once, assume it's always true | Continuous evaluation on new data |

---

## 🎯 Pareto Principle (20/80 Focus)

### The Vital 20% (Master These)

1. **Know Your Task Type**
   - Classification → Accuracy, Precision, Recall, F1
   - Regression → MAE, RMSE, R²
   - Generation → BLEU, ROUGE, Human Eval

2. **Match Metric to Business Cost**
   - False positives costly → Optimize precision
   - False negatives costly → Optimize recall
   - Both costly → Optimize F1

3. **Always Use Test Set**
   - Never evaluate on training data
   - Split data properly
   - Report honest numbers

### The Impactful 80% (Practice These)

1. **Build Evaluation Pipelines**
   - Automate metric calculation
   - Version control evaluation code
   - Make it repeatable

2. **Visualize Results**
   - Confusion matrices for classification
   - Actual vs. predicted for regression
   - Error distribution analysis

3. **Business Translation**
   - "80% recall" → "We catch 80% of fraud"
   - "RMSE = $500" → "Predictions off by $500 on average"
   - Connect metrics to KPIs

---

## 🛠️ Tools & Technologies

**Essential Libraries:**
- **scikit-learn**: Most common metrics built-in
- **numpy/pandas**: Data manipulation for evaluation
- **matplotlib/seaborn**: Visualization
- **pytest**: Test your evaluation code

**Advanced Tools:**
- **MLflow**: Track experiments and metrics
- **Weights & Biases**: Comprehensive experiment tracking
- **TensorBoard**: Real-time metric visualization
- **Great Expectations**: Data validation for evaluation

**For Production:**
- **Evidently AI**: ML monitoring and drift detection
- **WhyLabs**: Data quality monitoring
- **Arize AI**: Model performance monitoring

---

## 📝 Mini-Exercise: Metric Selection Challenge

**Scenario**: You're building AI systems. Choose the right metric:

1. **Email spam filter for CEO**
   - Cost: False positive (real email to spam) = $1000 in lost opportunity
   - Cost: False negative (spam to inbox) = $1 in annoyance
   - **Choose your metric**: _____________
   - **Why**: _____________

2. **Medical diagnosis assistant**
   - Cost: False positive (flag healthy as sick) = $500 in unnecessary tests
   - Cost: False negative (miss actual disease) = $50,000 in treatment delay
   - **Choose your metric**: _____________
   - **Why**: _____________

3. **Dynamic pricing for hotel rooms**
   - Task: Predict optimal room price
   - Context: Large errors (off by $100+) hurt booking rates
   - **Choose your metric**: _____________
   - **Why**: _____________

**Answers**:
1. **Precision** (minimize false positives)
2. **Recall** (minimize false negatives—can't miss diseases)
3. **RMSE** (penalize large prediction errors more than small ones)

---

## 📚 Resources

See `resources.md` for:
- scikit-learn metrics documentation
- Metric selection decision trees
- Case studies with business impact analysis
- Evaluation best practices guides

---

## ✅ Success Criteria

- [ ] Understand the importance of evaluation in AI projects
- [ ] Can select appropriate metrics for classification, regression, and generation tasks
- [ ] Implement evaluation pipelines in Python
- [ ] Interpret metrics in business context
- [ ] Avoid common evaluation pitfalls
- [ ] Create visualizations for evaluation results

**Track your progress in `progreso.md`**

---

## 🚀 Next Steps

1. Complete the **hands-on exercises** in `actividad-interactiva.md`
2. Evaluate your **capstone project** models (see `project-steps.md`)
3. Review **evaluation criteria** in `retroalimentacion.md`
4. Build a reusable evaluation framework

---

**Ready to evaluate like a pro?** Remember: "You can't improve what you don't measure." Let's make AI evaluation second nature! 📊
