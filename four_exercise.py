num1=0
num2=0
num1=float(input("Digite el numero 1: "))
num2=float(input("Digite el numero 2: "))
if num1 == num2:
    print("Numero %d y Numero %d son iguales" % (num1, num2))
elif num1 < num2:
    print("Numero 2: %d es mas grande que Numero 1: %d"  % (num1, num2))
else:
    print ("Numero 1: %d es mas grande que Numero 2: %d"  % (num1, num2))