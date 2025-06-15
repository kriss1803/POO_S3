
# Función para ingresar temperaturas diarias durante 7 días
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de cada día de la semana:")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
