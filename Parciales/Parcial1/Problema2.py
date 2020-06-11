N = 4750          # Limite para el numero primo

sumaPrimos = 0      # Suma de los primos

for o in range(2,N):                    # num tomara el valor desde 2 hasta N para determinar
    num = o                             # si es primo o no
    def primos(num):
        if num == 2:                    # Si es 2, entonces es primo y devulve que se cumple la funcion
            return True                 
        else:                           # Si el numero no tiene mas divisores aparte de 1 y el mismo numero
            for i in range(2, num):     # devulve que la funcion se cumple
                if num % i == 0:
                    return False        
            return True 
    if(primos(num)):
        print(num, "Es")
        sumaPrimos=sumaPrimos+num          # Imprime la suma
    else:
        print(num, "No es")
    
print(sumaPrimos)

        