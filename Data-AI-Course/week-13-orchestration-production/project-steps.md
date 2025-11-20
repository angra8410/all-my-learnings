# Project Steps - Week 13: Orchestration & Production

## 🎯 Capstone Integration: Production-ize Your ML Models

This week, you'll take your capstone project's ML models from notebooks to production with proper orchestration, CI/CD, and monitoring.

---

## Task 1: Convert Notebook to Production Pipeline (13.1)
**Estimated Time**: 60-75 minutes

### Objective
Transform your Jupyter notebook ML code into a production-ready pipeline.

### Steps

1. **Extract code from notebook**
   ```python
   # Before (in notebook):
   # Cell 1: Load data
   df = pd.read_csv('data.csv')
   
   # Cell 2: Clean data  
   df = df.dropna()
   
   # Cell 3: Train model
   model.fit(X, y)
   
   # Cell 4: Save model
   joblib.dump(model, 'model.pkl')
   ```

   ```python
   # After (in pipeline.py):
   class ProductionMLPipeline:
       def __init__(self, config):
           self.config = config
           self.logger = self._setup_logging()
       
       def extract_data(self):
           """Extract data with error handling"""
           try:
               df = pd.read_csv(self.config['data_path'])
               self.logger.info(f"Loaded {len(df)} records")
               return df
           except Exception as e:
               self.logger.error(f"Data extraction failed: {e}")
               raise
       
       def validate_data(self, df):
           """Validate data quality"""
           # Add your validation rules
           if df.isnull().sum().sum() > 0:
               raise ValueError("Data contains null values")
           return df
       
       def train_model(self, df):
           """Train with proper train/test split"""
           X_train, X_test, y_train, y_test = train_test_split(...)
           model = YourModel()
           model.fit(X_train, y_train)
           
           # Evaluate
           test_score = model.score(X_test, y_test)
           self.logger.info(f"Test score: {test_score:.3f}")
           
           return model, {'test_score': test_score}
       
       def save_model(self, model, metrics):
           """Save with versioning"""
           version = datetime.now().strftime("%Y%m%d_%H%M%S")
           model_path = f"models/model_v{version}.pkl"
           
           joblib.dump(model, model_path)
           
           # Save metadata
           metadata = {
               'version': version,
               'metrics': metrics,
               'timestamp': datetime.now().isoformat()
           }
           with open(f"models/model_v{version}_metadata.json", 'w') as f:
               json.dump(metadata, f, indent=2)
           
           self.logger.info(f"Model saved: {model_path}")
           return model_path
       
       def run(self):
           """Execute pipeline"""
           self.logger.info("=== Pipeline Started ===")
           
           df = self.extract_data()
           df = self.validate_data(df)
           model, metrics = self.train_model(df)
           model_path = self.save_model(model, metrics)
           
           self.logger.info("=== Pipeline Completed ===")
           return {'success': True, 'model_path': model_path}
   ```

2. **Add configuration**
   ```python
   # config.py
   import os
   from pathlib import Path

   class Config:
       # Paths
       BASE_DIR = Path(__file__).parent
       DATA_DIR = BASE_DIR / "data"
       MODELS_DIR = BASE_DIR / "models"
       LOGS_DIR = BASE_DIR / "logs"
       
       # Data
       DATA_PATH = DATA_DIR / "input.csv"
       
       # Model
       MIN_ACCURACY_THRESHOLD = 0.70
       TEST_SIZE = 0.2
       RANDOM_STATE = 42
       
       # Monitoring
       ALERT_EMAIL = os.getenv('ALERT_EMAIL', 'alerts@example.com')
       
       @classmethod
       def create_directories(cls):
           """Create necessary directories"""
           for dir in [cls.DATA_DIR, cls.MODELS_DIR, cls.LOGS_DIR]:
               dir.mkdir(parents=True, exist_ok=True)
   ```

3. **Add logging**
   ```python
   import logging
   from datetime import datetime

   def setup_logging(name='pipeline'):
       """Setup logging configuration"""
       log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log"
       
       logging.basicConfig(
           level=logging.INFO,
           format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
           handlers=[
               logging.FileHandler(log_file),
               logging.StreamHandler()
           ]
       )
       
       return logging.getLogger(name)
   ```

