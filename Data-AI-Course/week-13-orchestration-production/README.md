# Week 13: Orchestration & Production

## 🎯 Persona: Modern ML Ops Architect

*Hey there! I'm your ML ops architect who makes getting models live and reliable a breeze. I've taken dozens of ML models from notebooks to production, handling millions of predictions daily. My philosophy: Keep it simple, automate everything, monitor religiously. Production doesn't have to be scary—let's make deployment feel as easy as running `git push`!*

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Understand orchestration fundamentals** and why they're critical for durable AI projects
2. **Build end-to-end ML pipelines** using modern tools (Airflow, Prefect, or GitHub Actions)
3. **Deploy models to production** with confidence and proper monitoring
4. **Implement CI/CD for ML models** for automated testing and deployment
5. **Monitor and maintain** production ML systems

**Estimated Duration**: 4-5 hours of production-focused learning

## 📋 Prerequisites

- Completed Week 12 (Automation Models)
- Basic understanding of ML model training
- Python environment with orchestration libraries
- GitHub account for CI/CD

---

## 🧠 Chain of Thought: Why Orchestration Matters

Let me walk you through the journey from notebook to production:

### Step 1: The Notebook Problem

**The Reality**:
- Data scientists create amazing models in notebooks
- Models work great on local machines
- But production is different: data changes, models drift, pipelines break
- Manual deployment is error-prone and doesn't scale

**The Cost of No Orchestration**:
- 87% of data science projects never make it to production
- Those that do often fail within 6 months
- Manual processes cost 10-20 hours/week per model
- Downtime costs $5,000-$20,000/hour for businesses

### Step 2: What is Orchestration?

**Simple Definition**: Orchestration = Automated, reliable execution of your ML workflows

Think of it as a **conductor for your ML orchestra**:
- Ensures all parts play at the right time
- Handles failures gracefully
- Monitors performance
- Scales automatically

### Step 3: The Orchestration Stack (Pareto 80/20)

**80% of orchestration needs are met by focusing on:**

1. **Workflow Scheduling** (40% of value)
   - When to run training, inference, retraining
   - Dependencies between steps
   - Retry logic on failures

2. **Data Pipeline Management** (30% of value)
   - Extract → Transform → Load (ETL)
   - Data validation
   - Version control for data

3. **Model Deployment** (20% of value)
   - Packaging models
   - Serving infrastructure
   - Rollback capabilities

4. **Monitoring & Alerting** (10% of value)
   - Performance metrics
   - Data drift detection
   - Automated alerts

---

## 🎯 Pareto Principle (20/80): Focus on What Matters

### 20% Core Skills That Deliver 80% Results

#### 1. **Simple Pipeline First** (Most Critical)

Start with a minimal viable pipeline:

