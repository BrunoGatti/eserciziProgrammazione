#data una stringa stampa solo le vocali una ad una

x=input("scrivi una stringa ")

for carattere in x:
	if carattere in 'aeiouAEIOU': print(carattere)

#adesso invece di stampare le vocali una ad una, vorrei che stampasse l'intera parola

parola_intera=""
for carattere in x:
	if carattere in 'aeiouAEIOU': parola_intera+= carattere

print(parola_intera)
