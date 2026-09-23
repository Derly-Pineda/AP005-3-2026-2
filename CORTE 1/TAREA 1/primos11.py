# --- Medición SIN break ---
ciclos_sin_break = 0  # Contador de iteraciones internas sin interrupción
n = 0  # Inicialización del número a evaluar
primo = True  # Estado inicial
while n < tope_rango:  # Bucle principal hasta 30
    for div in range(2, n):  # Bucle interno de divisores
        ciclos_sin_break += 1  # Incrementa el contador por cada evaluación ejecutada
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
    if primo:  # Muestra el número si es primo
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_sin_break)
)  # Muestra el total de iteraciones completas (378)

# --- Medición CON break ---
ciclos_con_break = 0  # Contador de iteraciones internas optimizado
n = 0  # Reinicia el valor inicial a 0
primo = True  # Estado inicial
while n < tope_rango:  # Bucle principal hasta 30
    for div in range(2, n):  # Bucle interno de divisores
        ciclos_con_break += 1  # Incrementa el contador acumulativo
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
            break  # Detiene la búsqueda al primer divisor hallado
    if primo:  # Muestra el número si es primo
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_con_break)
)  # Muestra las iteraciones reducidas (134)
print(
    "Se optimizó a un "
    + str(ciclos_con_break / ciclos_sin_break * 100)
    + "% de ciclos aplicando break"
)  # Imprime la relación porcentual entre ambos procesos (~35.45%)
