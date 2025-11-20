# Week 14: Finance Case Study

## 💰 Persona: FinTech Data Scientist

*Hi! I'm your FinTech data scientist focused on extracting massive value from small improvements. In finance, a 0.1% improvement in fraud detection can save millions. I've built models that process billions of transactions, and I'll show you how to focus on what truly moves the needle. Remember: in FinTech, precision matters more than perfection.*

---

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. **Build fraud detection models** with >95% precision using the Pareto approach
2. **Implement risk scoring** for credit/loan decisions
3. **Detect anomalies** in financial transactions at scale
4. **Optimize for business metrics** (not just accuracy)
5. **Deploy financial ML** with proper compliance and monitoring

**Estimated Duration**: 4-5 hours of FinTech-focused ML

## 📋 Prerequisites

- Completed Week 13 (Orchestration & Production)
- Understanding of classification and anomaly detection
- Python with pandas, scikit-learn, imbalanced-learn

---

## �� Chain of Thought: Finance ML Challenges

### Step 1: Understanding the Finance Context

**Key Differences from General ML**:
- **Extreme class imbalance**: Fraud is ~0.1-1% of transactions
- **High cost of false positives**: Blocking legitimate transactions loses customers
- **Regulatory requirements**: GDPR, explainability, audit trails
- **Real-time requirements**: Decisions in <100ms
- **Adversarial environment**: Fraudsters adapt to detection

### Step 2: The Pareto Approach to Finance ML

**80% of fraud detection value comes from 20% of features:**

1. **Transaction patterns** (30% of value)
   - Amount deviation from normal
   - Velocity (transactions per hour)
   - Geographic anomalies

2. **User behavior** (25% of value)
   - Historical patterns
   - Account age
   - Typical transaction amounts

3. **Network features** (20% of value)
   - Connections to known fraud
   - Device fingerprints
   - IP reputation

4. **Temporal features** (15% of value)
   - Time of day
   - Day of week
   - Seasonal patterns

5. **Simple rules** (10% of value)
   - Blacklists
   - Amount thresholds
   - Geographic restrictions

---

## 🎯 Pareto Principle (20/80): Core Skills

### 1. Fraud Detection Pipeline (Critical)

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from imblearn.over_sampling import SMOTE

