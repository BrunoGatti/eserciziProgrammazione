#prendi una frase in input, conta le occorrenze restituendo il dizionario in ordine delle lettere che appaiono più volte

frase=input("scrivi una frase")

def dizionario(frase):
	d={}
	for lettera in frase:
		d[lettera]= d.get(lettera,0)+1
	return d
	
diz=dizionario(frase)
lista_d=[]
print(diz)
for k in diz:
	lista_d.append((k,diz[k]))
print(lista_d)
print(sorted(lista_d,key=lambda t:t[1]))
