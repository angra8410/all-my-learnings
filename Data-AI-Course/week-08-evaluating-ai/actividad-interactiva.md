# Actividades Interactivas - Week 08: Evaluating AI

## 🎯 Objective

Master AI evaluation through **practical, high-impact exercises** focused on the **Pareto 80/20 principle**: learn the vital few metrics that matter most.

---

## Exercise 1: Classification Metrics Mastery (45 min)

### 🎯 Objective
Implement and interpret the **top 4 classification metrics** (Accuracy, Precision, Recall, F1) that handle 80% of real-world scenarios.

### 📝 Context
You're evaluating a fraud detection model for an e-commerce company. Understanding these metrics determines whether the model ships to production or goes back to training.

### Steps

1. **Setup**
   ```bash
   mkdir week-08-exercise-1
   cd week-08-exercise-1
   ```

2. **Create Evaluation Script**
   
   Save as `fraud_detection_eval.py`:
   ```python
   import numpy as np
   from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   # Simulated fraud detection results
   # 1000 transactions: 50 actual fraud cases (5% - imbalanced!)
   np.random.seed(42)
   
   # Ground truth: 0 = legit, 1 = fraud
   y_true = np.array([0] * 950 + [1] * 50)
   
   # Model predictions (decent but not perfect)
   y_pred = y_true.copy()
   
   # Add some errors
   # Miss 10 fraud cases (false negatives)
   fraud_indices = np.where(y_true == 1)[0]
   missed_fraud = np.random.choice(fraud_indices, 10, replace=False)
   y_pred[missed_fraud] = 0
   
   # Incorrectly flag 20 legit as fraud (false positives)
   legit_indices = np.where(y_true == 0)[0]
   false_alarms = np.random.choice(legit_indices, 20, replace=False)
   y_pred[false_alarms] = 1
   
   # Calculate all metrics
   accuracy = accuracy_score(y_true, y_pred)
   precision = precision_score(y_true, y_pred)
   recall = recall_score(y_true, y_pred)
   f1 = f1_score(y_true, y_pred)
   
   # Confusion matrix
   cm = confusion_matrix(y_true, y_pred)
   tn, fp, fn, tp = cm.ravel()
   
   # Print report
   print("="*60)
   print("FRAUD DETECTION MODEL EVALUATION")
   print("="*60)
   print(f"\n📊 Confusion Matrix:")
   print(f"   True Negatives (Legit→Legit):   {tn:4d}")
   print(f"   False Positives (Legit→Fraud):  {fp:4d} ⚠️")
   print(f"   False Negatives (Fraud→Legit):  {fn:4d} ❌")
   print(f"   True Positives (Fraud→Fraud):   {tp:4d} ✅")
   
   print(f"\n📈 Core Metrics:")
   print(f"   Accuracy:  {accuracy:.2%}  {'✅' if accuracy > 0.95 else '⚠️'}")
   print(f"   Precision: {precision:.2%}  {'✅' if precision > 0.70 else '⚠️'}")
   print(f"   Recall:    {recall:.2%}  {'✅' if recall > 0.80 else '⚠️'}")
   print(f"   F1 Score:  {f1:.2%}  {'✅' if f1 > 0.75 else '⚠️'}")
   
   print(f"\n💡 Business Interpretation:")
   print(f"   • We catch {recall:.0%} of all fraud (Recall)")
   print(f"   • When we flag fraud, we're right {precision:.0%} of the time (Precision)")
   print(f"   • Missing {fn} fraud cases = ${fn * 100:,} in losses (if avg fraud = $100)")
   print(f"   • {fp} false alarms = {fp} customer service calls")
   
   print(f"\n⚖️ Which metric matters most?")
   print(f"   For fraud detection: RECALL > Precision")
   print(f"   Why? Missing fraud (FN) costs more than false alarms (FP)")
   
   # Visualize confusion matrix
   plt.figure(figsize=(8, 6))
   sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
               xticklabels=['Legit', 'Fraud'],
               yticklabels=['Legit', 'Fraud'])
   plt.ylabel('Actual')
   plt.xlabel('Predicted')
   plt.title('Fraud Detection Confusion Matrix')
   plt.savefig('confusion_matrix.png')
   print(f"\n📁 Saved: confusion_matrix.png")
   ```

