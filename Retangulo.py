#2. Crie uma classe chamada Retangulo, a qual possua os atribu tos largura e altura, e os métodos
#calcularPerimetro() e calcularArea(). No código de teste, crie um objeto e calcule, respectivamente,
#o perímetro e a área desse retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return 2 * (self.largura + self.altura)

    def calcularArea(self):
        return self.largura * self.altura

if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    print("Perímetro do retângulo:", retangulo.calcularPerimetro())
    print("Área do retângulo:", retangulo.calcularArea())