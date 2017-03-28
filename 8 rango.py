n=int(input("Ingresa un numero: "))

def rango(ran):
	for x in range(ran):
	        r= x+1
	        if (r>=20 and r<=60):
	            print(r)

rango(n)
