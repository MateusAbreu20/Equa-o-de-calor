import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animation

L=1
a=9.7e-5
To=800
Tr=0

tmax=3600

N=200
dx=L/N
dt=dx**2/(2*a)

x=np.linspace(0,L,N+1)
T=np.zeros(N+1)

print(f'Malha: {N} pontos')
T[:] = To
T[[0,-1]] = Tr

f=a*dt/dx**2
fm=1-2*f

fig = plt.figure()
plt.ylim(0,850)
plt.xlabel('x(m)')
plt.ylabel('T(C)')

plt.plot(x,[To]*(N+1),'--',)
perfil, = plt.plot(x, T)
tempo = plt.text(L/2,820,f't=0 s')

def diferencas(i):
    T[1:-1] = f*(T[:-2]+T[2:])+fm*T[1:-1]
    perfil.set_ydata(T)
    tempo.set_text(f't={i*dt:.2f} s')
    return perfil, tempo

an = animation(fig,diferencas,interval=1,blit=True)

plt.show()



