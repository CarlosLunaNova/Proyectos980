import random

N = 5
M = 3
P = 2

minRandom = 10
maxRandom = 100

dimension1 = []

for i in range(N):
    dimension2 = []
    for j in range(M):
        dimension3 = []
        for k in range(P):
            dimension3.append(random.randrange(minRandom,maxRandom,1))
        dimension2.append(random.randrange(minRandom,maxRandom,1))
    dimension3.append(random.randrange(minRandom,maxRandom,1))

