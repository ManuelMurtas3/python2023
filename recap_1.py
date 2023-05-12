#Scrivi un programma che richieda all'utente di inserire una stringa e che conti quante volte ogni lettera appare nella stringa. 

dizionario = dict()
stringa = input("Inserire una stringa: ")

for lettera in stringa: #eseguo un'iterazione su ogni lettera della stringa dell'utente
    if lettera not in dizionario.keys(): #se è la prima volta che incontriamo la lettera
        dizionario[lettera] = 1 #ci salviamo una nuova chiave
    else:
        dizionario[lettera] += 1 #abbiamo incontrato la lettera un'altra volta

print(dizionario)