from color import Color
from figurageometrica import figurageometrica

class cuadrado(figurageometrica, Color):
    def __init__(self, lado=0, color=None):
        figurageometrica.__init__(self, ancho=lado, alto=lado)  # ambos lados iguales en un cuadrado
        Color.__init__(self,nombre= color)

    def __str__(self):
        return f"cuadrado -> {self.__dict__.__str__()}"

if __name__ == "__main__":
    c1 = cuadrado(lado=6, color= "Rojo")
    print(c1)
    print(f'Area: {c1.area()}')
    print(f'Perimetro: {c1.perimetro()}')