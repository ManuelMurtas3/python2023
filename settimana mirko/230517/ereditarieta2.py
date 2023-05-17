# Creare un eredita lineare di tre classi che stampi tre attributi proprietari singoli

class Uno:
    def __init__(self, numero):
        self.numero = numero
    def to_string(self):
        print(f"Numero = {self.numero}")

class Due(Uno):
    def __init__(self, numero):
        super().__init__(numero)
    def to_string(self):
        super().to_string()

class Tre(Due):
    def __init__(self, numero):
        super().__init__(numero)
    def to_string(self):
        super().to_string()

uno = Uno(1)
due = Due(2)
tre = Tre(3)

uno.to_string()
due.to_string()
tre.to_string()