# Módulo 3: Ingesta de Documentos

## Introducción

En este módulo aprenderás a procesar documentos de múltiples formatos (PDF, Word, HTML, etc.) para preparar datos textuales que alimentarán sistemas de IA, especialmente sistemas RAG (Retrieval Augmented Generation).

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Extraer texto de PDFs, Word y HTML
- 🎯 Procesar tablas y estructuras complejas
- 🎯 Implementar estrategias de chunking
- 🎯 Limpiar y normalizar texto
- 🎯 Manejar diferentes encodings y formatos
- 🎯 Preparar documentos para embedding

## ¿Por qué es importante?

Los sistemas RAG y LLMs necesitan texto limpio y bien estructurado. La calidad de la ingesta determina la calidad de las respuestas del sistema. Mal procesamiento = malas respuestas.

## Conceptos Principales

### 1. Tipos de Documentos

**PDFs**:
- Text-based: Texto extraíble directamente
- Image-based: Requieren OCR
- Mixed: Combinación de ambos

**Word/DOCX**:
- Estructura XML
- Preserva formato
- Metadata rica

**HTML**:
- Estructura con tags
- Requiere limpieza de markup
- Web scraping

### 2. Extracción de Texto

**Con PyPDF2 (PDFs básicos)**:
```python
from PyPDF2 import PdfReader

def extract_text_pypdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
```

**Con pdfplumber (PDFs con tablas)**:
```python
import pdfplumber

def extract_with_tables(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            tables = page.extract_tables()
            yield text, tables
```

**Con python-docx (Word)**:
```python
from docx import Document

def extract_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text
```

**Con BeautifulSoup (HTML)**:
```python
from bs4 import BeautifulSoup

def extract_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Remover scripts y styles
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    return text
```

### 3. Chunking Strategies

**¿Por qué chunking?**
- LLMs tienen límite de tokens
- Mejor precisión en retrieval
- Contexto manejable

**Estrategias:**

**Fixed Size (Tamaño fijo)**:
```python
def fixed_size_chunks(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
```

**Semantic Chunking (Por significado)**:
```python
def semantic_chunks(text):
    # Dividir por párrafos
    paragraphs = text.split('\n\n')
    
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < 1000:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks
```

**Recursive Chunking (LangChain)**:
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)
```

### 4. Limpieza de Texto

```python
import re

def clean_text(text):
    # Remover múltiples espacios
    text = re.sub(r'\s+', ' ', text)
    
    # Remover caracteres especiales
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    
    # Normalizar puntuación
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    
    # Strip
    text = text.strip()
    
    return text
```

### 5. Metadata Extraction

```python
def extract_document_metadata(file_path):
    metadata = {
        'filename': os.path.basename(file_path),
        'size': os.path.getsize(file_path),
        'modified': datetime.fromtimestamp(
            os.path.getmtime(file_path)
        ),
        'extension': os.path.splitext(file_path)[1]
    }
    return metadata
```

## Implementación Práctica

### Ejercicio 1: Procesador Universal de Documentos

```python
import os
from typing import List, Dict
from PyPDF2 import PdfReader
from docx import Document

class DocumentProcessor:
    def __init__(self):
        self.supported_formats = ['.pdf', '.docx', '.txt']
    
    def process_file(self, file_path: str) -> Dict:
        """Procesa un archivo y retorna texto + metadata"""
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext not in self.supported_formats:
            raise ValueError(f"Formato no soportado: {ext}")
        
        if ext == '.pdf':
            text = self._extract_pdf(file_path)
        elif ext == '.docx':
            text = self._extract_docx(file_path)
        else:  # .txt
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        
        metadata = self._extract_metadata(file_path)
        
        return {
            'text': text,
            'metadata': metadata,
            'chunks': self._create_chunks(text)
        }
    
    def _extract_pdf(self, path: str) -> str:
        reader = PdfReader(path)
        return "\n".join([page.extract_text() for page in reader.pages])
    
    def _extract_docx(self, path: str) -> str:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    
    def _extract_metadata(self, path: str) -> Dict:
        return {
            'filename': os.path.basename(path),
            'size': os.path.getsize(path),
            'extension': os.path.splitext(path)[1]
        }
    
    def _create_chunks(self, text: str, size: int = 500) -> List[str]:
        words = text.split()
        chunks = []
        current = []
        
        for word in words:
            current.append(word)
            if len(' '.join(current)) >= size:
                chunks.append(' '.join(current))
                current = current[-20:]  # overlap
        
        if current:
            chunks.append(' '.join(current))
        
        return chunks

