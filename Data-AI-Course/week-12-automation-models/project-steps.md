# Project Steps - Week 12: Automation Models

## 🎯 Capstone Integration: Add Automation to Your Projects

This week, you'll integrate automation capabilities into your capstone projects to reduce manual work and improve efficiency.

---

## Task 1: Identify Automation Opportunities (12.1)
**Estimated Time**: 30 minutes

### Objective
Conduct an automation audit of your capstone project to find high-ROI opportunities.

### Steps

1. **List all repetitive tasks** in your project:
   ```python
   # Use this template to evaluate opportunities
   
   automation_opportunities = [
       {
           'task': 'Data validation before processing',
           'frequency_per_day': 20,
           'time_per_task_minutes': 5,
           'error_rate': 0.10,  # 10% error rate
           'complexity': 2  # 1-5 scale
       },
       {
           'task': 'Email notifications for alerts',
           'frequency_per_day': 50,
           'time_per_task_minutes': 2,
           'error_rate': 0.05,
           'complexity': 1
       },
       # Add your tasks here
   ]
   
   # Calculate opportunity scores
   def calculate_opportunity_score(task):
       return (task['frequency_per_day'] * 
               task['time_per_task_minutes'] * 
               task['error_rate']) / task['complexity']
   
   # Rank opportunities
   for task in automation_opportunities:
       task['score'] = calculate_opportunity_score(task)
   
   # Sort by score (highest ROI first)
   ranked = sorted(automation_opportunities, key=lambda x: -x['score'])
   
   print("🎯 Top Automation Opportunities (Pareto 20%):")
   for i, task in enumerate(ranked[:3], 1):
       print(f"\n{i}. {task['task']}")
       print(f"   Score: {task['score']:.2f}")
       print(f"   Daily time: {task['frequency_per_day'] * task['time_per_task_minutes']} minutes")
       print(f"   Monthly savings: {task['frequency_per_day'] * task['time_per_task_minutes'] * 20 / 60:.1f} hours")
   ```

2. **Choose your top 1-2 opportunities** (focus on score > 2.0)

3. **Document in your capstone README**:
   - What will be automated
   - Expected time savings
   - Expected error reduction
   - Implementation approach (rule-based vs ML)

### Deliverable
`docs/automation-opportunities.md` with ranked list and justification

---

## Task 2: Implement Core Automation (12.2)
**Estimated Time**: 60-90 minutes

### Objective
Build and integrate one high-impact automation into your capstone.

### Implementation Options

#### Option A: Data Validation Automation
Perfect for projects that process external data.

```python
# Add to your project: src/automation/data_validator.py

from typing import Dict, List
import pandas as pd

class DataValidator:
    """Automated data validation for your project"""
    
    def __init__(self, rules: Dict):
        self.rules = rules
        self.validation_log = []
    
    def validate_batch(self, df: pd.DataFrame) -> Dict:
        """Validate dataframe against rules"""
        results = {
            'total': len(df),
            'valid': 0,
            'invalid': 0,
            'errors': []
        }
        
        for idx, record in df.iterrows():
            if self._validate_record(record.to_dict(), idx):
                results['valid'] += 1
            else:
                results['invalid'] += 1
        
        return results
    
    def _validate_record(self, record: Dict, idx: int) -> bool:
        """Implement your validation logic here"""
        # Add your project-specific validation
        pass

# Integration example
validator = DataValidator(your_rules)
validation_results = validator.validate_batch(your_dataframe)

if validation_results['invalid'] > 0:
    print(f"⚠️ Found {validation_results['invalid']} invalid records")
    # Handle invalid records
```

#### Option B: Classification/Routing Automation
Perfect for projects with categorization needs.

