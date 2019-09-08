from pylab import *
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read

def frexp10(decimal):
	parts = ('%e' % decimal).split('e')
	return float(parts[0]), int(parts[1])

sheet_name='5.2'
rec = path.abspath('.\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
y=array(df['I'])
x=array(df['U'])
g = polyfit(x,y,1)
y=poly1d(g)
resistance=1/g[0]
sheet_name='5.3'
rec = path.abspath('.\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
x=array(df['I']) # В Амперах
y=array(df['U'])
g = polyfit(x,y,9)
error=poly1d(g)
l,b,d= 22e-3, 0.38e-3 , 3.5e-3

rho=resistance*(d*b)/l
print('Удельное сопротивление',rho)
#Проверил по таблицам вроде порядок тот же
sigma=(1/rho)

sheet_name='5.3'
rec = path.abspath('.\\rec\\rec.xlsx')
df=read(rec, sheet_name=sheet_name)
x=array(df['I']) # В Амперах
y=array(df['U'])
g = polyfit(x,y,9)
error=poly1d(g)
print(error(10))


df=read(rec, sheet_name='5.4, I=1mA')
x=array(df['I'])*773/1e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
print(g[0])
R1=g[0]*b/(1e-3)
print('Для I=1mA',R1)




df=read(rec, sheet_name='5.4, I=2mA')
x=array(df['I'])*773/1e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
R2=g[0]*b/(2e-3)
print('Для I=2mA',R2)



df=read(rec, sheet_name='5.4, I=4mA')
x=array(df['I'])*773/1e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
R4=g[0]*b/(4e-3)
print('Для I=4mA',R4)




df=read(rec, sheet_name='5.4, I=7mA')
x=array(df['I'])*773/1e4 # В Тл
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1)
R7=g[0]*b/(7e-3)
print('Для I=7mA',R7)
sheet_name='5.6, B=200'
df=read(rec, sheet_name=sheet_name)
x=array(df['I'])/1000 # В Амперах 
y=array(df['E']) # В Вольтах
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
R200=(g[0]*b/200e-4)
print('Для B=200Гс',R200)




sheet_name='5.6, B=400'
df=read(rec, sheet_name=sheet_name)
x=array(df['I1']) /1000
y=array(df['E1'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
R400=(g[0]*b/400e-4)
print('Для B=400 Гс',R400)



sheet_name='5.6, B=600'
df=read(rec, sheet_name=sheet_name)
x=array(df['I'])/1000 # В Амперах
y=array(df['E'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
R600=(g[0]*b/600e-4)
print('Для B=600 Гс',R600)



sheet_name='5.6, B=900'
df=read(rec, sheet_name=sheet_name)
x=array(df['I'])/1000 # В Амперах
y=array(df['E'])
g = polyfit(x,y,1,w=1/error(x))
y=poly1d(g)
R900=(g[0]*b/900e-4)
print('Для B=900 Гс',R900)



R=array([R1,R2,R4,R7,R200,R400,R600,R900])
mu=mean(sigma*R)

A=3*pi/8
e=1.60217662e-19
n=A/mean(R)/e

print('Концентрация=',n)
print('Подвижность=',mu)
print('Проводимость=',sigma)