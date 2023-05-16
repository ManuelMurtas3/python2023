# TASK: CREARE UN SISTEMA DI ORDINAMENTO AD OGGETTI
# SI POSSONO ORDINARE MAX 4 PIATTI FISSI, MODIFICARE UN PIATTO, O AVERE IL CONTO
# OGNI PIATTO HA NOME E PREZZO
# SE CHIEDIAMO IL CONTO, CI DEVE CHIEDERE NOME E COGNOME E POI STAMPARE IL TOTALE E PIATTI A SCHERMO POI RITORNIAMO AL MENU INIZIALE
# OGGETTO CON QUALI PIATTI, QUANTO HO SPESO, CHI HA SPESO
# Vai a far si che si possa eliminare e aggiungere alla lista un piatto (parte 2)
# Vai a far si che l'utente possa creare il suo profilo prima di poter ordinare (parte 3)

#classe per la memorizzazione dei piatti del menu
class Piatto:
    nome = ""
    prezzo = 0.0

    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def modifica_nome(self, nome):
        self.nome = nome
    
    def modifica_prezzo(self, prezzo):
        self.prezzo = prezzo
    
    def to_string(self):
        #stringa da utilizzare per stampare il nome
        return f"Piatto: {self.nome} | Prezzo: € {self.prezzo}"

#classe per la memorizzazione delle ordinazioni
class Ordinazione:
    piatti = []
    nominativo = ""

    def __init__(self):
        self.piatti = []
        self.nominativo = ""

    def ordina_piatto(self, piatto):
        if len(self.piatti) >= 4:
            print("Errore, non puoi aggiungere altri piatti all'ordinazione")
        else:
            #aggiungo il piatto alle ordinazioni (nuovo oggetto! se no si modifica)
            self.piatti.append(Piatto(piatto.nome, piatto.prezzo))

    def totale(self):
        totale = 0.0
        for piatto in self.piatti:
            totale += piatto.prezzo
        return totale

    def inserisci_nominativo(self, nominativo):
        self.nominativo = nominativo

    def stampa_conto(self):
        print(f"\nConto di {self.nominativo}")
        for piatto in self.piatti:
            print(piatto.to_string())
        print(f"Totale: € {self.totale()}\n")

#menu fisso del ristorante di 4 piatti
menu = [Piatto("Primo", 15.0), Piatto("Secondo", 20.0), Piatto("Contorno", 5.0), Piatto("Dolce", 10.0)]

def switch_accesso():
    option = "ok"
    while option != "0":
        print("Benvenuto! Selezione l'opzione desiderata:")
        print("1. Accedi")
        print("0. Esci")
        option = input("Inserisci la tua scelta: ")
        print()

        if option == "1":
            #accesso al sistema di ordinazione
            switch_menu()
        elif option == "0":
            #uscita dal programma
            print("Arrivederci")
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

def switch_menu():
    option = 0
    ordinazione = Ordinazione()
    while option != "3":
        print("Benvenuto! Selezione l'opzione desiderata:")
        print("1. Ordina un piatto")
        print("2. Modifica un piatto")
        print("3. Ottieni il conto ed esci")
        print("4. Aggiungi un piatto al menù")
        print("5. Rimuovi un piatto dal menù")
        option = input("Inserisci la tua scelta: ")
        print()

        if option == "1":
            #ordinazione piatto
            indice_piatto = switch_piatti("Ordina il tuo piatto")
            ordinazione.ordina_piatto(menu[indice_piatto])

        elif option == "2":
            #modifica piatto
            indice_piatto = switch_piatti("Seleziona che piatto modificare")
            nome = input("Inserisci il nuovo nome del piatto: ")
            prezzo = float(input("Inserisci il nuovo prezzo del piatto: € "))
            menu[indice_piatto].modifica_nome(nome)
            menu[indice_piatto].modifica_prezzo(prezzo)
            print("\nPiatto modificato con successo\n")

        elif option == "3":
            #ottieni conto
            nominativo = input("Inserisci il tuo nome e cognome: ")
            ordinazione.inserisci_nominativo(nominativo)
            ordinazione.stampa_conto()
        
        elif option == "4":
            #aggiungi piatto al menu
            nome = input("Inserisci il nome del nuovo piatto: ")
            prezzo = float(input("Inserisci il prezzo del nuovo piatto: € "))
            menu.append(Piatto(nome, prezzo))
            print("\nPiatto aggiunto con successo\n")

        elif option == "5":
            # rimuovi piatto dal menu
            indice_piatto = switch_piatti("Seleziona il piatto che vuoi rimuovere")
            menu.pop(indice_piatto)
            print("\nPiatto rimosso con successo\n")

        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

def switch_piatti(messaggio):
    exit_flag = False
    while not exit_flag:
        print(messaggio)
        numero_opzione = 1
        for piatto in menu:
            print(f"{numero_opzione}. {piatto.to_string()}")
            numero_opzione += 1

        option = int(input("Inserisci il numero del piatto: "))
        print()

        #selezione del piatto in base all'indice nel menu
        if option >= 1 and option <= len(menu):
            return option - 1
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")
            continue

switch_accesso()