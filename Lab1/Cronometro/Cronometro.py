import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = None

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return(time.time() * 1000) - self.__inicia
        return self.__finaliza - self.__inicia

#Programa de prueba testeo

def ordenacion_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

if __name__ == "__main__":
    print("generar lista de 100000 números...")
    numeros = [random.randint(1,100000) for _ in range(100000)]
    #Esta cantidad de números en python se hizo demasiado grande, y tarda varioa minutos en terminar
    #para pruebas, usé 10000 números, que dió un aproximado de 4 segundos en consola

    timer = Cronometro()

    print("ordenando lista por seleccion...")
    ordenacion_por_seleccion(numeros)

    timer.detener()

    print(f"El tiempo de ordenación de números fué: {timer.lapsoDeTiempo():.2f} ms")