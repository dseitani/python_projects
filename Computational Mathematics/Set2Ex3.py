import numpy as np

A = np.array([[4.0,1,2,1],[1,7,1,0],[2,1,4,-1],[1,0,-1,3]])
x = np.random.rand(4)

for i in range(40):
    xk = np.dot(A,x)
    xk_norm = np.linalg.norm(xk) #normalization
    x = xk/xk_norm #eigenvector
    l = np.dot(x,np.dot(A,x)) #eigenvalue

print(x)
print(l)
