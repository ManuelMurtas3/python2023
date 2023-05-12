#Realizzare un codice che prende una "frase" in input e ne restiuisce un dizionario che conti quante volte ogni parola appare nella "frase" 

dizionario = dict()
stringa = input("Inserire una stringa: ")

for parola in stringa.split(' '): #eseguo un'iterazione su ogni lettera della stringa dell'utente
    if parola not in dizionario.keys(): #se è la prima volta che incontriamo la lettera
        dizionario[parola] = 1 #ci salviamo una nuova chiave
    else:
        dizionario[parola] += 1 #abbiamo incontrato la lettera un'altra volta
print(dizionario)