```python
# Minimal ML Pipeline - Production Ready in 30 Minutes

import pandas as pd
from datetime import datetime
import pickle
import os

class SimpleMLPipeline:
    """
    Minimal production ML pipeline
    Focus: Simple, reliable, monitorable
    """
    
    def __init__(self, model_path="models/", data_path="data/"):
        self.model_path = model_path
        self.data_path = data_path
        self.metrics = {}
        
        # Create directories if they don't exist
        os.makedirs(model_path, exist_ok=True)
        os.makedirs(data_path, exist_ok=True)
    
    def extract_data(self):
        """Step 1: Extract data from source"""
        print("📥 [1/5] Extracting data...")
        
        # In production, this would connect to your database/API
        # For now, we'll simulate it
        data = pd.DataFrame({
            'feature1': range(100),
            'feature2': range(100, 200),
            'target': [x % 2 for x in range(100)]
        })
        
        # Save raw data with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data.to_csv(f"{self.data_path}raw_{timestamp}.csv", index=False)
        
        print(f"   ✓ Extracted {len(data)} records")
        self.metrics['records_extracted'] = len(data)
        return data
    
    def validate_data(self, data: pd.DataFrame) -> bool:
        """Step 2: Validate data quality"""
        print("🔍 [2/5] Validating data...")
        
        issues = []
        
        # Check for missing values
        missing = data.isnull().sum().sum()
        if missing > 0:
            issues.append(f"{missing} missing values")
        
        # Check for expected columns
        expected_cols = ['feature1', 'feature2', 'target']
        missing_cols = set(expected_cols) - set(data.columns)
        if missing_cols:
            issues.append(f"Missing columns: {missing_cols}")
        
        # Check data size
        if len(data) < 10:
            issues.append("Too few records")
        
        if issues:
            print(f"   ❌ Validation failed: {', '.join(issues)}")
            self.metrics['validation_passed'] = False
            return False
        
        print(f"   ✓ Data validation passed")
        self.metrics['validation_passed'] = True
        return True
    
    def train_model(self, data: pd.DataFrame):
        """Step 3: Train model"""
        print("🎓 [3/5] Training model...")
        
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score
        
        # Prepare data
        X = data[['feature1', 'feature2']]
        y = data['target']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train
        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        # Evaluate
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        
        print(f"   ✓ Model trained")
        print(f"   Train accuracy: {train_score:.2%}")
        print(f"   Test accuracy: {test_score:.2%}")
        
        self.metrics['train_accuracy'] = train_score
        self.metrics['test_accuracy'] = test_score
        
        return model
    
    def save_model(self, model, version: str = None):
        """Step 4: Save model with versioning"""
        print("💾 [4/5] Saving model...")
        
        if version is None:
            version = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        model_file = f"{self.model_path}model_v{version}.pkl"
        
        # Save model
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)
        
        # Save metadata
        metadata = {
            'version': version,
            'timestamp': datetime.now().isoformat(),
            'metrics': self.metrics
        }
        
        import json
        with open(f"{self.model_path}model_v{version}_metadata.json", 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"   ✓ Model saved as v{version}")
        print(f"   ✓ Metadata saved")
        
        return model_file
    
    def deploy_model(self, model_file: str):
        """Step 5: Deploy model (mark as production)"""
        print("🚀 [5/5] Deploying model...")
        
        # In production, this would:
        # - Copy to serving infrastructure
        # - Update load balancer
        # - Run smoke tests
        
        # For now, we'll create a symlink to mark as production
        production_link = f"{self.model_path}model_production.pkl"
        
        if os.path.exists(production_link):
            os.remove(production_link)
        
        # On Windows, use copy instead of symlink
        import shutil
        shutil.copy2(model_file, production_link)
        
        print(f"   ✓ Model deployed to production")
        print(f"   Production model: {production_link}")
        
        return production_link
    
    def run_pipeline(self):
        """Execute complete pipeline"""
        print("\n" + "="*60)
        print("🔄 ML PIPELINE EXECUTION")
        print("="*60 + "\n")
        
        start_time = datetime.now()
        
        try:
            # Execute pipeline steps
            data = self.extract_data()
            
            if not self.validate_data(data):
                raise Exception("Data validation failed")
            
            model = self.train_model(data)
            model_file = self.save_model(model)
            production_file = self.deploy_model(model_file)
            
            # Calculate execution time
            duration = (datetime.now() - start_time).total_seconds()
            
            print("\n" + "="*60)
            print("✅ PIPELINE COMPLETED SUCCESSFULLY")
            print("="*60)
            print(f"Duration: {duration:.2f} seconds")
            print(f"Records processed: {self.metrics['records_extracted']}")
            print(f"Test accuracy: {self.metrics['test_accuracy']:.2%}")
            print(f"Production model: {production_file}")
            print("="*60 + "\n")
            
            return {
                'success': True,
                'duration': duration,
                'metrics': self.metrics,
                'model_file': production_file
            }
            
        except Exception as e:
            print("\n" + "="*60)
            print("❌ PIPELINE FAILED")
            print("="*60)
            print(f"Error: {str(e)}")
            print("="*60 + "\n")
            
            return {
                'success': False,
                'error': str(e),
                'metrics': self.metrics
            }

# Run the pipeline
if __name__ == "__main__":
    pipeline = SimpleMLPipeline()
    result = pipeline.run_pipeline()
    
    # In production, you'd log these results to monitoring system
    print(f"\nPipeline {'succeeded' if result['success'] else 'failed'}")
```

