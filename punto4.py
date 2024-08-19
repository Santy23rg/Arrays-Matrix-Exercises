#4. Realice un algoritmo que llene una matriz de 10 * 10. Sumar las columnas e imprimir que columna tuvo la máxima suma y la suma de esa columna.
from Matriz import Matriz
import pandas as pd
import numpy as np

sumColumns = []

#Creacion y muestra de la matriz
mat = Matriz(3)
mat.fill()
mat.show()

sumColumns = mat.sumColumns()

columns = [f"columna {i+1}:" for i in range(len(sumColumns))]
arr = np.array(sumColumns).reshape(-1, mat.dim)

# Creamos el dataFrame para la tabla de la suma de las filas
df = pd.DataFrame(arr, columns=columns)
df.index = ["Suma"]
print(df)

sumMax = max(sumColumns)
print(f"La columna con la suma mayor es la {sumColumns.index(sumMax)+1} con un total de: {sumMax}")