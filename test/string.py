import string

#string varijable
ime= "Filip"
prezime = "Horvatin"

# string concat
sve_zajedno = ime + prezime

print("Ime je: " , ime)
print("Prezime je: " , prezime)
print("Ime i prezime zajedno je: " , str(ime + " " + prezime))
print("Ime i prezime zajedno je: " , sve_zajedno)

# string funkcije upper(), lower()
print("Sve velikim slovima je:" , sve_zajedno.upper() )
print("Sve malim slovima je:" , sve_zajedno.lower())


# string as char array
print("prvo slovo imena je: " , ime[0])
print("treće slovo imena je: " , ime[2])
print("Duljina cijelog stringa je:" , len(ime))



print("Hello, World!")

a = 14
b = 3
c = 50
d = 33

# + je za zbrajanje
print("Zbroj a i b je: " , a + b)

# * je za množenje
print("a puta b je: " , a * b )

# / je za dijeljenje
print("Dijeljenje a i b je: " , a / b)

# tzv modulus, tj. ostatak kod dijeljenja
# 14 % 3 = 2 jer je 4*3=12 pa TA DVA do 14
print("Modulus (ostatak) dijeljenja broj1 i broj2 je: " , a % b, "kuži operatore")


print("Cjelobrojno dijeljenje a i b je: " , int(a / b))

