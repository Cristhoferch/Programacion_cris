# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 28,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Accedemos y modificamos el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Quitio"  # Modificamos la ciudad

# Agregar una nueva clave-valor para "telefono"
informacion_personal["telefono"] = "0912345678"  # Agregamos un número de teléfono ficticio

# Verificar si la clave "telefono" existe en el diccionario (ya la hemos agregado previamente)
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0912345678"  # Solo lo agregaríamos si no existe

# Eliminar la clave "edad"
del informacion_personal["edad"]  # Eliminamos la clave "edad"

# Imprimir el diccionario final
print(informacion_personal)
