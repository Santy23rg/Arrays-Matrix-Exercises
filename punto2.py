#2. Realice un algoritmo que llene una matriz de 5 * 5 y determine la posición [fila ,columna] del número mayor almacenado en la matriz. Los números son diferentes.
from Matriz import Matriz

#Creacion y muestra de la matriz
mat = Matriz(5)
mat.fillNoRepeat()
mat.show()

#variables para validacion de numero mayor y array de guardado de posicion
maxNum = 0
position = ["",""]

for i,d in enumerate(mat.content):
    for j,data in enumerate(mat.content[i]):
        if mat.content[i][j] > maxNum:
            maxNum = mat.content[i][j]
            position[0] = i+1
            position[1] = j+1
    
print(f"El numero mayor de la matriz esta en la fila [{position[0]}] columna [{position[1]}]")