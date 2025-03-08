dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

temperaturas = [
    # Ciudad 1: Ciudad A
    [
        # Semana 1
        {"Lunes": 22, "Martes": 23, "Miércoles": 21, "Jueves": 20, "Viernes": 19, "Sábado": 21, "Domingo": 22},
        # Semana 2
        {"Lunes": 24, "Martes": 23, "Miércoles": 25, "Jueves": 22, "Viernes": 21, "Sábado": 23, "Domingo": 24}

    ],
    # Ciudad 2: Ciudad B
    [
        # Semana 1
        {"Lunes": 18, "Martes": 17, "Miércoles": 19, "Jueves": 20, "Viernes": 21, "Sábado": 22, "Domingo": 18},
        # Semana 2
        {"Lunes": 20, "Martes": 21, "Miércoles": 22, "Jueves": 23, "Viernes": 21, "Sábado": 20, "Domingo": 19}
        # Semana 2
    ],
    # Ciudad 3: Ciudad C
    [
    # Semana 1
        {"Lunes": 30, "Martes": 32, "Miércoles": 33, "Jueves": 31, "Viernes": 30, "Sábado": 32, "Domingo": 31},
    # Semana 2
        {"Lunes": 28, "Martes": 29, "Miércoles": 30, "Jueves": 31, "Viernes": 32, "Sábado": 30, "Domingo": 29}

    ]
]

for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")

    for semana_num, semana in enumerate(ciudad):
        suma_temperaturas = sum(semana.values())
        promedio = suma_temperaturas / len(semana)
        print(f"  Semana {semana_num + 1}: Promedio de temperatura: {promedio:.2f}°C")

    print()
