# Módulo 08: AI Fundamentos para Web3

## 🎯 Objetivos del Módulo

Este módulo te enseñará conceptos y prácticas avanzadas de AI Fundamentos para Web3 en el contexto de Blockchain y Web3.

**Duración estimada**: 3-5 horas

## 📚 Contenido Principal

Ver `actividad-interactiva.md` para ejercicios prácticos accionables con código listo para copiar/pegar.

## 🔧 Ejemplos Prácticos

Todos los ejemplos incluyen:
- Código Solidity cuando aplique
- JavaScript/TypeScript para interacción
- Docker/docker-compose snippets donde sea relevante
- FastAPI examples para módulos de AI
- Tests y validaciones

## 💡 Conceptos Clave

- Concepto 1: Explicación práctica
- Concepto 2: Código ejecutable
- Concepto 3: Ejemplos reales
- Concepto 4: Mejores prácticas

## 🚀 Quick Start

```bash
# Setup básico
npm install
# o pip install para módulos Python/AI

# Ejecutar ejemplos
npm run example
# o python main.py
```

## 📋 Checklist de Aprendizaje

- [ ] Completar ejercicios prácticos
- [ ] Ejecutar todos los ejemplos de código
- [ ] Pasar tests de validación
- [ ] Construir mini-proyecto del módulo

## 🔗 Recursos Adicionales

- Documentación oficial relevante
- Tutoriales complementarios
- Comunidades y soporte

---

**¡Importante!** Este es un curso 90% práctico. Asegúrate de ejecutar cada ejemplo y completar los ejercicios hands-on.

**Siguiente**: Módulo 09

## 🤖 FastAPI ML Service (Mock)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PredictionRequest(BaseModel):
    volume: float
    liquidity: float
    volatility: float

class PredictionResponse(BaseModel):
    predicted_price: float
    confidence: float
    model_version: str

@app.post("/predict/price", response_model=PredictionResponse)
async def predict_price(req: PredictionRequest):
    # Mock prediction (en producción usar modelo real)
    base_price = 2000
    price = base_price + (req.volume * 0.01) - (req.volatility * 10)
    
    return PredictionResponse(
        predicted_price=price,
        confidence=0.85,
        model_version="mock_v1.0"
    )

@app.post("/analyze/transaction")
async def analyze_transaction(tx_hash: str, value: float):
    # Mock fraud detection
    risk_score = random.uniform(0, 1)
    is_suspicious = risk_score > 0.7
    
    return {
        "tx_hash": tx_hash,
        "risk_score": risk_score,
        "is_suspicious": is_suspicious,
        "flags": ["unusual_amount"] if is_suspicious else []
    }

# Dockerfile para el servicio
"""
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# requirements.txt
"""
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.4.2
"""
```

## 🔗 Conectar desde Smart Contract

```solidity
// Off-chain computation, on-chain verification
contract AIOracle {
    address public aiService;
    
    struct Prediction {
        uint256 price;
        uint256 confidence;
        uint256 timestamp;
    }
    
    mapping(bytes32 => Prediction) public predictions;
    
    function submitPrediction(
        bytes32 requestId,
        uint256 price,
        uint256 confidence
    ) external {
        require(msg.sender == aiService, "Unauthorized");
        predictions[requestId] = Prediction(price, confidence, block.timestamp);
    }
}
```
