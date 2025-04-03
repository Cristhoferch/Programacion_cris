# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Primera línea de notas personales.\n")
    file.write("Segunda línea con información importante.\n")
    file.write("Tercera línea con un recordatorio importante.\n")

# Lectura del archivo utilizando readline()
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo:")
    line = file.readline()  # Lee la primera línea
    while line:
        print(line.strip())  # Imprime la línea sin saltos de línea adicionales
        line = file.readline()  # Lee la siguiente línea


