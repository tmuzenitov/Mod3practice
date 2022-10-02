import random
N = 5
m =[[random.randint(0,100) for i in range(N)] for j in range(N)]
max = 0
for i in range(N):
    for j in range(N):
        if(m[i][j]>max):
            max=m[i][j]
for i in range(N):
    print(m[i])
print(max)