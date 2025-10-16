# Módulo 5: AWS Bedrock

## Introducción

En este módulo aprenderás a trabajar con AWS Bedrock, el servicio de IA generativa de Amazon que proporciona acceso a modelos foundation de última generación a través de una API unificada.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Configurar AWS CLI y boto3
- 🎯 Trabajar con modelos en Bedrock
- 🎯 Implementar RAG con Bedrock
- 🎯 Crear APIs serverless con Lambda
- 🎯 Gestionar costos y límites
- 🎯 Monitorear uso con CloudWatch

## ¿Por qué es importante?

AWS Bedrock permite acceder a modelos como Claude, Llama 2, y otros sin gestionar infraestructura. Es la solución empresarial para IA generativa en la nube.

## Conceptos Principales

### 1. AWS Bedrock Overview

**Modelos disponibles:**
- **Anthropic Claude**: Excelente para texto largo, seguro
- **Amazon Titan**: Modelos propios de Amazon
- **Meta Llama 2**: Open source, customizable
- **Stability AI**: Para generación de imágenes
- **Cohere**: Embeddings y generación

**Ventajas:**
- Sin gestión de infraestructura
- Pago por uso
- Integración con AWS
- Seguridad y compliance
- Varios modelos en una API

### 2. Configuración Inicial

**Instalar AWS CLI**:
```bash
# Linux/Mac
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configurar
aws configure
# Ingresar: Access Key, Secret Key, Region (us-east-1)
```

**Instalar boto3**:
```bash
pip install boto3
```

### 3. Trabajar con Bedrock

**Invocar modelo Claude**:
```python
import boto3
import json

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def invoke_claude(prompt: str) -> str:
    body = json.dumps({
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 500,
        "temperature": 0.7,
        "top_p": 1,
    })
    
    response = bedrock.invoke_model(
        modelId='anthropic.claude-v2',
        body=body
    )
    
    response_body = json.loads(response['body'].read())
    return response_body['completion']

# Uso
answer = invoke_claude("¿Qué es data engineering?")
print(answer)
```

**Con streaming**:
```python
def invoke_claude_stream(prompt: str):
    body = json.dumps({
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 500
    })
    
    response = bedrock.invoke_model_with_response_stream(
        modelId='anthropic.claude-v2',
        body=body
    )
    
    stream = response['body']
    for event in stream:
        chunk = json.loads(event['chunk']['bytes'])
        if 'completion' in chunk:
            print(chunk['completion'], end='')
```

### 4. Embeddings con Titan

```python
def get_titan_embedding(text: str) -> list:
    body = json.dumps({
        "inputText": text
    })
    
    response = bedrock.invoke_model(
        modelId='amazon.titan-embed-text-v1',
        body=body
    )
    
    response_body = json.loads(response['body'].read())
    return response_body['embedding']

# Uso
embedding = get_titan_embedding("Data engineering con AWS")
print(f"Vector de {len(embedding)} dimensiones")
```

### 5. RAG con Bedrock

```python
import boto3
from opensearchpy import OpenSearch

class BedrockRAG:
    def __init__(self):
        self.bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.opensearch = OpenSearch(
            hosts=[{'host': 'your-domain', 'port': 443}],
            use_ssl=True
        )
    
    def embed_text(self, text: str) -> list:
        """Genera embedding con Titan"""
        body = json.dumps({"inputText": text})
        response = self.bedrock.invoke_model(
            modelId='amazon.titan-embed-text-v1',
            body=body
        )
        return json.loads(response['body'].read())['embedding']
    
    def index_document(self, doc_id: str, text: str):
        """Indexa documento en OpenSearch"""
        embedding = self.embed_text(text)
        self.opensearch.index(
            index='documents',
            id=doc_id,
            body={
                'text': text,
                'embedding': embedding
            }
        )
    
    def search(self, query: str, k: int = 3) -> list:
        """Búsqueda semántica"""
        query_embedding = self.embed_text(query)
        
        response = self.opensearch.search(
            index='documents',
            body={
                "size": k,
                "query": {
                    "knn": {
                        "embedding": {
                            "vector": query_embedding,
                            "k": k
                        }
                    }
                }
            }
        )
        
        return [hit['_source']['text'] for hit in response['hits']['hits']]
    
    def ask(self, question: str) -> str:
        """RAG: recupera contexto y genera respuesta"""
        # 1. Recuperar documentos relevantes
        context_docs = self.search(question)
        context = "\n\n".join(context_docs)
        
        # 2. Crear prompt con contexto
        prompt = f"""Contexto:
{context}

Pregunta: {question}

Responde basándote únicamente en el contexto proporcionado."""
        
        # 3. Generar respuesta con Claude
        body = json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 500,
            "temperature": 0.5
        })
        
        response = self.bedrock.invoke_model(
            modelId='anthropic.claude-v2',
            body=body
        )
        
        return json.loads(response['body'].read())['completion']

# Uso
rag = BedrockRAG()
rag.index_document('doc1', 'ETL es Extract Transform Load...')
answer = rag.ask("¿Qué es ETL?")
print(answer)
```

### 6. API Serverless con Lambda

