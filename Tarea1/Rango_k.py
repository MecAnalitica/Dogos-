import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.interpolate import interp1d


v0 = 500
g = 9.81
phi = 65*(m.pi/180)
V = v0 * m.cos(phi)
U = v0 * m.sin(phi)
R = (v0**2 / g) * m.sin(2*phi)
k = [0.001, 0.01, 0.02, 0.03, 0.04, 0.05]

def x(t):
	return (U/c)*(1 - math.exp(-c*t))

def Rango(KX):
	RX = R*(1 - ((4*V*KX) / (3*g)))
	return RX

file = open("RvsK.txt","w")

for c in k:
	file.write("%f " % c)
	file.write("%f" % Rango(c))
	file.write("\n")
file.close()


Ka, Ran = np.loadtxt('RvsK.txt', delimiter=' ', unpack=True)
Ki, T = np.loadtxt('k_T.txt', delimiter=' ', unpack=True)

plt.plot(Ki, T, label='Calculo numerico.')
plt.plot(Ka, Ran,label='Aproximacion (Perturbacion). ')



plt.xlabel('Parametro k, $[k] = s^{-1}$')
plt.ylabel('Rango $[R]=m$')
plt.title('Cambio del Rango en funcion del parametro $k, (s^{-1})$.')
plt.legend()
plt.grid()
plt.show()