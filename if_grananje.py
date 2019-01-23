
# selection ili grananje unutar programa
# na osnovu nekog logičkog ispitivanja

print("upiši broj a")
a = int(input())

print("upiši broj b")
b = int(input())

# if grananje 
if b > a:
  print("b je veće od a")
elif b < a:
  print("b je manje od a")
elif b ==a:
  print("b je BAŠ JEDNAKO a")


ime = input("Kako ti je ime ?")
prezime = input("Kako ti je prezime ?")

# int pretvara string "18" u broj 18
godine = int(input("A koliko imaš uopće godina? "))

if godine > 18:
    print("Punoljetna si.")
elif godine < 18:
    print("Maloljetna si.")
elif godine == 18:
    print("Neznam, neka ti mama odluči pošto imaš točno 18 godina!")        

print("Dakle da ponovim; tvoje ime je: ", ime, " a prezime ti je: ", prezime, " i ti zapravo imaš: ", godine, " godina")