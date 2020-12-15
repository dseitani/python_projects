import numpy as np

f = lambda x: x*np.exp(2*x)

#integration limits
a = 0
b = 3

#Simple Simpson's 1/3 integration
h = (b-a)/2
I1 = (b-a)*(f(a)+4*f(a+h)+f(b))/6
print(I1)


#Simpson's 1/3 integration for n=8
n=8
h = (b-a)/n
integr = f(a)+f(b)
for i in range(1,n):
    if i%2 == 0:
        integr += 2*f(a+i*h)
    else:
        integr += 4*f(a+i*h)
I2 = integr*(h/3)
print(I2)
