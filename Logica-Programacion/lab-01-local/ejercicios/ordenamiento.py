def ordenamiento(lista):
    """
    Ordena una lista de números de menor a mayor usando bubble sort.
    
    Args:
        lista: Lista de números a ordenar
    
    Returns:
        Lista ordenada
    """
    if not lista:
        return []
    
    # Crear copia para no modificar la original
    resultado = lista.copy()
    n = len(resultado)
    
    # Bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    
    return resultado
