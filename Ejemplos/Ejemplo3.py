def esPar(num):
    if(num%2>0):
        return False
    else:
        return True

for i in range(10):
    if(esPar(i)):
        print("Es par   : ",i)
    else:
        print("Es impar : ",i)