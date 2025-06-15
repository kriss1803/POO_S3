class ClimaDia:
    """
    Clase que representa el clima de un día.
    """
    def __init__(self, temperatura=0.0):
        self._temperatura = temperatura  # Encapsulamiento

    def establecer_temperatura(self, temperatura):
        self._temperatura = temperatura

    def obtener_temperatura(self):
        return self._temperatura


class SemanaClimatica:
    """
    Clase que gestiona las temperaturas de una semana.
    """
    def __init__(self):
        self.dias = [ClimaDia() for _ in range(7)]  # Composición

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas para los 7 días:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.dias[i].establecer_temperatura(temp)

    def calcular_promedio(self):
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)


def main():
    semana = SemanaClimatica()
    semana.ingresar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
