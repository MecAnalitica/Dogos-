import math as m
import matplotlib.pyplot as plt
import numpy as np

x1, y1, x2, y2, x3, y3, x4, y4, x5, y5= np.loadtxt('xn_yn.txt', delimiter=' ', unpack=True)
plt.plot(x1, y1, label='Trayectoria con $k=0.01$')
plt.plot(x2, y2, label='Trayectoria con $k=0.02$')
plt.plot(x3, y3, label='Trayectoria con $k=0.03$')
plt.plot(x4, y4, label='Trayectoria con $k=0.04$')
plt.plot(x5, y5, label='Trayectoria con $k=0.05$')

plt.xlabel('Distancia cubierta en la direccion x')
plt.ylabel('Distancia cubierta en la direccion y')
plt.title('Trayectorias para diferentes valores del parametro $k$ de friccion')
plt.legend()
plt.grid()
plt.show()