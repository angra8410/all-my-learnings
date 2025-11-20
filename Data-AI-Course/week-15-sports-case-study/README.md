# Week 15: Sports Case Study

## 🏆 Persona: AI Sports Analyst

*Hey! I'm your AI sports analyst who uncovers actionable insights with minimal data and effort. I've helped teams win championships by finding the patterns others miss. Sports analytics is about telling compelling stories with data—let's turn numbers into victories!*

---

## 🎯 Learning Objectives

1. **Build player performance prediction models** with limited data
2. **Implement win probability** calculators
3. **Create sports dashboards** with compelling visualizations
4. **Optimize team strategies** using data-driven insights
5. **Deploy real-time analytics** for live games

**Duration**: 4-5 hours

---

## 🧠 Chain of Thought: Sports ML Strategy

### The Pareto Approach to Sports Analytics

**80% of insights from 20% of data:**

1. **Player Performance Metrics** (35%)
   - Points/goals per game
   - Shooting/scoring efficiency
   - Plus-minus ratings
   - Minutes played

2. **Team Statistics** (25%)
   - Win-loss records
   - Home vs away performance
   - Head-to-head history
   - Recent form (last 5-10 games)

3. **Contextual Features** (20%)
   - Opponent strength
   - Rest days
   - Injuries/suspensions
   - Weather (outdoor sports)

4. **Advanced Metrics** (15%)
   - Expected goals (xG)
   - Player efficiency rating
   - Usage rate
   - Defensive metrics

5. **Momentum Indicators** (5%)
   - Winning/losing streaks
   - Scoring runs
   - Comeback statistics

---

## 🎯 Quick Sports ML Implementation

### Player Performance Prediction

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

class PlayerPerformancePredictor:
    """Predict player points/performance for next game"""
    
    def __init__(self):
        self.model = GradientBoostingRegressor(n_estimators=100, max_depth=4)
    
    def create_features(self, player_data):
        """Engineer key features (Pareto 20%)"""
        df = player_data.copy()
        
        # Rolling averages (key pattern indicators)
        for window in [3, 5, 10]:
            df[f'avg_points_{window}g'] = df.groupby('player_id')['points'].transform(
                lambda x: x.rolling(window, min_periods=1).mean()
            )
        
        # Recent form
        df['last_3_avg'] = df.groupby('player_id')['points'].transform(
            lambda x: x.rolling(3).mean()
        )
        
        # Home vs away
        df['home_advantage'] = df['is_home'].astype(int)
        
        # Opponent strength
        df['opp_def_rating'] = df.groupby('opponent')['points_allowed'].transform('mean')
        
        # Rest days
        df['rest_days'] = df.groupby('player_id')['date'].diff().dt.days
        df['rest_days'] = df['rest_days'].fillna(2)
        
        # Minutes expectation
        df['usage_rate'] = df['minutes'] / 48  # Assuming 48 min game
        
        return df
    
    def train(self, X, y):
        """Train model"""
        X_features = self.create_features(X)
        feature_cols = [c for c in X_features.columns if c not in ['player_id', 'date', 'opponent']]
        
        self.model.fit(X_features[feature_cols], y)
        self.feature_cols = feature_cols
        
        # Feature importance
        importances = pd.DataFrame({
            'feature': feature_cols,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("🏀 Top Predictive Features:")
        for _, row in importances.head(5).iterrows():
            print(f"   {row['feature']}: {row['importance']:.3f}")
        
        return self
    
    def predict(self, X):
        """Predict player performance"""
        X_features = self.create_features(X)
        return self.model.predict(X_features[self.feature_cols])
    
    def evaluate(self, X_test, y_test):
        """Evaluate predictions"""
        y_pred = self.predict(X_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"\n📊 Model Performance:")
        print(f"   MAE: {mae:.2f} points")
        print(f"   R² Score: {r2:.2%}")
        print(f"   (Can predict within ±{mae:.1f} points on average)")
        
        return {'mae': mae, 'r2': r2}

# Win Probability Calculator
class WinProbabilityCalculator:
    """Real-time win probability during games"""
    
    def calculate_win_prob(self, current_state):
        """
        Calculate win probability based on:
        - Current score differential
        - Time remaining
        - Possession
        - Team strength ratings
        """
        score_diff = current_state['home_score'] - current_state['away_score']
        time_left = current_state['minutes_remaining']
        
        # Simple logistic model (Pareto approach)
        # Each point is worth more as time decreases
        time_factor = 1 + (1 / (time_left + 1))
        adjusted_diff = score_diff * time_factor
        
        # Convert to probability using logistic function
        win_prob = 1 / (1 + np.exp(-adjusted_diff / 10))
        
        return win_prob
```

---

## 📚 Key Takeaways

### The Vital 20% for Sports Analytics:

1. **Rolling averages are king** - Recent form predicts future performance
2. **Context matters** - Home/away, opponent, rest
3. **Visualize effectively** - Stories > numbers
4. **Real-time is powerful** - Live probability updates engage fans
5. **Keep it simple** - Complex models often overfit with limited data

---

## 🚀 What's Next

Complete exercises in `actividad-interactiva.md` and integrate into capstone via `project-steps.md`.

**Let's turn data into victories!** 🏆⚽🏀
