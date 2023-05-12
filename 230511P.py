##Esercizio Bancomat, by Manuel Murtas & co.
# 
#u1_pin = '1234'
#u2_pin = '5678'
# 
#utente_corrente = 0
#counter_errore = 0
#pin_ok = True
# 
#u1_conto = 50
#u2_conto = 100
#
#u1_iban = "ABCD"
#u2_iban = "QWER"
# 
##saldo, prelevare, deposita, ci sono 2 conti e si puo fare bonifico, si fa iban corto per tutti e due
# 
# 
##prima parte per inserimento pin
#while counter_errore < 4:
#    pin_utente = input('inserire pin: ')
#    
#    if pin_utente == u1_pin:
#        utente_corrente = 1
#        break
#    elif pin_utente == u2_pin:
#        utente_corrente = 2
#        break
#    else:
#        print('PIN errato, reinserire pin')
#        counter_errore += 1
# 
# 
##parte per selezione operazione
#if counter_errore == 4:
#    print('Hai sbagliato troppe volte, riprova più tardi')
#else:
#    print(f'Benvenuto utente {utente_corrente} ')
#    while pin_ok:
#        scelta = input("""seleziona l'operazione: 
#        premi 1 per prelevare: 
#        premi 2 per visualizzare saldo:
#        premi 3 per ricarica cellulare:
#        premi 4 per fare bonifico:
#        scrivi 'exit' per uscire
#        """)
#    
#        if scelta == 'exit':
#            pin_ok = False
#        
#        elif scelta == '1': 
#            if utente_corrente == 1:
#                print(f'Il tuo saldo è {u1_conto}.')
#            else:
#                print(f'Il tuo saldo è {u2_conto}.')
#           
#            prelievoOk = True
#            while prelievoOk:
#                scelta_prelievo = input('Digitare 0 per importo fisso, altrimenti digitare 1 per importo a scelta: \n')
#                if scelta_prelievo == '0':
#                    
#                    ind_prelievoFisso = int(input("""quanto vuoi prelevare?: 
#                    premi 1 per prelevare 20: 
#                    premi 2 per prelevare 50:
#                    premi 3 per prelevare 100:
#                    """))
#                
#                    quantita_prelievi = [20, 50, 100]
#                    
#                    if utente_corrente == 1:
#                        if u1_conto - quantita_prelievi[ind_prelievoFisso - 1] < 0:
#                            print('Non ci sono abbastanza soldi')
#                        else:
#                            u1_conto -= quantita_prelievi[ind_prelievoFisso - 1]
#                    elif utente_corrente == 2:          
#                        if u2_conto - quantita_prelievi[ind_prelievoFisso - 1] < 0:
#                            print('Non ci sono abbastanza soldi')
#                        else:
#                            u2_conto -= quantita_prelievi[ind_prelievoFisso - 1]
#                    prelievoOk = False
#                elif scelta_prelievo == '1':
#                    prelievo_var = int(input("Digita la cifra da prelevare ricordando che deve essere multiplo di 5\n"))
#                    if prelievo_var % 5 != 0:
#                        print("Perdonami, rinizia")
#                    else:
#                        if utente_corrente == 1:
#                            if u1_conto - prelievo_var < 0:
#                                print('Non ci sono abbastanza soldi')
#                            else:
#                                u1_conto -= prelievo_var
#                        elif utente_corrente == 2:          
#                            if u2_conto - prelievo_var < 0:
#                                print('Non ci sono abbastanza soldi')
#                            else:
#                                u2_conto -= prelievo_var
#                    prelievoOk = False
#                else:
#                    print("L'opzione inserita non esiste")
#                    prelievoOk = True
#            pin_ok = False
#
#        elif scelta == '2':
#            if utente_corrente == 1:
#                print(f'Il tuo saldo è {u1_conto}.')
#            else:
#                print(f'Il tuo saldo è {u2_conto}.')
#        elif scelta == '4':
#            if utente_corrente == 1:
#                quantita = int(input("Inserire importo bonifico: "))
#                if quantita > u1_conto:
#                    print("Non hai abbastanza soldi")
#                else:
#                    iban_input = input("Inserisci iban: ").upper()
#                    if iban_input == u2_iban:
#                        u1_conto -= quantita
#                        u2_conto += quantita
#                    else:
#                        print("Iban non valido")
#                    print("Bonifico effettuato")
#                print(f"Il tuo saldo è {u1_conto}")
#            elif utente_corrente == 2:
#                quantita = int(input("Inserire importo bonifico: "))
#                if quantita > u2_conto:
#                    print("Non hai abbastanza soldi")
#                else:
#                    iban_input = input("Inserisci iban: ").upper()
#                    if iban_input == u1_iban:
#                        u2_conto -= quantita
#                        u1_conto += quantita
#                    else:
#                        print("Iban non valido")
#                    print("Bonifico effettuato")
#                print(f"Il tuo saldo è {u2_conto}")
#            
#
#print(u1_conto, u2_conto)

exit_flag = False

while not exit_flag:
    print("\nBuongiorno! Vuoi accedere al sistema? Selezionare l'opzione desiderata")
    print("1. Accedi")
    print("2. Esci")
    scelta = input("Inserisci la tua scelta: ")

    if scelta == '2':
        print("\nArrivederci!")
        exit_flag = True
    elif scelta == '1':
        access_flag = False
        while not access_flag:
            print("\nSeleziona l'operazione che vuoi eseguire")
            print("1. Addizione")
            print("2. Sottrazione")
            print("3. Moltiplicazione")
            print("4. Divisione")
            print("5. Torna indietro")
            scelta_operazione = input("Inserisci la tua scelta: ")

            if scelta_operazione == '5':
                access_flag = True
            elif scelta_operazione not in ['1', '2', '3', '4']:
                print("\nErrore, l'opzione da te selezionata non esiste")
            else:
                primo_valore = float(input("Inserire il primo valore: "))
                secondo_valore = float(input("Inserire il secondo valore: "))

                if scelta_operazione == '1':
                    print(f"\nIl risultato dell'addizione {primo_valore} + {secondo_valore} è {primo_valore + secondo_valore}")
                elif scelta_operazione == '2':
                    print(f"\nIl risultato della sottrazione {primo_valore} - {secondo_valore} è {primo_valore - secondo_valore}")
                elif scelta_operazione == '3':
                    print(f"\nIl risultato della moltiplicazione {primo_valore} * {secondo_valore} è {primo_valore * secondo_valore}")
                else:
                    if secondo_valore == 0:
                        print("\nErrore, non puoi dividere per 0")
                    else:
                        print(f"\nIl risultato della divisione {primo_valore} / {secondo_valore} è {primo_valore / secondo_valore}")
    else:
        print("\nErrore, l'opzione da te selezionata non esiste")