x = input('immetti un numero')
precisione = int(input('quanti zeri vuoi che abbia la precisione?'))
precisione = 10 ** (- precisione)
x= float(x)
passaggi=0
g=x

print(type(g))

while abs(g*g - x) > precisione:
	print(g)
	g = 0.5*(g+x/g)
	passaggi+=1

mess = 'la radice quadrata di x é'

print(mess,g)
print(type(mess))
print('la radice quadrata di ', x,' é ',g)
print('la precisione é di',precisione)
print('ci sono voluti ', passaggi, ' passaggi')
