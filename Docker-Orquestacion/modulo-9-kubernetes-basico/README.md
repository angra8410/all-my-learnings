# Módulo 9: Kubernetes Básico

## Introducción

¡Bienvenido a Kubernetes (K8s), el orquestador líder de la industria! En este módulo aprenderás:

- Arquitectura de Kubernetes
- Pods, Deployments, Services
- kubectl - La herramienta CLI
- Namespaces y contextos
- ConfigMaps y Secrets
- Desplegar tu primera app

## ¿Por qué es importante?

Kubernetes es esencial porque:

- **Estándar Industrial**: Usado por Google, Amazon, Microsoft
- **Escalabilidad**: De 10 a 10,000 contenedores
- **Ecosistema**: Miles de herramientas y extensiones
- **Multi-Cloud**: Funciona en cualquier nube
- **Futuro**: Habilidad más demandada en DevOps

## Conceptos Principales

### 1. Arquitectura de Kubernetes

```
┌─────────────────────────────────────────┐
│         Control Plane (Master)          │
│                                         │
│  API Server ← kubectl                   │
│  Scheduler                              │
│  Controller Manager                     │
│  etcd (Base de datos del cluster)       │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│             Worker Nodes                │
│                                         │
│  Node 1          Node 2      Node 3     │
│  ├─ kubelet     ├─ kubelet   ├─ kubelet │
│  ├─ kube-proxy  ├─ kube-proxy ├─ kube-proxy│
│  └─ Pods        └─ Pods       └─ Pods   │
└─────────────────────────────────────────┘
```

### 2. Pod - La Unidad Básica

Un Pod es un grupo de uno o más contenedores:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.24
    ports:
    - containerPort: 80
```

**Crear Pod:**
```bash
kubectl apply -f pod.yaml
kubectl get pods
kubectl describe pod nginx-pod
kubectl logs nginx-pod
kubectl delete pod nginx-pod
```

### 3. Deployment - Gestión de Pods

Deployments gestionan réplicas y actualizaciones:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24
        ports:
        - containerPort: 80
```

**Gestionar Deployment:**
```bash
# Crear
kubectl apply -f deployment.yaml

# Ver deployments
kubectl get deployments

# Escalar
kubectl scale deployment nginx-deployment --replicas=5

# Actualizar imagen
kubectl set image deployment/nginx-deployment nginx=nginx:1.25

# Ver rollout status
kubectl rollout status deployment/nginx-deployment

# Rollback
kubectl rollout undo deployment/nginx-deployment

# Ver histórico
kubectl rollout history deployment/nginx-deployment
```

### 4. Service - Exponer Aplicaciones

**ClusterIP (interno):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

**NodePort (externo):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

**LoadBalancer (cloud):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

### 5. ConfigMaps y Secrets

**ConfigMap (configuración):**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgres://db:5432"
  log_level: "info"
```

**Usar en Pod:**
```yaml
spec:
  containers:
  - name: app
    image: myapp:1.0
    env:
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database_url
```

**Secret (datos sensibles):**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: c3VwZXJzZWNyZXQ=  # base64
```

**Crear Secret:**
```bash
kubectl create secret generic db-secret \
  --from-literal=password=supersecret
```

### 6. Namespaces

Dividir cluster en espacios virtuales:

```bash
# Listar namespaces
kubectl get namespaces

# Crear namespace
kubectl create namespace desarrollo
kubectl create namespace produccion

# Desplegar en namespace
kubectl apply -f deployment.yaml -n desarrollo

# Ver recursos en namespace
kubectl get all -n desarrollo

# Cambiar namespace por defecto
kubectl config set-context --current --namespace=desarrollo
```

### 7. Labels y Selectors

**Labels:**
```yaml
metadata:
  labels:
    app: frontend
    environment: production
    tier: web
```

**Seleccionar por labels:**
```bash
# Ver pods con label
kubectl get pods -l app=frontend

# Multiple labels
kubectl get pods -l app=frontend,environment=production

# Eliminar por label
kubectl delete pods -l tier=web
```

## Implementación Práctica

### Ejercicio 1: Primera App en K8s

**1. Crear Deployment:**
```yaml
# app-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - name: hello
        image: gcr.io/google-samples/hello-app:1.0
        ports:
        - containerPort: 8080
```

**2. Crear Service:**
```yaml
# app-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-service
spec:
  type: LoadBalancer
  selector:
    app: hello
  ports:
  - port: 80
    targetPort: 8080
```

**3. Desplegar:**
```bash
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml

# Ver recursos
kubectl get deployments
kubectl get pods
kubectl get services

# Acceder (minikube)
minikube service hello-service
```

