import numpy as np
import matplotlib.pyplot as plt
from scipy._lib.six import xrange

#calculate the Lagrange coefficients
def Lagrange(y,x,n):

    L = np.poly1d(0.0)

    for j in xrange(n):
        pt=np.poly1d(y[j])
        for k in xrange(n):
            if k==j:
                continue
            factor= x[j]-x[k]
            pt *= np.poly1d([1.0,-x[k]])/factor
        L += pt
    return L


y_x = lambda x: 1+ np.sin(np.pi*x)
f_z = lambda z: 1/(1+pow(z,2))

#calculate values for y(x) and f(x) and make lists of the data
xi=[]
yi=[]
for i in range(-1,2):
    xi.append(i)
    yi.append(y_x(i))
x=np.array(xi) #we make the list into arrays so they work with poly1d
y=np.array(yi)

zi=[]
fi=[]
for i in range(-5,6):
    zi.append(i)
    fi.append(f_z(i))
z=np.array(zi)
f=np.array(fi)

#find the polynomials
Py=Lagrange(y,x,3)
Pf=Lagrange(f,z,11)

#keep significant terms
Py1=np.zeros(3)
Pf1=np.zeros(11)
for i in range(3):
    Py1[i]=round(Py.c[i],5)
for i in range(11):
    Pf1[i]=round(Pf.c[i],5)


Pol_y=np.poly1d(Py1)
print(Pol_y)
Pol_f=np.poly1d(Pf1)
print(Pol_f)


#plot the polynomials with the function they approach
x1=np.linspace(-1.0,1.0,100)
z1=np.linspace(-5.0,5.0,100)
plt.figure(1)
plt.axhline(y=1, color='r', linestyle='-',label='Py')
plt.plot(x1,y_x(x1),label='y = 1 + sin(pi*x)')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(alpha=.4,linestyle='--')
plt.legend()
plt.show()
plt.figure(2)
plt.plot(z,Pol_f,label='Pf')
plt.plot(z1,f_z(z1),label='f = 1/(1+x^2)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(alpha=.4,linestyle='--')
plt.legend()
plt.show()
