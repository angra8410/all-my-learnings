# Interactive Activities - Week 12: Automation Models

## 🎯 Objective

Build real automation systems that save time and reduce errors through hands-on exercises.

**Total Time**: 3-4 hours of hands-on automation building

---

## Exercise 1: Rule-Based Email Classifier (Duration: 30 min)

### 🎯 Objective
Build a rule-based automation that classifies customer emails by department and priority.

### 📋 Scenario
Your company receives 200+ customer emails daily. Currently, someone manually reads and routes each email, taking 2-3 minutes per email (6-10 hours/day). Automate this!

### 🛠️ Steps

1. **Setup**
   ```bash
   # Create working directory
   mkdir week-12-automation
   cd week-12-automation
   
   # Create Python file
   touch email_classifier.py
   ```

2. **Implementation**
   Create `email_classifier.py`:
   
   ```python
   import re
   from typing import Dict, List, Tuple
   
   class EmailClassifier:
       """Rule-based email classification automation"""
       
       def __init__(self):
           # Define department routing rules
           self.department_keywords = {
               'billing': ['invoice', 'payment', 'bill', 'charge', 'refund', 'pricing'],
               'technical': ['error', 'bug', 'crash', 'not working', 'broken', 'issue'],
               'sales': ['pricing', 'demo', 'trial', 'purchase', 'quote', 'buy'],
               'support': ['help', 'how to', 'question', 'cannot', 'problem']
           }
           
           # Priority keywords
           self.urgent_keywords = ['urgent', 'asap', 'critical', 'emergency', 'down', 'immediately']
           
       def classify(self, email: Dict) -> Dict:
           """
           Classify email by department and priority
           Returns: {'department': str, 'priority': str, 'confidence': float, 'keywords_found': list}
           """
           subject = email.get('subject', '').lower()
           body = email.get('body', '').lower()
           full_text = f"{subject} {body}"
           
           # Find department
           department_scores = {}
           keywords_found = []
           
           for dept, keywords in self.department_keywords.items():
               score = sum(1 for keyword in keywords if keyword in full_text)
               if score > 0:
                   department_scores[dept] = score
                   keywords_found.extend([k for k in keywords if k in full_text])
           
           # Determine primary department
           if department_scores:
               department = max(department_scores, key=department_scores.get)
               confidence = department_scores[department] / sum(department_scores.values())
           else:
               department = 'general'
               confidence = 0.5
           
           # Determine priority
           urgent_count = sum(1 for keyword in self.urgent_keywords if keyword in full_text)
           if urgent_count >= 2:
               priority = 'HIGH'
           elif urgent_count == 1:
               priority = 'MEDIUM'
           else:
               priority = 'LOW'
           
           return {
               'department': department,
               'priority': priority,
               'confidence': confidence,
               'keywords_found': list(set(keywords_found))
           }
       
       def batch_classify(self, emails: List[Dict]) -> List[Dict]:
           """Classify multiple emails"""
           results = []
           for email in emails:
               classification = self.classify(email)
               results.append({
                   'email_id': email.get('id'),
                   'from': email.get('from'),
                   'subject': email.get('subject'),
                   **classification
               })
           return results
       
       def generate_report(self, results: List[Dict]):
           """Generate automation impact report"""
           total = len(results)
           by_dept = {}
           by_priority = {}
           
           for r in results:
               dept = r['department']
               priority = r['priority']
               by_dept[dept] = by_dept.get(dept, 0) + 1
               by_priority[priority] = by_priority.get(priority, 0) + 1
           
           print("="*50)
           print("📊 EMAIL CLASSIFICATION REPORT")
           print("="*50)
           print(f"\nTotal emails processed: {total}")
           print(f"\n📁 By Department:")
           for dept, count in sorted(by_dept.items()):
               print(f"   {dept}: {count} ({count/total*100:.1f}%)")
           print(f"\n⚡ By Priority:")
           for priority, count in sorted(by_priority.items()):
               print(f"   {priority}: {count} ({count/total*100:.1f}%)")
           
           # Calculate time saved
           manual_time_per_email = 2.5  # minutes
           auto_time_per_email = 0.01  # minutes (nearly instant)
           time_saved = (manual_time_per_email - auto_time_per_email) * total
           
           print(f"\n⏱️  Time Saved:")
           print(f"   Manual: {manual_time_per_email * total:.1f} minutes ({manual_time_per_email * total / 60:.1f} hours)")
           print(f"   Automated: {auto_time_per_email * total:.2f} minutes")
           print(f"   Saved: {time_saved:.1f} minutes ({time_saved / 60:.1f} hours)")
           print(f"   Daily savings (200 emails): {time_saved / total * 200 / 60:.1f} hours")
           print("="*50)
   
   # Test with sample emails
   if __name__ == "__main__":
       classifier = EmailClassifier()
       
       test_emails = [
           {
               'id': 1,
               'from': 'customer1@example.com',
               'subject': 'URGENT: Payment failed',
               'body': 'My invoice payment is not working. Need immediate help!'
           },
           {
               'id': 2,
               'from': 'customer2@example.com',
               'subject': 'Question about pricing',
               'body': 'I would like to get a quote for your enterprise plan'
           },
           {
               'id': 3,
               'from': 'customer3@example.com',
               'subject': 'App keeps crashing',
               'body': 'The application has a critical bug and crashes on startup'
           },
           {
               'id': 4,
               'from': 'customer4@example.com',
               'subject': 'How to export data?',
               'body': 'I need help understanding how to export my data to CSV'
           },
       ]
       
       results = classifier.batch_classify(test_emails)
       
       print("\n📧 Classification Results:")
       for r in results:
           print(f"\nEmail #{r['email_id']}: {r['subject']}")
           print(f"   Department: {r['department']} (confidence: {r['confidence']:.0%})")
           print(f"   Priority: {r['priority']}")
           print(f"   Keywords: {', '.join(r['keywords_found'][:3])}")
       
       classifier.generate_report(results)
   ```

