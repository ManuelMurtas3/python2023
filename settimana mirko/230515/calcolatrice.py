#calcolatrice che esegua 3 calcoli in fila a scelta tra addizione, sottrazione e moltiplicazione che salvi ogni risultato e il risultato finale in un oggetto

class Calcolatrice:
    operazioni = []

    def pulisci_operazioni(self):
        self.operazioni = []

    def carica_risultato (self, risultato, operatore):
        self.operazioni.append((risultato, operatore))
        return

    def somma(self, primo_numero, secondo_numero):
        return primo_numero + secondo_numero
    
    def sottrai(self, primo_numero, secondo_numero):
        return primo_numero - secondo_numero
    
    def moltiplica(self, primo_numero, secondo_numero):
        return primo_numero * secondo_numero
    
    def totale(self):
        if self.operazioni == []:
            return None
        else:
            return self.operazioni[0][0] + self.operazioni[1][0] + self.operazioni[2][0]
        
    def stampa_operazioni(self):
        if self.operazioni == []:
            print("Non sono state eseguite operazioni")
        else:
            for risultato, operatore in self.operazioni:
                print(f"Risultato: {risultato} | Operazione: {operatore}")
        return
    

exit_flag = False
calcolatrice = Calcolatrice()

while not exit_flag:
    print("\nBuongiorno! Selezionare l'opzione desiderata")
    print("1. Conta")
    print("2. Stampa")
    print("0. Esci")
    scelta = input("Inserisci la tua scelta: ")
    print()

    if scelta == '0':
        print("Arrivederci!")
        exit_flag = True

    elif scelta == '1':
        calcolatrice.pulisci_operazioni()
        contatore = 0
        while contatore < 3:
            contatore += 1
            print(f"- operazione numero {contatore} -")
            primo_numero = float(input("Inserire il primo numero: "))
            secondo_numero = float(input("Inserire il secondo numero: "))
            operatore = input("Inserire l'operatore (+, -, *): ")

            if operatore == '+':
                risultato = calcolatrice.somma(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            elif operatore == '-':
                risultato = calcolatrice.sottrai(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            elif operatore == '*':
                risultato = calcolatrice.moltiplica(primo_numero, secondo_numero)
                calcolatrice.carica_risultato(risultato, operatore)

            else:
                print("Errore, l'operatore da te selezionato non esiste")
                contatore -= 1
            
            print()
        
        print(f"\nSomma totale: {calcolatrice.totale()}")

    elif scelta == '2':
        calcolatrice.stampa_operazioni()

    else:
        print("Errore, l'opzione da te selezionata non esiste")