# Imagen base con herramientas de desarrollo
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Evitar prompts interactivos durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    jq \
    make \
    python3 \
    python3-pip \
    postgresql-client \
    software-properties-common \
    gnupg \
    lsb-release \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instalar Terraform
ARG TERRAFORM_VERSION=1.6.6
RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    terraform --version

# Instalar AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip && \
    aws --version

# Instalar awscli-local para LocalStack
RUN pip3 install --no-cache-dir awscli-local

# Instalar Docker CLI (el daemon viene del feature docker-in-docker)
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/*

# Configurar usuario vscode
RUN groupadd -g 1000 vscode || true && \
    useradd -m -u 1000 -g 1000 -s /bin/bash vscode || true && \
    usermod -aG docker vscode || true

# Variables de entorno
ENV PATH="/usr/local/bin:${PATH}"
ENV SHELL=/bin/bash

# Usuario por defecto
USER vscode
WORKDIR /workspace

# Mensaje de bienvenida
RUN echo 'echo "🚀 DevOps AWS Lab Environment ready!"' >> ~/.bashrc && \
    echo 'echo "📦 Terraform $(terraform --version | head -1)"' >> ~/.bashrc && \
    echo 'echo "☁️  AWS CLI $(aws --version)"' >> ~/.bashrc && \
    echo 'echo "🐳 Docker $(docker --version)"' >> ~/.bashrc
