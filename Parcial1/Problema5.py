n = 6015                # Limite para el numero perfecto
num = 1                 # Inicia en 1 para ir aumentando el valor del numero
total = 0               # Sumatoria si es perfecto

def sumaDiv(x,suma):        # Determina los divisores del numero y luego los suma
    for i in range(1,x):    
        if x%i==0:         
            suma+=i 
    return suma

while num<n:                # Mientras el numero sea menor al limite (6015) seguira 
    num2=sumaDiv(num,0)     # buscando los numeros perfectos que existan dentro del rango
    if(num2==num):
        print("-----> Es perfecto : ",num)      # Si se comple que un numero es igual a la suma
        total = total+num                       # de sus divisores es porque es perfecto y lo agrega
        num+=1                                  # al resultado de la suma
    else:
        num+=1                                  # Si el numero no es perfecto simplemente aumenta su valor en 1
                                                # y sigue buscando numeros perfectos
print("\n")        
print("------> SUMA : ",total)
print("\n")
        
    