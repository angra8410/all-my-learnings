def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n: Número entero no negativo
    
    Returns:
        El factorial de n
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
