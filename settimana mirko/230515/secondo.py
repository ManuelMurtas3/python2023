class Persona:
    age = 0
    name = ""

    #metodo costruttore
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
def nomechevoglio(*kids):
    print("il più giovane è: " + kids[2])

nomechevoglio("Emil", "Tobias", "Linus")
pippo = Persona("mirko", 10)

