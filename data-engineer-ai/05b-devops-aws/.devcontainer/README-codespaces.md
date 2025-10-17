# Guía de Uso: VS Code Remote - Containers

Esta configuración de DevContainer proporciona un entorno completo para trabajar con los laboratorios de DevOps y AWS de forma local, sin necesidad de instalar herramientas en tu máquina.

## 🎯 ¿Qué incluye este DevContainer?

- **Terraform** v1.6.6 - Infrastructure as Code
- **AWS CLI v2** - Interfaz de línea de comandos de AWS
- **awscli-local** - Cliente para LocalStack
- **Docker CLI** - Para gestionar contenedores
- **Docker Compose** - Orquestación de contenedores
- **PostgreSQL Client** - Cliente de base de datos
- **Make** - Automatización de tareas
- **jq** - Procesamiento de JSON
- **Python 3** - Para scripts y aplicaciones

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

1. **Visual Studio Code** - [Descargar](https://code.visualstudio.com/)
2. **Docker Desktop** - [Descargar](https://www.docker.com/products/docker-desktop/)
3. **Extensión Remote - Containers** - Instalar desde VS Code Marketplace

## 🚀 Cómo usar este DevContainer

### Opción 1: Abrir en Container (Recomendado)

1. Clona el repositorio:
   ```bash
   git clone https://github.com/angra8410/all-my-learnings.git
   cd all-my-learnings/data-engineer-ai/05b-devops-aws
   ```

2. Abre VS Code en este directorio:
   ```bash
   code .
   ```

3. VS Code debería detectar el devcontainer y mostrarte una notificación:
   - Haz clic en **"Reopen in Container"**
   - O usa `F1` → `Remote-Containers: Reopen in Container`

4. Espera a que el contenedor se construya (primera vez tarda ~5-10 minutos)

5. Una vez dentro del contenedor, verás el mensaje de bienvenida con las versiones instaladas

### Opción 2: Desde la Paleta de Comandos

1. Abre VS Code
2. Presiona `F1` o `Ctrl+Shift+P` (Cmd+Shift+P en Mac)
3. Escribe: `Remote-Containers: Open Folder in Container...`
4. Selecciona la carpeta `data-engineer-ai/05b-devops-aws`
5. Espera a que el contenedor se construya

## ✅ Verificar que todo funciona

Una vez dentro del contenedor, abre una terminal integrada en VS Code y ejecuta:

```bash
# Verificar Terraform
terraform --version

# Verificar AWS CLI
aws --version

# Verificar Docker
docker --version

# Verificar Make
make --version

# Verificar jq
jq --version

# Verificar PostgreSQL client
psql --version
```

## 🧪 Ejecutar el Lab Local

Una vez dentro del DevContainer, puedes ejecutar el laboratorio local:

```bash
# Navegar al directorio del lab
cd labs/lab-01-local

# Instalar dependencias (si es necesario)
make install

# Levantar servicios
make up

# Verificar que todo funciona
make check

# Ver logs
make logs

# Detener servicios
make down
```

## 🔧 Puertos Expuestos

El DevContainer expone automáticamente estos puertos:

- **8080** - Aplicación Flask
- **5432** - PostgreSQL
- **4566** - LocalStack (AWS local)
- **9000** - MinIO (S3 local)

Puedes acceder a estos servicios desde tu navegador o herramientas locales.

## 📚 Extensiones VS Code Incluidas

El DevContainer instala automáticamente estas extensiones:

- **HashiCorp Terraform** - Syntax highlighting y autocompletado
- **Docker** - Gestión de contenedores
- **Python** - Soporte para Python
- **AWS Toolkit** - Integración con AWS

## 🐛 Solución de Problemas

### El contenedor no se construye

1. Verifica que Docker Desktop esté ejecutándose
2. Asegúrate de tener espacio en disco (mínimo 5GB libres)
3. Intenta reconstruir: `F1` → `Remote-Containers: Rebuild Container`

### No puedo acceder a los puertos

1. Verifica que los puertos no estén en uso por otras aplicaciones
2. Revisa el panel "PORTS" en VS Code (parte inferior)
3. Intenta reenviar manualmente el puerto: Click derecho → "Forward Port"

### Error de permisos con Docker

1. Asegúrate de que tu usuario tenga permisos para Docker
2. En Windows/Mac: Verifica que Docker Desktop esté configurado correctamente
3. En Linux: Añade tu usuario al grupo docker: `sudo usermod -aG docker $USER`

### El contenedor es muy lento

1. Asigna más recursos a Docker Desktop (Settings → Resources)
2. Recomendado: 4GB RAM, 2 CPUs mínimo
3. Considera usar WSL2 en Windows para mejor rendimiento

## 🔄 Actualizar el DevContainer

Si se actualiza la configuración del devcontainer:

1. `F1` → `Remote-Containers: Rebuild Container`
2. O elimina la imagen y reconstruye desde cero

## 🎓 Recursos Adicionales

- [VS Code Remote - Containers Docs](https://code.visualstudio.com/docs/remote/containers)
- [Docker Docs](https://docs.docker.com/)
- [Terraform Docs](https://www.terraform.io/docs)
- [LocalStack Docs](https://docs.localstack.cloud/)

## 💡 Consejos

- Todos tus cambios de código se sincronizan automáticamente
- Las extensiones y configuraciones se preservan entre sesiones
- Puedes tener múltiples contenedores abiertos simultáneamente
- El contenedor se detiene automáticamente al cerrar VS Code

## 🆘 ¿Necesitas Ayuda?

Si encuentras algún problema:

1. Revisa los logs del contenedor: `F1` → `Remote-Containers: Show Container Log`
2. Consulta la documentación del laboratorio en `labs/lab-01-local/README.md`
3. Abre un issue en el repositorio con los detalles del problema

---

**¡Listo para empezar a aprender DevOps!** 🚀
