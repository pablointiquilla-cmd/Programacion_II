#Solución modlar
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_desviacion(numeros):
    n = len(numeros)
    prom = calcular_promedio(numeros)
    suma_cuadrados = sum((x - prom) ** 2 for x in numeros)
    return (suma_cuadrados / (n - 1)) ** 0.5

# Programa de prueba estructurado
if __name__ == "__main__":
    datos = input("Ingrese 10 números: ").split()
    if len(datos) == 10:
        numeros = [float(x) for x in datos]
        print(f"El promedio es {calcular_promedio(numeros):.2f}")
        print(f"La desviación estándar es {calcular_desviacion(numeros):.5f}")