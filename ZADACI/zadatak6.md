###  Često puta ne želimo nešto ispisivati svaki puta ponovo, kao npr.

```` python
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
````

#### Umjesto toga, poslužit ćemo se for-loop petljom, novom strukturom. Pogledaj kako možemo sve to skratiti:


```` python
for a in range(0,7):
    print("hello")
````

####  Upravo si naučila for-loop petlju. Hajmo za primjer ispisati sve brojeve od 1 do 10, koristiti ćemo opet for-loop petlju:

```` python
for a in range(1,11):
    print(a)
````

#### Primjeti da smo u range() dijelu morali povećati zadnji broj za 1 da bismo ispisali i broj 10.

#### Možemo range "zamoliti" i da preskače po 3 broja, taj broj se zove step : 

```` python
for a in range(1,11,3):
    print(a)
````

## Pokušaj sam/sama izraditi program koji će:
* ispisati sve PARNE brojeve od 10 do recimo 22 (sjeti se koristiti step u range)
* ispisati SVE brojeve od 100 do 80 ali unazad (sjeti se da step može biti i -1) 

### Što misliš, što će se dogoditi u slijedećem programu:

```` python
for a in range(1, 10):
    print(a)
    if a == 5:
        break
````

### Probaj razmisliti što radi ovaj program.

```` python
zbroj = 0

for a in range(1, 5):
    zbroj = zbroj + a

print(zbroj)

````

## Pokušaj sam/sama izraditi program koji će:
* zbrojiti sve brojeve od 10 do 20
* ispisati tvoje ime u for-petlji 20 puta