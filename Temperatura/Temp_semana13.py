# Función para calcular la temperatura promedio de cada ciudad durante el período de tiempo
def calcular_promedio_ciudades(temperaturas):
    promedios = []  # Lista para almacenar los promedios de cada ciudad

    # Iteramos sobre cada ciudad
    for ciudad, semanas in enumerate(temperaturas):
        suma_temperaturas = 0  # Inicializamos la suma de temperaturas de la ciudad
        total_dias = 0  # Contador de los días

        # Iteramos sobre cada semana de la ciudad
        for semana in semanas:
            for temperatura in semana:
                suma_temperaturas += temperatura
                total_dias += 1

        # Cálculo del promedio con bloque if-else estándar
        if total_dias > 0:
            promedio = suma_temperaturas / total_dias
        else:
            promedio = 0

        # Agregamos el promedio a la lista de promedios
        promedios.append(promedio)

    # Devolvemos la lista de promedios
    return promedios


# Esta es una funcion extra para el ingreso de datos por parte del usuario
def ingresar_datos():
    ciudades = int(input("¿Cuántas ciudades deseas ingresar? "))
    temperaturas = []

    for i in range(ciudades):
        print(f"Ingresando datos para la Ciudad {i + 1}:")
        semanas = int(input(f"  ¿Cuántas semanas de datos tiene la Ciudad {i + 1}? "))
        ciudad_temperaturas = []

        for j in range(semanas):
            print(f"  Semana {j + 1}:")
            dias = int(input("    ¿Cuántos días tiene la semana? (generalmente 7) "))
            semana_temperaturas = []

            for k in range(dias):
                temp = float(input(f"    Día {k + 1} temperatura: "))
                semana_temperaturas.append(temp)

            ciudad_temperaturas.append(semana_temperaturas)

        temperaturas.append(ciudad_temperaturas)

    return temperaturas


# Llamamos a la función para ingresar los datos
temperaturas = ingresar_datos()

# Llamamos a la función para calcular los promedios de cada ciudad
promedios_ciudades = calcular_promedio_ciudades(temperaturas)

# Imprimimos los resultados
for i, promedio in enumerate(promedios_ciudades):
    print(f"Promedio de temperatura de la Ciudad {i + 1}: {promedio:.2f}°C")
