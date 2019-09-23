from pylab import *

c=3*10**10 #cm/s
a=2.861 #cm
d=0.2 #cm
sigma=0.7*10**17 #c^-1

f=500 #Hz
# eta=27 # 1
eta=85
omega=2*pi*f

def delta(mu):
	return c/sqrt(2*pi*sigma*mu*omega)

def F(mu):
	return exp(d/delta(mu))/(6*eta*delta(mu)*a)*sqrt(
			((mu*delta(mu))**2+3*a*mu*delta(mu)+a**2)**2+
			(a**2-(mu*delta(mu))**2)**2
		)

# mu=153.68
# mu=718.815
mu=500
for i in range(1,10):
	print(mu)
	mu=F(mu)