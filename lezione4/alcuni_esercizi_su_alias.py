'''
a=[1,2,3,4,5]
b=a

a[1]=10
print("questo è l'array b: ",b)

#cosa stampa print("questo è l'array b",b)

'''




'''
a=[1,2,3,4,5]
b=a[:]

a[1]=10
print("questo è l'array b",b)
print("questo è l'array a",a)

#cosa stampa print(b)
'''




'''
a=[1,2,[1,2,3]]
b=a[:]

a[2][0]=4

print("questo è l'array a:",a)
print("questo è l'array b:",b)

#cosa stampa la print?
'''

#scrivi una funzione che sostituisce ad ogni elemento di lista la parola "ciao" SENZA MODIFICARE LA LISTA!!!
lista=[1,3,8,2]

'''
def modifica(lis=[]):#sbagliata
	for i in range(len(lis)):
		lis[i]="ciao"
	return lis

print(modifica(lista))
print(modifica(lista[:]))
##print(lista)
'''

'''
def modifica(lis):
	lis_alias=lis[:]
	for i in range(len(lis_alias)):
		lis_alias[i]="ciao"
	return lis_alias

print(modifica(lista[:]))
print(lista)
'''

'''
def modifica(lis=[]):
	for i in range(len(lis)):
		lis[i]="ciao"
	return lis

print(modifica(lista[:]))
print(lista)
'''
