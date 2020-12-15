import numpy as np

A = np.array([[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]])
b = np.array([[-8],[-20],[-2],[4]])
AA = np.hstack((A,b)) #stacks arrays horizondally
n = len(b)

def S(AA,x,i,n):
    sol = 0
    for j in range(i+1,n):
        sol += AA[i][j]*x[j]
    return sol


for i in range(n):

    #pivoting
    max = abs(AA[i][i])
    maxind = i
    for j in range(i+1,n):
        if abs(AA[j][i])>max:
            max = abs(AA[j][i])
            maxind = j

    for k in range(i,n+1):
        temp = AA[maxind][k]
        AA[maxind][k] = AA[i][k]
        AA[i][k] = temp

    #creating the upper triangular matrix
    for j in range(i+1,n):
        for k in range(i+1,n+1):
            AA[j][k] += (-AA[j][i]/AA[i][i])*AA[i][k]
            AA[j][i] = 0

print(AA)
#solving the system with backsubstitution
x = np.zeros(n)
x[n-1] = AA[n-1][n]/AA[n-1][n-1]
for i in range(n-2,-1,-1):
        x[i] = 1/AA[i][i]*(AA[i][n]-S(AA,x,i,n))

print(x)
