import math

v=[100, 200, 300, 400, 500] 
phi=[30, 45, 60, 75]
g=9.81
ti=5.0
tf=100.0
error=0.001
k=[0.001, 0.01, 0.02, 0.03, 0.04, 0.05]


print("\nh / T / Vel_inicial / angulo_inicial \n")

file = open("kT_mix.txt","w")

for e in v:

	for d in phi:
		V=e*math.sin(d*(math.pi/180))
		U=e*math.cos(d*(math.pi/180))

		for c in k:

			def fun(T):
				y = (((c*V + g)/(g*c))*(1 - math.exp(-c * T))) - T
				return (y)
			
			raiz=[]
			raiz.insert(0,0)
			i=0
			ec=1

			while abs(ec) > error:
				tn = tf - (fun(tf) * (ti - tf))/(fun(ti) - fun(tf))
				raiz.append(tn)
				ti = tf
				tf = tn
				i = i+1
				ec = (raiz[i] - raiz[i-1])/(raiz[i])

			print(c, tn, e, d)

			def x(t):
				return (U/c)*(1 - math.exp(-c*t))
	
			file.write("%f " % c)
			file.write("%f" % x(tn))
			file.write("\n")
file.close()