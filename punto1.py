#1. Realice un algoritmo que almacene números en una matriz de 6 * 6. Imprimir la suma de los números almacenados en la matriz.
from Matriz import Matriz

#Creacion y muestra de la matriz
mat = Matriz(6)
mat.fill()
num = 0

#recorriendo la matriz y sumando cada dato
for i,d in enumerate(mat.content):
    for j,data in enumerate(mat.content[i]):
        num += int(mat.content[i][j])

mat.show()
print(f"El resultado de la suma de todos lo numeros de la matriz es: {num}")        