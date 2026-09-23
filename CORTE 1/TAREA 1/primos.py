tope_rango = 100  # Aumenta el alcance del cálculo hasta 100

# --- Medición SIN break ---
ciclos_sin_break = 0  # Acumulador de ciclos para la versión ineficiente
n = 0  # Inicializa el conteo en 0
primo = True  # Estado inicial
while n < tope_rango:  # Recorre el rango extendido
    for div in range(2, n):  # Bucle completo de divisores
        ciclos_sin_break += 1  # Registra la ejecución
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
    if primo:  # Muestra primos hallados
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Avanza al siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_sin_break)
)  # Muestra el total sin break (4753)

# --- Medición CON break ---
ciclos_con_break = 0  # Acumulador de ciclos para la versión eficiente
n = 0  # Reinicia la variable de control
primo = True  # Estado inicial
while n < tope_rango:  # Recorre el rango extendido
    for div in range(2, n):  # Bucle con parada temprana
        ciclos_con_break += 1  # Registra la ejecución
        if n % div == 0:  # Comprueba divisibilidad
            primo = False  # Marca como no primo
            break  # Sale del ciclo for inmediatamente al hallar un divisor
    if primo:  # Muestra primos hallados
        print(n)
    else:  # Si no fue primo...
        primo = True  # Restablece el flag
    n += 1  # Avanza al siguiente número

print(
    "Cantidad de ciclos: " + str(ciclos_con_break)
)  # Muestra el total con break (1132)
print(
    "Se optimizó a un "
    + str(ciclos_con_break / ciclos_sin_break * 100)
    + "% de ciclos aplicando break"
)  # Demuestra mayor impacto porcentual en rangos más grandes (~23.81%)
