#1. Crie uma classe chamada Ingresso, que possua o nome do
#evento e o valor do ingresso. Crie o método exibirValor(),
#que apenas retorne o valor do ingresso. Crie o método __str__ que
#retorne o nome do evento seguido do valor do ingresso. Crie um programa para testar sua classe.


class Ingresso:
    def __init__(self, nome_evento, valor):
        self.nome_evento = nome_evento
        self.valor = valor

    def exibirValor(self):
        return self.valor

    def __str__(self):
        return f"{self.nome_evento}: R${self.valor:.2f}"

if __name__ == "__main__":
    ingresso = Ingresso("Show de Samba", 10.00)
    print(ingresso)
    print("Valor do ingresso:", ingresso.exibirValor())