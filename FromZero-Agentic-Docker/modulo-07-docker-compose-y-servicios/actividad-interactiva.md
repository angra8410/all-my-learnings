# Módulo 07: Actividad Interactiva

## Ejercicio 1: Iniciar Servicios (10 min)

```bash
cd modulo-07-docker-compose-y-servicios/ejemplos
docker-compose up -d
docker-compose ps
```

**Servicios corriendo**: _____ de 3
**Todos healthy**: [ ] Sí - [ ] No

## Ejercicio 2: Probar Conectividad (15 min)

```bash
# API directa
curl http://localhost:8000
curl http://localhost:8000/health

# A través de nginx
curl http://localhost

# Verificar Redis
docker-compose exec redis redis-cli ping
```

**Todos los tests pasaron**: [ ] Sí

## Ejercicio 3: Ver Logs (10 min)

```bash
docker-compose logs agent-api
docker-compose logs redis
docker-compose logs nginx
docker-compose logs -f
```

**Logs revisados**: [ ] Sí

## Ejercicio 4: Gestión de Servicios (10 min)

```bash
# Detener un servicio
docker-compose stop agent-api

# Reiniciar
docker-compose start agent-api

# Reconstruir
docker-compose up -d --build

# Limpiar todo
docker-compose down
```

**Ciclo completo practicado**: [ ] Sí

## Total: 45 minutos
