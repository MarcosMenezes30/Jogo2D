from abc import ABC, abstractclassmethod


class Imprimir:
    def imprime(self):
        print("Ola mundo!")


class Imprimirpersonalizado(ABC):
    @abstractclassmethod
    def imprime(self):
        pass


class ImprimeNome(Imprimirpersonalizado):
    def imprime(self, nome):
        print(f"Olá, {nome}!")


class UtilizaImpressao(Imprimir): 
    def metodo(self):
        Imprimir.imprime(self)


if __name__ == "__main__":

    # ip = Imprimir()
    # ip.imprime()
    hp = UtilizaImpressao()
    hp.metodo()
