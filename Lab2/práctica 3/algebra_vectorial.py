import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # Componentes del vector tridimensional (a1, a2, a3)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # a) Suma de dos vectores: c = a + b
    def __add__(self, otro):
        return Vector3D(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )

    # b) Multiplicación de un escalar r por un vector: b = r * a
    def __rmul__(self, escalar):
        return Vector3D(
            escalar * self.x,
            escalar * self.y,
            escalar * self.z
        )

    # c) Longitud o módulo de un vector: |a|
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # d) Normal (vector unitario) de a: b = a / |a|
    def normal(self):
        mod = self.modulo()
        if mod == 0:
            print("Error: No se puede normalizar el vector nulo.")
            return Vector3D(0, 0, 0)
        return Vector3D(
            self.x / mod,
            self.y / mod,
            self.z / mod
        )

    # e) Producto escalar de a y b (Operador @ o multiplicación directa)
    def __matmul__(self, otro):
        return (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)

    # f) Producto vectorial de a y b: a x b (Sobrecarga de operador *)
    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            # Soporte para multiplicar vector * escalar
            return Vector3D(self.x * otro, self.y * otro, self.z * otro)
        
        # Producto vectorial si el otro objeto es un Vector3D
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return Vector3D(cx, cy, cz)

    # Representación en cadena para mostrar las coordenadas
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


# --- Programa Principal de Prueba ---
if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    print("Vector a:", a)
    print("Vector b:", b)
    print("-" * 35)

    # a) Suma
    suma = a + b
    print("a) Suma (a + b):", suma)

    # b) Multiplicación por escalar
    escalar = 3
    mult_escalar = escalar * a
    print(f"b) Escalar por vector ({escalar} * a):", mult_escalar)

    # c) Longitud / Módulo
    print(f"c) Longitud de a (|a|): {a.modulo():.4f}")

    # d) Normal
    print("d) Normal de a:", a.normal())

    # e) Producto escalar (usando el operador @)
    prod_escalar = a @ b
    print("e) Producto escalar (a · b):", prod_escalar)

    # f) Producto vectorial (usando el operador *)
    prod_vectorial = a * b
    print("f) Producto vectorial (a x b):", prod_vectorial)