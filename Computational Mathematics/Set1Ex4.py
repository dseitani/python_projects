from sympy import symbols,simplify
from sympy.plotting import plot as symplot


def s_cal(s, n):
    temp=s;
    for i in range(1, n):
        temp= temp*(s - i);
    return temp;

#function for factorial
def fact(n):
    f=1
    for i in range(2, n + 1):
        f *= i
    return f

x=symbols('x')
n=6
x0=0.2
h=0.1
s=(x-x0)/h

#initial values for f(x)
x_v=[0.2,0.3,0.4,0.5,0.6,0.7]
f=[[0 for i in range(n)]
        for j in range(n)]
f[0][0]=0.185
f[1][0]=0.106
f[2][0]=0.093
f[3][0]=0.24
f[4][0]=0.579
f[5][0]=0.561

#calculate forward differances
for i in range(1, n):
    for j in range(n - i):
        f[j][i] = f[j + 1][i - 1] - f[j][i - 1];

#find the polynomial
P = f[0][0]
for i in range(1,n):
    P += (s_cal(s,i)*f[0][i])/fact(i)
P=simplify(P)
print(P)
symplot(P)
