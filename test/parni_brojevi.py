
# for petlje - sluze uglavnom za ponavljanje
# nekog izvrsavanja
# recimo ispis brojeva od 0 do 3...
for x in range(4):
    print ("x je :" , x)

# ili ispis od 22 do 32-1 (31 dakle)
for x in range(22, 32):
    print ("x je :" , x)

# od 10 do 99, SAMO PARNI recimo !
for x in range(10, 20, 2):
    print ("x je :" , x)

# Zadatak kratak: 
# Upisi neki broj pa do tog NEKOG broja - ispisi sve parne brojeve.
# Poslije recimo neparne.

# pitaj korisnika
print("Upisi neki pozitivan broj veći od 0...")

x = int(input())

# sjeti se da je drugi nacin:
# x = int(input("Upisi neki broj"))


# ispiši SVE pozitivne brojeve od 0 do TOG broja, SAMO PARNE
# primjeti brojeve u range i razmisli zašto su takvi
print ("\nSvi PARNI brojevi do TVOG zamisljenog broja su :\n" )
for neki_broj in range(2, x, 2):
    print ("parni broj je :" , neki_broj)


print ("\nSvi NEPARNI brojevi do TVOG zamisljenog broja su :\n" )
# ispiši SVE od 0 do TOG broja, ali ovaj puta SAMO NEPARNE
for neki_broj in range(1, x, 2):
    print ("neparni broj je :" , neki_broj)

# drugi način ispisa parnih i neparnih brojeve uključuje
# logičko ispitivanje postoji li OSTATAK kod dijeljenja sa brojem 2.
# ukoliko postoji ostatak kod dijeljenja - broj je neparan, zar ne? ... 7 % 2 = 1 --> dakle ima ostatak
# ukoliko ne postoji ostatak kod takvog dijeljenja - broj je sigurno paran. primjer: 8 % 2 = 0  --> nema ostatka
# kako to logičko ispitivanje napisati u obliku python koda?
# 
#  if (nekibroj % 2 == 1)
#       broja nam je paran
# else
#       broj nam je neparan. 
# dakle kod bi mogao biti....

print ("\nDrugi način\n\nSvi parni i neparni brojevi do TVOG zamisljenog broja su :\n" )
for neki_broj in range(x):
    if neki_broj == 0:           # nulu ćemo preskočiti u petlji, ona nije ni parna ni neparna, zar ne?
        continue
    elif (neki_broj %2 == 1):    # razumijemo zašto?
        print ("broj je neparan: " , neki_broj)
    else:                        # ako nije ništa odozora još, onda samo može biti još neparan, zar ne?
        print ("broj je paran: " , neki_broj)



# nastavi kasnije sa jos kojim primjerom sam