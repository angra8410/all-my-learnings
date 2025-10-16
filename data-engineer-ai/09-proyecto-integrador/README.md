# Módulo 9: Proyecto Integrador

## Introducción

¡Bienvenido al módulo final! Aquí integrarás todos los conceptos aprendidos construyendo un **Sistema RAG Empresarial** completo, desde la ingesta de documentos hasta el despliegue en producción.

## Objetivos del Módulo

Al finalizar este módulo, habrás:

- 🎯 Construido un sistema RAG completo y funcional
- 🎯 Implementado pipeline ETL para documentos
- 🎯 Desplegado en AWS con arquitectura serverless
- 🎯 Aplicado buenas prácticas (testing, monitoring, logging)
- 🎯 Documentado el proyecto profesionalmente
- 🎯 Creado un portfolio piece para tu GitHub

## El Proyecto: Sistema RAG Empresarial

### Descripción

Construirás un sistema de Q&A que responde preguntas sobre documentación técnica usando RAG (Retrieval Augmented Generation).

**Funcionalidades:**
- ✅ Ingesta de documentos PDF, DOCX, TXT
- ✅ Procesamiento y chunking inteligente
- ✅ Generación de embeddings
- ✅ Almacenamiento en base vectorial
- ✅ API REST para hacer preguntas
- ✅ Sistema de búsqueda semántica
- ✅ Respuestas con referencias a fuentes
- ✅ Monitoreo y logging
- ✅ Despliegue en AWS

### Arquitectura

```
┌─────────────────┐
│   Documentos    │
│ (PDF/DOCX/TXT)  │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Pipeline Ingesta│ (Lambda)
│ - Extracción    │
│ - Chunking      │
│ - Embeddings    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Vector Store   │ (Pinecone/OpenSearch)
│   + Metadata    │
└────────┬────────┘
         │
         v
┌─────────────────┐     ┌──────────────┐
│   API Gateway   │────▶│ Lambda RAG   │
│  (REST API)     │     │ - Retrieval  │
└─────────────────┘     │ - Generation │
                        └──────┬───────┘
                               │
                               v
                        ┌──────────────┐
                        │AWS Bedrock/  │
                        │  OpenAI API  │
                        └──────────────┘
```

## Fase 1: Setup y Estructura del Proyecto

### Estructura de Carpetas

```
rag-enterprise-system/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── api_spec.md
│   └── deployment.md
├── src/
│   ├── __init__.py
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── document_processor.py
│   │   ├── chunker.py
│   │   └── embedder.py
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   ├── generation/
│   │   ├── __init__.py
│   │   └── generator.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── models.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_api.py
├── scripts/
│   ├── setup_vector_db.py
│   ├── ingest_documents.py
│   └── test_query.py
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── docker/
│       └── Dockerfile
└── notebooks/
    ├── exploration.ipynb
    └── evaluation.ipynb
```

### Setup Inicial

```bash
# Crear proyecto
mkdir rag-enterprise-system
cd rag-enterprise-system

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install fastapi uvicorn pandas langchain openai pinecone-client \
            python-multipart python-dotenv pydantic boto3 pytest

# Crear requirements.txt
pip freeze > requirements.txt

# Inicializar git
git init
git add .
git commit -m "Initial commit: RAG Enterprise System"
```

## Fase 2: Implementación del Sistema

### 1. Document Processor

```python
# src/ingestion/document_processor.py
from pathlib import Path
from typing import List, Dict
import PyPDF2
from docx import Document as DocxDocument

class DocumentProcessor:
    """Process documents of various formats"""
    
    def __init__(self):
        self.supported_formats = ['.pdf', '.docx', '.txt']
    
    def process_file(self, file_path: str) -> Dict:
        """
        Process a document file and extract text.
        
        Args:
            file_path: Path to document
        
        Returns:
            Dict with text and metadata
        """
        path = Path(file_path)
        
        if path.suffix not in self.supported_formats:
            raise ValueError(f"Unsupported format: {path.suffix}")
        
        if path.suffix == '.pdf':
            text = self._extract_pdf(file_path)
        elif path.suffix == '.docx':
            text = self._extract_docx(file_path)
        else:  # .txt
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        
        metadata = {
            'filename': path.name,
            'size': path.stat().st_size,
            'format': path.suffix,
            'char_count': len(text)
        }
        
        return {
            'text': text,
            'metadata': metadata
        }
    
    def _extract_pdf(self, path: str) -> str:
        """Extract text from PDF"""
        text = ""
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def _extract_docx(self, path: str) -> str:
        """Extract text from DOCX"""
        doc = DocxDocument(path)
        return "\n".join([para.text for para in doc.paragraphs])
```

