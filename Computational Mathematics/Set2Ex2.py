import numpy as np

f = lambda x: x*np.exp(x)
df = lambda x: np.exp(x)*(1+x)
x = np.array([1.7,1.8,1.9,2.0,2.1,2.2,2.3])
n = len(x)
fx = np.zeros(n)
dfx = np.zeros(n)
ndfx = np.zeros(n)
err = np.zeros(n)

#real values of f(x) and f'(x)
for i in range(n):
    fx[i] = f(x[i])
    dfx[i] = df(x[i])

#central differnces
for j in range(1,n-1):
    ndfx[j] = (f(x[j+1])-f(x[j-1]))/(2*(x[j]-x[j-1]))
    err[j] = dfx[j]-ndfx[j]

print(dfx)
print(ndfx)
print(err)

#Simpson's 1/3 integration

h = (x[n-2]-x[1])/(n-2)
integr = f(x[1])+f(x[n-2])
for k in range(2,n-2):
    if k%2 == 0:
        integr += 4*f(x[k])
    else:
        integr += 2*f(x[k])
integr = integr*(h/3)

print(integr)
