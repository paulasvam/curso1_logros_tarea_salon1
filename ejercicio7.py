año = int(input("Ingrese un año: "))

bisiesto = (año % 4 == 0)
no_bisiesto = (año % 4 != 0)

resultados = ["El año es bisiesto.", "El año no es bisiesto."]

print(resultados[no_bisiesto])