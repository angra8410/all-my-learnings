# Interactive Activities - Week 13: Orchestration & Production

## 🎯 Objective

Build production-ready ML pipelines with proper orchestration, monitoring, and deployment.

**Total Time**: 3-4 hours of hands-on pipeline building

---

## Exercise 1: Build Your First ML Pipeline (Duration: 45 min)

### 🎯 Objective
Create a complete, production-ready ML pipeline from scratch using the SimpleMLPipeline pattern.

### 📋 Scenario
You need to deploy an ML model that runs daily, validates data, trains, and deploys automatically.

### 🛠️ Implementation

Implement the `SimpleMLPipeline` class from README.md with these requirements:
- Extract data from a source
- Validate data quality
- Train a model
- Save with versioning
- Deploy to "production"

### ✅ Validation Checklist
- [ ] Pipeline runs end-to-end without errors
- [ ] Data validation catches bad data
- [ ] Model is saved with timestamp version
- [ ] Metrics are tracked (accuracy, execution time)
- [ ] Production model file is created

### 🎯 Expected Output
```
==================================================
🔄 ML PIPELINE EXECUTION
==================================================

📥 [1/5] Extracting data...
   ✓ Extracted 100 records
🔍 [2/5] Validating data...
   ✓ Data validation passed
🎓 [3/5] Training model...
   ✓ Model trained
   Train accuracy: 95.0%
   Test accuracy: 90.0%
💾 [4/5] Saving model...
   ✓ Model saved as v20240120_143022
   ✓ Metadata saved
🚀 [5/5] Deploying model...
   ✓ Model deployed to production

==================================================
✅ PIPELINE COMPLETED SUCCESSFULLY
==================================================
Duration: 2.34 seconds
```

**Duration**: 45 minutes

---

## Exercise 2: Add Scheduling & Automation (Duration: 40 min)

### 🎯 Objective
Automate your pipeline to run on a schedule using GitHub Actions (or Python schedule).

### 📋 Task Options

**Option A: GitHub Actions (Recommended)**

Create `.github/workflows/ml-pipeline.yml`:

```yaml
name: ML Pipeline

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:  # Manual trigger button

jobs:
  run-pipeline:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install pandas scikit-learn
      
      - name: Run ML Pipeline
        run: |
          python pipeline.py
      
      - name: Upload Model
        uses: actions/upload-artifact@v3
        with:
          name: ml-model
          path: models/model_production.pkl
```

**Option B: Python Scheduler**

```python
import schedule
import time
from pipeline import SimpleMLPipeline

def run_scheduled_pipeline():
    print(f"⏰ Starting scheduled run...")
    pipeline = SimpleMLPipeline()
    result = pipeline.run_pipeline()
    
    if not result['success']:
        # Send alert
        print(f"❌ ALERT: Pipeline failed - {result.get('error')}")

# Schedule daily at 2 AM
schedule.every().day.at("02:00").do(run_scheduled_pipeline)

print("🕐 Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(60)
```

### ✅ Validation Checklist
- [ ] Scheduler is configured
- [ ] Can trigger manually
- [ ] Scheduled time is set
- [ ] Pipeline runs automatically
- [ ] Artifacts are saved

**Duration**: 40 minutes

---

## Exercise 3: Add Monitoring & Alerts (Duration: 45 min)

### 🎯 Objective
Implement monitoring to track pipeline health and model performance.

### 🛠️ Implementation

Create `monitor.py` with the MLMonitor class from README.md:

```python
from datetime import datetime

class MLMonitor:
    def __init__(self):
        self.alerts = []
        self.thresholds = {
            'min_accuracy': 0.70,
            'max_execution_time': 300
        }
    
    def check_model_performance(self, accuracy: float):
        if accuracy < self.thresholds['min_accuracy']:
            return self.alert(
                'HIGH',
                f'Model accuracy {accuracy:.2%} below threshold',
                'Retrain model with more data'
            )
        return True
    
    def check_execution_time(self, duration: float):
        if duration > self.thresholds['max_execution_time']:
            return self.alert(
                'MEDIUM',
                f'Pipeline took {duration:.0f}s (threshold: {self.thresholds["max_execution_time"]}s)',
                'Investigate performance issues'
            )
        return True
    
    def alert(self, severity, message, action):
        alert = {
            'timestamp': datetime.now().isoformat(),
            'severity': severity,
            'message': message,
            'action': action
        }
        self.alerts.append(alert)
        
        print(f"\n{'🔴' if severity=='HIGH' else '🟡'} ALERT [{severity}]")
        print(f"   {message}")
        print(f"   Action: {action}\n")
        
        return alert
```

