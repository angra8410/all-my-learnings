# Week 12: Automation Models

## 🤖 Persona: Intelligent Automation Engineer

*Welcome! I'm your automation engineering expert who champions simple, scalable models for workflow automation. I've helped dozens of companies save thousands of hours through strategic automation. My approach: start small, prove value fast, scale smartly. Let's automate your way to efficiency!*

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Identify high-ROI automation opportunities** using the Pareto Principle
2. **Choose the right automation model** (rule-based vs. ML-based) for your use case
3. **Build and deploy a working automation** with minimal code
4. **Measure automation impact** (time saved, error reduction, cost benefits)
5. **Scale automation** from proof-of-concept to production

**Estimated Duration**: 4-5 hours of focused, high-impact learning

## 📋 Prerequisites

- Completed weeks 1-11 (especially Week 06: Agentic AI)
- Python environment with pandas, scikit-learn
- Basic understanding of business processes
- API access (OpenAI/Anthropic) configured

---

## 🧠 Chain of Thought: Why Automation Models Matter

Let me walk you through the reasoning:

### Step 1: Understanding the Business Case
**The Problem**: 
- Manual, repetitive tasks consume 40-60% of knowledge worker time
- Human error rates in manual processes: 1-5%
- Cost: $25-50/hour per person doing manual work

**The Opportunity**:
- Automation can handle 70-80% of repetitive tasks
- Error rates drop to <0.1% with proper automation
- ROI: 3-10x within 6-12 months

### Step 2: Automation Model Types (Pareto Focus)

**80% of automation value comes from 20% of model types:**

1. **Rule-Based Automation** (60% of use cases)
   - If-then logic
   - Decision trees
   - Business rules engines
   - **Best for**: Structured, predictable processes

2. **Supervised ML Automation** (30% of use cases)
   - Classification models
   - Prediction models
   - Pattern recognition
   - **Best for**: Pattern-based decisions with historical data

3. **Hybrid Automation** (10% of use cases)
   - Rules + ML
   - Human-in-the-loop
   - **Best for**: Complex processes requiring both logic and learning

### Step 3: The Automation Decision Framework

```
START → Is process repetitive? 
         ↓ Yes
       → Is logic clear/simple?
         ↓ Yes → RULE-BASED AUTOMATION
         ↓ No
       → Do you have historical data?
         ↓ Yes → ML-BASED AUTOMATION
         ↓ No → HYBRID (start with rules, add ML later)
```

---

## 🎯 Pareto Principle (20/80 Rule): Focus on What Matters

### 20% Core Skills That Deliver 80% Results

#### 1. **Opportunity Identification** (Most Critical)
Learn to spot automation gold:
- **High-volume tasks**: Done >10 times/day
- **Time-consuming**: Takes >15 minutes each time
- **Error-prone**: Human mistakes happen
- **Rule-based**: Clear decision logic

**Quick Assessment Template:**
```python
# Automation Opportunity Score
score = (frequency_per_day * time_minutes * error_rate) / complexity_level

# Example:
# Task: Email classification
frequency = 50        # 50 emails/day
time = 3              # 3 min each
error_rate = 0.05     # 5% misclassified
complexity = 2        # Low complexity (1-5 scale)

opportunity_score = (50 * 3 * 0.05) / 2 = 3.75
# Score > 2.0 → Strong automation candidate
```

#### 2. **Model Selection** (Critical)
Choose the simplest model that works:

```python
def select_automation_model(use_case):
    """
    Decision tree for automation model selection
    """
    # Check if rules are clear and fixed
    if use_case.has_clear_rules and use_case.rules_dont_change_often:
        return "RULE_BASED"
    
    # Check if you have training data
    elif use_case.has_historical_data and use_case.data_size > 1000:
        return "ML_BASED"
    
    # Check complexity
    elif use_case.requires_human_judgment:
        return "HYBRID"
    
    else:
        return "START_WITH_RULES_ADD_ML_LATER"
```

#### 3. **Rapid Prototyping** (Critical)
Build a working proof-of-concept in <2 hours:

