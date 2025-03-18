numero = int(input("Ingrese un número: "))

resultados = ["El número es impar.", "El número es par."]

print(resultados[numero % 2 == 0])