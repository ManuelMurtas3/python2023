def switch():
    option = "ok"
    while option != 0:
        print("Benvenuto! Selezione l'opzione desiderata:")
        print("1. Prima opzione")
        print("2. Seconda opzione")
        print("3. Terza opzione")
        print("4. Quarta opzione")
        print("5. Quinta opzione")
        print("0. Esci")
        option = input("Inserisci la tua scelta: ")

        if option == "1":
            return "Hai scelto la prima opzione"
        elif option == "2":
            return "Hai scelto la seconda opzione"
        elif option == "3":
            return "Hai scelto la terza opzione"
        elif option == "4":
            return "Hai scelto la quarta opzione"
        elif option == "5":
            return "Hai scelto la quinta opzione"
        elif option == "0":
            break
        else:
            continue

opzione = "ok"