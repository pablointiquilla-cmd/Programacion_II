class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__d = float(d)
        self.__e = float(e)
        self.__f = float(f)

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        if not self.tieneSolucion():
            return None
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        if not self.tieneSolucion():
            return None
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)

#Tester

if __name__ == "__main__":
    datos = input("ingrese a, b, c, d, e, f: ").split()

    if len(datos) == 6:
        coef_a, coef_b, coef_c, coef_d, coef_e, coef_f = map(float, datos)
        ecuacion = EcuacionLineal(coef_a, coef_b, coef_c, coef_d, coef_e, coef_f)

        if ecuacion.tieneSolucion():
            print(f"X = {ecuacion.getX():.1f}, Y = {ecuacion.getY():.1f}")
        else:
            print("La ecuación no tiene solución")
    else:
        print("ingrese seis numeros, coheficientes de su sistema")