```python
# Add to your project: src/automation/classifier.py

class AutomatedClassifier:
    """Rule-based classification for your project"""
    
    def __init__(self):
        # Define your project-specific rules
        self.categories = {
            'high_priority': ['urgent', 'critical', 'asap'],
            'medium_priority': ['important', 'soon'],
            'low_priority': []  # default
        }
    
    def classify(self, text: str) -> Dict:
        """Classify text into categories"""
        text_lower = text.lower()
        
        for category, keywords in self.categories.items():
            if any(keyword in text_lower for keyword in keywords):
                return {
                    'category': category,
                    'confidence': 0.9,  # High confidence for rule-based
                    'action': self._get_action(category)
                }
        
        return {
            'category': 'low_priority',
            'confidence': 0.7,
            'action': 'standard_processing'
        }
    
    def _get_action(self, category: str) -> str:
        """Map category to action"""
        actions = {
            'high_priority': 'immediate_processing',
            'medium_priority': 'fast_track',
            'low_priority': 'standard_processing'
        }
        return actions.get(category, 'standard_processing')

# Integration
classifier = AutomatedClassifier()
result = classifier.classify(your_input_text)
# Route based on result['action']
```

#### Option C: Workflow Automation
Perfect for projects with multi-step processes.

```python
# Add to your project: src/automation/workflow.py

from enum import Enum
from typing import Dict, List

class WorkflowStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class WorkflowAutomation:
    """Automate multi-step workflows"""
    
    def __init__(self):
        self.steps = []
        self.results = {}
    
    def add_step(self, step_name: str, function, auto_execute=True):
        """Add a step to the workflow"""
        self.steps.append({
            'name': step_name,
            'function': function,
            'auto_execute': auto_execute,
            'status': WorkflowStatus.PENDING
        })
    
    def execute(self, input_data: Dict) -> Dict:
        """Execute workflow steps"""
        current_data = input_data
        
        for step in self.steps:
            try:
                if step['auto_execute']:
                    step['status'] = WorkflowStatus.IN_PROGRESS
                    current_data = step['function'](current_data)
                    step['status'] = WorkflowStatus.COMPLETED
                else:
                    # Requires human review
                    step['status'] = WorkflowStatus.PENDING
                    break
            except Exception as e:
                step['status'] = WorkflowStatus.FAILED
                self.results['error'] = str(e)
                break
        
        self.results['final_data'] = current_data
        return self.results

# Example usage in your project
workflow = WorkflowAutomation()
workflow.add_step('validate_input', your_validator)
workflow.add_step('process_data', your_processor)
workflow.add_step('generate_output', your_generator)

results = workflow.execute(input_data)
```

### Deliverable
- Working automation module in `src/automation/`
- Integration with main project code
- Basic error handling and logging

---

## Task 3: Add Metrics & Monitoring (12.3)
**Estimated Time**: 30-40 minutes

### Objective
Track automation performance and ROI.

### Implementation

```python
# Add to your project: src/automation/metrics.py

from datetime import datetime
from typing import Dict, List
import json

class AutomationMetrics:
    """Track automation performance"""
    
    def __init__(self, automation_name: str):
        self.name = automation_name
        self.metrics = {
            'total_executions': 0,
            'successful_executions': 0,
            'failed_executions': 0,
            'total_time_saved_seconds': 0,
            'errors_prevented': 0
        }
        self.log_file = f"logs/automation_{automation_name}.json"
    
    def log_execution(self, success: bool, time_saved_seconds: float, 
                     errors_prevented: int = 0):
        """Log an automation execution"""
        self.metrics['total_executions'] += 1
        
        if success:
            self.metrics['successful_executions'] += 1
            self.metrics['total_time_saved_seconds'] += time_saved_seconds
            self.metrics['errors_prevented'] += errors_prevented
        else:
            self.metrics['failed_executions'] += 1
        
        # Append to log file
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'success': success,
            'time_saved': time_saved_seconds,
            'errors_prevented': errors_prevented
        }
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except:
            pass  # Logging failure shouldn't break automation
    
    def get_summary(self) -> Dict:
        """Get performance summary"""
        success_rate = (self.metrics['successful_executions'] / 
                       self.metrics['total_executions'] 
                       if self.metrics['total_executions'] > 0 else 0)
        
        return {
            'name': self.name,
            'executions': self.metrics['total_executions'],
            'success_rate': success_rate,
            'time_saved_hours': self.metrics['total_time_saved_seconds'] / 3600,
            'errors_prevented': self.metrics['errors_prevented'],
            'estimated_value': (self.metrics['total_time_saved_seconds'] / 3600) * 50  # $50/hour
        }
    
    def print_dashboard(self):
        """Print metrics dashboard"""
        summary = self.get_summary()
        
        print(f"\n{'='*50}")
        print(f"📊 {summary['name']} - Performance Dashboard")
        print(f"{'='*50}")
        print(f"Executions: {summary['executions']}")
        print(f"Success Rate: {summary['success_rate']:.1%}")
        print(f"Time Saved: {summary['time_saved_hours']:.2f} hours")
        print(f"Errors Prevented: {summary['errors_prevented']}")
        print(f"Estimated Value: ${summary['estimated_value']:.2f}")
        print(f"{'='*50}\n")

# Integration in your automation code
metrics = AutomationMetrics("data_validation")

# When automation runs:
start_time = time.time()
try:
    # Your automation logic here
    success = True
    errors_prevented = 5
except:
    success = False
    errors_prevented = 0
finally:
    time_saved = 300 - (time.time() - start_time)  # 300 sec manual time
    metrics.log_execution(success, time_saved, errors_prevented)
```

