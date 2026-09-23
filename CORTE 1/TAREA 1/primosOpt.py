tope_rango = 30  # Define el límite superior del rango a evaluar (exclusivo)
n = 0  # Inicializa el contador del ciclo en 0
primo = True  # Bandera (flag) booleana para asumir inicialmente que 'n' es primo

while n < tope_rango:  # Mantiene el ciclo mientras 'n' sea menor a 30
    for div in range(
        2, n
    ):  # Genera divisores desde 2 hasta n-1 para evaluar si es primo
        if n % div == 0:  # Evalúa si 'n' es divisible exactamente por 'div'
            primo = False  # Marca que 'n' NO es primo si la división es exacta
    if primo:  # Evalúa si la bandera se mantuvo como True
        print(n)  # Imprime 'n' por considerarse primo (nota: incluye 0 y 1)
    else:  # Si la bandera cambió a False...
        primo = True  # Reinicia la bandera a True para la siguiente iteración
    n += 1  # Incrementa el valor de 'n' en 1
