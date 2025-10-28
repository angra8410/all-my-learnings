# Dockerfile for MCP Agent
# This containerizes the example agent for easy deployment and testing

# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copy the agent code
COPY agent.py .

# Create a non-root user for security
RUN useradd -m -u 1000 mcpuser && \
    chown -R mcpuser:mcpuser /app

# Switch to non-root user
USER mcpuser

# Add labels for metadata
LABEL maintainer="MCP Agent Team" \
      version="0.1-mock" \
      description="MCP Agent - Containerized example implementation"

# Run the agent when container launches
CMD ["python", "agent.py"]
