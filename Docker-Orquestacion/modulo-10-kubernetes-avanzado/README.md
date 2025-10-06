# Módulo 10: Kubernetes Avanzado

## Introducción

¡El módulo final! Dominarás Kubernetes a nivel profesional. En este módulo aprenderás:

- Ingress Controllers y routing HTTP
- Persistent Volumes y almacenamiento
- StatefulSets para apps con estado
- DaemonSets y Jobs
- Horizontal Pod Autoscaler (HPA)
- Helm - El gestor de paquetes de K8s
- Monitoreo y observabilidad
- Mejores prácticas de producción

## ¿Por qué es importante?

Estos conceptos avanzados te permiten:

- **Producción Real**: Ejecutar apps críticas
- **Escalabilidad**: Auto-scaling inteligente
- **Persistencia**: Bases de datos en K8s
- **Automatización**: Helm y GitOps
- **Observabilidad**: Monitoreo y debugging
- **Carrera**: Habilidades de nivel senior

## Conceptos Principales

### 1. Ingress - Routing HTTP

Ingress gestiona acceso HTTP/HTTPS externo:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 3000
  - host: admin.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 80
```

**Instalar Ingress Controller (Nginx):**
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
```

### 2. Persistent Volumes (PV) y Claims (PVC)

**PersistentVolume (admin crea):**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-database
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /mnt/data
```

**PersistentVolumeClaim (usuario solicita):**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-database
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

**Usar en Pod:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: database-pod
spec:
  containers:
  - name: postgres
    image: postgres:15
    volumeMounts:
    - name: data
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: pvc-database
```

### 3. StatefulSet - Apps con Estado

Para bases de datos, queues, etc.:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 3
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
        image: postgres:15
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

**Características:**
- Nombres predecibles: postgres-0, postgres-1, postgres-2
- Orden de inicio/parada garantizado
- Volumen persistente único por pod
- DNS estable: postgres-0.postgres.default.svc.cluster.local

### 4. DaemonSet - Un Pod por Nodo

Para logging, monitoreo, networking:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        ports:
        - containerPort: 9100
      hostNetwork: true
      hostPID: true
```

**Casos de uso:**
- Agentes de monitoreo
- Recolectores de logs
- Drivers de red/almacenamiento

### 5. Jobs y CronJobs

**Job (una vez):**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-job
spec:
  template:
    spec:
      containers:
      - name: backup
        image: backup-tool:latest
        command: ["sh", "-c", "backup-database.sh"]
      restartPolicy: OnFailure
  backoffLimit: 4
```

**CronJob (programado):**
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "0 2 * * *"  # 2 AM diario
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: backup-tool:latest
            command: ["sh", "-c", "backup.sh"]
          restartPolicy: OnFailure
```

### 6. Horizontal Pod Autoscaler (HPA)

Auto-scaling basado en CPU/memoria/métricas custom:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

**Ver HPA:**
```bash
kubectl get hpa
kubectl describe hpa app-hpa
```

### 7. Helm - Gestor de Paquetes

**Instalar Helm:**
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

**Usar Helm:**
```bash
# Agregar repositorio
helm repo add bitnami https://charts.bitnami.com/bitnami

# Buscar charts
helm search repo nginx

# Instalar
helm install my-nginx bitnami/nginx

# Listar releases
helm list

# Actualizar
helm upgrade my-nginx bitnami/nginx --set replicaCount=3

# Desinstalar
helm uninstall my-nginx
```

**Crear tu propio Chart:**
```bash
# Crear estructura
helm create myapp

# Estructura:
# myapp/
# ├── Chart.yaml
# ├── values.yaml
# └── templates/
#     ├── deployment.yaml
#     ├── service.yaml
#     └── ingress.yaml

# Instalar
helm install myapp-release ./myapp
```

### 8. Monitoreo con Prometheus y Grafana

**Instalar stack de monitoreo:**
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack
```

**Acceder a Grafana:**
```bash
kubectl port-forward svc/prometheus-grafana 3000:80
# Usuario: admin
# Password: prom-operator
```

## Implementación Práctica

### Ejercicio 1: Stack Completo con Ingress