3. **Run Evaluation**
   ```bash
   python fraud_detection_eval.py
   ```

4. **Business Decision Exercise**
   
   Create `business_decision.md`:
   ```markdown
   # Fraud Detection Model: Ship or Iterate?
   
   ## Current Performance
   - Accuracy: [from output]
   - Precision: [from output]
   - Recall: [from output]
   - F1: [from output]
   
   ## Business Context
   - Average fraud transaction: $100
   - Cost per customer service call (false alarm): $5
   - Monthly transactions: 100,000
   - Expected fraud rate: 5%
   
   ## Cost Analysis
   
   ### Option A: Ship Current Model
   - Missed fraud: ___ cases/month × $100 = $___
   - False alarms: ___ cases/month × $5 = $___
   - **Total monthly cost: $___**
   
   ### Option B: No Model (Manual Review All)
   - Manual review cost: 100,000 × $2 = $200,000/month
   
   ### Option C: Improve Model (Optimize for Recall)
   - Additional development time: 2 weeks
   - Target: 95% recall, accept lower precision
   
   ## My Decision: [A/B/C]
   
   ## Reasoning:
   [Your analysis here]
   
   ## Key Takeaway:
   [What did this teach you about metric selection?]
   ```

### 🎓 Key Takeaway
**Context drives metric choice**: For fraud, missing cases costs more than false alarms → optimize RECALL. For spam email, false alarms (blocking real emails) cost more → optimize PRECISION.

### Validation Checklist
- [ ] Successfully calculated all 4 core metrics
- [ ] Understand the business meaning of each metric
- [ ] Created and interpreted confusion matrix
- [ ] Made data-driven business decision
- [ ] Can explain metric trade-offs

**Duration**: 45 minutes

---

## Exercise 2: Regression Evaluation (40 min)

### 🎯 Objective
Master **MAE, RMSE, and R²**—the vital metrics for regression tasks like price prediction.

### 📝 Context
You're building a house price prediction model. Evaluation determines if it's accurate enough for real estate agents to rely on.

### Steps

1. **Setup**
   ```bash
   mkdir week-08-exercise-2
   cd week-08-exercise-2
   ```

2. **Create Regression Evaluation**
   
   Save as `house_price_eval.py`:
   ```python
   import numpy as np
   from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
   import matplotlib.pyplot as plt
   
   # Simulated house price data (in thousands)
   np.random.seed(42)
   n_samples = 100
   
   # Actual prices: $200k - $800k
   y_true = np.random.uniform(200, 800, n_samples)
   
   # Predictions with some error
   # Model is pretty good but not perfect
   y_pred = y_true + np.random.normal(0, 50, n_samples)  # ±$50k error on average
   
   # Calculate metrics
   mae = mean_absolute_error(y_true, y_pred)
   rmse = np.sqrt(mean_squared_error(y_true, y_pred))
   r2 = r2_score(y_true, y_pred)
   
   # Calculate additional insights
   errors = y_true - y_pred
   mape = np.mean(np.abs(errors / y_true)) * 100  # Mean Absolute Percentage Error
   
   # Print report
   print("="*60)
   print("HOUSE PRICE PREDICTION MODEL EVALUATION")
   print("="*60)
   
   print(f"\n📊 Regression Metrics:")
   print(f"   MAE (Mean Absolute Error):    ${mae:,.2f}k")
   print(f"   RMSE (Root Mean Squared Error): ${rmse:,.2f}k")
   print(f"   R² Score:                      {r2:.4f}")
   print(f"   MAPE (Mean Absolute % Error):  {mape:.2f}%")
   
   print(f"\n💡 What These Mean:")
   print(f"   • MAE: On average, predictions are off by ${mae:,.0f}k")
   print(f"   • RMSE: Typical error is ${rmse:,.0f}k (penalizes big mistakes more)")
   print(f"   • R²: Model explains {r2:.1%} of price variation")
   print(f"   • MAPE: Predictions are off by {mape:.1f}% on average")
   
   print(f"\n✅ Business Acceptance Criteria:")
   print(f"   • MAE < $75k:  {'✅ PASS' if mae < 75 else '❌ FAIL'}")
   print(f"   • RMSE < $100k: {'✅ PASS' if rmse < 100 else '❌ FAIL'}")
   print(f"   • R² > 0.70:   {'✅ PASS' if r2 > 0.70 else '❌ FAIL'}")
   
   # Visualizations
   fig, axes = plt.subplots(1, 2, figsize=(14, 5))
   
   # Actual vs Predicted
   axes[0].scatter(y_true, y_pred, alpha=0.5)
   axes[0].plot([y_true.min(), y_true.max()], 
                [y_true.min(), y_true.max()], 'r--', lw=2, label='Perfect Prediction')
   axes[0].set_xlabel('Actual Price ($k)')
   axes[0].set_ylabel('Predicted Price ($k)')
   axes[0].set_title('Actual vs Predicted House Prices')
   axes[0].legend()
   axes[0].grid(True, alpha=0.3)
   
   # Residuals
   residuals = y_true - y_pred
   axes[1].scatter(y_pred, residuals, alpha=0.5)
   axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
   axes[1].set_xlabel('Predicted Price ($k)')
   axes[1].set_ylabel('Residuals (Actual - Predicted)')
   axes[1].set_title('Residual Plot')
   axes[1].grid(True, alpha=0.3)
   
   plt.tight_layout()
   plt.savefig('regression_evaluation.png')
   print(f"\n📁 Saved: regression_evaluation.png")
   
   # Find worst predictions
   abs_errors = np.abs(errors)
   worst_indices = np.argsort(abs_errors)[-5:]
   
   print(f"\n❌ Top 5 Worst Predictions:")
   for idx in worst_indices:
       print(f"   Actual: ${y_true[idx]:.0f}k, Predicted: ${y_pred[idx]:.0f}k, Error: ${errors[idx]:.0f}k")
   ```

