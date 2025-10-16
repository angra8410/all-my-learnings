# Módulo 4: RAG y Sistemas Agentic

## Introducción

En este módulo aprenderás a construir sistemas RAG (Retrieval Augmented Generation), la arquitectura más importante para aplicaciones de IA empresariales. También explorarás sistemas agentic que combinan LLMs con herramientas.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Entender la arquitectura RAG
- 🎯 Generar embeddings con OpenAI/Hugging Face
- 🎯 Trabajar con bases de datos vectoriales (Pinecone, Chroma)
- 🎯 Implementar búsqueda semántica
- 🎯 Construir un sistema RAG completo
- 🎯 Introducción a agentes y tools

## ¿Por qué es importante?

RAG es la solución a las "alucinaciones" de los LLMs. Permite que los modelos accedan a información actualizada y específica de tu dominio sin reentrenar.

## Conceptos Principales

### 1. Arquitectura RAG

```
Usuario → Query
    ↓
Convertir query a embedding (vector)
    ↓
Buscar en base vectorial (similarity search)
    ↓
Recuperar top-k documentos relevantes
    ↓
Combinar documentos + query en prompt
    ↓
LLM genera respuesta basada en contexto
    ↓
Respuesta al usuario
```

### 2. Embeddings

**¿Qué son?**
- Representación numérica de texto
- Capturan significado semántico
- Vectores de alta dimensión (ej: 1536 dimensiones)

**Generación con OpenAI**:
```python
from openai import OpenAI

client = OpenAI(api_key="tu-key")

def get_embedding(text: str) -> list:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Uso
embedding = get_embedding("Data engineering is important")
print(f"Vector de {len(embedding)} dimensiones")
```

**Con Hugging Face (gratis)**:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode("Data engineering is important")
print(f"Vector de {len(embedding)} dimensiones")
```

### 3. Bases de Datos Vectoriales

**Pinecone (Cloud)**:
```python
import pinecone

pinecone.init(api_key="tu-key")
index = pinecone.Index("mi-index")

# Insertar vectores
index.upsert(vectors=[
    ("id1", embedding1, {"text": "texto original"}),
    ("id2", embedding2, {"text": "otro texto"})
])

# Búsqueda
results = index.query(
    vector=query_embedding,
    top_k=5,
    include_metadata=True
)
```

**Chroma (Local)**:
```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("docs")

# Agregar documentos
collection.add(
    documents=["doc1", "doc2"],
    metadatas=[{"source": "file1"}, {"source": "file2"}],
    ids=["id1", "id2"]
)

# Búsqueda
results = collection.query(
    query_texts=["query"],
    n_results=5
)
```

### 4. Sistema RAG con LangChain

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 1. Crear vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

# 2. Crear retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# 3. Crear chain
llm = ChatOpenAI(model="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 4. Hacer pregunta
result = qa_chain({"query": "¿Qué es data engineering?"})
print(result['result'])
print(f"Fuentes: {result['source_documents']}")
```

### 5. Sistemas Agentic

**¿Qué son?**
- LLM que puede usar herramientas
- Decide qué herramienta usar según la tarea
- Ejemplos: calculadora, búsqueda web, APIs

**Agente simple con LangChain**:
```python
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

# Definir herramientas
tools = [
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Útil para cálculos matemáticos"
    ),
    Tool(
        name="Database",
        func=query_database,
        description="Busca información en la base de datos"
    )
]

# Crear agente
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Usar agente
agent.run("¿Cuál es el promedio de ventas en Q1 2024?")
```

## Implementación Práctica

### Sistema RAG Completo

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

class RAGSystem:
    def __init__(self, docs_path: str, persist_directory: str):
        self.docs_path = docs_path
        self.persist_directory = persist_directory
        self.vectorstore = None
        self.qa_chain = None
    
    def ingest_documents(self):
        """Carga e indexa documentos"""
        # Cargar documentos
        loader = DirectoryLoader(self.docs_path, glob="**/*.txt")
        documents = loader.load()
        
        # Dividir en chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        # Crear embeddings y store
        embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(
            chunks,
            embeddings,
            persist_directory=self.persist_directory
        )
        
        print(f"✅ Indexados {len(chunks)} chunks")
    
    def setup_qa_chain(self):
        """Configura el chain de Q&A"""
        if not self.vectorstore:
            raise ValueError("Primero debes ingestar documentos")
        
        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 5}
        )
        
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )
        
        print("✅ QA Chain configurado")
    
    def ask(self, question: str) -> dict:
        """Hace una pregunta al sistema"""
        if not self.qa_chain:
            raise ValueError("Primero debes configurar QA chain")
        
        result = self.qa_chain({"query": question})
        
        return {
            'answer': result['result'],
            'sources': [doc.metadata for doc in result['source_documents']]
        }

# Uso
rag = RAGSystem('./docs', './chroma_db')
rag.ingest_documents()
rag.setup_qa_chain()

response = rag.ask("¿Qué es ETL?")
print(f"Respuesta: {response['answer']}")
print(f"Fuentes: {response['sources']}")
```

## Mejores Prácticas

### 1. Optimización de Retrieval
```python
# Usar reranking para mejorar resultados
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)
```

### 2. Evaluation
```python
# Evaluar calidad de respuestas
from langchain.evaluation import load_evaluator

evaluator = load_evaluator("qa")
result = evaluator.evaluate_strings(
    prediction=response['answer'],
    reference="respuesta correcta",
    input=question
)
```

### 3. Caching
```python
# Cache para queries frecuentes
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_embedding(text: str):
    return get_embedding(text)
```

## De Open Source a Enterprise

| Aspecto | Open Source | Enterprise |
|---------|-------------|------------|
| **Vector DB** | Chroma, FAISS | Pinecone, Weaviate Cloud |
| **Embeddings** | Sentence Transformers | OpenAI, Cohere |
| **LLM** | Llama 2, Mistral | GPT-4, Claude |
| **Hosting** | Self-hosted | Managed services |

**Transferencia**: La arquitectura RAG es la misma, solo cambian las herramientas.

## Conceptos Clave

- 🔑 **RAG**: Retrieval Augmented Generation
- 🔑 **Embeddings**: Vectores que representan significado
- 🔑 **Vector DB**: Base de datos para búsqueda semántica
- 🔑 **Similarity Search**: Encontrar documentos similares
- 🔑 **Agentes**: LLMs que usan herramientas

## Próximos Pasos

En el **Módulo 5: AWS Bedrock** aprenderás:
- Usar modelos foundation en AWS
- Implementar RAG serverless
- Integración con servicios AWS
- Gestión de costos

## Recursos Adicionales

- 📖 [LangChain RAG Docs](https://python.langchain.com/docs/use_cases/question_answering/)
- 📖 [Pinecone Learning Center](https://www.pinecone.io/learn/)
- 🎥 [RAG Tutorial](https://www.youtube.com/watch?v=example)
- 📄 [RAG Paper](https://arxiv.org/abs/2005.11401)

---

**¡Excelente trabajo completando el Módulo 4!** 🎉

Ya sabes construir sistemas RAG. Continúa a [actividad-interactiva.md](actividad-interactiva.md).
