#Scrivere un programma che prenda una lista di numeri come input e rimuove i duplicati dalla lista,
#lasciando solo i valori "unici". L'ordine degli elementi nella lista deve rimanere invariato

lista = [1, 2, 2, 5, 1, 6, 6, 8, 4, 2, 1]
lista_risultato = []
numeri = set()

for numero in lista:
    numeri.add(numero)

for numero in lista:
    if numero in numeri:
        lista_risultato.append(numero)
        numeri.remove(numero)

print(lista_risultato)