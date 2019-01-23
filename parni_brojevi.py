
# for petlje - sluze uglavnom za ponavljanje
# nekog izvrsavanja
# recimo ispis brojeva od 0 do 3...
for x in range(4):
    print ("x je :" , x)

# ili ispis od 22 do 32-1 (31 dakle)
for x in range(22, 32):
    print ("x je :" , x)

# od 10 do 99, SAMO PARNI recimo !
for x in range(10, 100, 2):
    print ("x je :" , x)

# Zadatak kratak: 
# Upisi neki broj pa do tog NEKOG broja - ispisi sve parne brojeve.
# Poslije recimo neparne.

# pitaj korisnika
print("Upisi neki broj")

x = int(input())

# sjeti se da je drugi nacin:
# x = int(input("Upisi neki broj"))


# ispiši SVE pozitivne brojeve od 0 do TOG broja, SAMO PARNE
# primjeti brojeve u range i razmisli zašto su takvi
for neki_broj in range(2, x, 2):
    print ("neki_broj je :" , neki_broj)


# ispiši SVE od 0 do TOG broja, ali ovaj puta SAMO NEPARNE
for neki_broj in range(1, x, 2):
    print ("neki_broj je :" , neki_broj)


# nastavi kasnije sa jos kojim primjerom sam