Integrate into your pipeline:

```python
# In your pipeline
monitor = MLMonitor()

result = pipeline.run_pipeline()

if result['success']:
    monitor.check_model_performance(result['metrics']['test_accuracy'])
    monitor.check_execution_time(result['duration'])
```

### ✅ Validation Checklist
- [ ] Monitor tracks accuracy
- [ ] Monitor tracks execution time
- [ ] Alerts are generated when thresholds breached
- [ ] Alert severity levels work (HIGH/MEDIUM/LOW)
- [ ] Monitoring report is generated

**Duration**: 45 minutes

---

## Exercise 4: Build CI/CD Pipeline (Duration: 50 min)

### 🎯 Objective
Create a complete CI/CD pipeline for your ML model with testing, validation, and deployment.

### 🛠️ Implementation

Create `.github/workflows/ml-cicd.yml`:

```yaml
name: ML CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test Pipeline
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests
        run: |
          pytest tests/ --cov=. --cov-report=xml
      
      - name: Lint code
        run: |
          pip install flake8
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  
  validate:
    name: Validate Model
    needs: test
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run pipeline on test data
        run: |
          python pipeline.py --mode=test
      
      - name: Validate model metrics
        run: |
          python scripts/validate_metrics.py
  
  deploy:
    name: Deploy Model
    needs: [test, validate]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run production pipeline
        run: |
          python pipeline.py --mode=production
      
      - name: Upload model artifacts
        uses: actions/upload-artifact@v3
        with:
          name: production-model
          path: |
            models/model_production.pkl
            models/model_*_metadata.json
      
      - name: Notify deployment
        run: |
          echo "✅ Model deployed to production"
```

Also create simple tests in `tests/test_pipeline.py`:

```python
import pytest
from pipeline import SimpleMLPipeline
import pandas as pd

def test_pipeline_runs():
    """Test that pipeline executes successfully"""
    pipeline = SimpleMLPipeline()
    result = pipeline.run_pipeline()
    assert result['success'] == True

def test_data_validation_catches_errors():
    """Test that validation catches bad data"""
    pipeline = SimpleMLPipeline()
    
    # Create invalid data (missing columns)
    bad_data = pd.DataFrame({'wrong_col': [1, 2, 3]})
    
    is_valid = pipeline.validate_data(bad_data)
    assert is_valid == False

def test_model_metrics_above_threshold():
    """Test that model meets minimum accuracy"""
    pipeline = SimpleMLPipeline()
    result = pipeline.run_pipeline()
    
    assert result['metrics']['test_accuracy'] >= 0.60
```

### ✅ Validation Checklist
- [ ] CI/CD workflow file created
- [ ] Tests run on every commit
- [ ] Model validation happens before deployment
- [ ] Deployment only happens on main branch
- [ ] Artifacts are uploaded
- [ ] All tests pass

**Duration**: 50 minutes

---

## 📋 Final Checklist

### Completed Exercises
- [ ] Exercise 1: Built complete ML pipeline ✅
- [ ] Exercise 2: Added scheduling/automation ✅
- [ ] Exercise 3: Implemented monitoring & alerts ✅
- [ ] Exercise 4: Created CI/CD pipeline ✅

### Skills Mastered
- [ ] Can build end-to-end ML pipeline
- [ ] Understand orchestration patterns
- [ ] Can schedule automated runs
- [ ] Know how to monitor production models
- [ ] Can set up CI/CD for ML
- [ ] Ready to deploy models to production

### Production Readiness
- [ ] Pipeline has error handling
- [ ] Data validation in place
- [ ] Model versioning implemented
- [ ] Monitoring and alerting configured
- [ ] CI/CD pipeline working
- [ ] Documentation complete

### Key Takeaways
1. **Start simple** - Basic pipeline beats fancy pipeline that never ships
2. **Automate everything** - Scheduling, testing, deployment
3. **Monitor continuously** - Track performance, execution time, data drift
4. **Version all artifacts** - Models, data, code
5. **Test before deploy** - Catch issues early

**Total Time**: 3-3.5 hours of production ML engineering

---

**Excellent work!** 🎉 You've built a production-ready ML system. Continue to `project-steps.md` for capstone integration.
