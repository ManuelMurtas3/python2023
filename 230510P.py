# MATRICE
# La matrice è essenzialmente una lista di liste
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
elemento = matrix[0][1]
print('matrix[0][1]:', elemento) # il primo id indica la riga, il secondo id indica la colonna

for riga in matrix:
    print('riga n.', matrix.index(riga),':', riga)
    for elemento in riga:
        print('la riga contiene in ',riga.index(elemento),':',elemento)

# operatori di assegnazione
stringa = 'ciao sono una stringa'
numero = 3

# shortcut '+=' , '-=', '*=', '/='
stringa += ', vuoi conoscermi?'    # stringa = stringa + ', vuoi conoscermi?'
print(stringa)

numero += 7
print(numero)

# moltiplica stringa
print(stringa * numero)

# CONTROLLO DEL FLUSSO
# flusso condizionale IF

numero = 19
if numero > 0 and numero < 18:
  print('minorenne')
elif numero == 18:
  print('Auguri, devi iniziare a firmare le cambiali :D')
elif numero > 18:
  print('maggiorenne')
else:
  print('eta impossibile')

x = 10
y = 5

if x > y:
  print('x è maggiore di y')
elif x == y:
  print('x è uguale a y')
else:
  print('x è minore di y')

z = 4

if z <= x and z >= y:
  print('z è compreso tra x e y')
elif max(x,y,z) == z:
  print('z è il più grande')
else:
  print('z è il più piccolo')

# scrivere un prog py che prenda in input un numero intero positivo
# il prog deve restituire i seguenti out:
# se pari --> stampa pari
# se dispari e compreso tra 1 e 10 --> stampa dispari e compreso tra 1 e 10
# se dispari e compreso tra 11 e 20 --> stampa dispari e compreso tra 11 e 20
# se dispari e maggiore di 20 --> stampa dispari e maggiore di 20

# leggi sotto e impara :D
x = int(float(input('Inserisci un numero intero positivo :')))

if x < 0 :
  # messaggio di errore
  print('Messaggio di errore: il numero inserito è negativo.')
elif x % 2 == 0:
  print('pari')
elif 1 <= x <= 10 :
  print('dispari e compreso tra 1 e 10')
elif 11 <= x <= 20 :
  print('dispari e compreso tra 11 e 20')
else:
  print('dispari e maggiore di 20')

# programma py che prende in input int positivi e restituisce il più grande dei tre
# se sono tutti uguali, stampa tutti uguali
# se ci sono 2 numeri uguali, stampa idem
# se sono tutti diversi, idem

a = int(input('inserisci il primo numero intero positivo: '))
b = int(input('inserisci il secondo numero intero positivo: '))
c = int(input('inserisci il terzo numero intero positivo: '))

if a <= 0 or b <= 0 or c <= 0:
  print('Leggi bene la traccia... Solo numeri positivi interi')
else:
  if a == b and b == c and c == a:
    print('tutti i numeri sono uguali... riprova inserendo 3 numeri diversi')
  elif (a == b) or (b == c) or (c == a):
    print('due numeri su tre sono uguali... riprova inserendo 3 numeri diversi')
  else:
    print('tutti e tre i numeri sono diversi!')
    massimo = max(a, b, c)
    print(f'il maggiore dei numeri è: {massimo}')

## VERSIONE MALATA :) --USANDO LA TUPLA

# inserimento delle variabili
a = int(input('inserisci il primo numero intero positivo: '))
b = int(input('inserisci il secondo numero intero positivo: '))
c = int(input('inserisci il terzo numero intero positivo: '))

# creazione della tupla
tpl = (a,b,c)

# controllo del numero di occorrenze=3 : 
if tpl.count(a) == 3:
  print('tutti e tre i numeri sono uguali!')

# controllo del numero di occorrenze=2 : 
elif tpl.count(a) == 2 or tpl.count(b) == 2:
  print('due numeri su tre sono uguali... riprova inserendo 3 numeri diversi')