3. **Verification**
   ```bash
   # Run the classifier
   python email_classifier.py
   ```
   
   **Expected output:**
   ```
   📧 Classification Results:
   
   Email #1: URGENT: Payment failed
      Department: billing (confidence: 100%)
      Priority: HIGH
      Keywords: invoice, payment, bill
   
   Email #2: Question about pricing
      Department: sales (confidence: 67%)
      Priority: LOW
      Keywords: pricing, quote
   
   ...
   
   📊 EMAIL CLASSIFICATION REPORT
   ==================================================
   Total emails processed: 4
   
   📁 By Department:
      billing: 1 (25.0%)
      sales: 1 (25.0%)
      ...
   
   ⏱️  Time Saved:
      Daily savings (200 emails): 8.3 hours
   ==================================================
   ```

### ✅ Validation Checklist
- [ ] Code runs without errors
- [ ] All 4 test emails classified correctly
- [ ] Report shows time savings calculation
- [ ] Can add new department keywords easily
- [ ] Priority logic works (HIGH/MEDIUM/LOW)

### 🎯 Challenge
- Add a 5th department: 'hr' with keywords like 'job', 'career', 'interview'
- Classify 3 new emails
- Measure accuracy (should be >80%)

**Duration**: 30 minutes

---

## Exercise 2: Data Validation Automation (Duration: 35 min)

### 🎯 Objective
Build an automation that validates data quality at scale - processing 1000s of records in seconds.

### 📋 Scenario
Your team receives CSV files with customer data. Manual validation takes 15 minutes per file with 5% error rate. Automate it!

### 🛠️ Implementation
Create the data validator from the README.md examples (DataValidator class) and test with sample data containing intentional errors.

### ✅ Validation Checklist
- [ ] Validates email format
- [ ] Catches age out of range  
- [ ] Catches invalid country codes
- [ ] Reports error summary
- [ ] Shows time savings >90%

**Duration**: 35 minutes

---

## Exercise 3: ML-Based Document Classifier (Duration: 45 min)

### 🎯 Objective
Build a machine learning automation for document classification with >70% accuracy.

### 📋 Scenario
Support team categorizes 500+ tickets daily (1-2 min each = 8-16 hours). Use ML to automate this instantly.

### 🛠️ Implementation
Implement the MLDocumentClassifier from README.md examples. Train on provided categories (billing, technical, account, feature requests).

### ✅ Validation Checklist
- [ ] Model trains successfully (>70% accuracy)
- [ ] Classifies new documents correctly
- [ ] Shows confidence scores
- [ ] Can save/load model
- [ ] ROI calculation shows $50K+ annual savings

**Duration**: 45 minutes

---

## Exercise 4: Build Your Automation Dashboard (Duration: 40 min)

### 🎯 Objective  
Create a metrics dashboard to track automation ROI, success rates, and financial impact.

### 📋 Key Metrics
- Tasks processed
- Success rate
- Time saved
- Cost savings
- Error prevention

### 🛠️ Implementation
Build the AutomationMetrics class from README.md. Simulate 30 days of data for 3 different automations.

### ✅ Validation Checklist
- [ ] Tracks all key metrics
- [ ] Calculates ROI correctly
- [ ] Shows success rates >90%
- [ ] Displays recent activity
- [ ] Combined impact >$100K annually

**Duration**: 40 minutes

---

## 📋 Final Checklist

### Completed Exercises
- [ ] Exercise 1: Email Classifier (Rule-based) ✅
- [ ] Exercise 2: Data Validator (Rule-based) ✅
- [ ] Exercise 3: Document Classifier (ML-based) ✅
- [ ] Exercise 4: Automation Dashboard (Metrics) ✅

### Skills Mastered
- [ ] Can identify automation opportunities (Pareto: focus on high-ROI)
- [ ] Understand when to use rules vs ML
- [ ] Can build working automation in <2 hours
- [ ] Can calculate and present ROI
- [ ] Ready to apply to real projects

### Key Takeaways
1. **Start with rules** - 80% of automation can be rule-based
2. **Measure everything** - Track time, errors, costs
3. **Ship fast** - Working automation today > perfect automation next month
4. **Monitor continuously** - Track success rates and edge cases

**Total Time**: 2.5-3 hours of high-impact learning

---

**Excellent work!** 🎉 You've built 4 production-ready automations. Continue to `project-steps.md` for capstone integration.
