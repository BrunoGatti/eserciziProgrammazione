#trova il massimo di una lista, con liste annidate (usando la ricorsione)

def massimo_ricorsivo(lista):
	massimo=0
	for elemento in lista:
		if type(elemento)==int:
			if elemento>massimo: massimo=elemento
		elif type(elemento)==list:			
			massimo_della_sottolista = massimo_ricorsivo(elemento)
			if massimo_della_sottolista > massimo: massimo=massimo_della_sottolista
	return massimo

l=[1,2,3,[1,2,10],[1,6,2,[1,6,99]],[101],[32,41,22]]

print(massimo_ricorsivo(l))
