#Fai una funzione ricorsiva che sommi una lista del tipo: 

lista = [1,3,4,2,[1,2,3],4,3,5]

def deep_somma(l):
	somma=0
	for elemento in l:
		if type(elemento)==int: somma+=elemento
		elif type(elemento)==list: somma+=deep_somma(elemento)
	return somma

print(deep_somma(lista))
