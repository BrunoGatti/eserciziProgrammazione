lista1=[1,3,6,2,4]
lista2=["ciao",1,7,"t7",3.14,7,3.16,"leonardo pavoletti"]

#la funzione chiave chiarisce la precedenza tra stringhe e numeri

def f(elemento):
	if type(elemento)==str:
		return(1,elemento)
	elif type(elemento)==int:
		return(0,elemento)
	elif type(elemento)==float:
		return(2,elemento)
#[1,"ciao",3]

#(0,1)
#(1,"ciao")
#(0,3)
	

print(sorted(lista2,key=f))


##print(sorted(lista1))
##print(sorted(lista2))

##sorted(lista2,key=my_function)
##cosa fa sorted quando uso una key?

'''
#fai una funzione che, passata a sorted, mi da in output prima le stringhe, poi i numeri
def la_mia_funzione(elemento):
	if type(elemento)==str: return (1,elemento)
	else: return (0,elemento)

print(sorted(lista1))
print(sorted(lista2, key=la_mia_funzione))
'''
#posso fare la stessa cosa ma senza definire una funzione, facendo una lambda expression compatta

#le lambda sono a tutti gli effetti delle funzioni


'''
funzione:
INPUT ---------> OUTPUT

in una funzione normale

def funzione(input):
	istruzioni
	return output

nelle lambda questa roba è identica ma con una sintassi diversa

funzione = lambda input: output
'''




'''
#funzione che da in output True se l'input è un intero, e false se l'input è altro

def funzione(input):
	return True if type(input)==int else False
print(funzione(3))
print(funzione("ciao"))
'''





'''
#questa roba in lambda come la scrivo?

funzione = lambda input: True if type(input)==int else False
print(funzione(3))
print(funzione("ciao"))
'''




f=lambda elemento: (1,elemento) if type(elemento)==str else (2,elemento)
print(sorted(lista2,key=f))





