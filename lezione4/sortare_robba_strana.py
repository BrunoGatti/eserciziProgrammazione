lista1=[1,3,6,2,4]
lista2=["ciao",1,7,"come va",3.14,7,3.16]

#fai una funzione che, passata a sorted, mi da in output prima le stringhe, poi i float e poi gli interi
def la_mia_funzione(elemento):
	if type(elemento)==str: return (1,elemento)
	elif type(elemento)==int: return (2,elemento)
	elif type(elemento)==float: return (3,elemento)

print(sorted(lista1))
print(sorted(lista2, key=la_mia_funzione))


