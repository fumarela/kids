import re, string

word_list=[]    # array/list for holding all splitted words in line. later, we introspect with for-loop content 
word_dict={}  	# map structure for procesing
key_list=[]		# for later .sort method against list
count=0   		# simple counter
word=""
rijec={}
#
kombinacija={} 

in_text_string = open('carevo_novo_ruho.txt', "r").read()

word_list = re.split(r'[^a-zA-z\_\-\'\t]+',in_text_string)

for word in word_list:
	count = count + 1   # counter od 0 do kraja liste, koja je po redu zapravo?
	if word  in rijec:
		rijec[word] = rijec[word] + 1
		#print("Rijec je: ", word , "*", rijec[word])
	else:
		# u protivnom, postavi brojač unutra za tu riječ
		rijec[word] = 1
		#print("Rijec je: ", word , "*", rijec[word])
		

# key_list je OPET - LISTA
#key_list = list(word_dict)
rijeci_sve = list(rijec)


print("Svaka riječ i koliko se puta ponavlja u textu: " , str(rijec) )

# možemo ih i sortirati ako želimo funkcijom sort() ako funkciji damo listu... što imamo
rijeci_sve.sort()
print("Sve rijeci sortirane: " , str(rijeci_sve) )

# koliko se puta spominje riječ "car" u textu?
print("Riječ car se ponavlja: ", rijec["car"], " puta")
print("Riječ tkanina se ponavlja: ", rijec["tkanina"], " puta")

# koliko ih ima?
print("Ukupno ima rijeci u cijeloj prici :" , len(word_list), " rijeci")   
# koliko ih ima? drugi način...
print("Ukupno ima rijeci u cijeloj prici :" , count	, " rijeci")   
