class Persona:
    tipo = "umano"

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def MasterD(self):
        print(f"ciao sono {self.nome} {self.tipo}")

x = Persona("Mirko", 99)
x.MasterD()

class Allievo(Persona):
    tipo = "gatto"
    
    def __init__(self, nome, eta, grado):
        super().__init__(nome, eta)
        self.grado = grado

    def MasterD(self):
        print(f"ciao sono {self.nome} {self.tipo} {self.grado}")

y = Allievo("Marius", 23, "Terzo Dan")
y.MasterD()