class Auto:
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self._anio = None     # usaremos property para validar
        self.anio = anio      # pasa por el setter de anio
        self.__kilometraje = 0  # privado, arranca en 0

    # --- Kilometraje encapsulado ---
    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self.__kilometraje = valor

    # --- Año con property (opcional pero útil) ---
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if not isinstance(valor, int):
            raise TypeError("El año debe ser un entero.")
        if valor < 1886:
            raise ValueError("Un auto no puede ser anterior a 1886.")
        self._anio = valor

if __name__ == "__main__":
# Prueba rápida
    auto1 = Auto("Chevrolet", "Corsa Wagon", "azul marino", 2007)
    auto1.kilometraje = 120     # OK
# auto1.kilometraje = -5    # ← debería lanzar ValueError