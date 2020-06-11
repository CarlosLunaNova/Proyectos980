N = 48              # Hasta donde se quiere encontrar el resultado de las sumas

def cuadrados(num):
    respuesta = 0       # Resta de las sumas
    suma1 = 0           # Suma de valores 
    suma2 = 0           # Suma de valores al cuadrado
    for i in range(0,N+1):
        suma1=suma1+i       # Suma los valores de i
        suma2=suma2+(i*i)   # Suma los valroes cuadrados de i 
    suma1=suma1*suma1       # Saca el cuadrado de la suma de valores
    print(suma1)
    print(suma2)
    respuesta=suma1-suma2   # Hace la resta de las sumas
    print(respuesta)

cuadrados(N)



