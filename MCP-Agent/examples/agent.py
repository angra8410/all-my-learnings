#!/usr/bin/env python3
"""
MCP Agent - Minimal Implementation Example

Este es un agente MCP mínimo que expone una API HTTP para procesar prompts.
Usa únicamente la biblioteca estándar de Python (http.server, json) sin dependencias externas.

El agente implementa:
- POST /prompt: Procesa un prompt y devuelve una respuesta (mock LLM)
- GET /health: Endpoint de salud para verificar que el agente está funcionando

Para ejecutar:
    python3 agent.py

El servidor estará disponible en http://localhost:8000

Ejemplo de uso con curl:
    curl -X POST http://localhost:8000/prompt \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Hola, ¿cómo estás?"}'
"""

import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timezone
from urllib.parse import urlparse


# Configuración del agente
AGENT_VERSION = "1.0.0"
DEFAULT_PORT = 8000


def process_prompt(prompt, context=None, options=None):
    """
    Procesa un prompt y devuelve una respuesta.
    
    Esta es la función core del agente. En esta implementación mock,
    simplemente devuelve el prompt procesado. En una implementación real,
    aquí se invocaría el LLM (OpenAI, Anthropic, etc.).
    
    Args:
        prompt (str): El texto del prompt a procesar
        context (dict, opcional): Contexto adicional (user_id, session_id, etc.)
        options (dict, opcional): Opciones de configuración (temperature, max_tokens, etc.)
    
    Returns:
        dict: Diccionario con 'response' y 'metadata'
    """
    # Mock LLM: En producción, aquí invocarías el LLM real
    # Ejemplo: response_text = openai.ChatCompletion.create(...)
    
    # Por ahora, devolvemos una respuesta determinística
    response_text = f"Procesado: {prompt}"
    
    # Construir la respuesta con metadata
    response = {
        "response": response_text,
        "metadata": {
            "agent_version": AGENT_VERSION,
            "processed_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "model_used": "mock-llm",
            "tokens_used": len(prompt.split())  # Mock: contamos palabras como tokens
        }
    }
    
    # Si hay contexto, lo podríamos usar para personalizar la respuesta
    if context:
        response["metadata"]["context_received"] = True
    
    # Si hay opciones, las registramos en metadata
    if options:
        response["metadata"]["options_applied"] = list(options.keys())
    
    return response


class MCPAgentHandler(BaseHTTPRequestHandler):
    """
    HTTP Request Handler para el agente MCP.
    
    Maneja:
    - POST /prompt: Procesar prompts
    - GET /health: Health check
    """
    
    def _set_headers(self, status_code=200, content_type="application/json"):
        """Establece los headers HTTP de la respuesta."""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")  # CORS para desarrollo
        self.end_headers()
    
    def _send_json_response(self, data, status_code=200):
        """Envía una respuesta JSON."""
        self._set_headers(status_code)
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    
    def _send_error_response(self, message, status_code=400):
        """Envía una respuesta de error."""
        error_data = {
            "error": message,
            "status_code": status_code
        }
        self._send_json_response(error_data, status_code)
    
    def do_OPTIONS(self):
        """Maneja requests OPTIONS para CORS."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
        """
        Maneja requests GET.
        
        Endpoints soportados:
        - /health: Health check
        """
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == "/health":
            # Health check endpoint
            health_data = {
                "status": "healthy",
                "version": AGENT_VERSION,
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            }
            self._send_json_response(health_data)
        else:
            # Endpoint no encontrado
            self._send_error_response(f"Endpoint not found: {parsed_path.path}", 404)
    
    def do_POST(self):
        """
        Maneja requests POST.
        
        Endpoints soportados:
        - /prompt: Procesar un prompt
        """
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == "/prompt":
            # Leer el body del request
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length == 0:
                self._send_error_response("Request body is empty", 400)
                return
            
            try:
                # Parsear JSON del body
                body = self.rfile.read(content_length)
                data = json.loads(body.decode("utf-8"))
                
                # Validar que el prompt esté presente
                prompt = data.get("prompt")
                if not prompt:
                    self._send_error_response("Field 'prompt' is required", 400)
                    return
                
                # Extraer contexto y opciones (opcionales)
                context = data.get("context")
                options = data.get("options")
                
                # Procesar el prompt
                result = process_prompt(prompt, context, options)
                
                # Enviar respuesta exitosa
                self._send_json_response(result, 200)
                
            except json.JSONDecodeError as e:
                self._send_error_response(f"Invalid JSON: {str(e)}", 400)
            except Exception as e:
                self._send_error_response(f"Internal server error: {str(e)}", 500)
        else:
            # Endpoint no encontrado
            self._send_error_response(f"Endpoint not found: {parsed_path.path}", 404)
    
    def log_message(self, format, *args):
        """
        Override para personalizar el logging.
        Por defecto imprime en stdout con timestamp.
        """
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {format % args}")


def run_server(port=DEFAULT_PORT):
    """
    Inicia el servidor HTTP del agente MCP.
    
    Args:
        port (int): Puerto en el que escuchará el servidor (default: 8000)
    """
    server_address = ("", port)
    httpd = HTTPServer(server_address, MCPAgentHandler)
    
    print(f"=" * 60)
    print(f"🚀 MCP Agent v{AGENT_VERSION} - Starting...")
    print(f"=" * 60)
    print(f"Server listening on: http://localhost:{port}")
    print(f"Health check: http://localhost:{port}/health")
    print(f"Prompt endpoint: POST http://localhost:{port}/prompt")
    print(f"=" * 60)
    print(f"Press Ctrl+C to stop the server")
    print(f"=" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("🛑 Server stopped by user")
        print("=" * 60)
        httpd.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    # Leer puerto de argumentos de línea de comandos si se proporciona
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}")
            print(f"Usage: python3 agent.py [port]")
            sys.exit(1)
    
    run_server(port)