# controllo del numero di occorrenze=1 :
else:
  print('tutti e tre i numeri sono diversi!')

  # inizializza un counter a 0
  counter = 0

  # per ogni elemento in tupla, se maggiore di 0, aumenta il counter
  for x in tpl:
    if x >=0:
      counter += 1
  # se il counter = 3, esegui il resto
  if counter == 3: 
    massimo = max(a, b, c)
    print(f'il maggiore dei numeri è: {massimo}')
  # se il counter != 3: errore
  else:
    print('Leggi bene la traccia... Solo numeri positivi interi')

# ESERCIZIO PER CARLO
# scrivi un prog py che prende in input un numero intero positivo
# determini se il numero è multiplo di 3, di 5 o di entrambi
# se mult 5 >> stampa multiplo di 5
# se mult 3 >> stampa multiplo di 3
# se mult 5 e di 3 >> stampa multiplo di 5 e di 3

# inizializziamo le variabili
x = int(input('inserisci un intero positivo: '))

# controlliamo se è un n intero positivo
if x < 0:
  print("Error: l'input non è positivo")
# seconda parte
else:
  if x % 5 == 0 and x % 3 == 0:
    print('il numero inserito è multiplo di 5 e di 3.')
  elif x % 5 == 0:
    print('il numero inserito è multiplo di 5.')
  elif x % 3 == 0:
    print('il numero inserito è multiplo di 3.')
  else:
    print('il numero inserito non è multiplo nè di 5, nè di 3.')

# questo prog py prende in input nome ed età di una persona
# se la persona si chiama Alice e la sua età è compresa tra 18 e 25 inclusi
# >> Alice, sei una giovane adulta.
# se la persona si chiama Bob e la sua età è inferiore ai 18 anni
# >> Bob, sei un giovane adolescente.
# se la persona è Charlie e ha più di 25 anni
# >> Charlie, sei un adulto maturo
# per tutte le altre persone:
# >> {nome}, non posso fornire una descrizione per te.

# memorizziamo le variabili
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))

# ciclo condizionale:
if nome == 'Alice' and eta >= 18 and eta <=25:
  print(f'{nome}, sei una giovane adulta.')
elif nome == 'Bob' and eta < 18:
  print(f'{nome}, sei un giovane adolescente.')
elif nome == 'Charlie' and eta > 25:
  print(f'{nome}, sei un adulto maturo.')
else:
  print(f'{nome}, non posso fornire una descrizione per te.')

# questo prog py prende in input nome ed età di una persona
# se la sua età è compresa tra 18 e 25 inclusi
# >> Alice, sei una giovane adulta.
# se la sua età è inferiore ai 18 anni
# >> Bob, sei un giovane adolescente.
# se ha più di 25 anni
# >> Charlie, sei un adulto maturo

# memorizziamo le variabili
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))

# ciclo condizionale:
if eta <= 0:
  print('inserisci un età che parta da 1')
else:
  if eta >= 18 and eta <=25:
    print(f'{nome}, sei una giovane persona adulta.')
  elif eta < 18:
    print(f'{nome}, sei una giovane persona adolescente.')
  else:
    print(f'{nome}, sei una persona adulta matura.')

# ESERCIZIO COMBO CATTIVA!
# Questo prog py deve determinare se un anno è o non è bisestile
# un anno bisestile è div per 4, ma non per 100 a meno che non sia div per 400

anno = int(input('Inserisci anno :'))

'''if anno % 4 == 0:
  if anno % 400 == 0:
    print("L'anno inserito è bisestile.")'''

# variabili booleane?
divisibile_4 = anno % 4 == 0
divisibile_400 = anno % 400 == 0
divisibile_not_100 = anno % 100 != 0

if (divisibile_4 and divisibile_not_100) or divisibile_400:
  print("L'anno", anno, "è bisestile.")
else:
  print("L'anno", anno, "non è bisestile.")

for a in range(1,11):
  for b in range(1,11):
    print(a*b)

