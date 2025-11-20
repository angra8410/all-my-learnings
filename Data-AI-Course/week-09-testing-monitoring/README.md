# Week 09: Testing & Monitoring

## 👨‍💻 Your Expert Persona

**You're a pragmatic AI engineer** who ensures models stay reliable after deployment. You focus on the easiest-to-apply techniques that avoid big real-world failures. You believe that "an ounce of testing prevents a pound of debugging" and make testing accessible, not academic.

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Implement AI-specific unit tests** that catch bugs before deployment
2. **Set up integration tests** for end-to-end AI pipelines
3. **Monitor model performance** in production with minimal overhead
4. **Detect and respond to drift** (data drift, concept drift)
5. **Build automated alerts** for model degradation

**Estimated Duration**: 4-5 hours

---

## 🧠 Chain of Thought: Understanding AI Testing & Monitoring

### Step 1: Why Testing AI is Different

Traditional software testing checks: "Does the code run?"  
**AI testing checks: "Does the model work correctly?"**

The difference:
- ❌ Traditional: Deterministic (same input → same output)
- ✅ AI: Probabilistic (same input → similar but not identical output)
- ❌ Traditional: Logic bugs are obvious (crashes, wrong calculations)
- ✅ AI: Quality bugs are subtle (slightly worse predictions, bias)

**This requires new testing approaches.**

### Step 2: The Essential Test Types (Pareto 80/20)

The **20% of tests** that catch **80% of issues**:

#### 1. **Unit Tests for AI** (30% effort, 40% impact)

Test individual components:
```python
def test_data_preprocessing():
    """Test that data preprocessing works correctly"""
    raw_data = load_test_data()
    processed = preprocess(raw_data)
    
    # Check shape
    assert processed.shape[0] == raw_data.shape[0]
    
    # Check no NaN values
    assert not processed.isnull().any().any()
    
    # Check value ranges
    assert processed['age'].between(0, 120).all()
```

What to test:
- ✅ Data preprocessing (no NaN, correct types, valid ranges)
- ✅ Feature engineering (correct calculations, no inf values)
- ✅ Input validation (reject bad inputs before they reach model)
- ✅ Output validation (predictions in expected range)

#### 2. **Integration Tests** (20% effort, 30% impact)

Test the full pipeline:
```python
def test_end_to_end_prediction():
    """Test complete prediction pipeline"""
    # Raw input
    user_data = {"age": 35, "income": 50000, "credit_score": 700}
    
    # Run through pipeline
    prediction = model.predict(user_data)
    
    # Validate output
    assert 'prediction' in prediction
    assert 'confidence' in prediction
    assert 0 <= prediction['confidence'] <= 1
    assert prediction['prediction'] in ['approved', 'denied']
```

What to test:
- ✅ End-to-end pipeline (input → preprocessing → model → output)
- ✅ API endpoints (correct responses, error handling)
- ✅ Database interactions (save/load correctly)

#### 3. **Model Performance Tests** (25% effort, 20% impact)

Test model quality doesn't degrade:
```python
def test_model_performance():
    """Ensure model meets minimum quality standards"""
    X_test, y_test = load_test_set()
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    
    # Regression test: performance shouldn't drop
    assert accuracy >= 0.85, f"Model accuracy {accuracy} below threshold 0.85"
```

#### 4. **Production Monitoring** (25% effort, 10% impact initial, 80% long-term!)

Monitor in real-time:
- **Data drift**: Input distribution changes
- **Concept drift**: Relationship between inputs/outputs changes
- **Performance drift**: Accuracy decreases over time

### Step 3: Minimal Monitoring Setup

Here's a **battle-tested monitoring framework**:

```python
import numpy as np
from scipy import stats
import logging
from datetime import datetime

class ModelMonitor:
    """
    Lightweight model monitoring for production.
    Focuses on the vital few metrics that catch most issues.
    """
    
    def __init__(self, baseline_data, alert_threshold=0.05):
        """
        Args:
            baseline_data: Training data statistics
            alert_threshold: P-value threshold for drift detection
        """
        self.baseline_mean = baseline_data.mean()
        self.baseline_std = baseline_data.std()
        self.alert_threshold = alert_threshold
        self.predictions_log = []
        
    def check_data_drift(self, new_data):
        """
        Detect if input data distribution has changed.
        Uses Kolmogorov-Smirnov test.
        """
        drift_detected = {}
        
        for column in new_data.columns:
            if column in self.baseline_mean.index:
                # Statistical test for distribution change
                baseline_col = self.baseline_data[column]
                new_col = new_data[column]
                
                statistic, p_value = stats.ks_2samp(baseline_col, new_col)
                
                if p_value < self.alert_threshold:
                    drift_detected[column] = {
                        'p_value': p_value,
                        'severity': 'HIGH' if p_value < 0.01 else 'MEDIUM'
                    }
        
        return drift_detected
    
    def log_prediction(self, input_data, prediction, confidence, latency_ms):
        """Log prediction for monitoring"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'prediction': prediction,
            'confidence': confidence,
            'latency_ms': latency_ms
        }
        self.predictions_log.append(log_entry)
        
        # Check for anomalies
        if confidence < 0.5:
            logging.warning(f"Low confidence prediction: {confidence:.2f}")
        if latency_ms > 1000:
            logging.warning(f"High latency: {latency_ms}ms")
```

