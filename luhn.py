import random

for n in range(100):
	random_number = str(random.randrange(0000000000000000,9999999999999999))
	# Se define una variable llamada t que se inicializa en 0
	t = 0
	# Se realiza un bucle for que recorre los dígitos del número en orden inverso
	for x,y in enumerate((reversed(random_number))):
		# Cada dígito se convierte en un entero
		y = int(y)
		""" Si el índice del dígito en el número es impar (es decir, su posición en el número es impar), se multiplica por dos. 
		Si el resultado es mayor o igual a 10, se separan los dígitos y se suman. En caso contrario, se suma directamente """
		if x%2==1:
			y=y*2
			if y>=10:
				t+=y//10+y%10
			else:
				t+=y
		else:
			#Si el índice es par, simplemente se suma el dígito.
			t+=y
	# El resultado de todas las sumas se guarda en la variable t
	res = t%10==0
	# Si el resultado es verdadero se imprime el número validado por el algoritmo, de lo contrario, pasa al siguiente número
	if res == True:
		print(res,random_number)
	else:
		pass
