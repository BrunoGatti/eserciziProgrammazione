#definisci una funzione che dato un numero, ne calcola la congettura di collatz, e ritorna il numero di passi che ha impiegato.

def collatz_conta(n):
	conta=0
	while n!= 1:
		if n%2 == 0:
			n=n //2
		else:
			n = 3*n +1
		conta+=1
	return conta

print(collatz_conta(10))
