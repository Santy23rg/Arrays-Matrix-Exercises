import random
import pandas as pd

#OBJETO MATRIZ QUE SERA UTILIZADO EN TODOS LOS PUNTOS

class Matriz:
    def __init__(self, dim, dim2=None):
        if dim2 is None:
            self.dim = dim
            self.dim2 = None
            self.content = [["" for i in range(dim)]for j in range(dim)]
        else:
            self.dim = dim
            self.dim2 = dim2
            self.content = [["" for i in range(dim2)]for j in range(dim)]
    
    #llenar la matriz con numeros aleatorios (se pueden repetir)
    def fill(self):
        for i,d in enumerate(self.content):
            for j,data in enumerate(self.content[i]):
                num = random.randint(-100,100)
                self.content[i][j] = num
                
    #llenar la matriz con numeros aleatorios (no se pueden repetir)
    def fillNoRepeat(self):
        temp = []
        for i,d in enumerate(self.content):
            for j,data in enumerate(self.content[i]):
                num = random.randint(-100,100)
                while num in temp:
                    num = random.randint(0,100)
                self.content[i][j] = num
                temp.append(num)
    
    #mostrar matriz
    def show(self):
        rows = [f"{i+1}:" for i in range(self.dim)]
        columns = [f"{i+1}:" for i in range(self.dim2 if self.dim2 is not None else self.dim)]
        df = pd.DataFrame(self.content, columns=columns)
        df.index = rows
        print(df)
        
    def sumRows(self):
        sumRows = []
        for i in range(self.dim):
            sum = 0
            for j in range(self.dim2 if self.dim2 is not None else self.dim):
                sum += self.content[i][j]
            sumRows.append(sum)
        return sumRows
    
    def sumColumns(self):
        sumColumns = []
        for i in range(self.dim2 if self.dim2 is not None else self.dim):
            sum = 0
            for j in range(self.dim):
                sum += self.content[j][i]
            sumColumns.append(sum)
        return  sumColumns
        

