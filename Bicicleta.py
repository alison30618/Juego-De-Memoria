class Bicicleta:
    def __init__(self, id_bicicleta, tipo, tarifa_base_por_hora):
        """Establece el estado inicial de una bicicleta."""
        self.__id_bicicleta = id_bicicleta
        self.__tipo = tipo
        self.__tarifa_base_por_hora = tarifa_base_por_hora

    def calcular_costo_alquiler(self, horas_uso):
        """Calcula y retorna el costo de un alquiler."""
        costo_base = self.__tarifa_base_por_hora * horas_uso

        if self.__tipo == "montaña":
            costo_total = costo_base * 1.10
        elif self.__tipo == "eléctrica":
            costo_total = costo_base * 1.25
        else:
            costo_total = costo_base

        return costo_total

    def actualizar_tarifa(self, nueva_tarifa):
        """Actualiza la tarifa si el nuevo valor es válido."""
        if nueva_tarifa > 0:
            self.__tarifa_base_por_hora = nueva_tarifa
            return True

        return False

    def obtener_informacion(self):
        """Retorna un texto con la información de la bicicleta."""
        informacion = (
            f"Identificador: {self.__id_bicicleta}\n"
            f"Tipo: {self.__tipo}\n"
            f"Tarifa por hora: ${self.__tarifa_base_por_hora:,.0f}"
        )
        return informacion

    def main():
             

    