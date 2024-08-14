print("calculadora piton \n    hecha por fatpenguin35 \n \n no admite decimales \n \n ")

try:
	print("seleccione la operacion qje desee \n 1: Suma \n 2: Resta \n 3: Multiplicacion \n 4: Divison \n \n")
	sel = int(input())
	if sel == 1:
		print("Escriba el primer digito de su suma \n ? + ? \n" )
		suma = int(input())
		print("Escriba el segundo digito de su suma \n", suma, "+ ? \n")
		sumb = int(input())
		sumt = suma + sumb
		print("El resultado de", suma, "+", sumb, "es igual a: ", sumt)
	if sel == 2:
		print("Escriba el primer digito de su resta \n ? - ?")
		resa = int(input())
		print("Escriba el segundo digito de su resta \n", resa, "- ?")
		resb = int(input())
		rest = resa - resb
		print("El resultado de", resa, "+", resb, "es igual a: ", rest)
	if sel == 3:
		print("Escriba el primer digito de su multiplicacion \n ? x ? \n" )
		mula = int(input())
		print("Escriba el segundo digito de su multiplicacion \n", mula, "x ? \n")
		mulb = int(input())
		mult = mula * mulb
		print("El resultado de", mula, "x", mulb, "es igual a: ", mult)
	if sel == 4:
		print("Escriba el primer digito de su division \n ? ÷ ? \n" )
		diva = int(input())
		print("Escriba el segundo digito de su division \n", diva, "÷ ? \n")
		divb = int(input())
		divt = diva / divb
		print("El resultado de", diva, "÷", divb, "es igual a: ", divt)
except(ValueError, ZeroDivisionError):
		print("Mogolico retrasado de mierda no vuelvas a usar este programa nunca mas en tu puta miserable vida")
		
