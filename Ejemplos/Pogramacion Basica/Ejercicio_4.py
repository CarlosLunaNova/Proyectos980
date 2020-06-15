n=0
for i in range(1,1000):
    for j in range(1,1000):
        if (i*j)==(int(str(i*j)[::-1])):
            if (i*j>n):
                n=i*j
print(n)
        