#definire una funzione che ritorna 2 valori data una parola: le sue vocali e le sue consonanti

def vocali_e_consonanti(stringa):
	vocali=""
	consonanti=""
	for carattere in stringa:
		if carattere in 'aeiou':vocali+=carattere
		elif carattere in 'bcdfghjklmnpqrstvwxyz':consonanti+=carattere
	return vocali,consonanti

x=input("inserisci una stringa")
print(vocali_e_consonanti(x))
