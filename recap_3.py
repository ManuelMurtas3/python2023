#Scrivere un programma che prenda una lista di numeri come input e rimuove i duplicati dalla lista,
#lasciando solo i valori "unici". L'ordine degli elementi nella lista deve rimanere invariato

lista = [1, 2, 2, 5, 1, 6, 6, 8, 4, 2, 1]
lista_risultato = []
numeri = set()

#aggiungo tutti i numeri ad un set (struttura dati che non ammette duplicati)
for numero in lista:
    numeri.add(numero)

#mantenendo l'ordine della lista di input vado ad inserire i numeri nella lista risultato solo la prima volta che appaiono
for numero in lista:
    if numero in numeri:
        lista_risultato.append(numero)
        numeri.remove(numero)

print(lista_risultato)