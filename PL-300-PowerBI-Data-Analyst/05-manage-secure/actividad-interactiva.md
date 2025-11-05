# 🎮 Actividad Interactiva 05: Manage and Secure

## 🎯 Objetivo

Gestión de workspaces, seguridad RLS, gateway y refresh.

**Duración**: 180-210 minutos (3-3.5 horas)

---

## 📋 Ejercicio 1: Workspace (25 min)

### Pasos
1. Crear workspace "PL300-Production"
2. Configurar roles (Admin, Member, Viewer)
3. Publicar reporte

### ✅ Comprobación
- Workspace: _______
- Usuarios: _______

---

## 📋 Ejercicio 2: Row-Level Security (45 min)

### Código DAX
```dax
// Tabla Security
SecurityTable = 
DATATABLE(
    "Email", STRING,
    "Region", STRING,
    {
        {"user1@domain.com", "East"},
        {"user2@domain.com", "West"}
    }
)

// Rol RLS
[Region] = LOOKUPVALUE(
    SecurityTable[Region],
    SecurityTable[Email],
    USERPRINCIPALNAME()
)
```

### Pasos
1. Crear SecurityTable
2. Modeling > Manage Roles
3. View as Roles para probar
4. Publicar y asignar usuarios

### ✅ Comprobación
- RLS funcional: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 3: Gateway (40 min)

### Pasos
1. Descargar e instalar gateway
2. Registrar en Power BI Service
3. Configurar data sources
4. Asignar permisos

### ✅ Comprobación
- Gateway online: ⬜ Sí ⬜ No ⬜ N/A

---

## 📋 Ejercicio 4: Scheduled Refresh (30 min)

### Pasos
1. Configurar credenciales
2. Schedule: Daily, 6AM y 6PM
3. Refresh manual
4. Verificar historial

### ✅ Comprobación
- Refresh exitoso: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 5: Compartir y Apps (25 min)

### Pasos
1. Share reporte individual
2. Create app
3. Configure audience
4. Publish app

### ✅ Comprobación
- App creada: _______

---

## 📋 Ejercicio 6: Monitoreo (25 min)

### Pasos
1. View usage metrics
2. Lineage view
3. Audit logs (si admin)

### ✅ Comprobación
- Views last 7 days: _______

---

## 📋 Ejercicio 7: Governanza (30 min)

### Pasos
1. Endorse dataset (Promoted/Certified)
2. Agregar descripción
3. Sensitivity label
4. Naming conventions

### ✅ Comprobación
- Endorsed: ⬜ Sí ⬜ No

---

## 📊 Resumen
Total: 220 min (3.7 hrs)

---

**Siguiente**: [Módulo 06 →](../06-practice-exam/README.md)

**Última actualización**: Noviembre 2025
