import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animation

L=1 # comprimento da barra
a=9.7e-5 # difusidade termica
To=800# temperatura inicial
Tr=0# temperatura final

tmax=3600 #tempo maximo de execução

N=200 # tamanho da malha
dx=L/N #delta x
dt=dx**2/(2*a) #calculo de delta x para estbilidade

x=np.linspace(0,L,N+1) #Criando a malha
T=np.zeros(N+1)# vetor com a temperatura da barra em cada instante t

print(f'Malha: {N} pontos')
T[:] = To #condição incial
T[[0,-1]] = Tr #condição de contorno

#variveis auxliares
f=a*dt/dx**2
fm=1-2*f

#cria o grafico
fig = plt.figure()
plt.ylim(0,850)
plt.xlabel('x(m)')
plt.ylabel('T(C)')

plt.plot(x,[To]*(N+1),'--',)
perfil, = plt.plot(x, T)
tempo = plt.text(L/2,820,f't=0 s')

def diferencas(i): #Diferençs finitas
    T[1:-1] = f*(T[:-2]+T[2:])+fm*T[1:-1]#Nos internos utlizando slicing
    perfil.set_ydata(T)
    tempo.set_text(f't={i*dt:.2f} s')
    return perfil, tempo

an = animation(fig,diferencas,interval=1,blit=True)

plt.show()



