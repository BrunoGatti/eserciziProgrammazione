#looking for waldo

#in una lista c'è un intruso: waldo, scrivi un programma che trovi waldo anche quando la lista è un macello

def trova_waldo(lista):
	trovato=False
	for elemento in lista:
		if elemento=="waldo": return True
		elif type(elemento)==list:
			if(trova_waldo(elemento)==True): return True
	return trovato

print(trova_waldo([1,2,3,[1,2,3,4],[1,5,4,2,[1,2,"waldo"],4,3,2]]))