3. **Run Evaluation**
   ```bash
   python house_price_eval.py
   ```

4. **Metric Comparison Exercise**
   
   Answer these questions in `metric_comparison.md`:
   ```markdown
   # Regression Metrics: When to Use Which?
   
   ## Scenario 1: Real Estate Agent Tool
   - Agents need to quote approximate prices to clients
   - Occasional large errors (off by $200k) are acceptable if rare
   - **Best metric**: ___ (MAE / RMSE / R²)
   - **Why**: ___
   
   ## Scenario 2: Automated Bidding System
   - System auto-bids on houses
   - Large errors ($100k+) could cause financial loss
   - Need to heavily penalize big mistakes
   - **Best metric**: ___ (MAE / RMSE / R²)
   - **Why**: ___
   
   ## Scenario 3: Market Analysis Dashboard
   - Showing how well model captures market trends
   - Need to explain variance in prices
   - **Best metric**: ___ (MAE / RMSE / R²)
   - **Why**: ___
   
   ## Answers:
   1. **MAE** - Easy to interpret, robust to outliers
   2. **RMSE** - Penalizes large errors quadratically
   3. **R²** - Shows variance explained, good for trends
   ```

### 🎓 Key Takeaway
**MAE vs RMSE**: Use MAE for interpretability, RMSE when large errors are costly. R² tells you how much of the variance your model explains—closer to 1.0 is better.

### Validation Checklist
- [ ] Calculated MAE, RMSE, and R² correctly
- [ ] Understand what each metric measures
- [ ] Created actual vs. predicted visualization
- [ ] Analyzed residual patterns
- [ ] Know when to use which metric

**Duration**: 40 minutes

---

## Exercise 3: A/B Testing for Model Comparison (35 min)

### 🎯 Objective
Learn to **compare two models** statistically—essential for knowing if your "improvements" actually improve.

### 📝 Context
You have two versions of a recommendation engine. Which one is actually better? Feelings don't count—data does.

### Steps

