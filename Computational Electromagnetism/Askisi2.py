import numpy as np
import matplotlib.pyplot as plt

# coefficient definition
def A(theta,dx):
    return dx*np.sin(theta)/2

def B(theta,dy):
    return dy*np.cos(theta)/2

N = np.array([5,10,20])
dx = 1/N
dy = 1/N
dt = 0.5*dx
c = 1 #light speed
S1 = c*dt/dx  # Courant factor for dx=dy
C1 = (np.sin(np.pi*S1/N))**2/S1**2
l = 1 # wavelength
up = np.zeros((len(N),91)) # phase velocity

# numerical phase velocity for dx=dy
for i in range(len(N)):
    for theta in range(0,91):
        thetar = theta*np.pi/180
        k0 = 2*np.pi/l
        e = 1;
        while (abs(e)>0.0005):
            k = k0 - (np.sin(A(thetar,dx[i])*k0)**2 + np.sin(B(thetar,dy[i])*k0)**2-C1[i])/(A(thetar,dx[i])*np.sin(2*A(thetar,dx[i])*k0)+B(thetar,dy[i])*np.sin(B(thetar,dy[i])*k0))
            e = k-k0
            k0 = k
        up[i,theta] = (2*np.pi/k)

x = np.arange(0,91,1)
plt.clf()
plt.plot(x,up[0,:],'r',label='lambda/5')
plt.plot(x,up[1,:],'g',label='lambda/10')
plt.plot(x,up[2,:],'b',label='lambda/20')
plt.xlabel('Wave angle (degrees)')
plt.ylabel('Phase velocity up/c')
plt.legend()
plt.savefig('fig1.jpeg')

# numerical phase velocity for dx!=dy
N = np.array([5,10])
dx = 1/N
dy = dx/2
dt = 0.5*dx
S2 = c*dt/dx + c*dt/dy # Courant factor for dx!=dy
C2 = (np.sin(np.pi*S2/N))**2/S2**2
up = np.zeros((len(N),91))

for i in range(len(N)):
    for theta in range(0,91):
        thetar = theta*np.pi/180
        k0 = 2*np.pi/l
        e = 1;
        while (abs(e)>0.0005):
            k = k0 - (np.sin(A(thetar,dx[i])*k0)**2 + np.sin(B(thetar,dy[i])*k0)**2-C2[i])/(A(thetar,dx[i])*np.sin(2*A(thetar,dx[i])*k0)+B(thetar,dy[i])*np.sin(B(thetar,dy[i])*k0))
            e = k-k0
            k0 = k
        up[i,theta] = (2*np.pi/k)

plt.clf()
plt.plot(x,up[0,:],'r',label='lambda/5')
plt.plot(x,up[1,:],'g',label='lambda/10')
plt.xlabel('Wave angle (degrees)')
plt.ylabel('Phase velocity up/c')
plt.legend()
plt.savefig('fig2.jpeg')
