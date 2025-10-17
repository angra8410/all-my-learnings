def busqueda(lista, elemento):
    """
    Busca un elemento en una lista y retorna su índice.
    
    Args:
        lista: Lista donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Índice del elemento si se encuentra, -1 si no se encuentra
    """
    try:
        return lista.index(elemento)
    except ValueError:
        return -1
