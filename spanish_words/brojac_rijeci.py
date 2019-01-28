import re, string

word_list=[]    # array/list for holding all splitted words in line. later, we introspect with for-loop content 
word_dict={}  	# map structure for procesing
key_list=[]		# for later .sort method against list
count=0   		# simple counter
word=""

# procitaj cijelu datoteku i sve riječi, sve stavi u varijablu 
in_text_string = open('prica.txt', "r").read().lower()

# pošto je sada sve u toj varijabli, idemo je malo pretražiti i izvući samo slova
word_list = re.split(r'[^a-zA-z\_\-\']+',in_text_string)

# for loop petlja, sad ćemo po njoj "hodati" i za svaku riječ ćemo nešto obaviti.
# kad ju pronađemo, povećat ćemo jedan broj i staviti je u tu varijablu
for word in word_list:
	count = count + 1   # counter ide od 0 do kraja liste, odgovara na pitanje - koja je po redu zapravo?
	if word in word_dict:
		# ažuriraj riječ za jednu više ako je već ima u varijabli word_dict
		# word_dict{} je map što nam treba 
		word_dict[word] = word_dict[word] + ',' + str(count)
	else:
		# u protivnom, vidimo je prvi puta u toj varijabli pa ćemo postaviti samo brojač unutra za tu riječ...koji? count nam to govori.
		word_dict[word] = str(count)

# key_list je nova varijabla, zatrebat će nam malo kasnije. ovdje je pripremamo za upotrebu
key_list = list(word_dict)

# sve ćemo unutra sortirati
key_list.sort()

# ispisati ako baš želimo
print("Sve rijeci", word_dict)

# ili još ljepše ispisati, koristeći for petlju. Za svaku poseban text.
for key in key_list:
	print("Rijec: '" + key + "' se prikazuje od početka texta kao " + word_dict[key] + "-a po redu")




# output programa:
# Sve rijeci {'tri': '1,5', 'bika': '2,8', 'i': '3,36,49', 'lav': '4,15', 'su': '6,27,62', 'se': '7,63', 'bila': '9', 'zajedno': '10,29,64', 'nastanila': '11', 'neki': '12', 'ih': '13,21,24,39,43,47', 'je': '14,71', 'stalno': '16', 'slijedio': '17', 'u': '18,75', 'elji': '19', 'da': '20,37', 'ulovi': '22', 'ali': '23,66', 'sve': '25', 'dok': '26,61', 'bili': '28', 'nije': '30,67', 'mogao': '31,68', 'uhvatiti': '32', 'pa': '33,51', 'stoga': '34', 'zaklju': '35', 'e': '38,57', 'svladati': '40', 'po': '41', 'to': '42', 'razdvoji': '44', 'me': '45', 'usobno': '46', 'zavadi': '48', 'rastavi': '50', 'tako': '52', 'svakoga': '53','za': '54', 'sebe': '55', 'lak': '56', 'poubija': '58', 'one': '59', 'koje': '60', 'dr': '65', 'pobijediti': '69', 'sloga': '70', 'spas': '72', 'onima': '73', 'koji': '74', 'njoj': '76', 'ive': '77', '': '78'}

# detaljan output nize:
# Rijec: 'ali' se prikazuje od početka texta kao 23,66-a po redu
# Rijec: 'bika' se prikazuje od početka texta kao 2,8-a po redu
# Rijec: 'bila' se prikazuje od početka texta kao 9-a po redu
# itd.itd