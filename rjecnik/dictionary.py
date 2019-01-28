# TODO
# dokumentirati malo bolje sto se radi

#dictionary maps
spanish={}
english={}

file_spanish = "spanish_words.txt"
file_english = "english_words.txt"

file_s = open(file_spanish, "a")
file_e = open(file_english, "a")


with open('dictionary.txt', "r") as file:
	contents = file.read()    				# read as chars from file stream
	file_as_list = contents.splitlines()   	# splitlines() funkcija da izbacimo newline \n char, ne treba nam
	
	for line in file_as_list:   			
		# "šetamo" se po listi svih linija...od prve do zadnje. pritome nasa line varijabla sadrži svaku pojedinu liniju
		# split funkcijom ćemo razdvojiti svaku liniju na lijevi i desni dio od TAB znaka (\t) 
		# lijevi dio stavimo u varijablu r1. 
		# desni dio stavimo u r2.
		r1, r2 = line.split('\t')

		# formiramo dictionary map kao : 
		# english["hello"] 	= "hola"   
		# spanish["hola"] 	= "hello"
		english[r1] = r2
		spanish[r2] = r1

		# ubacimo odmah i sve u file, posebno za engleski i posebno za španjolske riječi
		file_s.write("%s\t%s\n" % (r1, r2)  )
		file_e.write("%s\t%s\n" % (r2, r1)  )
		

file.close()
file_s.close()
file_e.close()