# Week 02: Solving Natural Language Problems with RAG & Semantic Search

## 👤 Persona
**You are an expert data scientist and AI engineer with a passion for helping developers master foundational retrieval-augmented generation (RAG) skills. You explain complex concepts in clear, friendly language and always encourage hands-on experimentation. You focus on practical, production-ready solutions that deliver maximum impact with minimal complexity.**

## 🧠 Chain of Thought Approach
This week, we'll walk through RAG and semantic search step-by-step:
1. First, understand **why** RAG is the highest-leverage technique for LLM applications
2. Then, learn the **core components** that make up 80% of RAG systems
3. Next, implement **vector search** using the most popular, battle-tested tools
4. Finally, **integrate** these patterns into real-world applications

## 🎯 Learning Objectives

By the end of this week, you will be able to:

1. Understand and implement Retrieval-Augmented Generation (RAG) patterns
2. Build semantic search systems using vector embeddings
3. Work with vector databases (FAISS, Weaviate, Pinecone)
4. Create production-ready RAG pipelines
5. Optimize retrieval performance using the Pareto 80/20 approach
6. Integrate RAG into AI workflows and capstone projects

**Estimated Duration**: 4-5 hours

## 🚀 Why RAG Matters (Pareto Context)

RAG is the **single most important pattern** in modern LLM applications because it:
- ✅ Solves the **hallucination problem** by grounding responses in real data
- ✅ Enables LLMs to access **up-to-date information** beyond training cutoffs
- ✅ Works with **private/proprietary data** without expensive fine-tuning
- ✅ Delivers **90% of custom AI value** with 10% of the effort vs. fine-tuning

**Think of RAG as giving your LLM a search engine for your data** — it's that fundamental.

## 📋 Prerequisites