### 2. Chunker

```python
# src/ingestion/chunker.py
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class SmartChunker:
    """Intelligent text chunking for optimal retrieval"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def chunk_text(self, text: str, metadata: Dict) -> List[Dict]:
        """
        Split text into chunks with metadata.
        
        Args:
            text: Text to chunk
            metadata: Document metadata
        
        Returns:
            List of chunks with metadata
        """
        chunks = self.splitter.split_text(text)
        
        return [
            {
                'text': chunk,
                'metadata': {
                    **metadata,
                    'chunk_id': i,
                    'total_chunks': len(chunks)
                }
            }
            for i, chunk in enumerate(chunks)
        ]
```

### 3. Vector Store Manager

```python
# src/retrieval/vector_store.py
import pinecone
from typing import List, Dict
from openai import OpenAI

class VectorStoreManager:
    """Manage vector database operations"""
    
    def __init__(self, index_name: str, api_key: str):
        pinecone.init(api_key=api_key)
        self.index = pinecone.Index(index_name)
        self.openai_client = OpenAI()
    
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for text"""
        response = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def upsert_chunks(self, chunks: List[Dict]) -> None:
        """Insert chunks into vector store"""
        vectors = []
        
        for chunk in chunks:
            embedding = self.generate_embedding(chunk['text'])
            
            vectors.append({
                'id': f"{chunk['metadata']['filename']}_{chunk['metadata']['chunk_id']}",
                'values': embedding,
                'metadata': {
                    'text': chunk['text'],
                    **chunk['metadata']
                }
            })
        
        # Batch upsert
        self.index.upsert(vectors)
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search for relevant chunks"""
        query_embedding = self.generate_embedding(query)
        
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        return [
            {
                'text': match['metadata']['text'],
                'score': match['score'],
                'source': match['metadata']['filename']
            }
            for match in results['matches']
        ]
```

### 4. RAG Generator

```python
# src/generation/generator.py
from openai import OpenAI
from typing import List, Dict

class RAGGenerator:
    """Generate answers using RAG"""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.client = OpenAI()
        self.model = model
    
    def generate_answer(self, question: str, context_chunks: List[Dict]) -> Dict:
        """
        Generate answer using retrieved context.
        
        Args:
            question: User question
            context_chunks: Retrieved relevant chunks
        
        Returns:
            Answer with sources
        """
        # Build context
        context = "\n\n".join([
            f"[Source: {chunk['source']}]\n{chunk['text']}"
            for chunk in context_chunks
        ])
        
        # Create prompt
        prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided context.
If the answer cannot be found in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}

Answer:"""
        
        # Generate response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        answer = response.choices[0].message.content
        
        return {
            'answer': answer,
            'sources': [chunk['source'] for chunk in context_chunks],
            'context_used': len(context_chunks)
        }
```

### 5. FastAPI Application

```python
# src/api/routes.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import os

from src.ingestion.document_processor import DocumentProcessor
from src.ingestion.chunker import SmartChunker
from src.retrieval.vector_store import VectorStoreManager
from src.generation.generator import RAGGenerator

app = FastAPI(title="RAG Enterprise System")

# Initialize components
processor = DocumentProcessor()
chunker = SmartChunker()
vector_store = VectorStoreManager(
    index_name=os.getenv("PINECONE_INDEX"),
    api_key=os.getenv("PINECONE_API_KEY")
)
generator = RAGGenerator()

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float

@app.post("/api/ingest")
async def ingest_document(file: UploadFile = File(...)):
    """
    Ingest a new document into the system.
    """
    try:
        # Save uploaded file
        file_path = f"/tmp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Process
        doc_data = processor.process_file(file_path)
        chunks = chunker.chunk_text(doc_data['text'], doc_data['metadata'])
        vector_store.upsert_chunks(chunks)
        
        return {
            "message": "Document ingested successfully",
            "filename": file.filename,
            "chunks_created": len(chunks)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query", response_model=QueryResponse)
async def query_system(request: QueryRequest):
    """
    Query the RAG system.
    """
    try:
        # Retrieve relevant chunks
        chunks = vector_store.search(request.question, top_k=request.top_k)
        
        if not chunks:
            return QueryResponse(
                answer="No relevant information found.",
                sources=[],
                confidence=0.0
            )
        
        # Generate answer
        result = generator.generate_answer(request.question, chunks)
        
        return QueryResponse(
            answer=result['answer'],
            sources=result['sources'],
            confidence=chunks[0]['score']
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```

