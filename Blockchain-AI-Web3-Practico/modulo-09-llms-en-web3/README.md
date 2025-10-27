# Módulo 09: LLMs en Web3

## 🎯 Objetivos del Módulo

Este módulo te enseñará conceptos y prácticas avanzadas de LLMs en Web3 en el contexto de Blockchain y Web3.

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

**Siguiente**: Módulo 10

## 💬 LLM Mock Service

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ContractAnalysisRequest(BaseModel):
    contract_code: str
    analysis_type: str  # "security", "optimization", "explanation"

class LLMResponse(BaseModel):
    analysis: str
    suggestions: list[str]
    risk_level: str

@app.post("/llm/analyze-contract", response_model=LLMResponse)
async def analyze_contract(req: ContractAnalysisRequest):
    # Mock LLM response (en producción usar OpenAI/Anthropic API)
    
    if req.analysis_type == "security":
        return LLMResponse(
            analysis="Security analysis: Contract uses SafeMath and ReentrancyGuard. No obvious vulnerabilities detected.",
            suggestions=[
                "Consider adding access control",
                "Implement emergency pause mechanism",
                "Add input validation"
            ],
            risk_level="LOW"
        )
    
    elif req.analysis_type == "optimization":
        return LLMResponse(
            analysis="Gas optimization opportunities found.",
            suggestions=[
                "Use ++i instead of i++",
                "Cache array length in loops",
                "Use calldata instead of memory"
            ],
            risk_level="INFO"
        )
    
    else:
        return LLMResponse(
            analysis="This contract implements an ERC-20 token with transfer, approve, and transferFrom functions.",
            suggestions=["Add events for better tracking"],
            risk_level="INFO"
        )

@app.post("/llm/generate-test")
async def generate_test(contract_code: str):
    # Mock test generation
    test_template = '''
describe("Contract Tests", function () {
  it("Should deploy correctly", async function () {
    // Generated test
  });
});
'''
    return {"tests": test_template}

# docker-compose.yml para LLM service
"""
version: '3.8'

services:
  llm-service:
    build: ./llm-service
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=mock  # En prod usar real
    networks:
      - web3-net

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_LLM_API=http://llm-service:8000
    depends_on:
      - llm-service
    networks:
      - web3-net

networks:
  web3-net:
"""
```

## 🎨 Frontend Integration

```typescript
// components/ContractAnalyzer.tsx
import { useState } from 'react';

export function ContractAnalyzer() {
  const [code, setCode] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeContract = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/llm/analyze-contract', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contract_code: code,
          analysis_type: 'security'
        })
      });
      const data = await res.json();
      setAnalysis(data);
    } catch (error) {
      console.error('Analysis failed:', error);
    }
    setLoading(false);
  };

  return (
    <div>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste Solidity code here..."
        rows={20}
      />
      <button onClick={analyzeContract} disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze Contract'}
      </button>
      
      {analysis && (
        <div>
          <h3>Analysis Results</h3>
          <p>{analysis.analysis}</p>
          <h4>Suggestions:</h4>
          <ul>
            {analysis.suggestions.map((s, i) => <li key={i}>{s}</li>)}
          </ul>
          <p>Risk Level: {analysis.risk_level}</p>
        </div>
      )}
    </div>
  );
}
```
