import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        # a) Atributos privados
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)


#Tester programa de prueba
if __name__ == "__main__":
    datos = input("Ingrese a, b, c: ").split()
    
    if len(datos) == 3:
        coef_a, coef_b, coef_c = map(float, datos)
        eq = EcuacionCuadratica(coef_a, coef_b, coef_c)
        disc = eq.getDiscriminante()

        if disc > 0:
            print(f"La ecuación tiene dos raíces {eq.getRaiz1():.5f} y {eq.getRaiz2():.5f}")
        elif disc == 0:
            print(f"La ecuación tiene una raíz {eq.getRaiz1():.1f}")
        else:
            print("La ecuación no tiene raíces reales")
    else:
        print("Debe ingresar exactamente 3 números.")