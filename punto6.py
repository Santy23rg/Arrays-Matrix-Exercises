#6.Realice un algoritmo que llene una matriz de 8 * 8, que almacene la suma de las filas y la suma de las columnas en un vector. Imprimir el vector resultante.

from Matriz import Matriz
import pandas as pd

sumRows = []

#Creacion y muestra de la matriz
mat = Matriz(8)
mat.fill()
mat.show()

sumRows = mat.sumRows()
sumColumns = mat.sumColumns()
    
vector = []

for i in sumRows:
    vector.append(i)

for i in sumColumns:
    vector.append(i)

print(vector)