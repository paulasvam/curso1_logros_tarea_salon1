cantidad_estudiantes= int(input("ingresar cantidad de estudiantes:"))

lista_notas=[]

for i in range (cantidad_estudiantes):
        notas_estudiantes= float(input(f"ingresar nota del estudiante {i+1}: "))
        
        lista_notas.append(notas_estudiantes)
        
suma= sum(lista_notas)
promedio= sum(lista_notas)/cantidad_estudiantes
maxima= max(lista_notas)
minimo= min(lista_notas)

print(f"la suma de todas las notas es de: {suma} puntos")
print(f"el promedio de todas las notas es de: {promedio} puntos")
print(f"la mayor nota de todas es de: {maxima} puntos")
print(f"la menor nota de todas es de: {minimo} puntos")
print(f"la lista de notas es la siguiente: {lista_notas}")