numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultados = ["Los números son iguales.", "Los números son diferentes."]

indice = (numero1 - numero2) != 0

print(resultados[indice])