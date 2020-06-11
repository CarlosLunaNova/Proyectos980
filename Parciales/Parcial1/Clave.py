'''
Clave Primer Parcial - Serie 3
Proyectos de Computación AIE (0980)
Junio 2020 - Iván Morales
===========================================
Instrucciones de uso: en Python 3 importe
este script como módulo en y ejecute
cada una de las funciones correspondientes
a los ejercicios del examen:
Ex1, Ex2, Ex3, Ex4, Ex5, con sus parámetros,
según lo solicitado durante el examen.
=========================================== 
'''
def sumSquares(n):
    s = 0
    for i in range(n+1):
        s += i**2
    return s

def sumSquared(n):
    s = 0
    for i in range(n+1):
        s += i
    return s**2

def Ex1(n):
    return sumSquared(n) - sumSquares(n)

def primo(n):
    x = n // 2
    for i in range(x,1,-1):
        if n%i == 0:
            return False
    return True

def Ex2(n):
    suma = 0
    for i in range(2, n):
        if primo(i):
            suma += i
    return suma

def Ex3(n):
    '''
    n-Esimo primo
    '''
    cant = 0
    i = 1
    while(cant < n):
        i += 1
        if primo(i):
            cant += 1
    return i


def abundantNumber(n):
    suma = 0
    for i in range(n//2,0,-1):
        if n%i == 0:
            suma += i
    return suma > n

def Ex4(n):
    i = 0
    index = 0
    while index < n:
        i += 1
        if abundantNumber(i):
            index += 1
    return i

def perfectNumber(n):
    suma = 0
    for i in range(n//2,0,-1):
        if n%i == 0:
            suma += i
    return suma == n

def Ex5(n):
    suma = 0
    for i in range(6, n):
        if perfectNumber(i):
            suma += i
    return suma