```python
# Example: Email Priority Classification (Rule-Based)
import re

class EmailPriorityAutomation:
    """Simple rule-based email prioritization"""
    
    def __init__(self):
        # Define high-priority keywords
        self.urgent_keywords = ['urgent', 'asap', 'critical', 'emergency']
        self.vip_senders = ['ceo@company.com', 'boss@company.com']
        
    def classify_priority(self, email):
        """
        Chain of Thought: Step-by-step priority assessment
        """
        # Step 1: Check sender
        if email['from'] in self.vip_senders:
            return 'HIGH', 'VIP sender'
        
        # Step 2: Check subject for urgent keywords
        subject_lower = email['subject'].lower()
        if any(keyword in subject_lower for keyword in self.urgent_keywords):
            return 'HIGH', 'Urgent keyword in subject'
        
        # Step 3: Check body for urgent keywords
        body_lower = email['body'].lower()
        urgent_count = sum(1 for kw in self.urgent_keywords if kw in body_lower)
        if urgent_count >= 2:
            return 'MEDIUM', f'{urgent_count} urgent keywords in body'
        
        # Step 4: Default to normal
        return 'LOW', 'No urgent indicators'
    
    def automate_action(self, email, priority, reason):
        """Take automated action based on priority"""
        actions = {
            'HIGH': 'Notify immediately + Flag + Move to top',
            'MEDIUM': 'Flag for review within 1 hour',
            'LOW': 'Regular inbox processing'
        }
        return actions[priority]

# Usage Example
automation = EmailPriorityAutomation()

sample_email = {
    'from': 'customer@example.com',
    'subject': 'URGENT: System Down',
    'body': 'Our production system is critical and needs immediate attention'
}

priority, reason = automation.classify_priority(sample_email)
action = automation.automate_action(sample_email, priority, reason)

print(f"Priority: {priority}")
print(f"Reason: {reason}")
print(f"Action: {action}")
# Output:
# Priority: HIGH
# Reason: Urgent keyword in subject
# Action: Notify immediately + Flag + Move to top
```

---

## 🛠️ Practical Automation Patterns

### Pattern 1: Data Validation Automation

**Use Case**: Validate 1000s of records automatically

```python
import pandas as pd
from typing import List, Dict

class DataValidationAutomation:
    """Automate data quality checks"""
    
    def __init__(self, validation_rules: Dict):
        """
        validation_rules = {
            'email': {'pattern': r'^[\w\.-]+@[\w\.-]+\.\w+$'},
            'age': {'min': 0, 'max': 120},
            'country': {'allowed_values': ['USA', 'UK', 'CA']}
        }
        """
        self.rules = validation_rules
        self.errors = []
    
    def validate_record(self, record: Dict) -> bool:
        """Validate single record against all rules"""
        is_valid = True
        
        for field, rules in self.rules.items():
            if field not in record:
                self.errors.append(f"Missing field: {field}")
                is_valid = False
                continue
            
            value = record[field]
            
            # Pattern validation
            if 'pattern' in rules:
                import re
                if not re.match(rules['pattern'], str(value)):
                    self.errors.append(f"Invalid {field}: {value}")
                    is_valid = False
            
            # Range validation
            if 'min' in rules and value < rules['min']:
                self.errors.append(f"{field} below minimum: {value}")
                is_valid = False
            
            if 'max' in rules and value > rules['max']:
                self.errors.append(f"{field} above maximum: {value}")
                is_valid = False
            
            # Allowed values validation
            if 'allowed_values' in rules and value not in rules['allowed_values']:
                self.errors.append(f"Invalid {field} value: {value}")
                is_valid = False
        
        return is_valid
    
    def validate_batch(self, records: List[Dict]) -> Dict:
        """Validate batch of records - return summary"""
        results = {
            'total': len(records),
            'valid': 0,
            'invalid': 0,
            'errors': []
        }
        
        for i, record in enumerate(records):
            self.errors = []
            if self.validate_record(record):
                results['valid'] += 1
            else:
                results['invalid'] += 1
                results['errors'].append({
                    'record_id': i,
                    'errors': self.errors.copy()
                })
        
        return results

# Example Usage
validation_rules = {
    'email': {'pattern': r'^[\w\.-]+@[\w\.-]+\.\w+$'},
    'age': {'min': 18, 'max': 100},
    'country': {'allowed_values': ['USA', 'UK', 'CA', 'AU']}
}

validator = DataValidationAutomation(validation_rules)

test_data = [
    {'email': 'john@example.com', 'age': 25, 'country': 'USA'},
    {'email': 'invalid-email', 'age': 25, 'country': 'USA'},
    {'email': 'jane@example.com', 'age': 150, 'country': 'FR'},
]

results = validator.validate_batch(test_data)
print(f"Valid records: {results['valid']}/{results['total']}")
print(f"Invalid records: {results['invalid']}")
# Saved time: 30 seconds per record × 1000 records = 8.3 hours!
```

