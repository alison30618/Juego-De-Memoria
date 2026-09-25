from Bicicleta import Bicicleta

def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\nSISTEMA DE ALQUILER DE BICICLETAS")
    print("1. Consultar información de la bicicleta")
    print("2. Calcular costo de un alquiler")
    print("3. Actualizar tarifa por hora")
    print("0. Salir")

def main():
    bicicleta = Bicicleta("B001", "montaña", 10000)

    opcion = "-1"

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            informacion = bicicleta.obtener_informacion()

            print("\nINFORMACIÓN DE LA BICICLETA")
            print(informacion)

        elif opcion == "2":
            while True:
                try:
                    horas_uso = float(input("Ingrese las horas de uso: "))

                    if horas_uso <= 0:
                        print("Las horas de uso deben ser mayores que cero.")
                    else:
                        break

                except ValueError:
                    print("ERROR. Por favor, ingrese un número válido.")

            costo = bicicleta.calcular_costo_alquiler(horas_uso)

            print(f"El costo del alquiler es: ${costo:,.0f}")

        elif opcion == "3":
            try:
                nueva_tarifa = float(
                    input("Ingrese la nueva tarifa por hora: ")
                )

                actualizada = bicicleta.actualizar_tarifa(nueva_tarifa)

                if actualizada:
                    print("Tarifa actualizada correctamente.")
                else:
                    print(
                        "La tarifa debe ser mayor que cero. "
                        "La tarifa anterior se conserva."
                    )

            except ValueError:
                print(
                    "ERROR. Debe ingresar un valor numérico. "
                    "La tarifa anterior se conserva."
                )

        elif opcion == "0":
            print("Programa finalizado.")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()