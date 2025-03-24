# Definir la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Función principal para mostrar los resultados
def main():
    # Solicitar al usuario el monto total de la compra
    monto_compra = float(input("Ingresa el monto total de la compra: $"))

    # Solicitar al usuario el porcentaje de descuento (opcional, con valor predeterminado de 10%)
    descuento_opcional = input("Ingresa el porcentaje de descuento : ")

    # Si el usuario no ingresa un valor, se usa el valor predeterminado de 10%
    if descuento_opcional == "":
        porcentaje_descuento = 10
    else:
        porcentaje_descuento = float(descuento_opcional)

    # Calcular el descuento
    descuento = calcular_descuento(monto_compra, porcentaje_descuento)

    # Calcular el monto final a pagar
    monto_final = monto_compra - descuento

    # Mostrar los resultados
    print(f"\nMonto total: ${monto_compra}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Monto final a pagar: ${monto_final}")


# Llamar a la función main
main()
