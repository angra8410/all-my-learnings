# Módulo 6: ML Pipelines y Experiments

## Introducción

En este módulo aprenderás a crear pipelines de Machine Learning end-to-end, gestionar experimentos, versionar modelos y preparar sistemas de ML para producción usando herramientas modernas como MLflow.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Diseñar pipelines de ML completos
- 🎯 Usar MLflow para tracking de experimentos
- 🎯 Versionar modelos y datasets
- 🎯 Implementar feature stores
- 🎯 Monitorear modelos en producción
- 🎯 Detectar data drift y model drift

## ¿Por qué es importante?

Los modelos de ML en producción requieren más que solo entrenarlos. Necesitas reproducibilidad, versionado, monitoreo y un ciclo de vida gestionado. MLOps es la respuesta.

## Conceptos Principales

### 1. Pipeline de ML End-to-End

```
Datos Raw → Limpieza → Feature Engineering → Entrenamiento
    ↓           ↓              ↓                  ↓
Validación  Validación   Feature Store      Versionado
    ↓
Evaluación → Registro → Deployment → Monitoreo
```

### 2. MLflow: Gestión del Ciclo de Vida

**Componentes de MLflow**:
- **Tracking**: Registra experimentos y métricas
- **Projects**: Empaqueta código reproducible
- **Models**: Gestiona y despliega modelos
- **Model Registry**: Versionado de modelos

**Setup básico**:
```bash
pip install mlflow
mlflow ui  # Corre en http://localhost:5000
```

### 3. Tracking de Experimentos

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Iniciar experimento
mlflow.set_experiment("sentiment-classification")

with mlflow.start_run(run_name="rf-baseline"):
    # Parámetros
    params = {
        "n_estimators": 100,
        "max_depth": 10,
        "min_samples_split": 2
    }
    mlflow.log_params(params)
    
    # Entrenar modelo
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    
    # Evaluar
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average='weighted')
    
    # Log métricas
    mlflow.log_metrics({
        "accuracy": accuracy,
        "f1_score": f1
    })
    
    # Guardar modelo
    mlflow.sklearn.log_model(model, "model")
    
    # Artifacts adicionales
    mlflow.log_artifact("feature_importance.png")
    
print(f"Run ID: {mlflow.active_run().info.run_id}")
```

### 4. Feature Engineering Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

# Pipeline de features
feature_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1000)),
    ('scaler', StandardScaler(with_mean=False))
])

# Entrenar y transformar
X_train_features = feature_pipeline.fit_transform(X_train)
X_test_features = feature_pipeline.transform(X_test)

# Guardar pipeline con el modelo
import joblib
joblib.dump(feature_pipeline, 'feature_pipeline.pkl')
mlflow.log_artifact('feature_pipeline.pkl')
```

### 5. Feature Store

**¿Qué es?**
- Repositorio centralizado de features
- Features consistentes entre training e inferencia
- Reutilización de features

**Implementación simple**:
```python
import pandas as pd
from datetime import datetime

class SimpleFeatureStore:
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
    
    def register_features(self, name: str, df: pd.DataFrame):
        """Registra un grupo de features"""
        feature_path = f"{self.storage_path}/{name}.parquet"
        df.to_parquet(feature_path)
        
        # Metadata
        metadata = {
            'name': name,
            'columns': list(df.columns),
            'shape': df.shape,
            'created_at': datetime.now().isoformat()
        }
        
        with open(f"{self.storage_path}/{name}_meta.json", 'w') as f:
            json.dump(metadata, f)
    
    def get_features(self, name: str) -> pd.DataFrame:
        """Recupera features"""
        return pd.read_parquet(f"{self.storage_path}/{name}.parquet")

# Uso
store = SimpleFeatureStore('./feature_store')

# Registrar
features = pd.DataFrame({
    'user_id': [1, 2, 3],
    'total_purchases': [10, 5, 20],
    'avg_purchase_value': [100, 50, 150]
})
store.register_features('user_features', features)

# Recuperar
user_features = store.get_features('user_features')
```

### 6. Model Registry

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Registrar modelo
model_uri = f"runs:/{run_id}/model"
registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="sentiment-classifier"
)

# Transiciones de stage
client.transition_model_version_stage(
    name="sentiment-classifier",
    version=1,
    stage="Staging"  # Staging -> Production
)

# Cargar modelo en producción
model_prod = mlflow.pyfunc.load_model(
    model_uri="models:/sentiment-classifier/Production"
)

# Hacer predicción
prediction = model_prod.predict(new_data)
```

### 7. Versionado de Datasets

**Con DVC (Data Version Control)**:
```bash
# Instalar
pip install dvc

# Inicializar
dvc init

# Trackear dataset
dvc add data/raw/dataset.csv
git add data/raw/dataset.csv.dvc .gitignore
git commit -m "Add dataset v1"

# Configurar remote storage
dvc remote add -d storage s3://my-bucket/dvc-store
dvc push
```

**En MLflow**:
```python
import mlflow

with mlflow.start_run():
    # Log dataset
    mlflow.log_artifact("data/train.csv", "datasets")
    
    # O usar mlflow.data
    from mlflow.data.pandas_dataset import PandasDataset
    
    dataset = PandasDataset(df, source="training_data_v1")
    mlflow.log_input(dataset, context="training")
```

### 8. Monitoreo de Modelos

**Detectar drift**:
```python
from scipy.stats import ks_2samp

