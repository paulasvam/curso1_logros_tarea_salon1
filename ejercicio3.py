numero_elegido = float(input("Ingrese un número: "))

def esta_en_rango(numero):
    if numero >= 10 and numero <= 20:
        return True
    else:
        return False

if esta_en_rango(numero_elegido):
    print(f"El número {numero_elegido} si está en el rango de entre 10 y 20.")
else:
    print(f"El número {numero_elegido} no está en el rango de entre 10 y 20.")