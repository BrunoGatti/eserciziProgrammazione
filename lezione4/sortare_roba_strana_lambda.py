lista = [1,2,3.4,5.7,"ciao","come","stai",3,8,"Almqvist"]
















'''
def function(el):
	if type(el)==str:
		return (0,el)
	else:
		return (1,el)

print(sorted(lista,key=function))
'''




'''
f= lambda el: (0,el) if type(el)==str else (1,el)

print(sorted(lista,key=f))
'''
