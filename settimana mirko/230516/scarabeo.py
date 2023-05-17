"""
from random import random

class Scarabeo:
    lettere = 'abcdefghijklmnopqrstuvwxyz'
    lunghezza = 4

    def __init__(self, lunghezza):
        self.lunghezza = lunghezza

    def crea(self):
        parola = ['a','a','a','a']
        for i in range(4):
            parola[i] = self.lettere[int((random() * 100) % len(self.lettere))]
        return ''.join(parola)

scarabeo = Scarabeo(4)
print(scarabeo.crea())
"""

from random import random

class Scarabeo:
    consonanti = 'bcdfghjklmnpqrstvwxyz'
    vocali = 'aeiou'
    lunghezza = 4

    def __init__(self, lunghezza):
        self.lunghezza = lunghezza

    def crea(self):
        parola = ['a','a','a','a']
        for i in range(4):
            if i % 2 == 0:
                parola[i] = self.consonanti[int((random() * 100) % len(self.consonanti))]
            else:
                parola[i] = self.vocali[int((random() * 100) % len(self.vocali))]
        return ''.join(parola)

scarabeo = Scarabeo(4)
print(scarabeo.crea())