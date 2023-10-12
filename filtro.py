x= input('inserire prima stringa ')
y= input('inserire seconda stringa ')

#metodo da uomo delle caverne
def filtro2(stringa, stringa_filtro):
	caratteri_comuni=""
	i=0
	while i<len(stringa):
		j=0
		while j<len(stringa_filtro):
			if stringa[i]==stringa_filtro[j]: caratteri_comuni+=stringa[i] 
			j+=1
		i+=1
	return caratteri_comuni	

#metodo moderno
def filtro(stringa, stringa_filtro):
	caratteri_comuni=""
	for c in stringa:
		if c in stringa_filtro:
			caratteri_comuni+=c
	return caratteri_comuni

print(filtro(x,y))
print(filtro2(x,y))
