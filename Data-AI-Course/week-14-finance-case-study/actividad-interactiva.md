# Interactive Activities - Week 14: Finance Case Study

## 🎯 Objective
Build production-grade financial ML models focusing on fraud detection and risk scoring.

**Total Time**: 3-4 hours

---

## Exercise 1: Fraud Detection Model (Duration: 60 min)

### 🎯 Objective
Build a fraud detection model with >95% precision using the FraudDetectionModel from README.md.

### 📋 Tasks
1. Implement the complete FraudDetectionModel class
2. Create synthetic transaction data with 1% fraud rate
3. Engineer features: velocity, deviation, temporal patterns
4. Train with SMOTE to handle class imbalance
5. Optimize threshold for 95% precision
6. Calculate business impact ($ saved vs false positive cost)

### ✅ Validation
- [ ] Model achieves >90% precision
- [ ] Recall >50% (catches half of frauds)
- [ ] Net business value >$10,000
- [ ] Top features identified

---

## Exercise 2: Risk Scoring System (Duration: 45 min)

### 🎯 Objective
Build a credit risk scoring model for loan approvals.

### 📋 Implementation
```python
class RiskScorer:
    def calculate_risk_score(self, applicant):
        """Risk score 0-100 (0=lowest risk, 100=highest)"""
        score = 0
        
        # Credit history (40 points)
        if applicant['credit_score'] < 600:
            score += 40
        elif applicant['credit_score'] < 700:
            score += 20
        
        # Income stability (30 points)
        if applicant['employment_months'] < 12:
            score += 30
        elif applicant['employment_months'] < 36:
            score += 15
        
        # Debt-to-income ratio (30 points)
        dti = applicant['debt'] / applicant['income']
        if dti > 0.5:
            score += 30
        elif dti > 0.3:
            score += 15
        
        return score
    
    def make_decision(self, score):
        if score < 30:
            return 'APPROVED', 'Low risk'
        elif score < 60:
            return 'MANUAL_REVIEW', 'Medium risk'
        else:
            return 'DECLINED', 'High risk'
```

### ✅ Validation
- [ ] Risk scores calculated correctly
- [ ] Decisions align with business rules
- [ ] Can handle edge cases

---

## Exercise 3: Anomaly Detection (Duration: 45 min)

### 🎯 Objective
Detect unusual transactions using Isolation Forest.

### 📋 Implementation
```python
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01, random_state=42)
    
    def fit(self, transactions):
        features = self.create_features(transactions)
        self.model.fit(features)
    
    def detect(self, transactions):
        features = self.create_features(transactions)
        predictions = self.model.predict(features)
        scores = self.model.score_samples(features)
        
        # -1 = anomaly, 1 = normal
        anomalies = predictions == -1
        return anomalies, scores
```

### ✅ Validation
- [ ] Detects unusual patterns
- [ ] Low false positive rate (<2%)
- [ ] Identifies real anomalies

---

## Exercise 4: Financial ML Dashboard (Duration: 40 min)

### 🎯 Objective
Create monitoring dashboard for financial ML models.

### 📋 Metrics to Track
- Model performance (precision, recall)
- Business impact ($ saved, $ lost)
- Data drift detection
- Processing latency
- Alert frequency

### ✅ Validation
- [ ] All metrics displayed
- [ ] Real-time updates
- [ ] Alerts for issues

---

## 📋 Final Checklist

- [ ] Fraud detection model >90% precision
- [ ] Risk scoring system implemented
- [ ] Anomaly detection working
- [ ] Financial metrics calculated
- [ ] Business impact measured
- [ ] Ready for production deployment

**Total Time**: 3-3.5 hours

**Excellent work!** 🎉 Continue to `project-steps.md`