class FraudDetectionModel:
    """
    Production-ready fraud detection
    Optimized for precision (minimize false positives)
    """
    
    def __init__(self, precision_threshold=0.95):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=100,  # Prevent overfitting
            random_state=42
        )
        self.precision_threshold = precision_threshold
        self.scaler = None
        self.feature_names = None
        
    def create_features(self, df):
        """
        Engineer key fraud detection features (Pareto 20%)
        """
        features = df.copy()
        
        # Transaction amount features
        features['amount_log'] = np.log1p(features['amount'])
        features['amount_to_balance_ratio'] = features['amount'] / (features['balance'] + 1)
        
        # Velocity features (transactions in time window)
        features['tx_count_1h'] = features.groupby('user_id')['timestamp'].transform(
            lambda x: x.rolling('1H').count()
        )
        features['tx_sum_1h'] = features.groupby('user_id')['amount'].transform(
            lambda x: x.rolling('1H').sum()
        )
        
        # User historical features
        user_stats = features.groupby('user_id')['amount'].agg(['mean', 'std']).reset_index()
        user_stats.columns = ['user_id', 'user_avg_amount', 'user_std_amount']
        features = features.merge(user_stats, on='user_id', how='left')
        
        # Deviation from normal
        features['amount_deviation'] = np.abs(
            features['amount'] - features['user_avg_amount']
        ) / (features['user_std_amount'] + 1)
        
        # Time features
        features['hour'] = pd.to_datetime(features['timestamp']).dt.hour
        features['is_night'] = ((features['hour'] >= 22) | (features['hour'] <= 6)).astype(int)
        features['is_weekend'] = pd.to_datetime(features['timestamp']).dt.dayofweek >= 5
        
        # High-risk indicators
        features['is_high_amount'] = (features['amount'] > features['amount'].quantile(0.95)).astype(int)
        features['is_new_merchant'] = (features['merchant_id'].isin(
            features['merchant_id'].value_counts()[features['merchant_id'].value_counts() < 10].index
        )).astype(int)
        
        return features
    
    def train(self, X, y):
        """Train with SMOTE to handle class imbalance"""
        print(f"📊 Training data: {len(X)} samples, {y.sum()} frauds ({y.mean():.2%})")
        
        # Feature engineering
        X_features = self.create_features(X)
        
        # Select numerical features
        numeric_cols = X_features.select_dtypes(include=[np.number]).columns
        X_numeric = X_features[numeric_cols]
        
        # Handle class imbalance with SMOTE
        print("⚖️  Balancing classes with SMOTE...")
        smote = SMOTE(sampling_strategy=0.3, random_state=42)  # 30% fraud in training
        X_balanced, y_balanced = smote.fit_resample(X_numeric, y)
        
        print(f"   After SMOTE: {len(X_balanced)} samples, {y_balanced.sum()} frauds ({y_balanced.mean():.2%})")
        
        # Train model
        self.model.fit(X_balanced, y_balanced)
        self.feature_names = numeric_cols
        
        # Feature importance
        importances = pd.DataFrame({
            'feature': self.feature_names,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\n🔍 Top 5 Features:")
        for _, row in importances.head(5).iterrows():
            print(f"   {row['feature']}: {row['importance']:.3f}")
        
        return self
    
    def predict_proba(self, X):
        """Predict fraud probability"""
        X_features = self.create_features(X)
        X_numeric = X_features[self.feature_names]
        return self.model.predict_proba(X_numeric)[:, 1]
    
    def predict(self, X, threshold=0.5):
        """Predict fraud with custom threshold"""
        probas = self.predict_proba(X)
        return (probas >= threshold).astype(int)
    
    def optimize_threshold(self, X_val, y_val):
        """Find optimal threshold for target precision"""
        probas = self.predict_proba(X_val)
        
        # Try different thresholds
        thresholds = np.arange(0.1, 0.9, 0.05)
        results = []
        
        for thresh in thresholds:
            y_pred = (probas >= thresh).astype(int)
            
            precision = precision_score(y_val, y_pred, zero_division=0)
            recall = recall_score(y_val, y_pred, zero_division=0)
            f1 = f1_score(y_val, y_pred, zero_division=0)
            
            results.append({
                'threshold': thresh,
                'precision': precision,
                'recall': recall,
                'f1': f1
            })
        
        results_df = pd.DataFrame(results)
        
        # Find threshold that meets precision requirement
        valid_thresholds = results_df[results_df['precision'] >= self.precision_threshold]
        
        if len(valid_thresholds) > 0:
            # Choose threshold with highest recall among those meeting precision
            best = valid_thresholds.loc[valid_thresholds['recall'].idxmax()]
        else:
            # If can't meet precision, choose highest precision
            best = results_df.loc[results_df['precision'].idxmax()]
        
        print(f"\n🎯 Optimal Threshold: {best['threshold']:.2f}")
        print(f"   Precision: {best['precision']:.2%}")
        print(f"   Recall: {best['recall']:.2%}")
        print(f"   F1: {best['f1']:.2%}")
        
        return best['threshold']
    
    def evaluate(self, X_test, y_test, threshold=0.5):
        """Comprehensive evaluation"""
        y_pred = self.predict(X_test, threshold)
        y_proba = self.predict_proba(X_test)
        
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        # Calculate business metrics
        total_tx = len(y_test)
        actual_frauds = y_test.sum()
        detected_frauds = (y_test & y_pred).sum()
        false_positives = ((1 - y_test) & y_pred).sum()
        
        # Financial impact (example costs)
        avg_fraud_amount = 500  # $500 average fraud
        false_positive_cost = 10  # $10 per false positive (customer friction)
        
        frauds_prevented_value = detected_frauds * avg_fraud_amount
        false_positive_cost_total = false_positives * false_positive_cost
        net_value = frauds_prevented_value - false_positive_cost_total
        
        print("\n" + "="*60)
        print("📊 FRAUD DETECTION EVALUATION")
        print("="*60)
        print(f"\n🎯 Model Performance:")
        print(f"   Precision: {precision:.2%} (minimize false positives)")
        print(f"   Recall: {recall:.2%} (catch actual frauds)")
        print(f"   F1 Score: {f1:.2%}")
        
        print(f"\n📈 Detection Stats:")
        print(f"   Total transactions: {total_tx:,}")
        print(f"   Actual frauds: {actual_frauds:,} ({actual_frauds/total_tx:.2%})")
        print(f"   Detected frauds: {detected_frauds:,} ({detected_frauds/actual_frauds:.2%} of frauds)")
        print(f"   False positives: {false_positives:,} ({false_positives/total_tx:.2%} of total)")
        
        print(f"\n💰 Business Impact:")
        print(f"   Frauds prevented: ${frauds_prevented_value:,}")
        print(f"   False positive cost: ${false_positive_cost_total:,}")
        print(f"   Net value: ${net_value:,}")
        
        print("="*60 + "\n")
        
        return {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'net_value': net_value
        }

# Example usage
if __name__ == "__main__":
    # Simulate fraud data
    np.random.seed(42)
    n_samples = 10000
    n_frauds = 100  # 1% fraud rate
    
    # Create synthetic data
    data = {
        'user_id': np.random.randint(1, 1000, n_samples),
        'amount': np.random.exponential(100, n_samples),
        'balance': np.random.uniform(100, 5000, n_samples),
        'merchant_id': np.random.randint(1, 500, n_samples),
        'timestamp': pd.date_range('2024-01-01', periods=n_samples, freq='5T'),
    }
    df = pd.DataFrame(data)
    
    # Create fraud labels (frauds have different patterns)
    is_fraud = np.zeros(n_samples)
    fraud_indices = np.random.choice(n_samples, n_frauds, replace=False)
    is_fraud[fraud_indices] = 1
    
    # Frauds have higher amounts and unusual patterns
    df.loc[fraud_indices, 'amount'] *= 3
    
    # Split data
    train_size = int(0.6 * n_samples)
    val_size = int(0.2 * n_samples)
    
    X_train, y_train = df[:train_size], is_fraud[:train_size]
    X_val, y_val = df[train_size:train_size+val_size], is_fraud[train_size:train_size+val_size]
    X_test, y_test = df[train_size+val_size:], is_fraud[train_size+val_size:]
    
    # Train model
    model = FraudDetectionModel(precision_threshold=0.95)
    model.train(X_train, y_train)
    
    # Optimize threshold
    optimal_threshold = model.optimize_threshold(X_val, y_val)
    
    # Evaluate
    results = model.evaluate(X_test, y_test, threshold=optimal_threshold)
```

---

## 📚 Key Takeaways (Pareto Summary)

### The Vital 20% for FinTech ML:

1. **Optimize for business metrics** - Not just accuracy
2. **Handle class imbalance** - SMOTE, class weights, threshold tuning
3. **Feature engineering is king** - Velocity, deviation, patterns
4. **Precision > Recall** in most cases - False positives are expensive
5. **Explainability matters** - Regulatory compliance, customer trust

### Quick FinTech ML Checklist:
```
☐ Identify the business metric (fraud loss, approval rate, etc.)
☐ Engineer velocity and deviation features
☐ Handle extreme class imbalance
☐ Optimize threshold for business goals
☐ Measure financial impact, not just accuracy
☐ Add explainability for compliance
```

---

## 🚀 What's Next

1. **Complete exercises** in `actividad-interactiva.md` (fraud detection, risk scoring)
2. **Integrate into capstone** in `project-steps.md` (add financial ML use case)
3. **Track progress** in `progreso.md`

**Next Week**: Week 15 - Sports Case Study!

---

**Let's build financial ML that moves the bottom line!** 💰🚀
