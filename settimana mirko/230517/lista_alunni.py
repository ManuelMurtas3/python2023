#CREARE UNA CLASSE LISTAALLUNNI, che dovrà essere sempre valorizzata appena si accede al primo menu
#Un primo menu con entra o esci, se esci si chiude tutto, se entri devi darmi X nomi obbligatori e X corrispettivi voti agli studenti
# L'esercizio sarà creare un sistema che permetta di andare a scegliere un singolo utente e di modificare e aggiungere i suoi voti 

class Alunno:
    def __init__(self, nome):
        self.nome = nome

    def to_string(self):
        return f"Alunno: {self.nome}"

class SchedaAlunno(Alunno):
    def __init__(self, nome, voto):
        super().__init__(nome)
        self.voti = list()
        self.voti.append(voto)

    def modifica_voto(self, indice, voto):
        #modifico il voto in base al nuovo voto fornito e all'indice nella lista del voto che si vuole modificare
        if 0 <= indice < len(self.voti):
            self.voti[indice] = voto

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def to_string(self):
        return super().to_string() + f" | Voti: {' '.join([str(voto) for voto in self.voti])}"
    
class ListaAlunni:
    lista_schede_alunni = []

    def __init__(self, nomi, voti):
        for i in range(len(nomi)):
            self.lista_schede_alunni.append(SchedaAlunno(nomi[i], voti[i]))

    def cerca_alunno(self, nome):
        for alunno in self.lista_schede_alunni:
            if alunno.nome == nome:
                return alunno
        return None
    
    def stampa_registro(self):
        for scheda in self.lista_schede_alunni:
            print(scheda.to_string())

def switch_accesso():
    option = "ok"
    while option != "0":
        print("Benvenuto! Selezione l'opzione desiderata:")
        print("1. Accedi")
        print("0. Esci")
        option = input("Inserisci la tua scelta: ")
        print()

        if option == "1":
            #accesso al sistema lista alunni
            alunni = input("Inserisci la lista dei nomi degli alunni: ").strip().lower().split(" ")
            voti = input("Inserisci la lista di voti degli alunni: ").strip().lower().split(" ")
            print()
            lista_alunni = ListaAlunni(alunni, [int(voto) for voto in voti])
            switch_registro(lista_alunni)
        elif option == "0":
            #uscita dal programma
            print("Arrivederci")
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

def switch_registro(lista_alunni):
    option = "ok"
    while option != "0":
        print("Selezione l'opzione desiderata:")
        print("1. Visualizza registro")
        print("2. Gestisci voti alunno")
        print("0. Esci")
        option = input("Inserisci la tua scelta: ")
        print()

        if option == "1":
            #visualizza registro
            lista_alunni.stampa_registro()
            print()

        elif option == "2":
            #gestisci voti alunno
            nome = input("Inserisci il nome dell'alunno di cui gestire i voti: ")
            print()
            alunno = lista_alunni.cerca_alunno(nome) #ottengo l'alunno cercato
            switch_alunno(alunno)

        elif option == "0":
            #uscita dal programma
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

def switch_alunno(alunno):    
    option = "ok"
    while option != "0":
        print("Selezione l'opzione desiderata:")
        print("1. Modifica voto")
        print("2. Aggiungi voto")
        print("0. Esci")
        option = input("Inserisci la tua scelta: ")
        print()

        if option == "1":
            #modifica voto
            indice = switch_voto(alunno) #ottengo il voto cercato
            nuovo_voto = int(input("Inserisci il nuovo voto: "))
            alunno.modifica_voto(indice, nuovo_voto)
            print("Voto modificato correttamente\n")

        elif option == "2":
            #aggiungi voto
            voto = int(input("Inserisci un nuovo voto: "))
            alunno.aggiungi_voto(voto)
            print("Voto aggiunto correttamente\n")

        elif option == "0":
            #uscita dal programma
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

def switch_voto(alunno):
    #switch che ritorna l'indice del voto selezionato come "da modificare"
    exit_flag = False
    while not exit_flag:
        print("Seleziona il voto da modificare: ")

        #visualizzo una lista di voti indicizzati da numero_opzione
        numero_opzione = 1
        for voto in alunno.voti:
            print(f"{numero_opzione}. {voto}")
            numero_opzione += 1

        option = int(input("Inserisci il numero del dell'indice del voto: "))
        print()

        #selezione del voto in base all'indice nell'elenco dei voti
        if option >= 1 and option <= len(alunno.voti):
            return option - 1
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

switch_accesso()