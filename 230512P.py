'''
Scrivere un programma python per la gestione di un registro vendite 
Il programma deve permettere di aggiungere le vendite di diversi prodotti e calcolare il totale delle vendite (per ogni prodotto)
OPERAZIONI: 
1) Aggiungi una vendita di un prodotto (si richiede all'utente il nome del prodotto, la quantità ed il prezzo per unità)
2) Visualizzare il totale delle vendite per ogni prodotto per ogni prodotto presente nel registro 
Suggerimento: utilizzare un dizionario per memorizzare le vendite dei prodotti
(le chiavi sono i nomi dei prodotti e i valori sono liste che contengono quantità e prezzo unitario) 
'''

exit_flag = False #mi indica quando uscire dal ciclo di richiesta dei comandi
prodotti = {}

while not exit_flag:
    print("\nBenvenuto nel registro vendite. Selezionare l'opzione desiderata")
    print("1. Registra una vendita")
    print("2. Visualizza il totale delle vendite")
    print("0. Esci")
    scelta = input("Inserisci la tua scelta: ")
    print()

    if scelta == '0':
        #richiesta uscita dal programma
        exit_flag = True

    elif scelta == '1':
        #richiesta registrazione di una vendita
        nome_prodotto = input("Inserire il nome del prodotto: ").strip().lower() #in modo che prodotti scritti in modo simile siano uguali
        quantita = int(input(f"Inserire la quantità di {nome_prodotto} venduto: "))
        prezzo = float(input("Inserire il prezzo del prodotto unitario: € "))

        #controllo che non abbia inserito prezzi o quantità negativi
        if prezzo < 0 or quantita < 0:
            print("Errore, non puoi inserire una quantità o un prezzo negativo")
        else:
            #mi salvo strutturalmente quantità e prezzi venduti (vengono sovrascritti se reinserito)
            prodotti[nome_prodotto] = {"quantita": quantita, "prezzo": prezzo}
            print("\nVendita registrata correttamente")

    elif scelta == '2':
        #richiesta visualizzazione prodotti
        for nome, dettagli in prodotti.items():
            print(f"Prodotto: {nome}, fatturato: € {dettagli['quantita'] * dettagli['prezzo']}")

    else:
        #opzione inesistente
        print("Errore, l'opzione da te selezionata non esiste")
