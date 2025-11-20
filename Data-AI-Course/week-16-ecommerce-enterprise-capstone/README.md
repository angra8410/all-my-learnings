# Week 16: Ecommerce Enterprise Case Study

## 🛒 Persona: Ecommerce AI Lead

*Welcome! I'm your ecommerce AI lead who delivers rapid, measurable improvements at enterprise scale. I've built recommendation systems serving millions of users and increased conversion rates by 30%+. In ecommerce, personalization is everything—let's make every customer feel like the site was built just for them!*

---

## 🎯 Learning Objectives

1. **Build recommendation systems** (collaborative filtering, content-based)
2. **Implement customer churn prediction** to retain high-value users
3. **Create personalized experiences** at scale
4. **Optimize conversion funnels** using ML
5. **Deploy enterprise-grade ecommerce AI**

**Duration**: 4-5 hours (final capstone integration)

---

## 🧠 Chain of Thought: Ecommerce ML Strategy

### The Pareto Approach to Ecommerce AI

**80% of revenue impact from 20% of AI features:**

1. **Product Recommendations** (40% of value)
   - "You may also like"
   - Collaborative filtering
   - Personalized homepage
   - **ROI**: 20-30% increase in average order value

2. **Search & Discovery** (25% of value)
   - Smart search ranking
   - Auto-complete
   - Visual search
   - **ROI**: 15-20% increase in conversion

3. **Personalization** (20% of value)
   - Dynamic pricing
   - Email campaigns
   - Landing page customization
   - **ROI**: 10-25% increase in engagement

4. **Churn Prevention** (10% of value)
   - At-risk customer identification
   - Win-back campaigns
   - Retention offers
   - **ROI**: 5-10% reduction in churn

5. **Inventory Optimization** (5% of value)
   - Demand forecasting
   - Stock management
   - Dynamic reordering

---

## 🎯 Core Implementations

### 1. Recommendation Engine (Most Critical)

