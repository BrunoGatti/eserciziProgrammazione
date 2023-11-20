lista1=[1,2,3,[1,2,3],4,5]

def somma_ricorsiva(lista):
	somma=0
	for el in lista:
		somma+=el
	return somma

print(somma_ricorsiva(lista1))
