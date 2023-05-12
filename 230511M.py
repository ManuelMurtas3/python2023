#esercizio 1: stampiamo numeri da 1 a 5
#for i in range(5):
#	print(i + 1)

#esercizio 2: stampare i numeri pari da 1 a 10
#for i in range (2, 11, 2):
#	print(i)

#esercizio 3: stampare i quadrati dei numeri da 1 a 5
#for i in range (1, 6):
#    print(i**2)

#esercizio 4: stampare ogni carattere della stringa hello
#for c in "hello world":
#    print(c)

#esercizio 5: la somma dei numeri da 1 a 10 utilizzando un ciclo for
#somma = 0
#for i in range(1,11):
#    somma += i
#print(somma)

#esercizio 6: stampare i numeri primi da 2 a 20
#for numero in range(2, 21):
#	for i in range(2, numero//2):
#		if numero % i == 0:
#			break
#	else:
#		print(numero)

#esercizio 7: dato un elenco di nomi, stampare solo i nomi più lunghi di 5 caratteri
#nomi = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank"]
#
#for nome in nomi:
#    if len(nome) > 5:
#        print(nome)

#esercizio 8: Dato un elenco di parole, contare quante volte appare ciascuna parola utilizzando un ciclo for e un dizionario.
#parole = ["casa", "albero", "cane", "casa", "cane", "gatto", "cane"]
#dizionario = {}
#
#for parola in parole:
#    if parola in dizionario.keys():
#        dizionario[parola] += 1
#    else:
#        dizionario[parola] = 1
#
#for key, value in dizionario.items():
#    print(f"{key}: {value}")

#esercizio 9: soddisfare la curiosità di nicola splittando una stringa lunga per ottenerne le parole
#testo = "data una lista con tante parole, conta quante volte compare una parola usando un ciclo e un dizionario"
#parole = testo.split(' ')
#
#dizionario = {}
##
#for parola in parole:
#    if parola in dizionario.keys():
#        dizionario[parola] += 1
#    else:
#        dizionario[parola] = 1
##
#for key, value in dizionario.items():
#    print(f"{key}: {value}")

#esercizio 10: contare il numero di vocali in una stringa
#stringa = "Hello, World!"
#numero_vocali = 0
#
#for c in stringa:
#    if c in 'aeiou':
#        numero_vocali += 1
#        
#print(numero_vocali)

#esercizio 11: stampare da 10 a 1 in ordine decrescente
#for i in range (1, 11):
#    print(11 - i)
##oppure
#for i in range (10, 0, -1):
#    print(i)
#

#esercizio 12: data una lista di numeri, trovare il massimo della lista
#numeri = [8, 3, 12, 5, 9]
#max_numero = numeri[0]
#for numero in numeri[1:]:
#    if numero > max_numero:
#        max_numero = numero
#
#print(f"Numero massimo: {max_numero}")

#esercizio 13: Stampa i numeri da 1 a 10, ma se il numero è divisibile per 3 stampa "Fizz", se è divisibile per 5 stampa "Buzz", e se è divisibile sia per 3 che per 5 stampa "FizzBuzz".
#for i in range(1, 11):
#    if i % 15 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)

#esercizio 14: stampare solo le vocali (usare il continue)
#stringa = "Hello, World!"
#vocali = "aeiouAEIOU"
#
#for c in stringa:
#    if c not in vocali:
#        continue
#    print(c)

#esercizio 15: stampa i numero da 1 a 10, ma salta l'iterazione se il numero è compreso tra 3 e 7
#for i in range(1, 11):
#    if 3 <= i <= 7:
#        continue
#    print(i)

#esercizio 16: stampare i numeri da 1 a 10 con un while
#count = 1
#while count <= 10:
#    print(count)
#    count += 1

#esercizio 17: stampare i numeri da 1 a 10 pari con il count

#count = 1
#
#while count <= 10:
#    if count % 2 == 0:
#        print(count)
#    count += 1

#esercizio 18: stampare i numeri da 1 a 10 ma interrompersi quando si arriva a 5

#counter = 1
#
#while counter <= 10:
#    if counter == 5:
#        break
#    print(counter)
#    counter += 1

#esercizio bancomat

u1_pin = "1234"
u2_pin = "5678"
u1_saldo = 50
u2_saldo = 0
utente_corrente = 0
counter_errore = 0

while counter_errore <= 4:
    pin = input("Inserire il tuo pin: ")
    if pin == u1_pin:
        utente_corrente = 1
        break
    elif pin == u2_pin:
        utente_corrente = 2
        break
    else:
        counter_errore += 1
        print("Hai inserito un pin errato, ritenta")

if counter_errore == 4:
    print("Hai sbagliato troppe volte, riprova più tardi")
else:
    print(f"Benvenuto utente {utente_corrente}")
    scelta = input("""- Seleziona l'operazione -
    premi 1 per prelevare:
    premi 2 per visualizzare il saldo
    premi 3 per ricarica cellulare
    premi 4 per fare bonifico
    scrivi exit per uscire\n> """)