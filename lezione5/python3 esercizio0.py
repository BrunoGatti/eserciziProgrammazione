#scrivi una funzione ricorsiva che trova il massimo in una lista

def massimo_ricorsivo(l):
	massimo=0
	if type(l[0])==list: l[0]=massimo_ricorsivo(l[0])
	if len(l)==1: return l[0]
	else:
		massimo_del_resto_della_lista= massimo_ricorsivo(l[1:])
		if l[0]>massimo_del_resto_della_lista:
			massimo=l[0]
		else:
			massimo=massimo_del_resto_della_lista
	return massimo

print(massimo_ricorsivo([1,4,2,6,2,43,78,[1,4,5,99],2,5,4,2]))
		