**Lambda function**:
```python
import json
import boto3

bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    """API endpoint para invocar Bedrock"""
    try:
        # Extraer pregunta del request
        body = json.loads(event['body'])
        question = body['question']
        
        # Invocar Bedrock
        prompt = f"\n\nHuman: {question}\n\nAssistant:"
        response = bedrock.invoke_model(
            modelId='anthropic.claude-v2',
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 300
            })
        )
        
        answer = json.loads(response['body'].read())['completion']
        
        return {
            'statusCode': 200,
            'body': json.dumps({'answer': answer})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

**API Gateway + Lambda**:
```yaml
# serverless.yml
service: bedrock-api

provider:
  name: aws
  runtime: python3.11
  region: us-east-1
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - bedrock:InvokeModel
          Resource: "*"

functions:
  ask:
    handler: handler.lambda_handler
    events:
      - http:
          path: ask
          method: post
```

### 7. Gestión de Costos

**Pricing de Bedrock**:
- Claude: ~$0.01 / 1k tokens input, ~$0.03 / 1k tokens output
- Titan Embeddings: ~$0.0001 / 1k tokens
- Varía por modelo y región

**Optimizar costos**:
```python
def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    """Estima costo de llamada a Claude"""
    input_cost = (input_tokens / 1000) * 0.01
    output_cost = (output_tokens / 1000) * 0.03
    return input_cost + output_cost

# Antes de invocar
tokens_estimate = len(prompt.split()) * 1.3  # rough estimate
print(f"Costo estimado: ${estimate_cost(tokens_estimate, 300):.4f}")
```

**Límites y quotas**:
```python
# Implementar rate limiting
import time
from functools import wraps

def rate_limit(calls_per_minute: int):
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = 60.0 / calls_per_minute
            
            if elapsed < wait_time:
                time.sleep(wait_time - elapsed)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        
        return wrapper
    return decorator

@rate_limit(calls_per_minute=10)
def invoke_bedrock(prompt: str):
    # ...
    pass
```

## Implementación Práctica

### Sistema RAG Serverless con AWS

**Arquitectura**:
```
S3 (docs) → Lambda (procesamiento) → OpenSearch (vectores)
                ↓
API Gateway → Lambda (RAG) → Bedrock → Respuesta
```

**Despliegue con Terraform**:
```hcl
# main.tf
resource "aws_s3_bucket" "documents" {
  bucket = "rag-documents-${random_id.suffix.hex}"
}

resource "aws_lambda_function" "rag" {
  filename      = "lambda.zip"
  function_name = "bedrock-rag"
  role          = aws_iam_role.lambda.arn
  handler       = "handler.lambda_handler"
  runtime       = "python3.11"
  
  environment {
    variables = {
      OPENSEARCH_ENDPOINT = aws_opensearch_domain.rag.endpoint
    }
  }
}

resource "aws_api_gateway_rest_api" "rag" {
  name = "bedrock-rag-api"
}
```

## Mejores Prácticas

### 1. Manejo de Errores
```python
from botocore.exceptions import ClientError

def safe_invoke(prompt: str, retries: int = 3):
    for attempt in range(retries):
        try:
            return invoke_claude(prompt)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':
                time.sleep(2 ** attempt)  # exponential backoff
            else:
                raise
```

### 2. Logging y Monitoring
```python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def invoke_with_logging(prompt: str):
    logger.info(f"Invoking Bedrock - prompt length: {len(prompt)}")
    start = time.time()
    
    response = invoke_claude(prompt)
    
    duration = time.time() - start
    logger.info(f"Response received in {duration:.2f}s")
    
    return response
```

### 3. Seguridad
```python
# No hardcodear credenciales
# Usar IAM roles y AWS Secrets Manager

def get_api_key():
    secrets_client = boto3.client('secretsmanager')
    response = secrets_client.get_secret_value(SecretId='api-key')
    return json.loads(response['SecretString'])['key']
```

## De Open Source a Enterprise

| Aspecto | Self-Hosted (OS) | AWS Bedrock |
|---------|------------------|-------------|
| **Setup** | Complejo | Simple |
| **Infraestructura** | Tu gestión | Managed |
| **Escalabilidad** | Manual | Automática |
| **Costo** | GPU pricing | Pay-per-use |
| **Latencia** | Variable | Consistente |

**Cuándo usar Bedrock**:
- ✅ Aplicación empresarial
- ✅ Necesitas compliance (SOC2, HIPAA)
- ✅ Múltiples modelos
- ✅ Integración con AWS

## Conceptos Clave

- 🔑 **Bedrock**: Servicio managed de IA generativa
- 🔑 **Foundation Models**: Modelos pre-entrenados grandes
- 🔑 **Serverless**: Sin gestión de servidores
- 🔑 **Pay-per-use**: Pago por invocación
- 🔑 **IAM**: Gestión de permisos AWS

## Próximos Pasos

En el **Módulo 6: ML Pipelines y Experiments** aprenderás:
- Diseñar pipelines de ML
- Tracking con MLflow
- Versionado de modelos
- Feature stores

## Recursos Adicionales

- 📖 [AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)
- 📖 [boto3 Bedrock Guide](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html)
- 🎥 [AWS re:Invent Bedrock Session](https://www.youtube.com/watch?v=example)
- 💰 [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)

---

**¡Excelente trabajo completando el Módulo 5!** 🎉

Ya sabes usar AWS Bedrock para IA empresarial. Continúa a [actividad-interactiva.md](actividad-interactiva.md).
