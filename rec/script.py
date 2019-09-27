 
from pylab import *
from matplotlib import rc
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

rec = path.abspath('rec.xlsx')

df=read(rec, sheet_name=0,header=[0,2])
columns = df.columns
freq = array(df.iloc[:,0])


c = 299792458  # m/s
sigma_lat = 1.5*10**(17)
sigma_st = 0.7*10**(17)
mu_lat = 1
mu_st = 200

d_lat = [0.002, 0.005, 0.01]  # lat
cutoff = [4000,628,156]
R_IN = 0.025

sigma = [sigma_lat,sigma_st]
mu = [mu_lat,mu_st]
fig_name = ['lat','st']
offset = [3,9]
cutoff = [16,2.56,0.65]     
freq_ext = np.linspace(20, 10000, 10*3)
U0=array(df.iloc[:,2])
V0=array(df.iloc[:,1])
for j in range(2):
    colors = ['#1459CC', '#FF006A', '#222222']
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    for i in range(3):
        name = columns[offset[j]+2*i][0]
        Ve = array(df.iloc[:,offset[j]+2*i])
        Ue = array(df.iloc[:,offset[j]+1+2*i])
        eta = V0/Ve * Ue/U0
        skin = c/np.sqrt(4*np.pi**2*sigma[j]*mu[j]*freq_ext)
        radius = R_IN + d_lat[i]
        print(radius)
        mda = mu[j]*skin/radius
        amd = 1/mda
        eta_t_high = 1/6*np.exp(d_lat[i]/skin)*np.sqrt((mda + amd + 3)**2 + (amd - mda)**2)
        eta_t_low = np.sqrt( (1+2/3*d_lat[i]/radius*(mu[j]-1)**2/mu[j])**2 + (2/3*radius*d_lat[i]/mu[j]/skin**2)**2 )
        print('Строим ', name, '...')
        ax.plot(freq, eta,'o-',color = colors[i], label=name)
        ax.plot(freq_ext[freq_ext>cutoff[i]], eta_t_high[freq_ext>cutoff[i]],'--',color = colors[i])
        ax.plot(freq_ext[freq_ext<cutoff[i]], eta_t_low[freq_ext<cutoff[i]],'--',color = colors[i])


    ax.set_xlabel(r'Частота $f$, Гц')
    ax.set_ylabel(r'$|\eta_m|$')
    ax.grid(which='both')
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.legend(fancybox = False,shadow = False, framealpha = 1)
    plt.savefig(path.join('..', 'fig', fig_name[j]+'.pdf'))
    plt.show()