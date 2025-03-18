numero1= float(input("introducir primer numero:"))
numero2= float(input("introducir segundo numero:"))

suma= (numero1+numero2)
resta= (numero1-numero2)
multiplicacion= (numero1*numero2)
if numero2 !=0:
    division= numero1/numero2
else:
    division = "error"

print(f"suma: {numero1}+{numero2} ={suma}")
print(f"resta: {numero1}-{numero2} ={resta}")
print(f"multiplicacion: {numero1}*{numero2} ={multiplicacion}")
print(f"division: {numero1}/{numero2} ={division}")