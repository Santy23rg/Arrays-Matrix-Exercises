#8.Diseñe un pseudocódigo que escriba el número de la fila cuya suma sea mayor que las demás filas. Suponga que todas las filas suman diferente cantidad.

from Matriz import Matriz
import pandas as pd


mat = Matriz(8)
mat.fill()
mat.show()

sumRows = mat.sumRows()
df = pd.DataFrame(sumRows, columns=["Suma"])
df.index = [f"fila {i+1}:" for i in range(mat.dim)]
print(df)

print(f"La fila con la suma mayor es la {sumRows.index(max(sumRows))+1}")