1. **Create Comparison Framework**
   
   Save as `ab_test_models.py`:
   ```python
   import numpy as np
   from scipy import stats
   import matplotlib.pyplot as plt
   
   # Simulate A/B test results
   np.random.seed(42)
   n_users = 1000
   
   # Model A (baseline): 25% click-through rate
   model_a_results = np.random.binomial(1, 0.25, n_users)
   
   # Model B (new): 28% click-through rate (3% improvement)
   model_b_results = np.random.binomial(1, 0.28, n_users)
   
   # Calculate metrics
   ctr_a = model_a_results.mean()
   ctr_b = model_b_results.mean()
   lift = (ctr_b - ctr_a) / ctr_a * 100
   
   # Statistical significance test
   chi2, p_value = stats.chi2_contingency([
       [model_a_results.sum(), n_users - model_a_results.sum()],
       [model_b_results.sum(), n_users - model_b_results.sum()]
   ])[:2]
   
   # Print report
   print("="*60)
   print("A/B TEST: MODEL COMPARISON")
   print("="*60)
   
   print(f"\n📊 Results:")
   print(f"   Model A (Baseline):  {ctr_a:.2%} CTR")
   print(f"   Model B (New):       {ctr_b:.2%} CTR")
   print(f"   Absolute Lift:       {(ctr_b - ctr_a):.2%}")
   print(f"   Relative Lift:       {lift:.1f}%")
   
   print(f"\n🔬 Statistical Significance:")
   print(f"   P-value: {p_value:.4f}")
   print(f"   Significance Level: α = 0.05")
   
   if p_value < 0.05:
       print(f"   ✅ SIGNIFICANT: Model B is statistically better!")
       print(f"      (p < 0.05 means <5% chance this is random)")
   else:
       print(f"   ❌ NOT SIGNIFICANT: Difference could be random")
       print(f"      (p ≥ 0.05 means ≥5% chance this is luck)")
   
   print(f"\n💡 Business Decision:")
   if p_value < 0.05 and ctr_b > ctr_a:
       print(f"   ✅ SHIP Model B to production")
       print(f"   Expected impact: {lift:.1f}% improvement in recommendations")
   elif p_value < 0.05 and ctr_b < ctr_a:
       print(f"   ❌ Keep Model A (new model is worse)")
   else:
       print(f"   ⚠️ No clear winner - need more data or bigger improvement")
   
   # Calculate required sample size for power
   from statsmodels.stats.power import zt_ind_solve_power
   effect_size = (ctr_b - ctr_a) / np.sqrt(ctr_a * (1 - ctr_a))
   required_n = zt_ind_solve_power(effect_size=effect_size, alpha=0.05, power=0.8)
   
   print(f"\n📏 Sample Size Analysis:")
   print(f"   Current sample: {n_users} users")
   print(f"   Required for 80% power: {int(required_n)} users")
   print(f"   {'✅ Sufficient' if n_users >= required_n else '⚠️ Need more data'}")
   
   # Visualization
   fig, ax = plt.subplots(figsize=(10, 6))
   
   models = ['Model A\n(Baseline)', 'Model B\n(New)']
   ctrs = [ctr_a, ctr_b]
   colors = ['#3498db', '#2ecc71' if ctr_b > ctr_a else '#e74c3c']
   
   bars = ax.bar(models, ctrs, color=colors, alpha=0.7, edgecolor='black')
   ax.set_ylabel('Click-Through Rate')
   ax.set_title(f'Model Comparison (p={p_value:.4f})', fontsize=14)
   ax.set_ylim([0, max(ctrs) * 1.2])
   
   # Add value labels
   for bar, ctr in zip(bars, ctrs):
       height = bar.get_height()
       ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{ctr:.2%}',
               ha='center', va='bottom', fontsize=12, fontweight='bold')
   
   # Add significance indicator
   if p_value < 0.05:
       ax.text(0.5, max(ctrs) * 1.1, '✅ Statistically Significant',
               ha='center', fontsize=11, color='green', fontweight='bold')
   
   plt.tight_layout()
   plt.savefig('ab_test_results.png')
   print(f"\n📁 Saved: ab_test_results.png")
   ```

2. **Run A/B Test**
   ```bash
   python ab_test_models.py
   ```

3. **Decision Framework**
   
   Create `ab_test_checklist.md`:
   ```markdown
   # A/B Testing Decision Checklist
   
   ## Before Running Test
   - [ ] Define success metric (CTR, conversion, revenue, etc.)
   - [ ] Calculate required sample size
   - [ ] Set significance level (α = 0.05 standard)
   - [ ] Decide minimum detectable effect (e.g., 5% lift)
   
   ## During Test
   - [ ] Random assignment of users to A/B groups
   - [ ] No peeking at results mid-test (wait for full sample)
   - [ ] Monitor for data quality issues
   
   ## After Test
   - [ ] Check p-value < 0.05 for significance
   - [ ] Verify practical significance (is lift meaningful?)
   - [ ] Check for segment effects (works for all user types?)
   - [ ] Consider business costs (implementation effort)
   
   ## Decision Rules
   - **p < 0.05 AND lift > 5%**: Ship new model ✅
   - **p < 0.05 BUT lift < 5%**: Maybe ship (low impact)
   - **p ≥ 0.05**: Keep baseline (no proof of improvement)
   ```

