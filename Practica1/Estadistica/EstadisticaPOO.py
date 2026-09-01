# --- ENFOQUE ORIENTADO A OBJETOS ---

class Estadistica:
    def __init__(self, datos):
        # Acá encapsulamos la lista
        self.__datos = [float(x) for x in datos]

    # COMENTARIO SOBRE POO:
    # Lo mejor de POO aquí es que los métodos no necesitan recibir "datos" por parámetro
    # cada método trabaja directamente con el estado interno (__datos) de la clase.
    def promedio(self):
        if not self.__datos:
            return 0.0
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        n = len(self.__datos)
        if n <= 1:
            return 0.0
        prom = self.promedio() # Reutilizamos el método propio del objeto
        suma_cuadrados = sum((x - prom) ** 2 for x in self.__datos)
        return (suma_cuadrados / (n - 1)) ** 0.5


#Tester
if __name__ == "__main__":
    entrada = input("Ingrese 10 números: ").split()
    
    if len(entrada) == 10:
        stats = Estadistica(entrada)
        
        print(f"El promedio es {stats.promedio():.2f}")
        print(f"La desviación estándar es {stats.desviacion():.5f}")
    else:
        print("Debe ingresar exactamente 10 números.")


"""
Acá pude usar cosas como encapsulamiento de objetos, reutilización y otros, cosa que
con programación modular o estructurada no es posible
"""