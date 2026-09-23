n = 0  # Inicializa el número 'n' a evaluar en 0
primo = True  # Asume por defecto que el número es primo
while n < tope_rango:  # Itera hasta alcanzar el límite fijado
    for div in range(2, n):  # Evalúa posibles divisores entre 2 y n-1
        if n % div == 0:  # Si encuentra un divisor exacto...
            primo = False  # Cambia la bandera a False
            break  # Interrumpe el bucle 'for' de inmediato sin evaluar los demás divisores
    if primo:  # Si no se encontró ningún divisor exacto...
        print(n)  # Imprime el número primo
    else:  # Si se detectó que no era primo...
        primo = True  # Restablece la bandera para el siguiente número
    n += 1  # Avanza al siguiente número del rango
