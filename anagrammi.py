#CONSEGNA: scrivere un programma che prende in input due stringhe e decide se sono anagrammi

x= input('inserire una stringa ').strip()

y= input('inserire altra stringa ').strip()

def anagramma(x,y):
    if len(x)!=len(y):
        return False
    else:
        viste=[False] * len(x)
        for c in x:
            print(c)
            i=0
            trovato=False
            while i<len(y) and not trovato:
                print(y[i],end=" ")
                if (c == y[i]) and (viste[i]==False):
                    viste[i]=True
                    trovato = True
                i+=1
            print()
            if not trovato:
                return False
        return True
                
def anagramma2(x,y):
	occorrenze_in_x=0
	occorrenze_in_y=0
	for c1 in x:
		if occorrenze(c1,y)!=occorrenze(c1,x): return False
	return True
		
def occorrenze(char,stringa):
	occ=0
	for c in stringa:
		if char==c: occ+=1
	return occ			 

if anagramma2(x,y):
    print('sono anagrammi')
else :
	print('non sono anagrammi')
