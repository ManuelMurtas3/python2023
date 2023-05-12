menu = {}
ordine = {}

exit_flag = False #mi indica quando uscire dal ciclo di richiesta dei comandi

while not exit_flag:
    print("\nBenvenuto nel ristorante. Selezionare l'opzione desiderata")
    print("1. Aggiungi un piatto al menù")
    print("2. Visualizza il menù")
    print("3. Cancella un piatto dal menù")
    print("4. Ordina un piatto")
    print("5. Richiedi il conto")
    print("0. Esci")
    scelta = input("Inserisci la tua scelta: ")
    print()

    if scelta == '0':
        #richiesta uscita dal programma
        print("Arrivederci!")
        exit_flag = True

    elif scelta == '1':
        # Aggiungi un piatto al menù
        nome_piatto = input("Inserisci il nome del piatto da inserire: ").strip().lower()
        prezzo = float(input("Inserisci il prezzo del piatto da inserire: € "))
        
        if prezzo < 0:
            print("\nErrore, il prezzo non può essere negativo.")
        else:
            # registro il piatto nel menu come nome: prezzo
            menu[nome_piatto] = prezzo
            print("Piatto registrato correttamente")
    
    elif scelta == '2':
        # Visualizza il menù
        for nome, prezzo in menu.items():
            print(f"Piatto: {nome} - Prezzo: €{prezzo}")

    elif scelta == '3':
        # Cancella un piatto dal menù
        nome_piatto = input("Inserisci il nome del piatto da cancellare: ").strip().lower()
        if nome_piatto in menu.keys():
            menu.pop(nome_piatto)
            print("Piatto rimosso correttamente")
        else:
            print("Errore, il piatto da te inserito è non presente nel menù")

    elif scelta == '4':
        # Ordina un piatto
        nome_piatto = input("Inserisci il nome del piatto da ordinare: ").strip().lower()
        quantita = int(input("Inserisci la quantità da ordinare: "))

        if nome_piatto not in menu.keys():
            print("Errore, il piatto da te inserito non è presente nel menù")
        elif quantita < 0:
            print("\nErrore, la quantità non può essere negativa.")
        else:
            if nome_piatto in ordine.keys():
                #aggiungo una nuova quantità di piatto all'ordinazione
                ordine[nome_piatto] += quantita
            else:
                #registro la prima ordinazione per questo piatto
                ordine[nome_piatto] = quantita
            print("Piatto ordinato correttamente")

    elif scelta == '5':
        # Richiedi il conto
        totale = 0.0
        for nome, quantita in ordine.items():
            print(f"{nome} x {quantita} = € {menu[nome]} x {quantita} = € {menu[nome] * quantita}")
            totale += (menu[nome] * quantita)
        print(f"Totale: € {totale}")
        ordine = {} #una volta richiesto il conto azzero l'ordine

    else:
        #opzione inesistente
        print("Errore, l'opzione da te selezionata non esiste")