# Uso
processor = DocumentProcessor()
result = processor.process_file('document.pdf')
print(f"Extraídos {len(result['chunks'])} chunks")
```

### Ejercicio 2: Pipeline de Ingesta para RAG

```python
from pathlib import Path
import json

class IngestionPipeline:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.processor = DocumentProcessor()
    
    def run(self):
        """Procesa todos los documentos en input_dir"""
        documents = []
        
        for file_path in self.input_dir.glob('**/*'):
            if file_path.is_file():
                try:
                    doc = self.processor.process_file(str(file_path))
                    documents.append(doc)
                    print(f"✅ Procesado: {file_path.name}")
                except Exception as e:
                    print(f"❌ Error en {file_path.name}: {e}")
        
        # Guardar resultados
        self._save_results(documents)
        return documents
    
    def _save_results(self, documents: List[Dict]):
        output_file = self.output_dir / 'processed_documents.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(documents, f, ensure_ascii=False, indent=2)
        print(f"\n📁 Guardados {len(documents)} documentos en {output_file}")

# Ejecutar pipeline
pipeline = IngestionPipeline('./documents', './output')
results = pipeline.run()
```

## Mejores Prácticas

### 1. Manejo de Errores
```python
try:
    text = extract_text(file)
except UnicodeDecodeError:
    # Intentar con encoding diferente
    with open(file, 'r', encoding='latin-1') as f:
        text = f.read()
```

### 2. Validación de Chunks
```python
def validate_chunk(chunk: str, min_length: int = 50) -> bool:
    return len(chunk) >= min_length and chunk.strip() != ""
```

### 3. Preservar Contexto
```python
# Agregar metadata al chunk
def enrich_chunk(chunk: str, doc_metadata: Dict) -> Dict:
    return {
        'text': chunk,
        'source': doc_metadata['filename'],
        'chunk_id': generate_id(),
        'timestamp': datetime.now().isoformat()
    }
```

## De Open Source a Enterprise

| Característica | Open Source | Enterprise |
|----------------|-------------|------------|
| **Extracción PDF** | PyPDF2, pdfplumber | AWS Textract, Adobe PDF Services |
| **OCR** | Tesseract | Google Vision API, AWS Textract |
| **Chunking** | LangChain | Customizado + LLM |
| **Costo** | Gratis | Pay per page |

**Transferencia**: Los conceptos de chunking, limpieza y metadata son universales.

## Conceptos Clave

- 🔑 **Chunking**: Dividir texto en partes manejables
- 🔑 **OCR**: Optical Character Recognition para PDFs escaneados
- 🔑 **Metadata**: Información sobre el documento
- 🔑 **Encoding**: UTF-8 para texto universal

## Próximos Pasos

En el **Módulo 4: RAG y Sistemas Agentic** aprenderás:
- Generar embeddings de los chunks
- Almacenar en bases vectoriales
- Implementar búsqueda semántica
- Construir sistema RAG completo

## Recursos Adicionales

- 📖 [PyPDF2 Docs](https://pypdf2.readthedocs.io/)
- 📖 [python-docx Docs](https://python-docx.readthedocs.io/)
- 📖 [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- 🎥 [PDF Processing Tutorial](https://www.youtube.com/watch?v=example)

---

**¡Excelente trabajo completando el Módulo 3!** 🎉

Ahora sabes cómo ingestar y preparar documentos para sistemas de IA. Continúa a [actividad-interactiva.md](actividad-interactiva.md).
