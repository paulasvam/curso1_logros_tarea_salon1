precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

precio_final = precio * (1 - descuento / 100)

resultado_menor_100 = (precio_final < 100) * 1

resultados = ["El precio final es mayor a 100.", "El precio final es menor a 100."]

print(f"El precio final es: {precio_final:.2f}")
print(resultados[resultado_menor_100])