**Why This Matters**:
- ✅ Complete pipeline in <100 lines of code
- ✅ Data validation catches issues early
- ✅ Model versioning prevents disasters
- ✅ Metrics tracking for monitoring
- ✅ Error handling and logging

#### 2. **Scheduling (Critical)**

Automate pipeline execution:

```python
# Option 1: Simple Cron-like Scheduler (No Dependencies)

import schedule
import time
from datetime import datetime

def scheduled_pipeline():
    """Run pipeline on schedule"""
    print(f"\n🕐 Scheduled run started at {datetime.now()}")
    
    pipeline = SimpleMLPipeline()
    result = pipeline.run_pipeline()
    
    # Send notification (email, Slack, etc.)
    if result['success']:
        print("✅ Sending success notification...")
    else:
        print("❌ Sending failure alert...")
    
    return result

# Schedule options
schedule.every().day.at("02:00").do(scheduled_pipeline)  # Daily at 2 AM
schedule.every().hour.do(scheduled_pipeline)  # Every hour
schedule.every(6).hours.do(scheduled_pipeline)  # Every 6 hours

print("🕐 Scheduler started. Press Ctrl+C to stop.")
print("Next run:", schedule.next_run())

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
```

```python
# Option 2: GitHub Actions (CI/CD for ML - Recommended!)

# Create .github/workflows/ml-pipeline.yml
"""
name: ML Pipeline

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
  push:
    branches: [ main ]
  workflow_dispatch:  # Manual trigger

jobs:
  train-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run ML Pipeline
      run: |
        python pipeline.py
    
    - name: Upload Model Artifacts
      uses: actions/upload-artifact@v3
      with:
        name: model
        path: models/
    
    - name: Deploy to Production
      if: github.ref == 'refs/heads/main'
      run: |
        # Deploy script here
        echo "Deploying model to production..."
"""
```

#### 3. **Monitoring (Critical)**

Know when things break:

```python
class MLMonitor:
    """Simple monitoring for ML pipelines"""
    
    def __init__(self):
        self.alerts = []
        self.thresholds = {
            'min_accuracy': 0.70,
            'max_data_drift': 0.20,
            'max_execution_time_seconds': 300
        }
    
    def check_model_performance(self, accuracy: float):
        """Monitor model accuracy"""
        if accuracy < self.thresholds['min_accuracy']:
            self.alert(
                severity='HIGH',
                message=f"Model accuracy dropped to {accuracy:.2%} "
                       f"(threshold: {self.thresholds['min_accuracy']:.2%})",
                action="Consider retraining model with more recent data"
            )
            return False
        return True
    
    def check_data_drift(self, current_stats, baseline_stats):
        """Monitor data distribution changes"""
        # Simplified drift detection
        drift_score = abs(current_stats['mean'] - baseline_stats['mean'])
        
        if drift_score > self.thresholds['max_data_drift']:
            self.alert(
                severity='MEDIUM',
                message=f"Data drift detected: {drift_score:.2%}",
                action="Review data pipeline and consider model retraining"
            )
            return False
        return True
    
    def check_execution_time(self, duration_seconds: float):
        """Monitor pipeline execution time"""
        if duration_seconds > self.thresholds['max_execution_time_seconds']:
            self.alert(
                severity='LOW',
                message=f"Pipeline took {duration_seconds:.0f}s "
                       f"(threshold: {self.thresholds['max_execution_time_seconds']}s)",
                action="Investigate performance bottlenecks"
            )
            return False
        return True
    
    def alert(self, severity: str, message: str, action: str):
        """Send alert (print for now, send to Slack/email in production)"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'severity': severity,
            'message': message,
            'action': action
        }
        self.alerts.append(alert)
        
        # Color-coded output
        colors = {'HIGH': '🔴', 'MEDIUM': '🟡', 'LOW': '🟢'}
        print(f"\n{colors[severity]} ALERT [{severity}]")
        print(f"   {message}")
        print(f"   Action: {action}\n")
        
        # In production, send to Slack, email, PagerDuty, etc.
        return alert
    
    def generate_report(self):
        """Generate monitoring report"""
        print("\n" + "="*60)
        print("📊 MONITORING REPORT")
        print("="*60)
        print(f"Total alerts: {len(self.alerts)}")
        
        by_severity = {}
        for alert in self.alerts:
            severity = alert['severity']
            by_severity[severity] = by_severity.get(severity, 0) + 1
        
        for severity, count in sorted(by_severity.items()):
            print(f"   {severity}: {count}")
        
        if self.alerts:
            print(f"\nRecent Alerts:")
            for alert in self.alerts[-3:]:  # Last 3 alerts
                print(f"   [{alert['severity']}] {alert['message']}")
        
        print("="*60 + "\n")

# Usage
monitor = MLMonitor()

# After pipeline runs
monitor.check_model_performance(accuracy=0.85)
monitor.check_execution_time(duration_seconds=45)

monitor.generate_report()
```