### Deliverable
- `pipeline.py` with production code
- `config.py` with configuration
- `requirements.txt` with dependencies
- All notebook logic converted and tested

---

## Task 2: Add CI/CD Pipeline (13.2)
**Estimated Time**: 45-60 minutes

### Objective
Set up automated testing and deployment using GitHub Actions.

### Implementation

1. **Create test suite** (`tests/test_pipeline.py`):
   ```python
   import pytest
   from pipeline import ProductionMLPipeline
   from config import Config
   import pandas as pd

   @pytest.fixture
   def sample_data():
       """Create sample data for testing"""
       return pd.DataFrame({
           'feature1': range(100),
           'feature2': range(100, 200),
           'target': [0, 1] * 50
       })

   def test_pipeline_runs_end_to_end(tmp_path, sample_data):
       """Test complete pipeline execution"""
       # Setup
       config = Config()
       config.DATA_PATH = tmp_path / "test_data.csv"
       config.MODELS_DIR = tmp_path / "models"
       
       sample_data.to_csv(config.DATA_PATH, index=False)
       config.create_directories()
       
       # Run pipeline
       pipeline = ProductionMLPipeline(config)
       result = pipeline.run()
       
       # Assert
       assert result['success'] == True
       assert (tmp_path / "models").exists()

   def test_data_validation_catches_errors(tmp_path):
       """Test that validation catches bad data"""
       # Create invalid data
       bad_data = pd.DataFrame({'wrong_column': [1, 2, 3]})
       
       config = Config()
       config.DATA_PATH = tmp_path / "bad_data.csv"
       bad_data.to_csv(config.DATA_PATH, index=False)
       
       pipeline = ProductionMLPipeline(config)
       
       with pytest.raises(ValueError):
           pipeline.run()

   def test_model_meets_accuracy_threshold(tmp_path, sample_data):
       """Test model performance"""
       config = Config()
       config.DATA_PATH = tmp_path / "data.csv"
       config.MODELS_DIR = tmp_path / "models"
       sample_data.to_csv(config.DATA_PATH, index=False)
       config.create_directories()
       
       pipeline = ProductionMLPipeline(config)
       result = pipeline.run()
       
       # Load metadata and check accuracy
       import json
       import glob
       
       metadata_files = glob.glob(str(tmp_path / "models" / "*_metadata.json"))
       with open(metadata_files[0]) as f:
           metadata = json.load(f)
       
       assert metadata['metrics']['test_score'] >= config.MIN_ACCURACY_THRESHOLD
   ```

2. **Create GitHub Actions workflow** (`.github/workflows/ml-pipeline.yml`):
   ```yaml
   name: ML Pipeline CI/CD

   on:
     push:
       branches: [ main, develop ]
     pull_request:
       branches: [ main ]
     schedule:
       - cron: '0 2 * * *'  # Daily at 2 AM
     workflow_dispatch:

   jobs:
     test:
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
           pytest tests/ -v --cov=. --cov-report=xml --cov-report=term
       
       - name: Upload coverage
         uses: codecov/codecov-action@v3
         with:
           files: ./coverage.xml
     
     train-and-deploy:
       needs: test
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
       
       - name: Run ML Pipeline
         run: python pipeline.py
       
       - name: Validate Model
         run: python scripts/validate_model.py
       
       - name: Upload Model Artifacts
         uses: actions/upload-artifact@v3
         with:
           name: ml-model-${{ github.sha }}
           path: |
             models/model_*.pkl
             models/model_*_metadata.json
       
       - name: Notify Success
         if: success()
         run: |
           echo "✅ Pipeline completed successfully"
           # Add Slack/email notification here
   ```

### Deliverable
- Complete test suite with >80% coverage
- GitHub Actions workflow configured
- Tests passing on every commit
- Automated deployment on main branch

---

## Task 3: Add Monitoring & Alerting (13.3)
**Estimated Time**: 40-50 minutes

### Objective
Implement monitoring to track model performance and pipeline health in production.

### Implementation