### 🎓 Key Takeaway
**Statistical significance matters**: A 3% improvement might look good, but if p-value > 0.05, it could just be random chance. Always test before shipping "improvements."

### Validation Checklist
- [ ] Understand A/B testing fundamentals
- [ ] Can calculate and interpret p-values
- [ ] Know when a result is statistically significant
- [ ] Can make ship/no-ship decisions based on data
- [ ] Understand sample size requirements

**Duration**: 35 minutes

---

## Exercise 4: Evaluating Generative AI (60 min)

### 🎯 Objective
Learn to evaluate **LLM outputs** where traditional metrics don't apply—using BLEU, ROUGE, and human evaluation.

### 📝 Context
You're evaluating a text summarization model. Unlike classification where we have clear right/wrong answers, summarization needs nuanced evaluation.

### Steps

1. **Install Required Libraries**
   ```bash
   pip install rouge-score nltk
   ```

2. **Create Generative Eval Script**
   
   Save as `summarization_eval.py`:
   ```python
   from rouge_score import rouge_scorer
   import nltk
   from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
   import numpy as np
   
   # Download required NLTK data
   nltk.download('punkt', quiet=True)
   
   # Sample article and summaries
   reference_summary = """
   The company reported strong Q3 earnings with revenue up 15% year-over-year.
   Profits exceeded analyst expectations despite challenging market conditions.
   The CEO attributed success to new product launches and cost optimization.
   """
   
   # Model A: Good summary
   model_a_summary = """
   Q3 earnings showed 15% revenue growth, beating expectations.
   New products and cost controls drove the strong performance.
   """
   
   # Model B: Poor summary (misses key info)
   model_b_summary = """
   The company had a good quarter with increased revenue.
   Management was pleased with the results.
   """
   
   # Baseline: Just first sentence (naive approach)
   baseline_summary = """
   The company reported strong Q3 earnings with revenue up 15% year-over-year.
   """
   
   def evaluate_summary(reference, candidate, model_name):
       """Evaluate a summary using ROUGE and BLEU"""
       print(f"\n{'='*60}")
       print(f"EVALUATING: {model_name}")
       print(f"{'='*60}")
       
       # ROUGE scores (Recall-Oriented Understudy for Gisting Evaluation)
       scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
       rouge_scores = scorer.score(reference, candidate)
       
       print(f"\n📊 ROUGE Scores:")
       print(f"   ROUGE-1 (unigram overlap):  {rouge_scores['rouge1'].fmeasure:.3f}")
       print(f"   ROUGE-2 (bigram overlap):   {rouge_scores['rouge2'].fmeasure:.3f}")
       print(f"   ROUGE-L (longest sequence): {rouge_scores['rougeL'].fmeasure:.3f}")
       
       # BLEU score
       reference_tokens = [reference.lower().split()]
       candidate_tokens = candidate.lower().split()
       smoothie = SmoothingFunction().method4
       bleu = sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoothie)
       
       print(f"\n📊 BLEU Score: {bleu:.3f}")
       
       # Overall grade
       avg_rouge = np.mean([s.fmeasure for s in rouge_scores.values()])
       if avg_rouge > 0.5 and bleu > 0.3:
           grade = "✅ EXCELLENT"
       elif avg_rouge > 0.3 and bleu > 0.2:
           grade = "✔️ GOOD"
       elif avg_rouge > 0.2 and bleu > 0.1:
           grade = "⚠️ FAIR"
       else:
           grade = "❌ POOR"
       
       print(f"\n🎯 Overall Grade: {grade}")
       print(f"   Average ROUGE: {avg_rouge:.3f}")
       
       return rouge_scores, bleu
   
   # Evaluate all models
   print("="*60)
   print("SUMMARIZATION MODEL COMPARISON")
   print("="*60)
   
   print(f"\n📄 Reference Summary:\n{reference_summary.strip()}")
   
   results = {}
   results['Model A'] = evaluate_summary(reference_summary, model_a_summary, "Model A")
   results['Model B'] = evaluate_summary(reference_summary, model_b_summary, "Model B")
   results['Baseline'] = evaluate_summary(reference_summary, baseline_summary, "Baseline")
   
   # Final comparison
   print(f"\n{'='*60}")
   print("FINAL COMPARISON")
   print(f"{'='*60}")
   
   for model_name, (rouge_scores, bleu) in results.items():
       avg_rouge = np.mean([s.fmeasure for s in rouge_scores.values()])
       print(f"{model_name:15} | Avg ROUGE: {avg_rouge:.3f} | BLEU: {bleu:.3f}")
   
   print(f"\n💡 Interpretation:")
   print(f"   • ROUGE measures word overlap (higher = better)")
   print(f"   • BLEU measures n-gram precision (higher = better)")
   print(f"   • Both range from 0 (worst) to 1 (perfect)")
   print(f"   • Good summaries typically score > 0.3 on both")
   ```