- Completed Week 00 (environment setup) and Week 01 (prompt engineering)
- Working OpenAI or Anthropic API access
- Python 3.9+
- Basic understanding of embeddings (we'll cover this)
- 8GB+ RAM (for local vector databases)

## 🎓 Key Concepts

### 1. What is RAG? (The Vital Few Concepts)

**RAG = Retrieval + Augmentation + Generation**

```
User Query → [Retrieve Relevant Docs] → [Augment Prompt] → [Generate Answer]
```

#### The Three Steps (Focus Here):
1. **Retrieve**: Find relevant documents using semantic search
2. **Augment**: Inject retrieved context into the prompt
3. **Generate**: LLM generates answer grounded in context

### 2. Semantic Search vs. Keyword Search

**Why Semantic Search Wins:**

| Approach | Query: "How do I reset my password?" | Found? |
|----------|--------------------------------------|--------|
| Keyword Search | Matches: "password reset" | ✅ Maybe |
| Semantic Search | Matches: "recover account access" | ✅ Yes! |

**Key Insight**: Semantic search understands **meaning**, not just words.

### 3. Vector Embeddings (20% You Need to Know)

**Embeddings convert text → numbers** that capture meaning:

```python
# Text
text = "The quick brown fox"

# Embedding (simplified)
embedding = [0.23, -0.45, 0.89, ..., 0.12]  # Usually 1536 dimensions

# Similar texts have similar embeddings
text2 = "A fast auburn canine"  # Similar meaning → similar vector
```

**What You Need to Know:**
- Embeddings are **dense vectors** (arrays of floats)
- Similar texts have **close vectors** (measured by cosine similarity)
- You **don't** need to understand the math deeply
- You **do** need to know how to generate and compare them

### 4. Vector Databases (The Essential Tools)

Focus on these **three options** (80% of use cases):

| Database | Best For | Setup | Cost |
|----------|----------|-------|------|
| **FAISS** | Local dev, prototyping | Easy | Free |
| **Pinecone** | Production, scale | Medium | Paid |
| **Weaviate** | Self-hosted, features | Medium | Free/Paid |

**Pareto Recommendation**: Start with **FAISS** for learning, move to **Pinecone** for production.

## 🛠️ Building Your First RAG System

### Step 1: Generate Embeddings

```python
from openai import OpenAI

client = OpenAI()

def get_embedding(text: str, model="text-embedding-3-small"):
    """Generate embedding for text. Use small model for cost efficiency."""
    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

# Example
text = "RAG enables LLMs to access external knowledge"
embedding = get_embedding(text)
print(f"Embedding dimension: {len(embedding)}")  # 1536
```

**Pro Tip**: Use `text-embedding-3-small` (1536 dims) for **most use cases**. It's 10x cheaper than large models and works for 80% of scenarios.

### Step 2: Build a Simple Vector Store with FAISS

```python
import faiss
import numpy as np
from typing import List, Tuple

class SimpleVectorStore:
    """Lightweight vector store using FAISS."""
    
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)  # L2 distance
        self.documents = []
    
    def add_documents(self, texts: List[str], embeddings: np.ndarray):
        """Add documents and their embeddings to the store."""
        self.index.add(embeddings)
        self.documents.extend(texts)
    
    def search(self, query_embedding: np.ndarray, k: int = 3) -> List[Tuple[str, float]]:
        """Search for k most similar documents."""
        distances, indices = self.index.search(query_embedding, k)
        
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(dist)))
        
        return results

# Usage
store = SimpleVectorStore()

# Add documents
docs = [
    "RAG helps reduce hallucinations in LLM responses",
    "Vector databases store embeddings for fast retrieval",
    "Semantic search finds documents by meaning, not keywords"
]

# Generate embeddings for all docs
doc_embeddings = np.array([get_embedding(doc) for doc in docs])
store.add_documents(docs, doc_embeddings)

# Search
query = "How to prevent false information from AI?"
query_emb = np.array([get_embedding(query)])
results = store.search(query_emb, k=2)

for doc, score in results:
    print(f"Score: {score:.2f} | Doc: {doc}")
```

### Step 3: Build a Complete RAG Pipeline

```python
from openai import OpenAI
from typing import List

client = OpenAI()

class RAGPipeline:
    """Production-ready RAG pipeline focusing on the vital few components."""
    
    def __init__(self, vector_store: SimpleVectorStore):
        self.vector_store = vector_store
        self.client = OpenAI()
    
    def retrieve(self, query: str, k: int = 3) -> List[str]:
        """Retrieve relevant documents."""
        query_embedding = np.array([get_embedding(query)])
        results = self.vector_store.search(query_embedding, k)
        return [doc for doc, _ in results]
    
    def augment_prompt(self, query: str, context_docs: List[str]) -> str:
        """Create augmented prompt with retrieved context."""
        context = "\n\n".join([f"Document {i+1}: {doc}" 
                               for i, doc in enumerate(context_docs)])
        
        prompt = f"""Answer the question based on the context below.
        If the answer cannot be found in the context, say "I don't have enough information."

Context:
{context}

Question: {query}

Answer:"""
        return prompt
    
    def generate(self, prompt: str) -> str:
        """Generate response using LLM."""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # Fast and cost-effective for most cases
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers based on provided context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Low temperature for factual responses
        )
        return response.choices[0].message.content
    
    def query(self, question: str, k: int = 3) -> dict:
        """End-to-end RAG query."""
        # 1. Retrieve
        context_docs = self.retrieve(question, k)
        
        # 2. Augment
        augmented_prompt = self.augment_prompt(question, context_docs)
        
        # 3. Generate
        answer = self.generate(augmented_prompt)
        
        return {
            "question": question,
            "answer": answer,
            "sources": context_docs
        }

# Usage
rag = RAGPipeline(store)
result = rag.query("What does RAG help with?")

print(f"Question: {result['question']}")
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
```

## 🎯 Pareto Principle (80/20 for RAG)

### 20% of Techniques That Deliver 80% of Value

#### 1. **Chunking Strategy** (Most Critical)
Split documents effectively:

```python
def chunk_text_simple(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Simple chunking - works for 80% of cases."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # Overlap prevents split sentences
    return chunks

# Use this for most documents
# Adjust chunk_size based on your needs:
# - 200-300: Short, precise chunks (Q&A)
# - 500-800: Medium chunks (general docs)
# - 1000+: Long chunks (detailed articles)
```

#### 2. **Hybrid Search** (Simple but Powerful)
Combine semantic + keyword search:

```python
from rank_bm25 import BM25Okapi

def hybrid_search(query: str, semantic_results: List[str], 
                  keyword_results: List[str], alpha: float = 0.5) -> List[str]:
    """Combine semantic and keyword search (simple version)."""
    # Simple approach: take top from each and merge
    combined = list(set(semantic_results[:3] + keyword_results[:3]))
    return combined[:5]  # Return top 5

# This simple approach outperforms pure semantic search in many cases
```

#### 3. **Reranking** (Easy Wins)
Rerank retrieved documents for better relevance:

```python
def rerank_simple(query: str, documents: List[str]) -> List[str]:
    """Simple reranking based on query overlap."""
    query_words = set(query.lower().split())
    
    scored = []
    for doc in documents:
        doc_words = set(doc.lower().split())
        overlap = len(query_words & doc_words) / len(query_words)
        scored.append((doc, overlap))
    
    # Sort by score
    scored.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in scored]

# For production: Use Cohere Rerank API or similar
```

### 80% of Practice (Focus Your Time Here)

1. **Build 5 RAG pipelines** for different document types:
   - Technical documentation
   - Customer support FAQs
   - Product catalogs
   - Meeting notes
   - Research papers

2. **Experiment with chunk sizes**: 200, 500, 1000 tokens

3. **Test different k values**: Try k=1, 3, 5, 10 retrieved documents

4. **Measure retrieval quality**: Track how often the right doc is retrieved

## 🔧 Production-Ready Patterns

### Pattern 1: Document Preprocessing Pipeline

```python
from typing import List, Dict

class DocumentProcessor:
    """Process documents for RAG ingestion."""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Basic cleaning - remove extra whitespace, fix encoding."""
        import re
        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters (keep alphanumeric and basic punctuation)
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        return text.strip()
    
    @staticmethod
    def add_metadata(chunks: List[str], source: str) -> List[Dict]:
        """Add metadata to chunks for better tracking."""
        return [
            {
                "text": chunk,
                "source": source,
                "chunk_id": i,
                "length": len(chunk)
            }
            for i, chunk in enumerate(chunks)
        ]
    
    def process_document(self, text: str, source: str, 
                        chunk_size: int = 500) -> List[Dict]:
        """Full pipeline: clean → chunk → add metadata."""
        cleaned = self.clean_text(text)
        chunks = chunk_text_simple(cleaned, chunk_size)
        return self.add_metadata(chunks, source)

# Usage
processor = DocumentProcessor()
doc_chunks = processor.process_document(
    text="Your long document text...",
    source="user_manual.pdf"
)
```

### Pattern 2: Caching for Performance

```python
from functools import lru_cache

class CachedRAG(RAGPipeline):
    """RAG with embedding caching for repeated queries."""
    
    @lru_cache(maxsize=1000)
    def get_cached_embedding(self, text: str) -> tuple:
        """Cache embeddings for common queries."""
        return tuple(get_embedding(text))
    
    def retrieve(self, query: str, k: int = 3) -> List[str]:
        """Use cached embeddings."""
        query_embedding = np.array([self.get_cached_embedding(query)])
        results = self.vector_store.search(query_embedding, k)
        return [doc for doc, _ in results]

# Caching reduces API calls by 60-80% for repeated queries
```

### Pattern 3: Error Handling

```python
class RobustRAG(RAGPipeline):
    """RAG with proper error handling."""
    
    def query(self, question: str, k: int = 3, max_retries: int = 2) -> dict:
        """Query with retry logic and fallbacks."""
        for attempt in range(max_retries):
            try:
                return super().query(question, k)
            except Exception as e:
                if attempt == max_retries - 1:
                    # Final fallback
                    return {
                        "question": question,
                        "answer": "I encountered an error processing your request.",
                        "error": str(e),
                        "sources": []
                    }
                continue
```

## 📊 Evaluating RAG Performance

### Key Metrics (Focus on These)

1. **Retrieval Accuracy**: Are the right documents retrieved?
2. **Answer Relevance**: Does the answer address the question?
3. **Faithfulness**: Is the answer grounded in the retrieved context?

```python
def evaluate_retrieval(questions: List[str], 
                      expected_docs: List[List[str]],
                      rag_pipeline: RAGPipeline,
                      k: int = 3) -> float:
    """Simple retrieval accuracy metric."""
    correct = 0
    total = len(questions)
    
    for question, expected in zip(questions, expected_docs):
        retrieved = rag_pipeline.retrieve(question, k)
        # Check if any expected doc is in retrieved
        if any(exp in retrieved for exp in expected):
            correct += 1
    
    return correct / total

# Example usage
questions = ["What is RAG?", "How do embeddings work?"]
expected = [
    ["RAG helps reduce hallucinations"],
    ["Vector databases store embeddings"]
]
accuracy = evaluate_retrieval(questions, expected, rag, k=3)
print(f"Retrieval Accuracy: {accuracy:.2%}")
```

## 🛠️ Tools & Technologies

### Essential Tools (20% You Need)

#### 1. **FAISS** (Start Here)
```bash
pip install faiss-cpu  # or faiss-gpu for GPU support
```

**Pros**:
- ✅ Free and open source
- ✅ Extremely fast
- ✅ Great for development/prototyping

**Cons**:
- ❌ Requires manual persistence
- ❌ No built-in distributed search

#### 2. **Pinecone** (Production)
```bash
pip install pinecone-client
```

```python
import pinecone

# Initialize
pinecone.init(api_key="YOUR_API_KEY", environment="us-west1-gcp")

# Create index
pinecone.create_index("my-rag-index", dimension=1536)

# Use index
index = pinecone.Index("my-rag-index")
index.upsert(vectors=[("id1", embedding, {"text": "document"})])
results = index.query(query_embedding, top_k=3)
```

**Pros**:
- ✅ Fully managed
- ✅ Built for scale
- ✅ Simple API

**Cons**:
- ❌ Costs money (starts free tier)
- ❌ Vendor lock-in

#### 3. **Weaviate** (Self-Hosted)
```bash
pip install weaviate-client
```

**Pros**:
- ✅ Feature-rich
- ✅ Self-hosted option
- ✅ Hybrid search built-in

**Cons**:
- ❌ More complex setup
- ❌ Resource intensive

### Supporting Libraries

```bash
# Install the essential stack
pip install openai numpy faiss-cpu tiktoken
```

## 💡 Common Pitfalls & Solutions

### Pitfall 1: Chunks Too Large or Too Small
❌ **Problem**: 2000-token chunks → irrelevant info included
✅ **Solution**: Use 300-500 token chunks for most use cases

### Pitfall 2: Not Handling No Results
❌ **Problem**: Empty retrieval → LLM hallucinates
✅ **Solution**: Always check if documents were retrieved:

```python
def query_safe(self, question: str, k: int = 3) -> dict:
    context_docs = self.retrieve(question, k)
    
    if not context_docs:
        return {
            "question": question,
            "answer": "I don't have information to answer this question.",
            "sources": []
        }
    
    # Continue with normal RAG...
```

### Pitfall 3: Ignoring Metadata
❌ **Problem**: Can't trace answers back to sources
✅ **Solution**: Always store document metadata:

```python
metadata = {
    "source": "user_manual.pdf",
    "page": 42,
    "section": "Troubleshooting",
    "timestamp": "2024-01-15"
}
```

### Pitfall 4: Using Wrong Embedding Model
❌ **Problem**: Using large expensive models unnecessarily
✅ **Solution**: Use `text-embedding-3-small` for 80% of cases

## 🎯 Week 02 Project Component

Build a **Document Q&A System** that you'll expand in later weeks:

**Requirements**:
1. Ingest at least 10 documents (PDFs, text files, or web pages)
2. Implement chunking and embedding generation
3. Store in FAISS vector database
4. Create query interface
5. Return answers with source citations
6. Measure retrieval accuracy on 10 test questions

See `project-steps.md` for detailed implementation guide.

## 📚 Further Reading (Vital Resources Only)

### Must-Read
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [FAISS Documentation](https://github.com/facebookresearch/faiss/wiki)
- [Pinecone Learning Center](https://www.pinecone.io/learn/)

### Nice-to-Have
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [RAG Paper (Lewis et al.)](https://arxiv.org/abs/2005.11401)

## ✅ Success Criteria

By the end of Week 02, you should be able to:
- [x] Explain RAG in 3 sentences to a non-technical person
- [x] Generate embeddings using OpenAI API
- [x] Build a working vector search system with FAISS
- [x] Create a complete RAG pipeline (retrieve → augment → generate)
- [x] Evaluate retrieval quality
- [x] Handle edge cases (no results, errors)
- [x] Choose appropriate chunk sizes for different document types

## 🏁 Quick Start Checklist

Before starting exercises:
- [ ] Install required packages: `pip install openai numpy faiss-cpu tiktoken`
- [ ] Set OpenAI API key: `export OPENAI_API_KEY="sk-..."`
- [ ] Download sample documents (provided in resources)
- [ ] Review Week 01 prompt engineering patterns

---

**Next Steps**: 
1. Complete hands-on exercises in `actividad-interactiva.md` 
2. Start building your Document Q&A System in `project-steps.md`
3. Focus on the **20% of techniques** that deliver **80% of the value**!

🚀 **Remember**: RAG is about **retrieval quality** first. Perfect your document chunking and embedding strategy before optimizing generation!
