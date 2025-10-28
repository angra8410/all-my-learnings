# MCP Agent Dockerfile
# This Dockerfile creates a container image for the MCP Agent example

# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create a non-root user for security
RUN useradd -m -u 1000 mcpuser && \
    chown -R mcpuser:mcpuser /app

# Copy the agent code
COPY agent.py /app/

# Switch to non-root user
USER mcpuser

# Expose port (for future web interface)
EXPOSE 8000

# Health check (simple Python check)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Run the agent
CMD ["python", "agent.py"]
