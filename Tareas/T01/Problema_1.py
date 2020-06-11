print(
'''
================================================
   ENCONTRAR LOS PRIMEROS N NUMEROS PERFECTOS 
================================================
'''
)

while True:    
    try:
        n=int(input("Introduzca un numero ( N ) : ")) # Hasta aqui se encuentran los N numeros perfectos
        if n <= 0:
            print("--> ERROR : Debe ingresar un numero mayor a cero \n")
            continue
        else:
            break
    except ValueError:
        print("--> ERROR : Debe ingresar un numero \n")

print("\n")

contador=0
num = 1

def sumaDiv(x,suma):
    for i in range(1,x):
        if x%i==0:
            suma+=i 
    return suma

while contador<n:
    num2=sumaDiv(num,0)
    if(num2==num):
        print("-----> Es perfecto : ",num)
        num+=1
        contador+=1        
    else:
        num+=1
print("\n")
        
    