1. **Create monitoring module** (`monitoring.py`):
   ```python
   import json
   from datetime import datetime
   from pathlib import Path
   import smtplib
   from email.message import EmailMessage

   class PipelineMonitor:
       def __init__(self, config):
           self.config = config
           self.metrics_file = Path("logs/metrics.jsonl")
           self.alerts = []
       
       def log_metrics(self, metrics: dict):
           """Log metrics for tracking"""
           entry = {
               'timestamp': datetime.now().isoformat(),
               **metrics
           }
           
           with open(self.metrics_file, 'a') as f:
               f.write(json.dumps(entry) + '\n')
       
       def check_model_performance(self, accuracy: float):
           """Alert if model performance drops"""
           if accuracy < self.config.MIN_ACCURACY_THRESHOLD:
               self.alert(
                   severity='HIGH',
                   message=f'Model accuracy {accuracy:.2%} below threshold {self.config.MIN_ACCURACY_THRESHOLD:.2%}',
                   action='Investigate data quality and retrain model'
               )
               return False
           return True
       
       def check_data_quality(self, data_stats: dict):
           """Monitor data distribution"""
           # Load baseline stats
           baseline_file = Path("logs/baseline_stats.json")
           
           if baseline_file.exists():
               with open(baseline_file) as f:
                   baseline = json.load(f)
               
               # Simple drift detection
               for col, stats in data_stats.items():
                   if col in baseline:
                       mean_diff = abs(stats['mean'] - baseline[col]['mean'])
                       if mean_diff > 0.2:  # 20% drift threshold
                           self.alert(
                               severity='MEDIUM',
                               message=f'Data drift detected in {col}: {mean_diff:.2%}',
                               action='Review data pipeline and consider retraining'
                           )
           else:
               # Save as baseline
               with open(baseline_file, 'w') as f:
                   json.dump(data_stats, f, indent=2)
       
       def alert(self, severity: str, message: str, action: str):
           """Send alert"""
           alert = {
               'timestamp': datetime.now().isoformat(),
               'severity': severity,
               'message': message,
               'action': action
           }
           
           self.alerts.append(alert)
           
           # Log alert
           print(f"\n🚨 ALERT [{severity}]")
           print(f"   {message}")
           print(f"   Action: {action}\n")
           
           # Send email if HIGH severity
           if severity == 'HIGH':
               self._send_email_alert(alert)
           
           return alert
       
       def _send_email_alert(self, alert):
           """Send email alert (implement based on your email service)"""
           # Placeholder - implement with your email service
           print(f"📧 Email alert sent to {self.config.ALERT_EMAIL}")
       
       def generate_dashboard(self):
           """Generate monitoring dashboard"""
           if not self.metrics_file.exists():
               print("No metrics logged yet")
               return
           
           # Load all metrics
           metrics = []
           with open(self.metrics_file) as f:
               for line in f:
                   metrics.append(json.loads(line))
           
           # Calculate summary
           recent = metrics[-10:]  # Last 10 runs
           
           print("\n" + "="*60)
           print("📊 MONITORING DASHBOARD")
           print("="*60)
           print(f"Total pipeline runs: {len(metrics)}")
           print(f"Recent runs: {len(recent)}")
           
           if recent:
               avg_accuracy = sum(m.get('test_score', 0) for m in recent) / len(recent)
               print(f"Average accuracy (last 10): {avg_accuracy:.2%}")
           
           print(f"\nTotal alerts: {len(self.alerts)}")
           
           if self.alerts:
               print("\nRecent alerts:")
               for alert in self.alerts[-5:]:
                   print(f"  [{alert['severity']}] {alert['message']}")
           
           print("="*60 + "\n")
   ```

2. **Integrate monitoring into pipeline**:
   ```python
   # In pipeline.py
   from monitoring import PipelineMonitor

   class ProductionMLPipeline:
       def __init__(self, config):
           self.config = config
           self.monitor = PipelineMonitor(config)
       
       def run(self):
           # ... existing code ...
           
           model, metrics = self.train_model(df)
           
           # Monitor performance
           self.monitor.check_model_performance(metrics['test_score'])
           
           # Calculate data stats
           data_stats = {
               col: {'mean': df[col].mean(), 'std': df[col].std()}
               for col in df.select_dtypes(include=[np.number]).columns
           }
           self.monitor.check_data_quality(data_stats)
           
           # Log metrics
           self.monitor.log_metrics(metrics)
           
           # ... rest of code ...
   ```

