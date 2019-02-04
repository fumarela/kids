# Napiši Python program koji će provjeriti da li je uneseni broj djeljiv s 5 i
# ispisati sljedeće poruke ovisno o rezultatu: Ako je broj djeljiv tada će se
# ispisati poruka – Broj je djeljiv s 5, a ako nije – Broj nije djeljiv s 5. . Program
# je potrebno spremiti u mapu ime i prezime koja se treba nalaziti na radnoj
# površini.

# razmisli - kada je broj djeljiv sa 5? ili 8?
# odgovor: kao i kod parnosti, ukoliko neki broj podijelimo sa 8, nesmije biti ostatak kod dijeljenja, zar ne?
# ako ostatak ima --> NIJE DJELJIV
# ako ga dakle ima --> DJELJIV JE, 100% ;)

# dakle logičko ispitivanje je zapravo:
#  if neki_broj % 5 == 0:
#    print "naš broj je djeljiv sa 5"
#  else:
#   print "naš broj NIJE djeljiv sa 5"
# 
#  RAZUMIJEMO? 

# pitaj korisnika za neki broj za kojeg ćeš ispitivati tu djeljivost
print("Upisi neki pozitivan broj veci od 0...")

x = int(input())

if x < 0 or x == 0:
    print("Upisao si broj manji od 0 ili samu nulu. \nNeznam to uraditi - upisi POZITIVAN broj. Bye.")
elif (x % 5 == 0):
    print ("Tvoj broj:", x , "JE DJELJIV sa brojem 5. ;)")
else:
    print ("Tvoj broj:", x , "NIJE DJELJIV sa brojem 5. ;(")

# TO DO:
# pokušaj preurediti program tako da ispituje djeljivost sa recimo brojem 9.
# pokušaj preurediti program da stalno ispituje za unos broja. Što bismo trebali uvesti u naš program, koju ono strukturu osim logičkog ispitivanja?

