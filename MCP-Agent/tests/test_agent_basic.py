"""
Tests unitarios básicos para el agente MCP.

Estos tests validan la funcionalidad core del agente sin necesidad
de levantar el servidor HTTP.

Para ejecutar:
    pytest tests/test_agent_basic.py -v

Para ejecutar con coverage:
    pytest tests/test_agent_basic.py --cov=examples --cov-report=html
"""

import sys
import os

# Añadir el directorio examples al path para poder importar agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'examples'))

from agent import process_prompt, AGENT_VERSION


def test_process_prompt_basic():
    """Test básico: procesar un prompt simple."""
    prompt = "Hola, ¿cómo estás?"
    result = process_prompt(prompt)
    
    # Verificar que la respuesta tiene la estructura correcta
    assert "response" in result
    assert "metadata" in result
    
    # Verificar que el prompt fue procesado
    assert "Hola, ¿cómo estás?" in result["response"]
    
    # Verificar metadata
    assert result["metadata"]["agent_version"] == AGENT_VERSION
    assert "processed_at" in result["metadata"]
    assert result["metadata"]["model_used"] == "mock-llm"


def test_process_prompt_with_context():
    """Test: procesar prompt con contexto adicional."""
    prompt = "¿Cuál es mi ID?"
    context = {
        "user_id": "user123",
        "session_id": "session456"
    }
    result = process_prompt(prompt, context=context)
    
    # Verificar que la respuesta incluye metadata sobre contexto
    assert "context_received" in result["metadata"]
    assert result["metadata"]["context_received"] is True


def test_process_prompt_with_options():
    """Test: procesar prompt con opciones de configuración."""
    prompt = "Genera un texto creativo"
    options = {
        "temperature": 0.9,
        "max_tokens": 500
    }
    result = process_prompt(prompt, options=options)
    
    # Verificar que las opciones fueron registradas
    assert "options_applied" in result["metadata"]
    assert "temperature" in result["metadata"]["options_applied"]
    assert "max_tokens" in result["metadata"]["options_applied"]


def test_process_prompt_empty():
    """Test: procesar un prompt vacío."""
    prompt = ""
    result = process_prompt(prompt)
    
    # El agente debe manejar prompts vacíos sin errores
    assert "response" in result
    assert result["response"] == "Procesado: "


def test_process_prompt_special_characters():
    """Test: procesar prompt con caracteres especiales."""
    prompt = "¿Qué tal? ¡Hola! @#$%^&*()"
    result = process_prompt(prompt)
    
    # Verificar que los caracteres especiales se manejan correctamente
    assert "response" in result
    assert prompt in result["response"]


def test_process_prompt_unicode():
    """Test: procesar prompt con caracteres Unicode (español, emojis)."""
    prompt = "Hola 👋 ¿Cómo está el día? 🌞"
    result = process_prompt(prompt)
    
    # Verificar que Unicode se maneja correctamente
    assert "response" in result
    assert "👋" in result["response"] or "Hola" in result["response"]


def test_process_prompt_long_text():
    """Test: procesar un prompt largo."""
    prompt = "Esta es una frase muy larga. " * 100  # 500+ palabras
    result = process_prompt(prompt)
    
    # Verificar que textos largos se procesan sin errores
    assert "response" in result
    assert result["metadata"]["tokens_used"] > 100  # Aproximadamente


def test_metadata_structure():
    """Test: verificar la estructura de metadata."""
    prompt = "Test metadata"
    result = process_prompt(prompt)
    
    metadata = result["metadata"]
    
    # Verificar campos requeridos en metadata
    required_fields = ["agent_version", "processed_at", "model_used", "tokens_used"]
    for field in required_fields:
        assert field in metadata, f"Campo '{field}' faltante en metadata"
    
    # Verificar tipos de datos
    assert isinstance(metadata["agent_version"], str)
    assert isinstance(metadata["processed_at"], str)
    assert isinstance(metadata["model_used"], str)
    assert isinstance(metadata["tokens_used"], int)


def test_process_prompt_returns_dict():
    """Test: verificar que process_prompt siempre devuelve un diccionario."""
    prompt = "Test return type"
    result = process_prompt(prompt)
    
    assert isinstance(result, dict)
    assert isinstance(result["response"], str)
    assert isinstance(result["metadata"], dict)


def test_multiple_prompts_independence():
    """Test: verificar que múltiples prompts son independientes."""
    prompt1 = "Primera pregunta"
    prompt2 = "Segunda pregunta"
    
    result1 = process_prompt(prompt1)
    result2 = process_prompt(prompt2)
    
    # Las respuestas deben ser diferentes
    assert result1["response"] != result2["response"]
    assert "Primera pregunta" in result1["response"]
    assert "Segunda pregunta" in result2["response"]
