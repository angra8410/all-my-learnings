"""
Simple Flask application for ECS demonstration
Provides a health check endpoint and basic API functionality
"""

import os
import json
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuración desde variables de entorno
APP_ENV = os.getenv('APP_ENV', 'development')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'appdb')

@app.route('/')
def home():
    """Endpoint principal"""
    return jsonify({
        'message': 'Welcome to DevOps Learning App!',
        'environment': APP_ENV,
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    """
    Health check endpoint para ECS
    Este endpoint es usado por:
    - Docker HEALTHCHECK
    - ECS health checks
    - Load balancer health checks (si se usa ALB)
    """
    return jsonify({
        'status': 'healthy',
        'service': 'devops-app',
        'timestamp': datetime.utcnow().isoformat(),
        'environment': APP_ENV
    }), 200

@app.route('/info')
def info():
    """Endpoint con información de la aplicación y conexión a DB"""
    return jsonify({
        'application': 'DevOps Learning App',
        'environment': APP_ENV,
        'database': {
            'host': DB_HOST,
            'port': DB_PORT,
            'name': DB_NAME,
            'status': 'configured'  # En producción, validar conexión real
        },
        'container': {
            'hostname': os.getenv('HOSTNAME', 'unknown'),
            'platform': os.getenv('PLATFORM', 'unknown')
        },
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/data', methods=['GET', 'POST'])
def data_endpoint():
    """Endpoint de ejemplo para operaciones de datos"""
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({
            'message': 'Data received',
            'data': data,
            'timestamp': datetime.utcnow().isoformat()
        }), 201
    else:
        return jsonify({
            'message': 'Use POST to send data',
            'example': {
                'name': 'example',
                'value': 123
            }
        })

@app.errorhandler(404)
def not_found(error):
    """Handler para rutas no encontradas"""
    return jsonify({
        'error': 'Not found',
        'message': 'The requested URL was not found on the server',
        'timestamp': datetime.utcnow().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para errores internos"""
    return jsonify({
        'error': 'Internal server error',
        'message': 'An internal error occurred',
        'timestamp': datetime.utcnow().isoformat()
    }), 500

if __name__ == '__main__':
    # Configuración para desarrollo local
    # En producción se usa gunicorn (ver Dockerfile CMD)
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=(APP_ENV == 'development'))