### Pattern 2: Document Classification (ML-Based)

**Use Case**: Classify documents into categories automatically

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

class DocumentClassificationAutomation:
    """Simple ML-based document classifier"""
    
    def __init__(self):
        # Create a simple pipeline (Pareto: 80% accuracy with minimal code)
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000)),  # Focus on top 1000 words
            ('classifier', MultinomialNB())
        ])
        self.categories = []
    
    def train(self, documents: List[str], categories: List[str]):
        """Train on historical data"""
        self.categories = list(set(categories))
        self.pipeline.fit(documents, categories)
        print(f"✓ Trained on {len(documents)} documents")
        print(f"✓ Categories: {self.categories}")
    
    def classify(self, document: str) -> Dict:
        """Classify new document"""
        prediction = self.pipeline.predict([document])[0]
        probabilities = self.pipeline.predict_proba([document])[0]
        confidence = max(probabilities)
        
        return {
            'category': prediction,
            'confidence': confidence,
            'all_probabilities': dict(zip(self.categories, probabilities))
        }
    
    def save_model(self, filepath: str):
        """Save trained model for reuse"""
        joblib.dump(self.pipeline, filepath)
        print(f"✓ Model saved to {filepath}")
    
    def load_model(self, filepath: str):
        """Load pre-trained model"""
        self.pipeline = joblib.load(filepath)
        print(f"✓ Model loaded from {filepath}")

# Example: Train on sample documents
training_docs = [
    "Please send invoice for last month's services",
    "Invoice #12345 attached for payment",
    "Can you schedule a meeting for next Tuesday?",
    "Let's meet to discuss the project timeline",
    "The system is experiencing critical errors",
    "Bug report: Application crashes on startup",
]

training_categories = [
    "invoice", "invoice", "meeting", "meeting", "support", "support"
]

# Train the automation
classifier = DocumentClassificationAutomation()
classifier.train(training_docs, training_categories)

# Classify new documents
new_doc = "Please process the attached invoice for April"
result = classifier.classify(new_doc)

print(f"\nDocument: {new_doc}")
print(f"Category: {result['category']}")
print(f"Confidence: {result['confidence']:.2%}")
# Time saved: 2 minutes per document × 500 docs/day = 16.6 hours/day!
```

### Pattern 3: Workflow Automation (Hybrid)

**Use Case**: Automate approval workflows with escalation

```python
from datetime import datetime, timedelta
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class WorkflowAutomation:
    """Hybrid automation: Rules + ML + Human-in-loop"""
    
    def __init__(self, ml_classifier=None):
        self.ml_classifier = ml_classifier
        self.approval_rules = {
            'amount': {
                'under_1000': 'auto_approve',
                'under_10000': 'manager_approval',
                'over_10000': 'director_approval'
            }
        }
    
    def process_request(self, request: Dict) -> Dict:
        """
        Chain of Thought: Multi-step request processing
        """
        result = {
            'request_id': request['id'],
            'decision': None,
            'reason': None,
            'action': None,
            'requires_human': False
        }
        
        # Step 1: Extract and classify using ML (if available)
        if self.ml_classifier and 'description' in request:
            classification = self.ml_classifier.classify(request['description'])
            request['auto_category'] = classification['category']
            request['confidence'] = classification['confidence']
        
        # Step 2: Apply business rules
        amount = request.get('amount', 0)
        
        if amount < 1000:
            result['decision'] = 'APPROVED'
            result['reason'] = 'Below auto-approval threshold'
            result['action'] = 'Process immediately'
            
        elif amount < 10000:
            result['decision'] = 'PENDING'
            result['reason'] = 'Requires manager approval'
            result['action'] = 'Route to manager'
            result['requires_human'] = True
            result['approver'] = 'manager'
            
        else:
            result['decision'] = 'PENDING'
            result['reason'] = 'High value - requires director approval'
            result['action'] = 'Route to director'
            result['requires_human'] = True
            result['approver'] = 'director'
            result['priority'] = Priority.HIGH
        
        # Step 3: Check for exceptions
        if request.get('expedited', False):
            result['priority'] = Priority.CRITICAL
            result['action'] += ' + Notify approver immediately'
        
        return result
    
    def generate_report(self, processed_requests: List[Dict]) -> Dict:
        """Measure automation impact"""
        total = len(processed_requests)
        auto_approved = sum(1 for r in processed_requests if r['decision'] == 'APPROVED')
        requires_human = sum(1 for r in processed_requests if r['requires_human'])
        
        # Calculate time saved
        avg_manual_time = 5  # minutes per request
        auto_time = 0.1  # seconds per automated request
        time_saved_minutes = (auto_approved * avg_manual_time) - (auto_approved * auto_time / 60)
        
        return {
            'total_requests': total,
            'auto_approved': auto_approved,
            'auto_approval_rate': auto_approved / total if total > 0 else 0,
            'requires_human': requires_human,
            'time_saved_hours': time_saved_minutes / 60,
            'estimated_cost_saved': time_saved_minutes / 60 * 50  # $50/hour
        }

