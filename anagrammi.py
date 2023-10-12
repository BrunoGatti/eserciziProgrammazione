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
                



if anagramma(x,y):
    print('sono anagrammi')
else :
	print('non sono anagrammi')
