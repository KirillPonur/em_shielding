import numpy as np
import xlrd
import matplotlib.pyplot as plt
from matplotlib import rc
# import matplotlib
# from matplotlib.backends.backend_pdf import PdfPages

plt.rc('text', usetex=True)
plt.rc('font', size=14, family='serif')
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
# plt.rc('text.latex',unicode=True)


def removeEmptyStrings(lst):
    new_lst = []
    for i in range(0, len(lst)):
        if lst[i]:
            new_lst.append(lst[i])
        else:
            new_lst.append(float('nan'))
    return new_lst


loc = 'data/Ekranirovanie2.xlsx'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
freq = sheet.col_values(0)[3:]
colors = ['#1459CC', '#FF006A', '#222222']
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
# freq_ext = np.arange(20, 10000, 1)

c = 299792458  # m/s
sigma_lat = 1.5*10**(17)
sigma_st = 0.7*10**(17)
mu_lat = 1
mu_st = 200
d_lat = [0.002, 0.005, 0.01]  # lat
# cutoff = [4000,628,156]
R_IN = 0.025

mu_t = np.arange(100,225,0.1)
# steel
cutoff = [16,2.56,0.65]
# freq_ext = np.arange(20, 5000, 1)
# freq_ext = 500
for i in range(4, 6):
    name = sheet.col_values(i*3)[0]
    eta = removeEmptyStrings(sheet.col_values(i*3+2)[3:])
    pp = 4
    eta = eta[pp]
    freq_ext = freq[pp]

    skin = c/np.sqrt(4*np.pi**2*sigma_st*mu_t*freq_ext)
    radius = R_IN + d_lat[i-4]
    mda = mu_t*skin/radius
    amd = 1/mda
    rhs = 1/6*np.sqrt((mda + amd + 3)**2 + (amd - mda)**2)
    lhs = eta*np.exp(-d_lat[i-4]/skin)
    print('Строим ', name, '...')
    ax.plot(mu_t, rhs,'-',color = colors[i-4], label=name+' RHS '+ str(freq_ext)+' Гц')
    ax.plot(mu_t, lhs,'-',color = colors[i-4], label=name+' LHS '+ str(freq_ext)+' Гц')

for i in range(6, 7):
    name = sheet.col_values(i*3)[0]
    eta = removeEmptyStrings(sheet.col_values(i*3+2)[3:])
    pp = 3
    eta = eta[pp]
    freq_ext = freq[pp]

    skin = c/np.sqrt(4*np.pi**2*sigma_st*mu_t*freq_ext)
    radius = R_IN + d_lat[i-4]
    mda = mu_t*skin/radius
    amd = 1/mda
    rhs = 1/6*np.sqrt((mda + amd + 3)**2 + (amd - mda)**2)
    lhs = eta*np.exp(-d_lat[i-4]/skin)
    print('Строим ', name, '...')
    ax.plot(mu_t, rhs,'-',color = colors[i-4], label=name+' RHS '+ str(freq_ext)+' Гц')
    ax.plot(mu_t, lhs,'-',color = colors[i-4], label=name+' LHS '+ str(freq_ext)+' Гц')

plt.plot(152.63,1.293,'o',color = colors[0],markersize = 10)
plt.plot(154.7,1.218,'o',color = colors[1],markersize = 10)
plt.plot(126.1,1.381,'o',color = colors[2],markersize = 10)
ax.set_xlabel('$\mu$')
# ax.set_ylabel('')
ax.grid(which='both')
ax.set_ylim((1,1.8))
# ax.set_xscale('log')
plt.legend(loc='upper right', fancybox = False,shadow = False, framealpha = 1)
plt.savefig('imgs/graphs/mu.png',dpi=600)
plt.show()
