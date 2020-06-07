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
n=10
while n>0:
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)
