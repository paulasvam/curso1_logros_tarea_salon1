numero1= int(input("ingresar primer numero:"))
numero2= int(input("ingresar segundo numero:"))

positivo= numero1 >0 and numero2 >0
print(f"ambos numeros son positivos: {positivo}")

al_menos= numero1 >0 or numero2 >0
print(f"al menos uno es positivo: {al_menos}")

menor= not numero1 <0
print(f"el primer numero no es negativo: {menor}")