3. **Run Evaluation**
   ```bash
   python summarization_eval.py
   ```

4. **Human Evaluation Exercise**
   
   Create `human_eval_template.md`:
   ```markdown
   # Human Evaluation Template for LLM Outputs
   
   ## Evaluation Criteria (1-5 scale)
   
   ### 1. Factual Accuracy
   - 5: All facts correct
   - 3: Mostly correct, minor errors
   - 1: Major factual errors
   
   ### 2. Completeness
   - 5: Covers all key points
   - 3: Covers main points, misses some details
   - 1: Misses critical information
   
   ### 3. Coherence
   - 5: Flows naturally, easy to read
   - 3: Understandable but choppy
   - 1: Confusing or disjointed
   
   ### 4. Conciseness
   - 5: No unnecessary words
   - 3: Some redundancy
   - 1: Very verbose
   
   ## Evaluation Sheet
   
   | Model | Accuracy | Completeness | Coherence | Conciseness | Total | Average |
   |-------|----------|--------------|-----------|-------------|-------|---------|
   | Model A | [1-5] | [1-5] | [1-5] | [1-5] | [sum] | [avg] |
   | Model B | [1-5] | [1-5] | [1-5] | [1-5] | [sum] | [avg] |
   | Baseline | [1-5] | [1-5] | [1-5] | [1-5] | [sum] | [avg] |
   
   ## Winner: [Model Name]
   
   ## Reasoning:
   [Explain why this model is best for production]
   
   ## Key Insight:
   [What did you learn about automated vs. human evaluation?]
   ```

### 🎓 Key Takeaway
**Generative AI needs multi-metric evaluation**: ROUGE/BLEU for automated benchmarking, human eval for nuanced quality. No single metric captures everything.

### Validation Checklist
- [ ] Calculated ROUGE and BLEU scores
- [ ] Understand what these metrics measure
- [ ] Completed human evaluation exercise
- [ ] Know when automated metrics aren't enough
- [ ] Can design comprehensive evaluation frameworks

**Duration**: 60 minutes

---

## 📋 Final Checklist

- [ ] **Exercise 1**: Classification metrics (Accuracy, Precision, Recall, F1) ✅
- [ ] **Exercise 2**: Regression metrics (MAE, RMSE, R²) ✅
- [ ] **Exercise 3**: A/B testing and statistical significance ✅
- [ ] **Exercise 4**: Generative AI evaluation (ROUGE, BLEU, Human Eval) ✅

**Total Time**: ~3 hours (Pareto-optimized!)

---

## 🎉 Congratulations!

You've mastered the **vital 20%** of AI evaluation that covers **80% of real-world scenarios**:

✅ Classification: Accuracy, Precision, Recall, F1  
✅ Regression: MAE, RMSE, R²  
✅ A/B Testing: Statistical significance  
✅ Generative AI: ROUGE, BLEU, Human Eval  

**Next Steps**:
1. Apply these to your **capstone project** (`project-steps.md`)
2. Track progress in `progreso.md`
3. Review feedback in `retroalimentacion.md`

**You can now evaluate any AI system with confidence!** 📊🚀
