def bubble_sort(lista):
	n = len(lista)
	ordinata=False
	c=0

	while not ordinata and c < n-1:
		ordinata=True
		for i in range(n-1-c):
			if lista[i]>lista[i+1]:
				ordinata =False
				lista[i],lista[i+1] = lista[i+1],lista[i]
		c+=1
	return lista

def anagrammi_con_liste(parola1,parola2):
	#metto le due parole nelle liste
	lista1=list(parola1)
	lista2=list(parola2)
	#ordino le liste in ordine alfabetico
	lista1_ordinata=bubble_sort(lista1)
	lista2_ordinata=bubble_sort(lista2)
	#se sono uguali sono anagrammi
	if lista1_ordinata==lista2_ordinata: return True
	return False

print(anagrammi_con_liste("ciaoccc","oaaccic"))
