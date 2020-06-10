num = 232000000
rango = 20
out = []

def divisor(n):
    for i in range(1,rango+1):
        if(n%i==0):
            out.append(i)


while True:
    divisor(num)
    if(len(out)<rango):
        out.clear()
        num=num+1       
    elif(len(out)==rango):
        print(out)
        print(num)
        break
        




        