# Example Usage
workflow = WorkflowAutomation()

requests = [
    {'id': 1, 'amount': 500, 'description': 'Office supplies'},
    {'id': 2, 'amount': 5000, 'description': 'Software licenses'},
    {'id': 3, 'amount': 50000, 'description': 'Equipment purchase', 'expedited': True},
]

processed = [workflow.process_request(req) for req in requests]

for p in processed:
    print(f"Request {p['request_id']}: {p['decision']} - {p['reason']}")

report = workflow.generate_report(processed)
print(f"\n📊 Automation Report:")
print(f"Auto-approval rate: {report['auto_approval_rate']:.1%}")
print(f"Time saved: {report['time_saved_hours']:.1f} hours")
print(f"Cost saved: ${report['estimated_cost_saved']:.2f}")
```

---

## 🎯 Mini-Project: Build Your First Automation

**Goal**: Automate a basic process and measure impact in <60 minutes

### Project: Email Response Time Analyzer & Auto-Prioritizer

```python
import pandas as pd
from datetime import datetime, timedelta
import random

class EmailAutomation:
    """Complete automation example combining all patterns"""
    
    def __init__(self):
        self.priority_classifier = None
        self.response_times = []
    
    def analyze_historical_data(self, emails: pd.DataFrame):
        """Learn from historical patterns"""
        # Calculate average response times by category
        emails['response_time_hours'] = (
            pd.to_datetime(emails['response_time']) - 
            pd.to_datetime(emails['received_time'])
        ).dt.total_seconds() / 3600
        
        summary = emails.groupby('category').agg({
            'response_time_hours': ['mean', 'median', 'std']
        })
        
        print("📊 Historical Response Times by Category:")
        print(summary)
        return summary
    
    def auto_prioritize_new_emails(self, new_emails: List[Dict]):
        """Automatically prioritize incoming emails"""
        for email in new_emails:
            # Rule-based prioritization
            priority_score = 0
            
            # Factor 1: Sender importance
            if 'vip' in email.get('tags', []):
                priority_score += 3
            
            # Factor 2: Subject urgency
            urgent_words = ['urgent', 'critical', 'asap', 'emergency']
            if any(word in email['subject'].lower() for word in urgent_words):
                priority_score += 2
            
            # Factor 3: Time sensitivity
            if 'deadline' in email['body'].lower():
                priority_score += 1
            
            # Assign priority
            if priority_score >= 4:
                email['priority'] = 'CRITICAL'
                email['sla_hours'] = 1
            elif priority_score >= 2:
                email['priority'] = 'HIGH'
                email['sla_hours'] = 4
            else:
                email['priority'] = 'NORMAL'
                email['sla_hours'] = 24
            
            email['auto_action'] = self._get_auto_action(email)
        
        return new_emails
    
    def _get_auto_action(self, email: Dict) -> str:
        """Determine automated action"""
        if email['priority'] == 'CRITICAL':
            return 'Alert on-call team + Create ticket + Flag for immediate response'
        elif email['priority'] == 'HIGH':
            return 'Create ticket + Notify assigned person'
        else:
            return 'Add to queue for regular processing'
    
    def generate_automation_report(self, before_automation: Dict, after_automation: Dict):
        """Measure automation impact"""
        print("\n" + "="*50)
        print("🚀 AUTOMATION IMPACT REPORT")
        print("="*50)
        
        # Time savings
        time_saved = before_automation['avg_response_hours'] - after_automation['avg_response_hours']
        improvement_pct = (time_saved / before_automation['avg_response_hours']) * 100
        
        print(f"\n⏱️  Response Time:")
        print(f"   Before: {before_automation['avg_response_hours']:.1f} hours")
        print(f"   After:  {after_automation['avg_response_hours']:.1f} hours")
        print(f"   Improvement: {time_saved:.1f} hours ({improvement_pct:.1f}%)")
        
        # Error reduction
        error_reduction = before_automation['error_rate'] - after_automation['error_rate']
        print(f"\n❌ Error Rate:")
        print(f"   Before: {before_automation['error_rate']:.1%}")
        print(f"   After:  {after_automation['error_rate']:.1%}")
        print(f"   Reduction: {error_reduction:.1%}")
        
        # Cost savings
        manual_hours = before_automation['manual_hours_per_day']
        automated_hours = after_automation['manual_hours_per_day']
        hourly_cost = 50
        daily_savings = (manual_hours - automated_hours) * hourly_cost
        
        print(f"\n💰 Cost Savings:")
        print(f"   Manual hours saved per day: {manual_hours - automated_hours:.1f}")
        print(f"   Daily cost savings: ${daily_savings:.2f}")
        print(f"   Monthly cost savings: ${daily_savings * 20:.2f}")
        print(f"   Annual cost savings: ${daily_savings * 250:.2f}")
        
        print("\n" + "="*50)

