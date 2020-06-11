N = 491 # Limite de iteraciones para serie
lista = []

archivo = open('collatz.txt','w')

for o in range(2,N+1): # Se recorre hasta el limite
    num = o

    def esPar(num): # Se define si es par
        if num%2>0:
            return False
        else:
            return True

    while num!=1: # Si es par num/2 si es impar 3num+1
        if(esPar(num)):
            lista.append(int(num))
            num=int(num/2)
        else:
            lista.append(int(num))
            num = int(3*num+1)

    if(num==1):
        lista.append(int(num))        
    print(lista)
    archivo.write(str(lista)) # Agrega al archiva la lista, luego la vacia para limpiar
    archivo.write(str("\n"))  # los valores y volver a ingresar los nuevos
    archivo.write(str("\n"))
    archivo.write(str("\n"))
    lista.clear()    
archivo.close()

    
