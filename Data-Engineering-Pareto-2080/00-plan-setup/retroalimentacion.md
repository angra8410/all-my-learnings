# 📝 Retroalimentación y Evaluación — Módulo 00: Plan & Setup

## 🎯 Criterios de Evaluación

Este módulo se evalúa mediante **verificación práctica** de instalaciones y configuraciones. No hay examen teórico.

---

## 📊 Rúbrica de Evaluación

### 1. Instalaciones Base (20%)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Excelente (18-20)** | 18-20 | Todas las herramientas instaladas, verificadas y configuradas correctamente. Git configurado globalmente. |
| **Bueno (15-17)** | 15-17 | Todas instaladas, alguna configuración menor pendiente (ej: extensiones VSCode). |
| **Suficiente (12-14)** | 12-14 | Herramientas principales instaladas pero configuración incompleta. |
| **Insuficiente (0-11)** | 0-11 | Falta una o más herramientas clave (Git, Docker, Python). |

**Tu puntuación:** _____ / 20

---

### 2. Servicios Docker (30%)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Excelente (27-30)** | 27-30 | PostgreSQL y Airflow corriendo. Conexiones exitosas. DAG ejecutado. Tabla de prueba creada. |
| **Bueno (23-26)** | 23-26 | Ambos servicios corriendo, alguna verificación menor pendiente. |
| **Suficiente (18-22)** | 18-22 | Al menos un servicio (PostgreSQL) corriendo y funcional. |
| **Insuficiente (0-17)** | 0-17 | Servicios no funcionan o no están corriendo. |

**Tu puntuación:** _____ / 30

---

### 3. Databricks Community (25%)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Excelente (23-25)** | 23-25 | Cuenta creada, cluster iniciado, notebook ejecutado exitosamente con output correcto. |
| **Bueno (20-22)** | 20-22 | Cuenta y cluster OK, notebook con errores menores. |
| **Suficiente (16-19)** | 16-19 | Cuenta creada, cluster iniciado pero notebook no ejecutado. |
| **Insuficiente (0-15)** | 0-15 | Cuenta no creada o cluster no inicia. |

**Tu puntuación:** _____ / 25

---

### 4. Repositorio y Workflow Git (15%)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Excelente (14-15)** | 14-15 | Repo clonado, rama personal creada con nombre correcto, branch activo. |
| **Bueno (12-13)** | 12-13 | Repo clonado y rama creada. |
| **Suficiente (9-11)** | 9-11 | Repo clonado pero sin rama personal. |
| **Insuficiente (0-8)** | 0-8 | Repo no clonado. |

**Tu puntuación:** _____ / 15

---

### 5. Verificación y Documentación (10%)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Excelente (9-10)** | 9-10 | Archivo `setup-verification.md` creado con todos los outputs correctos. |
| **Bueno (7-8)** | 7-8 | Archivo creado con la mayoría de verificaciones. |
| **Suficiente (5-6)** | 5-6 | Archivo creado pero incompleto. |
| **Insuficiente (0-4)** | 0-4 | Archivo no creado. |

**Tu puntuación:** _____ / 10

---

## 🎯 Puntuación Total

**Suma total:** _____ / 100

### Interpretación:
- **90-100:** 🏆 Excelente — Setup perfecto, listo para el curso
- **75-89:** ✅ Bueno — Setup funcional, algunos ajustes menores
- **60-74:** ⚠️ Suficiente — Setup básico, revisar servicios fallidos
- **< 60:** ❌ Insuficiente — Rehacer instalaciones antes de continuar

---

## 🔍 Autoevaluación Detallada

### Checklist de Verificación Técnica

**Docker:**
- [ ] `docker --version` retorna versión 20.x o superior
- [ ] `docker ps` ejecuta sin errores
- [ ] PostgreSQL contenedor en estado "Up"
- [ ] Airflow contenedor en estado "Up"