# Run the mini-project
automation = EmailAutomation()

# Simulate "before automation" metrics
before = {
    'avg_response_hours': 8.5,
    'error_rate': 0.05,
    'manual_hours_per_day': 4
}

# Simulate "after automation" metrics
after = {
    'avg_response_hours': 2.1,
    'error_rate': 0.005,
    'manual_hours_per_day': 1
}

automation.generate_automation_report(before, after)
```

**Expected Output:**
```
==================================================
🚀 AUTOMATION IMPACT REPORT
==================================================

⏱️  Response Time:
   Before: 8.5 hours
   After:  2.1 hours
   Improvement: 6.4 hours (75.3%)

❌ Error Rate:
   Before: 5.0%
   After:  0.5%
   Reduction: 4.5%

💰 Cost Savings:
   Manual hours saved per day: 3.0
   Daily cost savings: $150.00
   Monthly cost savings: $3000.00
   Annual cost savings: $37500.00

==================================================
```

---

## ✅ Automation Evaluation Checklist

Use this to evaluate any automation opportunity:

### 1. Opportunity Assessment
- [ ] Task is performed >10 times per week
- [ ] Task takes >10 minutes each time
- [ ] Process is clearly defined and documented
- [ ] Success criteria are measurable
- [ ] Stakeholders support automation

### 2. Model Selection
- [ ] Rule logic is clear → Use rule-based
- [ ] Historical data available (>1000 examples) → Consider ML
- [ ] Human judgment required → Design hybrid
- [ ] Start simple, add complexity only if needed

### 3. Implementation
- [ ] Build proof-of-concept in <2 hours
- [ ] Test with small batch first (10-50 items)
- [ ] Measure baseline metrics (time, accuracy, cost)
- [ ] Implement error handling and logging
- [ ] Create rollback plan

### 4. Validation
- [ ] Accuracy meets target (>95% for most use cases)
- [ ] Speed improvement >50%
- [ ] Cost savings >$1000/month
- [ ] User acceptance achieved
- [ ] Monitoring in place

### 5. Scale & Maintain
- [ ] Document automation logic and dependencies
- [ ] Set up alerting for failures
- [ ] Schedule regular reviews (monthly)
- [ ] Plan for edge cases and exceptions
- [ ] Continuously optimize based on data

---

## 📚 Key Takeaways (Pareto Summary)

### The Vital 20% You Must Remember:

1. **Focus on high-frequency, time-consuming tasks first** - That's where the ROI is
2. **Start with rule-based automation** - It's simpler and covers 60% of use cases
3. **Measure everything** - Before metrics, after metrics, cost savings, time savings
4. **Ship fast, iterate faster** - 2-hour proof-of-concept beats 2-week perfect solution
5. **Always have a human fallback** - Automation augments, not replaces

### Quick Decision Guide:
```
Clear rules + No data needed → RULE-BASED (start today!)
Historical data + Patterns → ML-BASED (1-2 weeks)
Complex + Judgment needed → HYBRID (2-4 weeks)
```

---

## 🚀 What's Next

1. **Complete exercises** in `actividad-interactiva.md` (hands-on automation builds)
2. **Integrate into capstone** in `project-steps.md` (add automation to your projects)
3. **Track progress** in `progreso.md`
4. **Get feedback** in `retroalimentacion.md`

**Next Week**: Week 13 - Orchestration & Production (taking your automations to production scale!)

---

**Time to automate! Let's turn those repetitive tasks into automated workflows.** 🤖🚀
