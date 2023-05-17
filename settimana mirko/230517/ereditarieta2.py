# Creare un eredita lineare di tre classi che stampi tre attributi proprietari singoli

class Uno:
    def __init__(self, numero):
        self.numero = numero
    def to_string(self):
        print(f"Numero = {self.numero}")

class Due(Uno):
    def __init__(self, numero, decimale):
        super().__init__(numero)
        self.decimale = decimale
    def to_string(self):
        super().to_string()
        print(f"Decimale = {self.decimale}")

class Tre(Due):
    def __init__(self, numero, decimale, stringa):
        super().__init__(numero, decimale)
        self.stringa = stringa
    def to_string(self):
        super().to_string()
        print(f"Stringa = {self.stringa}")

uno = Uno(1)
due = Due(1, 2.0)
tre = Tre(1, 2.0, "3")

uno.to_string()
print()
due.to_string()
print()
tre.to_string()