### Step 4: Automated Testing Checklist

**Before Deployment:**
- [ ] Unit tests for data preprocessing (100% pass rate)
- [ ] Integration test for full pipeline (working end-to-end)
- [ ] Performance test on held-out data (meets threshold)
- [ ] Load test (handles expected traffic)
- [ ] Error handling test (graceful failures)

**After Deployment:**
- [ ] Data drift monitoring (daily checks)
- [ ] Performance monitoring (accuracy, latency)
- [ ] Error rate tracking (< 1% errors)
- [ ] Confidence distribution (no major shifts)
- [ ] Resource usage (CPU, memory, API costs)

### Step 5: Common Pitfalls & Solutions

| Pitfall | Why It's Bad | Solution |
|---------|--------------|----------|
| **No test data versioning** | Can't reproduce test results | Version control test datasets |
| **Testing only happy path** | Miss edge cases and errors | Test edge cases, invalid inputs, boundary conditions |
| **No monitoring after deployment** | Silent failures and degradation | Set up automated monitoring from day 1 |
| **Ignoring low-confidence predictions** | Model might be struggling | Alert when confidence < threshold |
| **No drift detection** | Model becomes stale | Monitor data distribution weekly |

---

## 🎯 Pareto Principle (20/80 Focus)

### The Vital 20% (Master These)

1. **Data Validation Tests**
   - Check for NaN, inf values
   - Validate data types and ranges
   - Test preprocessing functions

2. **End-to-End Integration Test**
   - One test covering full pipeline
   - Validates all components work together
   - Catches integration issues

3. **Basic Drift Detection**
   - Monitor input data distribution
   - Alert when significant changes occur
   - Simple statistical tests (KS test)

### The Impactful 80% (Practice These)

1. **Automated Test Suite**
   - Run tests on every code change
   - CI/CD integration
   - Fast feedback loop

2. **Production Monitoring Dashboard**
   - Track key metrics in real-time
   - Set up alerts for anomalies
   - Review weekly

3. **Incident Response Plan**
   - What to do when tests fail
   - How to roll back deployments
   - Escalation procedures

---

## 🛠️ Tools & Technologies

**Testing Frameworks:**
- **pytest**: Python testing (most popular)
- **unittest**: Built-in Python testing
- **Great Expectations**: Data quality testing
- **pytest-xdist**: Parallel test execution

**Monitoring Tools:**
- **Evidently AI**: ML monitoring (open-source)
- **WhyLabs**: Data quality monitoring
- **Prometheus + Grafana**: General purpose monitoring
- **MLflow**: Experiment and model tracking
- **Weights & Biases**: Comprehensive ML platform

**CI/CD Integration:**
- **GitHub Actions**: Automated testing on commits
- **Jenkins**: Traditional CI/CD
- **CircleCI**: Cloud-based CI/CD
- **GitLab CI**: Integrated with GitLab

---

## 📚 Resources

See `resources.md` for:
- pytest documentation and best practices
- Great Expectations tutorials
- Evidently AI guides
- ML monitoring case studies

---

## ✅ Success Criteria

- [ ] Implemented unit tests for data preprocessing
- [ ] Created integration test for full pipeline
- [ ] Set up performance regression tests
- [ ] Deployed basic monitoring (data drift, latency)
- [ ] Created automated alert system
- [ ] Understand when to use each test type

**Track your progress in `progreso.md`**

---

## 🚀 Next Steps

1. Complete **hands-on exercises** in `actividad-interactiva.md`
2. Add tests to your **capstone project** (see `project-steps.md`)
3. Set up monitoring dashboard
4. Review criteria in `retroalimentacion.md`

---

**Ready to build bulletproof AI systems?** Testing and monitoring aren't glamorous, but they're what separates toy projects from production systems. Let's make reliability a habit! 🛡️
