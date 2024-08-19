#7.Realice un algoritmo que llene una matriz de 5 * 6 y que imprima cuantos de los números almacenados son ceros, cuántos son positivos y cuantos son negativos.
from Matriz import Matriz
import pandas as pd
import numpy as np

mat = Matriz(5,6)
mat.fill()
mat.show()

zeros=0
negatives=0

for i in range(mat.dim):
    for j in range(mat.dim2):
        if mat.content[i][j] == 0:
            zeros += 1
        if mat.content[i][j] < 0:
            negatives += 1

print(f"La matriz tiene {zeros} ceros y {negatives} números negativos")
