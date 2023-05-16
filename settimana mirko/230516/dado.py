from random import random

class Dado:
    facce = 20

    def __init__(self, numero_facce):
        facce = numero_facce

    def lancia(self):
        return int(((random() * 100) % self.facce) + 1) #il limite di facce è 100

dado = Dado(20)
print(dado.lancia())