### Ejercicio 2: Stack Completo

**Estructura:**
```
k8s/
├── namespace.yaml
├── configmap.yaml
├── secret.yaml
├── postgres-deployment.yaml
├── postgres-service.yaml
├── app-deployment.yaml
└── app-service.yaml
```

**namespace.yaml:**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: myapp
```

**configmap.yaml:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: myapp
data:
  DATABASE_HOST: "postgres-service"
  DATABASE_NAME: "myapp"
```

**postgres-deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  namespace: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_DB
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_NAME
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        ports:
        - containerPort: 5432
```

**Desplegar:**
```bash
# Crear namespace
kubectl apply -f namespace.yaml

# Crear secret
kubectl create secret generic db-secret \
  --from-literal=password=supersecret \
  -n myapp

# Desplegar todo
kubectl apply -f configmap.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml

# Verificar
kubectl get all -n myapp
```

### Ejercicio 3: Rolling Update

```bash
# Actualizar imagen
kubectl set image deployment/hello-app \
  hello=gcr.io/google-samples/hello-app:2.0 \
  -n myapp

# Ver progreso
kubectl rollout status deployment/hello-app -n myapp

# Si hay problemas, rollback
kubectl rollout undo deployment/hello-app -n myapp

# Ver histórico
kubectl rollout history deployment/hello-app -n myapp
```

## Comandos Esenciales kubectl

```bash
# BÁSICOS
kubectl version                      # Versión
kubectl cluster-info                 # Info del cluster
kubectl get nodes                    # Nodos

# RECURSOS
kubectl get pods                     # Listar pods
kubectl get deployments              # Listar deployments
kubectl get services                 # Listar services
kubectl get all                      # Todo

# DETALLES
kubectl describe pod <pod>           # Detalles
kubectl logs <pod>                   # Logs
kubectl logs -f <pod>                # Seguir logs
kubectl exec -it <pod> -- sh         # Entrar al pod

# CREAR/APLICAR
kubectl apply -f file.yaml           # Aplicar configuración
kubectl create -f file.yaml          # Crear recurso
kubectl delete -f file.yaml          # Eliminar

# EDITAR
kubectl edit deployment <name>       # Editar en vivo
kubectl scale deployment <name> --replicas=5

# NAMESPACES
kubectl get pods -n <namespace>      # En namespace específico
kubectl get all -n <namespace>       # Todo en namespace
kubectl config set-context --current --namespace=<ns>

# DEBUG
kubectl describe pod <pod>
kubectl logs <pod>
kubectl exec -it <pod> -- sh
kubectl port-forward <pod> 8080:80
```

## Mejores Prácticas

### 1. Usa Namespaces

```bash
# Separar ambientes
kubectl create namespace dev
kubectl create namespace staging
kubectl create namespace prod
```

### 2. Labels Consistentes

```yaml
labels:
  app: myapp
  version: "1.0"
  environment: production
  tier: frontend
```

### 3. Resource Limits

```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

### 4. Liveness y Readiness Probes

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 5. Declarativo sobre Imperativo

```bash
# ✅ Declarativo (mejor)
kubectl apply -f deployment.yaml

# ❌ Imperativo (evitar en producción)
kubectl run nginx --image=nginx
kubectl create deployment nginx --image=nginx
```

## Conceptos clave para recordar

- 🔑 **Pod**: Unidad mínima, 1+ contenedores
- 🔑 **Deployment**: Gestiona réplicas y updates
- 🔑 **Service**: Expone pods (ClusterIP, NodePort, LoadBalancer)
- 🔑 **kubectl**: CLI para interactuar con K8s
- 🔑 **Namespace**: Aislamiento virtual en cluster
- 🔑 **ConfigMap**: Configuración no sensible
- 🔑 **Secret**: Datos sensibles (base64)

## Próximos pasos

En el Módulo 10 aprenderás **Kubernetes Avanzado**:
- Ingress y routing avanzado
- Persistent Volumes
- StatefulSets
- DaemonSets
- Jobs y CronJobs
- HPA (Auto-scaling)
- Helm y gestión de paquetes

**¿Qué necesitas saber antes de continuar?**
✅ Entender arquitectura de K8s  
✅ Crear Pods y Deployments  
✅ Usar Services para exponer apps  
✅ Gestionar ConfigMaps y Secrets  
✅ Comandos básicos de kubectl  

---

**¡Ahora tienes las bases de Kubernetes! ⚓**

**¡Nos vemos en el Módulo 10 - K8s Avanzado!** 🚀
