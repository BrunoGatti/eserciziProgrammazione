#non sarebbe piu comodo avere un modo per rifare piú volte questa operazione senza dover riscrivere d'accapo tutto il codice?

def vocali(stringa):
	vocals=""
	for carattere in stringa:
		if carattere in 'aeiouAEIOU': vocals+=carattere
	return vocals

x=input("scrivi una stringa ")
print(vocali(x))
