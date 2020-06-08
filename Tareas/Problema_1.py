print(
'''
=================================================
  ENCONTRAR TODOS LOS NUMEROS PERFECTOS HASTA N 
=================================================
'''
)

while True:    
    try:
        numero=int(input("Introduzca un numero ( N ) : ")) # Hasta aqui se encuentran los N numeros perfectos
        if numero <= 0:
            print("--> ERROR : Debe ingresar un numero mayor a cero \n")
            continue
        else:
            break
    except ValueError:
        print("--> ERROR : Debe ingresar un numero \n")

print("\n")

lista = range(1,numero+1)
resultado = []

for o in lista:
    num = o
    def NumeroPerfecto(num):
        suma=0
        for i in range(1,num):
            if(num%i==0):
                suma = suma+i    
        if(num==suma):
            return True
        else:
            return False
    if NumeroPerfecto(num):
        resultado.append(num)

print("Numeros perfectos encontrados: \n")

if(len(resultado)==0):
    print("---> No se encontraron numeros perfectos")
else:
    for m in resultado:
        print("-> ",m)
print("\n")       