**Estructura:**
```
k8s-advanced/
├── namespace.yaml
├── configmap.yaml
├── secret.yaml
├── postgres-statefulset.yaml
├── postgres-service.yaml
├── backend-deployment.yaml
├── backend-service.yaml
├── frontend-deployment.yaml
├── frontend-service.yaml
├── ingress.yaml
└── hpa.yaml
```

**ingress.yaml:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: myapp
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend
            port:
              number: 3000
```

### Ejercicio 2: Base de Datos Persistente

```yaml
# postgres-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
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
        image: postgres:15
        env:
        - name: POSTGRES_DB
          value: myapp
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        ports:
        - containerPort: 5432
          name: postgres
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

### Ejercicio 3: Auto-Scaling

```bash
# Habilitar metrics-server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Crear HPA
kubectl autoscale deployment backend --cpu-percent=50 --min=2 --max=10

# Generar carga
kubectl run -it load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://backend; done"

# Ver escalado en acción
watch kubectl get hpa
```

### Ejercicio 4: Helm Chart Custom

**myapp/values.yaml:**
```yaml
replicaCount: 3

image:
  repository: myapp
  tag: "1.0.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  host: myapp.local

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
```

## Mejores Prácticas de Producción

### 1. Resource Requests y Limits

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### 2. Probes Configurados

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

### 3. Pod Disruption Budgets

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
```

### 4. Network Policies

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 3000
```

### 5. Security Context

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000
  capabilities:
    drop:
    - ALL
  readOnlyRootFilesystem: true
```

## Comandos Avanzados

```bash
# DEBUGGING
kubectl logs -f pod-name --previous      # Logs del contenedor anterior
kubectl top pods                         # Uso de recursos
kubectl top nodes                        # Recursos por nodo
kubectl get events --sort-by=.metadata.creationTimestamp

# MANIFESTS
kubectl apply -k ./kustomize/           # Kustomize
kubectl diff -f deployment.yaml         # Ver cambios antes de aplicar

# CONTEXTOS
kubectl config get-contexts             # Listar contextos
kubectl config use-context prod         # Cambiar contexto

# HELM
helm upgrade --install app ./chart      # Install o upgrade
helm rollback app 1                     # Rollback a revision

# DEBUGGING AVANZADO
kubectl debug pod-name -it --image=busybox --target=container-name
```

## Conceptos clave para recordar

- 🔑 **Ingress**: Routing HTTP/HTTPS inteligente
- 🔑 **PV/PVC**: Almacenamiento persistente
- 🔑 **StatefulSet**: Apps con estado y orden
- 🔑 **HPA**: Auto-scaling horizontal
- 🔑 **Helm**: Gestor de paquetes de K8s
- 🔑 **Probes**: Liveness y readiness
- 🔑 **Resources**: Requests y limits siempre

## ¡Felicitaciones! 🎉

Has completado el curso de Docker y Orquestación. Ahora dominas:

✅ Docker desde básico hasta avanzado  
✅ Dockerfile y optimización de imágenes  
✅ Docker Compose para multi-contenedor  
✅ Docker Swarm para orquestación simple  
✅ Kubernetes básico y avanzado  
✅ Helm y gestión de paquetes  
✅ Mejores prácticas de producción  

## Próximos Pasos en tu Carrera

1. **Práctica Real**
   - Containeriza tus proyectos
   - Despliega en Kubernetes
   - Contribuye a proyectos open source

2. **Certificaciones**
   - Docker Certified Associate (DCA)
   - Certified Kubernetes Administrator (CKA)
   - Certified Kubernetes Application Developer (CKAD)

3. **Especialización**
   - Service Mesh (Istio, Linkerd)
   - GitOps (ArgoCD, Flux)
   - Observabilidad (Prometheus, Grafana, Jaeger)
   - Seguridad (Falco, OPA)

4. **Cloud Providers**
   - AWS EKS
   - Google GKE
   - Azure AKS

---

**¡Has llegado lejos! Ahora tienes habilidades muy demandadas en la industria. 🚀**

**¡Éxito en tu carrera como DevOps/Cloud Engineer!** ⚓🐳☸️
