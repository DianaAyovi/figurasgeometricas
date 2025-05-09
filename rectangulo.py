from figurageometrica import figurageometrica
from color import Color

class rectangulo(figurageometrica, Color):
    def __init__(self, alto=0, ancho=0, color=None):
        figurageometrica.__init__(self, alto, ancho)
        Color.__init__(self,color)

    def __str__(self):
        return f"rectángulo -> {self.__dict__.__str__()}"

if __name__ == "__main__":
    r1 = rectangulo(alto=5,ancho=3, color="Rojo")
    print(r1)
    print(f'Area: {r1.area()}')
    print(f'Perimetro: {r1.perimetro()}')