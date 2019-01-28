import string, sys

# prvi nacin
with open('lista_rijeci.txt', "r") as file:
	file_as_list = file.readlines()  
	#  readlines() cita doslovno liniju, zajedno sa newline charom.   
	# file_as_list ['lijevo:desno\n', 'Hola:Hello\n']

	print("file_as_list", file_as_list)
	for line in file_as_list:    
		# line = baca newline van
		# sadrzaj line variable je:  lijevo:desno 
		print(line)

file.close()

# drugi nacin
with open('lista_rijeci.txt', "r") as file:
	contents = file.read()    				# read as chars from file stream
	file_as_list = contents.splitlines()   	# nema vise newline-a kao u prvom primjeru. splitlines() funkcija to radi
	
	for line in file_as_list:   			# "šetamo" se po listi svih linija... line varijabla sadrži samu liniju 
											#Linija je:  lijevo:desno  
		r1, r2 = line.split(':')			# split linije na znaku ":" - uzmemo lijevi dio i stavimo u varijablu r1. desni dio stavimo u r2. 
		print(r1, "*", r2)					# pa recimo to ispišemo, kao u prvom gore primjeru.

file.close()

# umjesto readlines() koji čuva newline - upotrebljavati splitlines() koji splita linije na \n, \r, \t itd. 