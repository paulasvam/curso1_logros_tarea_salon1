edad= int(input("ingresar edad de la persona:"))

resultado_mayor= edad >18 and edad <65
print(f"la persona se encuentra en el rango de 18 o 65 años: {resultado_mayor}")

resultado_menor= not edad <18
print(f"la persona no es menor de edad: {resultado_menor}")