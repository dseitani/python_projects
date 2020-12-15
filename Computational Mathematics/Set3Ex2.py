import numpy as np
import math as m

f = lambda t,y: y*m.pow(t,2)-1.1*y
y0 = 1
t0=0
#h = 0.5
h = 0.25

#Euler's method
y = y0+h*f(t0,y0)
for i in np.arange(t0+h,2+h,h):
    ynew = y+h*f(i,y)
    y = ynew
print(y)


#4rth order Runge-Kutta
k1 = f(t0,y0)
k2 = f(t0+h/2,y0+h/2*k1)
k3 = f(t0+h/2,y0+h/2*k2)
k4 = f(t0+h,y0+h*k3)
y = y0+h*(1/6*k1+1/3*k2+1/3*k3+1/6*k4)
for i in np.arange(t0+h,2+h,h):
    k1 = f(i,y)
    k2 = f(i+h/2,y+h/2*k1)
    k3 = f(i+h/2,y+h/2*k2)
    k4 = f(i+h,y+h*k3)
    ynew = y+h*(1/6*k1+1/3*k2+1/3*k3+1/6*k4)
    y = ynew
print(y)
