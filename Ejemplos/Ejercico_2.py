'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = 11
item = fib(n)
print(f"El item {n} de la serie de Fibonacci es {item}")
'''
a=0
b=1
c=0
sumaT=0

while c<4000000:
    c=a+b
    a=b
    b=c
    if c%2==0:
        sumaT = sumaT+c
    
print(sumaT)
