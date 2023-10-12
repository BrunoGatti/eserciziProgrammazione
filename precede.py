x=input('digita la prima parola')
y=input('digita la second parola')

i=0

#salvo la lunghezza della stringa piu piccola ES: x=ciao y=ciaone salvo 4 (lunghezza di ciao)
if len(x) < len(y):
	n=len(x)
else:
	n = len(y)

#guardo le lettere delle due parole a partire dalla prima posizione, se le lettere sono uguali passo alla posizione successiva
while i < n and x[i] == y[i]:
	i+=1

#se abbiamo finito la parola piu piccola decido quale parola viene prima in base alla lunghezza, nel nostro caso x=ciao y=ciaone risultano uguali le prime quattro lettere, allora la parola piu corta precede quella piu lunga ---> ciao precede ciaone
if i == n:
	if len(x) == len(y):
		print('le stringhe sono uguali')
	elif len(x) < len(y):
		print(x, 'precede',y)
	else:
		print(y, 'precede',x)
#se troviamo una lettera differente prima della fine della parola allora in base a quella si decide quale parola viene prima
else:
	if x[i] < y[i]:
		print(x,'precede',y)
	else:
		print(y, 'precede', x)