def detect_drift(reference_data, current_data, threshold=0.05):
    """Detecta drift usando Kolmogorov-Smirnov test"""
    drifted_features = []
    
    for feature in reference_data.columns:
        statistic, p_value = ks_2samp(
            reference_data[feature],
            current_data[feature]
        )
        
        if p_value < threshold:
            drifted_features.append(feature)
    
    return drifted_features

# Uso
drifted = detect_drift(train_data, production_data)
if drifted:
    print(f"⚠️ Drift detectado en: {drifted}")
    # Alertar o reentrenar
```

**Monitoreo de predicciones**:
```python
import mlflow

def log_prediction(model_name, input_data, prediction, actual=None):
    """Log predicción para monitoreo"""
    with mlflow.start_run(run_name="inference"):
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("timestamp", datetime.now().isoformat())
        mlflow.log_metric("prediction", prediction)
        
        if actual is not None:
            error = abs(prediction - actual)
            mlflow.log_metric("error", error)
```

## Implementación Práctica

### Pipeline ML Completo

```python
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

class MLPipeline:
    def __init__(self, experiment_name: str):
        mlflow.set_experiment(experiment_name)
        self.model = None
    
    def load_data(self, path: str):
        """Carga datos"""
        self.df = pd.read_csv(path)
        mlflow.log_param("data_path", path)
        mlflow.log_param("data_shape", self.df.shape)
    
    def preprocess(self):
        """Preprocesa datos"""
        # Feature engineering
        self.df['feature_1'] = self.df['col1'] * self.df['col2']
        
        # Split
        X = self.df.drop('target', axis=1)
        y = self.df['target']
        
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(X, y, test_size=0.2, random_state=42)
        
        mlflow.log_params({
            "train_size": len(self.X_train),
            "test_size": len(self.X_test)
        })
    
    def train(self, params: dict):
        """Entrena modelo"""
        with mlflow.start_run(run_name="training"):
            mlflow.log_params(params)
            
            self.model = RandomForestClassifier(**params)
            self.model.fit(self.X_train, self.y_train)
            
            # Evaluar
            train_score = self.model.score(self.X_train, self.y_train)
            test_score = self.model.score(self.X_test, self.y_test)
            
            mlflow.log_metrics({
                "train_accuracy": train_score,
                "test_accuracy": test_score
            })
            
            # Guardar modelo
            mlflow.sklearn.log_model(
                self.model,
                "model",
                registered_model_name="my-classifier"
            )
            
            return test_score
    
    def evaluate(self):
        """Evaluación detallada"""
        predictions = self.model.predict(self.X_test)
        report = classification_report(self.y_test, predictions)
        
        # Log report
        with open("classification_report.txt", "w") as f:
            f.write(report)
        mlflow.log_artifact("classification_report.txt")
        
        print(report)

# Ejecutar pipeline
pipeline = MLPipeline("my-ml-experiment")
pipeline.load_data("data.csv")
pipeline.preprocess()

# Probar varios hiperparámetros
for n_est in [50, 100, 200]:
    params = {
        "n_estimators": n_est,
        "max_depth": 10,
        "random_state": 42
    }
    score = pipeline.train(params)
    print(f"n_estimators={n_est}, score={score:.4f}")

pipeline.evaluate()
```

## Mejores Prácticas

### 1. Reproducibilidad
```python
# Fijar seeds
import random
import numpy as np

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    # Si usas torch: torch.manual_seed(seed)

set_seed(42)
```

### 2. Validación Cruzada
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
mlflow.log_metrics({
    "cv_mean": scores.mean(),
    "cv_std": scores.std()
})
```

### 3. Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy'
)

with mlflow.start_run():
    grid_search.fit(X_train, y_train)
    
    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("best_score", grid_search.best_score_)
```

## De Open Source a Enterprise

| Aspecto | Open Source | Enterprise |
|---------|-------------|------------|
| **Experiment Tracking** | MLflow | SageMaker, Weights & Biases |
| **Model Registry** | MLflow | AWS Model Registry, Databricks |
| **Feature Store** | Feast | SageMaker Feature Store |
| **Monitoring** | Evidently | DataRobot, Arize |

**Transferencia**: Los conceptos de versionado, tracking y monitoreo son universales.

## Conceptos Clave

- 🔑 **MLflow**: Plataforma open source para MLOps
- 🔑 **Experiment Tracking**: Registro de experimentos
- 🔑 **Model Registry**: Versionado de modelos
- 🔑 **Feature Store**: Repositorio de features
- 🔑 **Drift**: Cambio en distribución de datos
- 🔑 **MLOps**: DevOps para ML

## Próximos Pasos

En el **Módulo 7: Buenas Prácticas** aprenderás:
- Testing de pipelines y modelos
- CI/CD para ML
- Logging y monitoring
- Data quality

## Recursos Adicionales

- 📖 [MLflow Docs](https://mlflow.org/docs/latest/index.html)
- 📖 [Feast Feature Store](https://docs.feast.dev/)
- 📖 [DVC Documentation](https://dvc.org/doc)
- 📚 "Building Machine Learning Pipelines" - O'Reilly

---

**¡Excelente trabajo completando el Módulo 6!** 🎉

Ya sabes gestionar el ciclo de vida de ML. Continúa a [actividad-interactiva.md](actividad-interactiva.md).
