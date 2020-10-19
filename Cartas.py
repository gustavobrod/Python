from random import shuffle

class Baralho:
    'representa um baralho de 52 cartas'

# valores e naipes são variáveis da classe Baralho
valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
# naipes são 4 símbolos Unicode representando os 4 naipes
naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

def __init__(self):
    'inicializa baralho de 52 cartas'
    self.baralho = []       # baralho está inicialmente vazio
    
    for naipe in Baralho.naipes: # naipes e valores são Baralho
        for valor in Baralho.valores: # variáveis da classe
            # inclui Carta com certo valor e naipe no baralho
            self.baralho.append(Carta(valor, naipe))

def distribuiCarta:
    'distribui (remove e retorna) carta do topo do baralho'
    return self.baralho.pop()

def shuffle(self):
    'mistura o baralho'
    shuffle(self.baralho)
    