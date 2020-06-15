# MULTIPLOS DE 3 & 5 HASTA 1000

lista = list(range(0,1000))

sumaT=0

for i in lista:
    if (i%3==0 or i%5==0):
        sumaT += i
print(sumaT)

