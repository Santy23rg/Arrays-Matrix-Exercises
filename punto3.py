#3. Realice un algoritmo que llene una matriz de 5 * 5. Calcular la suma de cada fila y almacenarla en un vector, la suma de cada columna y almacenarla en otro vector.
from Matriz import Matriz
import pandas as pd
import numpy as np

#Creacion y muestra de la matriz
mat = Matriz(5)
mat.fillNoRepeat()
mat.show()

#Sumamos cada fila y columnas y los guardamos en sus respectivos vectores
sumRows = mat.sumRows()
sumColumns = mat.sumColumns()


# Creamos el dataFrame para la tabla de la suma de las filas
df = pd.DataFrame(sumRows, columns=["Suma"])
rows = [f"fila {i+1}:" for i in range(mat.dim)]
df.index = rows
print(df)

#modificamos la dimension del array de las sumas de las columnas para poder mostrarlo en columnas correspondientemente
columns = [f"columna {i+1}:" for i in range(len(sumColumns))]
arr = np.array(sumColumns).reshape(-1, mat.dim)

# Creamos el dataFrame para la tabla de la suma de las filas
df = pd.DataFrame(arr, columns=columns)
df.index = ["Suma"]
print(df)
