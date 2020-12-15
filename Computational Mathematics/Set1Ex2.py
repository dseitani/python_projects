import math as m
import numpy as np
import bigfloat as bf

f= lambda x: 2*np.exp(x)-3*pow(x,2) #x[-1,1]
df= lambda x: 2*np.exp(x)-6*x
g= lambda x: -m.sqrt(2/3*(bf.exp(x,bf.precision(100))))
#used bigfloat because of overflow error

i_g=0; i_nr=0

#x=g(x) method
x1=0; e_a=1
while (e_a>0.0005):
    i_g=i_g+1
    x2=g(x1)
    e_a=abs(x2-x1)
    x1=x2
print('x=g(x) method: x=%.4f' %x2,'\n iterations: ',i_g)

#Newton-Raphson method
x1=0; e_a=1
while (e_a>0.0005):
    i_nr=i_nr+1
    x2=x1-(f(x1)/df(x1))
    e_a=abs(f(x1)/df(x1))
    x1=x2
print('Newton-Raphson method: x=%.4f' %x2,'\n iterations: ',i_nr)