**PostgreSQL:**
- [ ] Conexión exitosa via `psql`
- [ ] Query `SELECT version();` funciona
- [ ] Tabla `test_setup` creada
- [ ] Datos insertados y consultados correctamente

**Airflow:**
- [ ] UI accesible en http://localhost:8080
- [ ] Login exitoso
- [ ] DAG `test_setup_dag` visible y activo
- [ ] DAG ejecutado con estado "Success"

**Databricks:**
- [ ] Cuenta Community creada y verificada
- [ ] Cluster iniciado (estado Running)
- [ ] Notebook creado y adjunto a cluster
- [ ] Código Scala ejecutado con output correcto

**Git/Repo:**
- [ ] Repositorio clonado localmente
- [ ] Rama personal creada
- [ ] `git branch --show-current` muestra tu rama

---

## 📝 Reflexión Personal

### ¿Qué fue lo más difícil de este módulo?
```
_______________________________________________
_______________________________________________
_______________________________________________
```

### ¿Qué aprendiste que no sabías antes?
```
_______________________________________________
_______________________________________________
_______________________________________________
```

### ¿Qué herramienta te genera más curiosidad?
```
_______________________________________________
```

### ¿Necesitas repasar algo antes de continuar?
```
_______________________________________________
_______________________________________________
```

---

## ✅ Recomendaciones Según Tu Puntuación

### Si obtuviste 90-100:
🎉 ¡Excelente! Estás completamente listo. Avanza directamente a Módulo 01.

### Si obtuviste 75-89:
👍 Buen trabajo. Revisa las áreas con puntuación menor antes de continuar. Consulta `recursos.md` para troubleshooting.

### Si obtuviste 60-74:
⚠️ Setup funcional pero incompleto. **Acción requerida:**
1. Identifica qué servicios fallaron
2. Revisa logs: `docker logs <container_name>`
3. Consulta troubleshooting en `recursos.md`
4. Repite ejercicios que no completaste

### Si obtuviste < 60:
❌ Setup insuficiente para continuar. **Acción urgente:**
1. Revisa requisitos del sistema (RAM, disco, SO)
2. Reinstala herramientas que fallaron
3. Consulta documentación oficial de cada herramienta
4. Considera pedir ayuda en forums/Discord
5. **No avances hasta tener al menos 75/100**

---

## 🆘 Recursos de Ayuda

### Troubleshooting Común:

**Docker no inicia:**
- Windows: Verificar que WSL2 esté habilitado
- Mac M1/M2: Usar imágenes ARM64
- Linux: Verificar que usuario esté en grupo `docker`

**PostgreSQL no acepta conexiones:**
```bash
# Verificar logs
docker logs postgres-pareto

# Reintentar conexión
docker restart postgres-pareto
sleep 10
docker exec -it postgres-pareto psql -U dataeng -d learning_db
```

**Airflow no carga DAGs:**
```bash
# Verificar path de montaje
docker inspect airflow-standalone | grep -A 5 Mounts

# Reiniciar Airflow
docker restart airflow-standalone
```

**Databricks cluster no inicia:**
- Verificar que cuenta sea Community Edition (no Trial)
- Esperar al menos 7-10 minutos
- Revisar quotas de uso (Community tiene límites)

---

## 📅 Próximos Pasos

### Si tu puntuación es ≥ 75:
1. Marca módulo como completado en `progreso.md`
2. Commit y push de tu rama personal
3. Avanza a **Módulo 01: Introducción al Pareto 20/80**

### Si tu puntuación es < 75:
1. Identifica gaps específicos
2. Consulta `recursos.md` para soluciones
3. Repite ejercicios fallidos
4. Re-evalúa hasta obtener ≥ 75

---

**🎯 Fecha de autoevaluación:** _________________  
**🎯 Puntuación final:** _____ / 100  
**🎯 ¿Listo para Módulo 01?** □ Sí  □ No (necesito repasar: ____________)

---

**💡 Recuerda:** Un setup sólido es fundamental. Es mejor invertir tiempo ahora que tener problemas en módulos posteriores.
