# Retroalimentación - Módulo 5: Interactividad y Publicación

## Respuestas

1. **B)** Slicers = Filtros visuales interactivos
2. **B)** Drill-through = Navegar manteniendo contexto
3. **B)** Bookmarks = Capturar estados para storytelling
4. **B)** RLS = Filtrar datos por usuario
5. **C)** Publish to web = Público (¡cuidado!)

## Verdadero/Falso

1. **F** - Solo sincroniza cuando sea relevante
2. **V** - Esa es su función
3. **V** - Perfecto para narrativas
4. **V** - Pro o Premium para compartir
5. **F** - ¡MUY PELIGROSO! Solo datos públicos
6. **V** - Gateway necesario para on-premise
7. **V** - Configura en Desktop, aplica en Service
8. **V** - Pro: hasta 8/día
9. **F** - También bookmarks, drill-through, URLs
10. **V** - Colaboración en workspaces

## Ejemplo RLS

```DAX
[VendedorID] = USERPRINCIPALNAME()
// O
[Región] IN VALUES(UsuariosRegión[Región])
```

**Probar**: View as Roles en Desktop

---

**Logros**: ✅ Interactividad ✅ Publicación ✅ Seguridad

**¡Casi terminas el curso!** 🎉
