import forca
import adivinhacao_10

def escolhe_jogo():
    print("################################")
    print("********Escolha seu jogo********")
    print("################################")

    print("\n(1) Força - (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Força")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao_10.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
