# Week 11: Ethical AI

## 🧭 Your Expert Persona

**You are an ethical AI facilitator** who guides learners through critical thinking, balancing responsibility with actionability. You believe AI ethics isn't just philosophy—it's practical decisions we make every day that impact real people.

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Understand core ethical principles** for AI (fairness, transparency, accountability)
2. **Detect and mitigate bias** in AI systems
3. **Implement fairness metrics** and auditing processes
4. **Apply privacy-preserving techniques** 
5. **Make ethically-informed decisions** in AI projects

**Estimated Duration**: 4-5 hours

---

## 🧠 Chain of Thought: Understanding AI Ethics

### Step 1: Why Ethics Matters in AI

**The harsh reality**: Unethical AI causes real harm.

Real-world examples:
- **Hiring algorithms** that discriminate against women
- **Credit scoring models** that perpetuate racial bias
- **Healthcare AI** that works worse for minorities
- **Facial recognition** with accuracy gaps across demographics

**Ethics isn't optional—it's:**
- 🏛️ **Legal requirement** (GDPR, AI Act, anti-discrimination laws)
- 💰 **Business imperative** (reputation, lawsuits, customer trust)
- ✅ **Engineering standard** (like security and testing)

### Step 2: Core Ethical Principles (Pareto 80/20)

The **20% of principles** that guide **80% of ethical decisions**:

#### 1. **Fairness** (35% of ethical issues)

**What it means**: AI treats all groups equitably.

**Types of fairness**:
- **Demographic parity**: Same approval rate across groups
- **Equal opportunity**: Same true positive rate across groups
- **Equalized odds**: Same TPR and FPR across groups

#### 2. **Transparency** (25% of ethical issues)

**What it means**: Stakeholders understand how AI makes decisions.

**Levels of transparency**:
- **Explainability**: "Why did the model make this decision?"
- **Interpretability**: "How does the model work overall?"
- **Disclosure**: "Is AI being used? How?"

#### 3. **Accountability** (20% of ethical issues)

**What it means**: Someone is responsible for AI decisions.

**Key questions**:
- Who is responsible when AI makes a mistake?
- How can affected people appeal decisions?
- What oversight exists?

#### 4. **Privacy** (20% of ethical issues)

**What it means**: Protecting user data and preventing surveillance.

**Privacy techniques**:
- **Data minimization**: Collect only what's needed
- **Anonymization**: Remove PII
- **Differential privacy**: Add noise to protect individuals
- **Federated learning**: Train without centralizing data

### Step 3: Practical Bias Detection Framework

```python
def audit_model_fairness(df, sensitive_attr, pred_col, true_col):
    """
    Audit AI model for bias across demographic groups.
    Returns key fairness metrics.
    """
    results = {}
    
    # Demographic Parity: P(Y_hat=1 | A=0) ≈ P(Y_hat=1 | A=1)
    for group in df[sensitive_attr].unique():
        group_df = df[df[sensitive_attr] == group]
        positive_rate = (group_df[pred_col] == 1).mean()
        results[f'{group}_positive_rate'] = positive_rate
    
    # Equal Opportunity: TPR should be same across groups
    for group in df[sensitive_attr].unique():
        group_df = df[df[sensitive_attr] == group]
        actual_positives = group_df[group_df[true_col] == 1]
        if len(actual_positives) > 0:
            tpr = (actual_positives[pred_col] == 1).mean()
            results[f'{group}_tpr'] = tpr
    
    # Disparate Impact Ratio (should be > 0.8)
    rates = [v for k, v in results.items() if 'positive_rate' in k]
    di_ratio = min(rates) / max(rates) if max(rates) > 0 else 1.0
    results['disparate_impact_ratio'] = di_ratio
    results['passes_80_rule'] = di_ratio >= 0.8
    
    return results
```

### Step 4: Bias Mitigation Strategies

**Pre-processing** (Fix the data):
- Re-sample to balance representation
- Re-weight to give more weight to underrepresented groups
- Remove biased features

**In-processing** (Fix during training):
- Add fairness constraints to optimization
- Use fairness-aware algorithms
- Apply adversarial debiasing

**Post-processing** (Fix the outputs):
- Adjust decision thresholds per group
- Calibrate predictions
- Apply equalized odds post-processing

### Step 5: Practical Ethics Checklist

**Before Training:**
- [ ] Diverse, representative training data
- [ ] No PII unless absolutely necessary
- [ ] Documented data sources and collection methods
- [ ] Consent obtained for data use

**During Development:**
- [ ] Bias audit on validation set
- [ ] Fairness metrics tracked alongside accuracy
- [ ] Model explainability implemented
- [ ] Edge cases tested (especially for minorities)

**Before Deployment:**
- [ ] Final bias audit completed
- [ ] Stakeholder review (include affected communities)
- [ ] Appeal/recourse process defined
- [ ] Monitoring plan for ongoing fairness

**In Production:**
- [ ] Regular bias audits (monthly/quarterly)
- [ ] Feedback mechanism for users
- [ ] Incident response plan for ethical issues
- [ ] Documented accountability structure

---

## 🎯 Pareto Principle (20/80 Focus)

### The Vital 20% (Master These)

1. **Bias Detection**
   - Measure demographic parity
   - Calculate equal opportunity
   - Compute disparate impact ratio

2. **Explainability**
   - Provide reasons for decisions
   - Show top features
   - Enable human understanding

3. **Privacy Basics**
   - Data minimization
   - Anonymization
   - Secure storage

### The Impactful 80% (Practice These)

1. **Regular Audits**
   - Bias audits before and after deployment
   - Continuous monitoring
   - Stakeholder feedback

2. **Transparency by Default**
   - Document model decisions
   - Disclose AI use
   - Explain outcomes

3. **Inclusive Design**
   - Test on diverse populations
   - Involve affected communities
   - Design for edge cases

---

## 🛠️ Tools & Technologies

**Bias Detection & Mitigation:**
- **Fairlearn**: Microsoft's fairness toolkit
- **AI Fairness 360**: IBM's comprehensive toolkit
- **What-If Tool**: Google's model analysis
- **Aequitas**: Bias audit toolkit

**Explainability:**
- **SHAP**: SHapley Additive exPlanations
- **LIME**: Local Interpretable Model-agnostic Explanations
- **InterpretML**: Microsoft's interpretability library
- **ELI5**: Simple Python explainability

**Privacy:**
- **Opacus**: PyTorch differential privacy
- **PySyft**: Federated learning framework
- **TensorFlow Privacy**: Privacy-preserving ML
- **ARX**: Data anonymization tool

---

## 📚 Resources

See `resources.md` for:
- NIST AI Risk Management Framework
- EU AI Act requirements
- Academic papers on fairness
- Case studies of AI ethics failures

---

## ✅ Success Criteria

- [ ] Understand core ethical principles (fairness, transparency, accountability, privacy)
- [ ] Can detect bias using multiple fairness metrics
- [ ] Implemented bias mitigation strategy
- [ ] Added explainability to model outputs
- [ ] Completed ethics checklist for a project
- [ ] Know when to escalate ethical concerns

**Track your progress in `progreso.md`**

---

## 🚀 Next Steps

1. Complete **ethics exercises** in `actividad-interactiva.md`
2. Ethics audit of your **capstone project** (see `project-steps.md`)
3. Review criteria in `retroalimentacion.md`
4. Join AI ethics communities

---

**Ready to build responsible AI?** Ethics isn't a checkbox—it's a mindset and a practice. The decisions we make today shape the AI-powered world of tomorrow. Let's get it right! 🌍
