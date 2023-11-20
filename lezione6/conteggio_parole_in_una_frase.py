def conteggio_lettere(frase=""):
	d={}
	for lettera in frase:
		print(lettera)
		d[lettera]=d.get(lettera,0)+1
	return d

frase=input("scrivi una frase: ")
print(conteggio_lettere(frase))
