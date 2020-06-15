# 201602491
class Matriz(object):

    # Constructor de la matriz: Se define la matriz como una
    # lista de listas para que cumpla con el requerimiento de 
    # de 2 dimensiones, si la lista de listas solo lleva un parametro
    # entonces se vuelve un vector
    def __init__(self, datos=[]):
        self.data = list(datos)
    
    # Sobrecarga de operador str
    def __str__(self):
       return str("Matriz : "+ str(self.data))
        
    # Sobrecarga de operador repr
    def __repr__(self):
        return self.__str__()
    
    # Sobrecarga de operador len
    def __len__(self):
        return (len(self.data))

    # Sobrecarga de operador suma: Se evalua si las matrices 
    # son del mismo tamaño antes de realizar la operacion
    # de lo contrario se levantara el error de dimensiones
    def __add__(self, nextSum):
        try:
            if self.tamIgual(nextSum):
                suma = []
                for i in range(len(self.data)):
                    suma.append([])
                    for j in range(len(self.data[0])):
                        suma[i].append(self.data[i][j] + nextSum.data[i][j])
                return Matriz(suma)       
            elif (self.tamIgual(nextSum)==False or type(nextSum)==int or type(nextSum)==str):
                raise errorDimension
            else:
                raise errorDimension
        except AttributeError:
            raise errorDimension
   
    # Sobrecarga de operador resta : Se evalua si las matrices 
    # son del mismo tamaño antes de realizar la operacion
    # de lo contrario se levantara el error de dimensiones
    def __sub__(self, nextRes):
        try:
            if self.tamIgual(nextRes):
                resta = []
                for i in range(len(self.data)):
                    resta.append([])
                    for j in range(len(self.data[0])):
                        resta[i].append(self.data[i][j] - nextRes.data[i][j])
                return Matriz(resta)
            elif (self.tamIgual(nextRes)==False or type(nextRes)==int or type(nextRes)==str):
                    raise errorDimension
            else:
                    raise errorDimension
        except AttributeError:
            raise errorDimension
    
    # Sobrecarga de operado multiplicacion: Se evalua si es un escalar (int o float)
    # si es un escalar multiplica cada termino en la matriz por el valor del escalar
    # si es otra matriz, se verifica que cumplan con la condicion de m*n X p*q donde m=q
    # y la matriz resultante es de dimensiones m*q
    def __mul__(self, nextMul):
        if (type(nextMul)==int or type(nextMul)==float):
            mulEscalar = []
            for i in range(len(self.data)):
                mulEscalar.append([])
                for j in range(len(self.data[0])):
                    mulEscalar[i].append(self.data[i][j]*nextMul)
            return Matriz(mulEscalar)

        elif len(self.data)==len(nextMul.data[0]):
            mult = []
            for i in range(len(self.data)):    
                mult.append([0]*len(nextMul.data[0]))           
                for j in range(len(nextMul.data[0])):
                    for k in range(len(self.data[0])):
                            mult[i][j]+=(self.data[i][k] * nextMul.data[k][j])
            return Matriz(mult)
        else:
            raise noCumple
               
    # Metodo que compara si son del mismo tamanio: Determina si las matrices tienen las mismas dimensiones
    # de lo contrario la funcion devuevle un valor FALSE inidicando que no se cumple
    def tamIgual(self, nextTam=[]):
        if(len(self.data)==len(nextTam.data) and len(self.data[0])==len(nextTam.data[0])):
            return True
        else:
            return False

    # Determina si la matriz es cuadrada: Determina si la matriz es de dimensiones m*m
    # si no lo es, se levanta el error de matriz no cuadrada
    def matrizCuadrada(self):
        if(len(self.data)==len(self.data[0])):
            return True
        else:
            raise noCuadra

    # Metodo para calcular el determinante de la matriz: Se evalua si la matriz es cuadrada
    # este metiande tel metodo matrizCuadrada(); si se cumple, se procede a calcular el determinante
    # de lo contrario se levanta el error de matriz no cuadrada
    def determinante(self):
        if self.matrizCuadrada()==True:
            matrizDet = self.data
            for i in range (len(matrizDet)-1):
                for j in range(1, len(matrizDet)-i):
                    if (matrizDet[i][i] != 0 ):
                        p = matrizDet[j+i][i] / matrizDet[i][i]
                        for k in range (len(matrizDet)):
                            matrizDet[j+i][k] = matrizDet[j+i][k] - (matrizDet[i][k]*p)
            det = 1
            for i in range (len(matrizDet)):
                det = matrizDet[i][i] * det
            return det
        else:
            raise noCuadra

# Error que se da al intentar hacer una operacion con matrices
# que no tienen las mismas dimensiones
class errorDimension(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return str("No se puede realizar la operacion, verifique el tamaño o tipo de datos en la matriz")

    def __repr__(self):
        return self.__str__()


# Error que se da al intentar realizar una multiplicacion de matrices
# y estas no cumplen con la condicion establecidad para su procedimiento
class noCumple(Exception):
    
    def __init__(self):
        pass

    def __str__(self):
        return str("La matrices no cumplen la condicion para multiplicarse > m*n X p*q donde m=q")

    def __repr__(self):
        return self.__str__()

# Error que se da cuando la matriz no es de m*m dimensiones
# evitando calcular el determinante de la matriz
class noCuadra(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return str("La matriz no es cuadrada y no se puede calcular el determinante")

    def __repr__(self):
        return self.__str__()

# Instancias de matrices y escalares para pruebas internas:                    
m1 = Matriz([[1,5,2],[0,3,6]])
m2 = Matriz([[0,2],[5,2],[9,3]])
m3 = Matriz([[0,5,6],[9,3,5]])
m4 = Matriz([[4,2,5],[2,5,3],[5,3,8]])
num = 2
num2 = 5.65