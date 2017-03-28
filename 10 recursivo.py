n=int(input("Ingresa un numero: "))

def suma(num):
	s=0
	for x in range(num):
	        r = pow(x+1,2)
	        print(r)
	        suma()+=r

suma(n)
