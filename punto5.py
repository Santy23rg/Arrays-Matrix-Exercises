#5.Realice un algoritmo que llene una matriz de 5 * 5 y que almacene toda la matriz en un vector. Imprimir el vector resultante.
from Matriz import Matriz
#Creacion y muestra de la matriz
mat = Matriz(5)
mat.fill()
mat.show()

vector = []

#Recorremos la matriz y vamos ingresando cada dato en el vector
for i in range(len(mat.content)):
    for j in range(len(mat.content[i])):
        vector.append(mat.content[i][j])

print(vector)
