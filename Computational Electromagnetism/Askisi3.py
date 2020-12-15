import numpy as np
import matplotlib.pyplot as plt


Nx = 200  #space values
Nt = 100  #time values

c = 2.99*10**8   #light speed
f = 1*10**9     #frequency=1GHz
l = c/f        #wave length
dx = l/20.0
dt = dx/c
mu0 = 4.0*np.pi*10**(-7)    #permeability of free space
epsilon0 = 1.0/(c**2*mu0) #permittivity of free space
E0 = 10.0      #amplitude of electric field


#define incident fields
def Hyinc(n,eta):
    return E0*np.cos(2*np.pi*f*n*dt - 2*(np.pi/l)*49*dx)/eta

def Ezinc(n):
    return E0*np.cos(2*np.pi*f*n*dt - 2*(np.pi/l)*49*dx)

#Yee algorithm coefficients for electric field
def Ca(s,e):
    return (1.0 - (dt*s)/(2.0*epsilon0*e))/(1.0 + (dt*s)/(2.0*epsilon0*e))

def Cb(s,e):
    return (dt/(epsilon0*e*dx))/(1.0 + (dt*s)/(2.0*epsilon0*e))

sigma = np.zeros(Nx)          #conductivity
epsilon = np.ones(Nx)        #relative permittivity

for i in range(50,Nx):
    epsilon[i] = 9
    sigma[i] = 0.01

eta = np.sqrt(mu0/epsilon)   #wave impedance

#initial values
Ez = np.zeros(Nx)
Hy = np.zeros(Nx)


for n in range(Nt):

    #past values for ABC
    Hy0 = Hy[-1]
    Ez0 = Ez[0]

    #update magnetic field
    for i in range(Nx-1):
        Hy[i] = Hy[i] - dt/(mu0*dx)*(Ez[i+1] - Ez[i])

    #TFSF correction
    Hy[49] = Hy[49] - dt/(mu0*dx)*(Ez[50] - Ez[49]) - dt/(mu0*dx)*Ezinc(n)

    #Mur's ABC for right side
    Hy[-1] = -Hy0 + (c*dt - dx)/(c*dt + dx)*(Hy[-2] + Hy0) + 2*dx/(c*dt + dx)*(Hy[-1] + Hy[-2])
    Hy0 = Hy[-1]

    #update electric field
    for i in range(1,Nx):
        Ez[i] = Ca(sigma[i],epsilon[i])*Ez[i] - Cb(sigma[i],epsilon[i])*(Hy[i] - Hy[i-1])

    #TFSF correction
    Ez[50] = Ca(sigma[50],epsilon[50])*Ez[50] - Cb(sigma[50],epsilon[50])*(Hy[50] - Hy[49] - Hyinc(n,eta[49]))

    #Mur's ABC for left side
    Ez[0] = -Ez0 + (c*dt - dx)/(c*dt + dx)*(Ez[1] + Ez0) + 2*dx/(c*dt + dx)*(Ez[0] + Ez[1])
    Exz0 = Ez[0]