### Deliverable
- Monitoring module implemented
- Alerts configured for model performance
- Data drift detection in place
- Metrics logged to file
- Dashboard generated

---

## Task 4: Documentation & Runbook (13.4)
**Estimated Time**: 30 minutes

### Objective
Create comprehensive documentation for operating the production system.

### Create `RUNBOOK.md`:

```markdown
# ML Pipeline Runbook

## Overview
Production ML pipeline for [your capstone project].

## Architecture
```
Data Source → Extract → Validate → Train → Deploy → Monitor
```

## Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run pipeline
python pipeline.py
```

### Deployment
Automatic deployment on push to `main` branch via GitHub Actions.

## Monitoring

### Check Pipeline Status
```bash
# View recent metrics
tail -20 logs/metrics.jsonl

# Generate dashboard
python -c "from monitoring import PipelineMonitor; from config import Config; PipelineMonitor(Config()).generate_dashboard()"
```

### Common Issues

#### Pipeline Fails with "Data validation error"
**Symptom**: Pipeline stops at validation step  
**Cause**: Input data doesn't meet quality standards  
**Fix**: 
1. Check `logs/pipeline_YYYYMMDD.log` for specific errors
2. Verify data source is accessible
3. Run data validation manually: `python scripts/validate_data.py`

#### Model Accuracy Below Threshold
**Symptom**: Alert "Model accuracy below threshold"  
**Cause**: Model performance degraded  
**Fix**:
1. Check for data drift: review `logs/baseline_stats.json`
2. Retrain with more recent data
3. Consider feature engineering improvements

#### Deployment Fails
**Symptom**: GitHub Actions workflow fails at deploy step  
**Cause**: Usually model didn't pass validation  
**Fix**:
1. Check workflow logs in GitHub Actions
2. Verify model metrics meet thresholds
3. Run validation locally: `python scripts/validate_model.py`

## Maintenance

### Weekly Tasks
- [ ] Review monitoring dashboard
- [ ] Check alert frequency
- [ ] Verify model performance trends

### Monthly Tasks
- [ ] Review and update baseline statistics
- [ ] Evaluate need for model retraining
- [ ] Update dependencies (security patches)

### Quarterly Tasks
- [ ] Full model performance review
- [ ] Update accuracy thresholds if needed
- [ ] Review and optimize pipeline performance

## Rollback Procedure

If production model needs to be rolled back:

```bash
# List available model versions
ls -lt models/model_v*.pkl

# Update production symlink to previous version
ln -sf models/model_vYYYYMMDD_HHMMSS.pkl models/model_production.pkl
```

## Contacts
- Model Owner: [Your Name]
- On-Call: [Team]
- Alerts: [Email/Slack channel]
```

### Deliverable
- Complete runbook documentation
- Troubleshooting guide
- Maintenance schedule
- Contact information

---

## ✅ Week 13 Integration Checklist

- [ ] Notebook converted to production pipeline
- [ ] CI/CD pipeline configured and working
- [ ] Automated tests passing (>80% coverage)
- [ ] Monitoring and alerting implemented
- [ ] Model versioning in place
- [ ] Documentation complete (runbook)
- [ ] Pipeline runs automatically on schedule
- [ ] Ready to handle production traffic

### Success Metrics
- Pipeline runs reliably (>95% success rate)
- Model deployed automatically on code changes
- Monitoring catches issues before users do
- Complete documentation for operations team

---

## 🎯 Expected Outcomes

By completing Week 13 capstone integration:

1. **Your ML model is production-ready** with proper orchestration
2. **CI/CD automates everything** from testing to deployment
3. **Monitoring ensures reliability** with alerts for issues
4. **Documentation enables operations** - team can maintain it

**Your capstone project is now enterprise-grade!**

---

**Progress tracking**: Update your progress in `progreso.md`  
**Next**: Week 14 - Finance Case Study (apply to real financial problems!)
