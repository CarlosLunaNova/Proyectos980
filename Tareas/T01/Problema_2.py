print(
'''
==============================================
   ENCONTRAR LOS PRIMEROS N NUMEROS AMIGOS 
==============================================
'''
)

while True:
    try:
        n = int(input("Introduzca un numero ( N ) : "))
        if n <= 0:
            print("--> ERROR : Debe ingresar un numero mayor a cero \n")
            continue
        else:
            break
    except ValueError:
        print("--> ERROR : Debe ingresar un numero \n")

print("\n")

contador = 0

num1 = 1

def sumaDiv(x,suma):
    for i in range(1,x):
        if x%i==0:
            suma+=i
    return suma

while contador<n:
    num2=sumaDiv(num1,0)
    if(sumaDiv(num2,0)==num1 and num1!=num2 and num1<num2):
        print("-----> Son amigos",num1," & ",num2)
        num1+=1
        contador+=1
    else:
        num1+=1
print("\n")   