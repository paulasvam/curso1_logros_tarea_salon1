numero1= int(input("ingresar primer numero:"))
numero2= int(input("ingresar segundo numero:"))
numero3= int(input("ingresar tercer numero:"))

mayor= (numero1 * (numero2 >= numero3) + numero2 * (numero1 >= numero3) + numero3 * (numero2 >= numero1))
menor= (numero1 * (numero1 <= numero2) * (numero1 <= numero3) + numero2 * (numero2 <= numero3) * (numero2 <= numero1) + numero3 * (numero3 <= numero1) * (numero3 <= numero2))

print(f"el numero mayor es:{mayor}")
print(f"el numero menor es:{menor}")