---

## 🛠️ Production Patterns & Tools

### Pattern 1: Lightweight Orchestration with Prefect

**Perfect for**: Small to medium teams, fast iteration

```python
from prefect import flow, task
from datetime import timedelta

@task(retries=3, retry_delay_seconds=60)
def extract_data():
    """Extract data with automatic retries"""
    print("📥 Extracting data...")
    # Your data extraction logic
    return data

@task
def validate_data(data):
    """Validate data quality"""
    print("🔍 Validating...")
    if not is_valid(data):
        raise ValueError("Data validation failed")
    return data

@task
def train_model(data):
    """Train ML model"""
    print("🎓 Training...")
    model = train(data)
    return model

@task
def deploy_model(model):
    """Deploy to production"""
    print("🚀 Deploying...")
    deploy(model)
    return "success"

@flow(name="ML Pipeline")
def ml_pipeline_flow():
    """Complete ML pipeline as Prefect flow"""
    data = extract_data()
    valid_data = validate_data(data)
    model = train_model(valid_data)
    result = deploy_model(model)
    return result

# Run locally
if __name__ == "__main__":
    ml_pipeline_flow()

# Or schedule in Prefect Cloud
# prefect deployment build ml_pipeline.py:ml_pipeline_flow -n "Daily ML Pipeline" -q "default"
# prefect deployment apply ml_pipeline_flow-deployment.yaml
```

**Why Prefect?**:
- ✅ Python-native (no YAML!)
- ✅ Built-in retries and error handling
- ✅ Free tier for small teams
- ✅ Great UI for monitoring
- ✅ Easy local testing

### Pattern 2: Enterprise Orchestration with Airflow

**Perfect for**: Large teams, complex dependencies, enterprise requirements

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ml-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def extract_data_task(**context):
    """Extract data"""
    data = extract_data()
    # Push to XCom for next task
    return data

def train_model_task(**context):
    """Train model"""
    # Pull from XCom
    data = context['task_instance'].xcom_pull(task_ids='extract_data')
    model = train_model(data)
    return model

def deploy_model_task(**context):
    """Deploy model"""
    model = context['task_instance'].xcom_pull(task_ids='train_model')
    deploy_model(model)

# Define DAG
with DAG(
    'ml_pipeline',
    default_args=default_args,
    description='ML training and deployment pipeline',
    schedule_interval='@daily',  # Run daily
    catchup=False,
) as dag:
    
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data_task,
    )
    
    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model_task,
    )
    
    deploy = PythonOperator(
        task_id='deploy_model',
        python_callable=deploy_model_task,
    )
    
    # Define dependencies
    extract >> train >> deploy