### Deliverable
- Metrics tracking integrated
- Dashboard function callable
- Log file for audit trail

---

## Task 4: Testing & Documentation (12.4)
**Estimated Time**: 30 minutes

### Objective
Ensure automation quality and document usage.

### Steps

1. **Write tests** for your automation:
   ```python
   # tests/test_automation.py
   
   def test_automation_handles_valid_data():
       """Test automation with valid input"""
       result = your_automation.process(valid_data)
       assert result['success'] == True
       assert result['errors'] == []
   
   def test_automation_handles_invalid_data():
       """Test automation with invalid input"""
       result = your_automation.process(invalid_data)
       assert result['success'] == False
       assert len(result['errors']) > 0
   
   def test_automation_metrics():
       """Test metrics are tracked"""
       metrics = AutomationMetrics("test")
       metrics.log_execution(True, 100, 1)
       summary = metrics.get_summary()
       assert summary['executions'] == 1
       assert summary['time_saved_hours'] > 0
   ```

2. **Update project documentation**:
   - Add automation section to README
   - Document what's automated
   - Include before/after metrics
   - Add usage examples

3. **Create automation guide**:
   ```markdown
   # Automation Guide
   
   ## What's Automated
   - Data validation (saves 2 hours/day)
   - Email classification (saves 4 hours/day)
   - Report generation (saves 1 hour/day)
   
   ## How to Use
   ```python
   from automation import DataValidator
   
   validator = DataValidator(rules)
   results = validator.validate(data)
   ```
   
   ## Monitoring
   Check `logs/automation_*.json` for execution history
   Run `python -m automation.metrics` for dashboard
   ```

### Deliverable
- Test suite passing
- Documentation updated
- Usage guide created

---

## ✅ Week 12 Integration Checklist

- [ ] Automation opportunities identified and ranked
- [ ] Top automation implemented and working
- [ ] Metrics tracking in place
- [ ] Tests passing (>80% coverage)
- [ ] Documentation updated
- [ ] Time savings calculated and validated
- [ ] Ready to demonstrate automation value

### Success Metrics
- At least 1 automation fully integrated
- Measured time savings >2 hours/week
- Success rate >90%
- Clear ROI documentation

---

## 🎯 Expected Outcomes

By completing Week 12 capstone integration:

1. **Your project now has working automation** that reduces manual work
2. **You can demonstrate ROI** with real metrics
3. **You have a metrics system** to track ongoing value
4. **Your code is more maintainable** with automated quality checks

**This automation foundation will be crucial for Week 13 (Orchestration & Production)!**

---

**Progress tracking**: Update your progress in `progreso.md`  
**Next**: Week 13 - Orchestration & Production (scale your automations!)
