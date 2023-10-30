def bob(n):
	l=n%2
	if l==0:
		n=n/2
	if l==1:
		n=3*n+1
	return n

n=int(input('inserire un numero naturale'))

i=0
while n!=1:
	n=int(bob(n))
	print(n)
	i+=1
	print('Coverage ad 1 dopo %.d iterazioni' %(i))