## Fase 3: Testing

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from src.api.routes import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_query_endpoint():
    response = client.post(
        "/api/query",
        json={"question": "What is ETL?", "top_k": 3}
    )
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "sources" in response.json()
```

## Fase 4: Deployment

### Docker

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.routes:app", "--host", "0.0.0.0", "--port", "8000"]
```

### AWS Lambda con Serverless

```yaml
# serverless.yml
service: rag-system

provider:
  name: aws
  runtime: python3.11
  region: us-east-1

functions:
  query:
    handler: handler.query
    events:
      - http:
          path: query
          method: post
  
  ingest:
    handler: handler.ingest
    events:
      - s3:
          bucket: documents-bucket
          event: s3:ObjectCreated:*
```

## Fase 5: Documentación

### README.md Principal

```markdown
# RAG Enterprise System

Intelligent Q&A system using Retrieval Augmented Generation.

## Features
- Multi-format document ingestion (PDF, DOCX, TXT)
- Semantic search with vector database
- GPT-powered answer generation
- REST API
- Monitoring and logging

## Quick Start
```bash
git clone https://github.com/yourusername/rag-system
cd rag-system
pip install -r requirements.txt
cp .env.example .env  # Configure your keys
uvicorn src.api.routes:app --reload
```

## API Documentation
See [API_SPEC.md](docs/api_spec.md)

## Architecture
See [ARCHITECTURE.md](docs/architecture.md)

## Deployment
See [DEPLOYMENT.md](docs/deployment.md)

## License
MIT
```

## Criterios de Evaluación

### Funcionalidad (40%)
- [ ] Sistema ingesta documentos correctamente
- [ ] Búsqueda semántica funciona
- [ ] Genera respuestas coherentes
- [ ] API responde correctamente

### Código (30%)
- [ ] Código bien estructurado
- [ ] Funciones documentadas
- [ ] Manejo de errores
- [ ] Tests implementados

### Buenas Prácticas (20%)
- [ ] Logging implementado
- [ ] Variables de entorno
- [ ] Git commits descriptivos
- [ ] .gitignore apropiado

### Documentación (10%)
- [ ] README completo
- [ ] Docstrings en funciones
- [ ] Arquitectura documentada
- [ ] Instrucciones de setup claras

## Entregables

1. **Código en GitHub**
   - Repositorio público
   - README detallado
   - Commits significativos

2. **Demo**
   - Video de 3-5 minutos
   - O deploy funcional

3. **Documentación**
   - Architecture diagram
   - API specification
   - Deployment guide

4. **Presentación** (opcional)
   - Explicación del sistema
   - Decisiones de diseño
   - Lecciones aprendidas

## Extensiones Opcionales

### 🌟 Nivel Avanzado
- [ ] Implementar caching de queries
- [ ] Agregar autenticación JWT
- [ ] Multi-idioma support
- [ ] Feedback loop (thumbs up/down)
- [ ] Analytics dashboard

### 🚀 Nivel Experto
- [ ] Deploy en AWS con Terraform
- [ ] CI/CD pipeline completo
- [ ] Monitoring con Grafana
- [ ] A/B testing de modelos
- [ ] Rate limiting avanzado

## Recursos de Apoyo

- 📖 [FastAPI Docs](https://fastapi.tiangolo.com/)
- 📖 [LangChain RAG Guide](https://python.langchain.com/docs/use_cases/question_answering/)
- 🎥 [RAG System Tutorial](https://www.youtube.com/watch?v=example)
- 💬 Discord del curso para ayuda

---

**¡Felicitaciones por llegar al proyecto final!** 🎉

Este proyecto será la pieza central de tu portfolio. Tómate tu tiempo, hazlo bien, y estarás listo para roles de Data Engineer en IA.

**¡Mucho éxito!** 🚀
