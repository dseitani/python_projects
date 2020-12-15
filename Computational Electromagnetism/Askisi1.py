import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

Nx = 11     #space values
Nt = 61     #time values

ue = np.zeros((Nx,Nt))  #explicit solution
ui = np.zeros((Nx,Nt))     #implicit solution
c = 1     #light speed
dx = 1    #space step
dt = 1.1  #time step

#initial values
for i in range(3,Nx):
    if i==10:
        ue[i,0] = 1
        ue[i,1] = 1
        ui[i,0] = 1
        ui[i,0] = 1
        continue
    ue[i,0] = 1
    ue[i+1,1] = 1
    ui[i,0] = 1
    ui[i+1,1] = 1

#dirichlet boundary conditions
for n in range(0,Nt):
    ue[0,n] = 0
    ue[Nx-1,n] = 0
    ui[0,n] = 0
    ui[Nx-1,n] = 0

# explicit scheme
for n in range(1,Nt-1):
    for i in range(1,Nx-1):
        ue[i,n+1] = (c*dt)**2*(ue[i+1,n]-2*ue[i,n]+ue[i-1,n])/dx**2 +2*ue[i,n]-ue[i,n-1]

#implicit scheme
beta = 0.25
I = np.identity(Nx)   #identity matrix
L = diags([-1, 2, -1], [-1, 0, 1], shape=(Nx, Nx)).toarray()  #tridiagonal matrix
A = beta*L + dx**2/(c*dt)**2*I
B = (2*beta-1)/2*L + dx**2/(c*dt)**2*I
AA = np.linalg.inv(A)
AB = np.matmul(AA,B)

for n in range(1,Nt-1):
    ui[:,n+1] = 2*AB.dot(ui[:,n])-ui[:,n-1]

#plot snapshot of the wave
x = np.arange(0,11,1) # x-axis values
for n in [20,30,40,50,60]:
    plt.plot(x,ue[:,n])
    plt.xlabel('x')
    plt.ylabel('u')
    plt.savefig('ue_'+str(n)+'_dt11.jpeg')
    plt.clf()
    plt.plot(x,ui[:,n])
    plt.xlabel('x')
    plt.ylabel('u')
    plt.savefig('ui_'+str(n)+'_dt11.jpeg')
    plt.clf()