```python
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class EcommerceRecommender:
    """
    Hybrid recommendation system
    Combines collaborative filtering + content-based
    """
    
    def __init__(self, min_interactions=5):
        self.min_interactions = min_interactions
        self.user_item_matrix = None
        self.item_features = None
        self.user_similarity = None
        self.item_similarity = None
    
    def fit(self, interactions, item_features=None):
        """
        Train recommender on user-item interactions
        interactions: DataFrame with [user_id, item_id, rating/interaction_strength]
        """
        # Create user-item matrix
        self.user_item_matrix = interactions.pivot_table(
            index='user_id',
            columns='item_id',
            values='rating',
            fill_value=0
        )
        
        # Calculate user similarity (collaborative filtering)
        self.user_similarity = cosine_similarity(self.user_item_matrix)
        
        # Calculate item similarity
        self.item_similarity = cosine_similarity(self.user_item_matrix.T)
        
        # Store item features for content-based recommendations
        if item_features is not None:
            self.item_features = item_features
        
        print(f"✅ Trained on {len(self.user_item_matrix)} users, {len(self.user_item_matrix.columns)} items")
        
        return self
    
    def recommend_for_user(self, user_id, n_recommendations=5, method='hybrid'):
        """
        Generate personalized recommendations
        method: 'collaborative', 'content', or 'hybrid'
        """
        if user_id not in self.user_item_matrix.index:
            # New user - recommend popular items
            return self._recommend_popular(n_recommendations)
        
        if method == 'collaborative' or method == 'hybrid':
            collab_recs = self._collaborative_filtering(user_id, n_recommendations)
        
        if method == 'content' and self.item_features is not None:
            content_recs = self._content_based(user_id, n_recommendations)
        
        if method == 'hybrid':
            # Combine both approaches
            return self._combine_recommendations(collab_recs, content_recs, n_recommendations)
        elif method == 'collaborative':
            return collab_recs
        elif method == 'content':
            return content_recs
    
    def _collaborative_filtering(self, user_id, n):
        """Recommend based on similar users"""
        user_idx = self.user_item_matrix.index.get_loc(user_id)
        similar_users = self.user_similarity[user_idx]
        
        # Get top similar users
        similar_user_indices = np.argsort(similar_users)[::-1][1:21]  # Top 20 similar users
        
        # Aggregate their ratings
        recommendations = {}
        user_interactions = set(self.user_item_matrix.loc[user_id][self.user_item_matrix.loc[user_id] > 0].index)
        
        for similar_idx in similar_user_indices:
            similar_user_id = self.user_item_matrix.index[similar_idx]
            similarity_score = similar_users[similar_idx]
            
            # Get items this similar user liked
            liked_items = self.user_item_matrix.loc[similar_user_id]
            liked_items = liked_items[liked_items > 0]
            
            for item_id, rating in liked_items.items():
                if item_id not in user_interactions:
                    if item_id not in recommendations:
                        recommendations[item_id] = 0
                    recommendations[item_id] += rating * similarity_score
        
        # Sort and return top N
        top_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n]
        return [item_id for item_id, score in top_items]
    
    def _recommend_popular(self, n):
        """Recommend popular items for new users"""
        item_popularity = self.user_item_matrix.sum(axis=0)
        return item_popularity.nlargest(n).index.tolist()
    
    def _combine_recommendations(self, collab, content, n):
        """Combine collaborative and content-based recommendations"""
        # Simple approach: alternate between sources
        combined = []
        for i in range(n):
            if i < len(collab) and collab[i] not in combined:
                combined.append(collab[i])
            if len(combined) >= n:
                break
            if i < len(content) and content[i] not in combined:
                combined.append(content[i])
            if len(combined) >= n:
                break
        return combined[:n]
    
    def evaluate(self, test_interactions, n_recommendations=5):
        """
        Evaluate recommendation quality
        Metrics: Precision@K, Recall@K, Coverage
        """
        precisions = []
        recalls = []
        recommended_items = set()
        
        for user_id in test_interactions['user_id'].unique():
            if user_id not in self.user_item_matrix.index:
                continue
            
            # Get actual items user interacted with
            actual_items = set(test_interactions[test_interactions['user_id'] == user_id]['item_id'])
            
            # Get recommendations
            recs = self.recommend_for_user(user_id, n_recommendations)
            recommended_items.update(recs)
            
            # Calculate precision and recall
            hits = len(set(recs) & actual_items)
            precision = hits / len(recs) if recs else 0
            recall = hits / len(actual_items) if actual_items else 0
            
            precisions.append(precision)
            recalls.append(recall)
        
        # Calculate metrics
        avg_precision = np.mean(precisions)
        avg_recall = np.mean(recalls)
        coverage = len(recommended_items) / len(self.user_item_matrix.columns)
        
        print(f"\n📊 Recommendation Quality:")
        print(f"   Precision@{n_recommendations}: {avg_precision:.2%}")
        print(f"   Recall@{n_recommendations}: {avg_recall:.2%}")
        print(f"   Coverage: {coverage:.2%}")
        print(f"   (Recommending {len(recommended_items)} unique items)")
        
        return {
            'precision': avg_precision,
            'recall': avg_recall,
            'coverage': coverage
        }

# Churn Prediction
class ChurnPredictor:
    """Predict customer churn risk"""
    
    def __init__(self):
        from sklearn.ensemble import GradientBoostingClassifier
        self.model = GradientBoostingClassifier(n_estimators=100)
    
    def create_features(self, customer_data):
        """Engineer churn prediction features"""
        df = customer_data.copy()
        
        # Recency, Frequency, Monetary (RFM)
        df['days_since_last_purchase'] = (pd.Timestamp.now() - df['last_purchase_date']).dt.days
        df['purchase_frequency'] = df['total_orders'] / df['days_as_customer']
        df['avg_order_value'] = df['total_revenue'] / df['total_orders']
        
        # Engagement metrics
        df['email_open_rate'] = df['emails_opened'] / (df['emails_sent'] + 1)
        df['cart_abandonment_rate'] = df['carts_abandoned'] / (df['carts_created'] + 1)
        
        # Trend indicators
        df['revenue_trend'] = df['revenue_last_30d'] - df['revenue_30_60d']
        df['order_trend'] = df['orders_last_30d'] - df['orders_30_60d']
        
        return df
    
    def predict_churn_risk(self, customer_data):
        """Predict churn probability"""
        features = self.create_features(customer_data)
        churn_prob = self.model.predict_proba(features)[:, 1]
        
        # Segment by risk
        def risk_segment(prob):
            if prob > 0.7:
                return 'HIGH_RISK'
            elif prob > 0.4:
                return 'MEDIUM_RISK'
            else:
                return 'LOW_RISK'
        
        features['churn_probability'] = churn_prob
        features['risk_segment'] = features['churn_probability'].apply(risk_segment)
        
        return features[['customer_id', 'churn_probability', 'risk_segment']]
```

---

## 📚 Key Takeaways

### The Vital 20% for Ecommerce AI:

1. **Start with recommendations** - Highest ROI (20-30% increase in AOV)
2. **Measure business metrics** - Revenue, conversion, retention (not just accuracy)
3. **Personalize everything** - Homepage, emails, search, pricing
4. **Prevent churn proactively** - Identify at-risk customers early
5. **A/B test continuously** - Data-driven optimization

### Ecommerce ML Success Formula:
```
1. Deploy recommendations (Week 1)
2. Measure lift in AOV and conversion (Week 2-3)
3. Add personalization layers (Month 2)
4. Implement churn prevention (Month 3)
5. Scale and optimize (Ongoing)
```

---

## 🚀 What's Next

This is your final week! Complete all exercises and fully integrate everything into your capstone project for the final demo.

**Let's build ecommerce AI that drives real revenue!** 🛒💰🚀
