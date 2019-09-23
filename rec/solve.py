############################################
from pylab import *
import os.path as path
import sys
from pandas import read_excel as read
rec = path.abspath('rec.xlsx')
df=read(rec, sheet_name=0,header=[0,2])
columns = df.columns
freq = array(df.iloc[:,0])
U0=array(df.iloc[:,2])
V0=array(df.iloc[:,1])
Ve=[1,1,1]
Ue=[1,1,1]
eta=[1,1,1]
offset=9
for i in range(3):
    name = columns[offset+2*i][0]
    Ve[i] = array(df.iloc[:,offset+2*i])
    Ue[i] = array(df.iloc[:,offset+1+2*i])
    eta[i] = V0/Ve[i] * Ue[i]/U0
############################################

from scipy.optimize import newton,root_scalar

c=3*10**10 #cm/s
a=2.861 #cm
d=0.2 #cm
sigma=0.7*10**17 #c^-1


def delta(mu):
	return c/sqrt(2*pi*sigma*mu*omega)

def F(mu):
	return exp(d/delta(mu))/(6*eta0*delta(mu)*a)*\
	sqrt(
			((mu*delta(mu))**2+3*a*mu*delta(mu)+a**2)**2+
			(a**2-(mu*delta(mu))**2)**2
		)-mu

x=[1,1,1]
j=5
i=0
f=freq[j] #Hz
eta0=eta[i][j]
omega=2*pi*f

# x[i]=newton(F,130,maxiter=5000,)
x[i]=newton(F,x0=130,maxiter=5000,)

print(x)