```

**Why Airflow?**:
- ✅ Industry standard
- ✅ Massive ecosystem
- ✅ Great for complex workflows
- ⚠️ Steeper learning curve
- ⚠️ More infrastructure needed

### Pattern 3: Serverless with GitHub Actions (Recommended for Startups)

**Perfect for**: Startups, small teams, cost-conscious

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:  # Manual trigger

jobs:
  ml-pipeline:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Extract data
        run: python scripts/extract_data.py
      
      - name: Validate data
        run: python scripts/validate_data.py
      
      - name: Train model
        run: python scripts/train_model.py
      
      - name: Evaluate model
        run: python scripts/evaluate_model.py
      
      - name: Deploy to production
        if: github.ref == 'refs/heads/main'
        run: |
          python scripts/deploy_model.py
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: model-artifacts
          path: |
            models/
            metrics/
      
      - name: Notify on failure
        if: failure()
        run: |
          # Send Slack/email notification
          python scripts/send_alert.py --status=failed
```

**Why GitHub Actions?**:
- ✅ Free for public repos, generous free tier for private
- ✅ No infrastructure to manage
- ✅ Integrated with your code repo
- ✅ Easy to set up and maintain
- ✅ Built-in secrets management

---

## 📚 Quick Decision Guide: Which Orchestration Tool?

```
START → How complex is your pipeline?
         ↓
       SIMPLE (< 5 steps, 1-2 dependencies)
         ├→ GitHub Actions (FREE, easy)
         └→ Cron + Python script (simplest)
         ↓
       MEDIUM (5-15 steps, some dependencies)
         ├→ Prefect (Python-native, great DX)
         └→ GitHub Actions (if already using GitHub)
         ↓
       COMPLEX (15+ steps, many dependencies, enterprise)
         ├→ Airflow (industry standard)
         └→ Prefect (if you prefer Python over YAML)
```

---

## ✅ Production Deployment Checklist

### Before Deployment
- [ ] Model tested on held-out data (accuracy > threshold)
- [ ] Data validation rules defined and tested
- [ ] Error handling in place for all pipeline steps
- [ ] Rollback plan documented
- [ ] Monitoring dashboards created
- [ ] Alert thresholds defined
- [ ] Documentation complete

### Deployment
- [ ] Deploy to staging first
- [ ] Run smoke tests
- [ ] Monitor for 24 hours
- [ ] Deploy to production with canary release (10% traffic)
- [ ] Monitor for 48 hours
- [ ] Gradually increase traffic to 100%

### Post-Deployment
- [ ] Monitor key metrics daily for first week
- [ ] Set up weekly performance reviews
- [ ] Document any issues and solutions
- [ ] Plan for model retraining schedule

---

## 📊 Key Takeaways (Pareto Summary)

### The Vital 20% You Must Remember:

1. **Start simple** - Basic pipeline > fancy pipeline that never ships
2. **Automate scheduling** - Manual runs don't scale
3. **Version everything** - Models, data, code
4. **Monitor always** - You can't fix what you can't see
5. **Have a rollback plan** - Things will break

### Quick Start Checklist:
```
☐ Build minimal pipeline (30 min)
☐ Add basic monitoring (20 min)
☐ Set up GitHub Actions OR Prefect (60 min)
☐ Deploy to staging (30 min)
☐ Monitor for 24 hours
☐ Deploy to production (20 min)

Total: ~3 hours to production! 🚀
```

---

## 🚀 What's Next

1. **Complete exercises** in `actividad-interactiva.md` (build real pipelines)
2. **Integrate into capstone** in `project-steps.md` (production-ize your models)
3. **Track progress** in `progreso.md`
4. **Get feedback** in `retroalimentacion.md`

**Next Week**: Week 14 - Finance Case Study (apply these skills to real financial ML problems!)

---

**Time to productionize! Let's get those models deployed reliably.** 🚀🔧
