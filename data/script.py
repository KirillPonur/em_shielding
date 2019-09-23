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
freq_ext = np.arange(20, 10000, 1)

c = 299792458  # m/s
sigma_lat = 1.5*10**(17)
sigma_st = 0.7*10**(17)
mu_lat = 1
mu_st = 200
d_lat = [0.002, 0.005, 0.01]  # lat
cutoff = [4000,628,156]
R_IN = 0.025
# for i in range(1, 4):
#     name = sheet.col_values(i*3)[0]
#     Ve = removeEmptyStrings(sheet.col_values(i*3)[3:])
#     Ue = removeEmptyStrings(sheet.col_values(i*3+1)[3:])
#     eta = removeEmptyStrings(sheet.col_values(i*3+2)[3:])

#     skin = c/np.sqrt(4*np.pi**2*sigma_lat*mu_lat*freq_ext)
#     radius = R_IN + d_lat[i-1]
#     mda = mu_lat*skin/radius
#     amd = 1/mda
#     eta_t_high = 1/6*np.exp(d_lat[i-1]/skin)*np.sqrt((mda + amd + 3)**2 + (amd - mda)**2)
#     eta_t_low = np.sqrt( (1+2/3*d_lat[i-1]/radius*(mu_lat-1)**2/mu_lat)**2 + (2/3*radius*d_lat[i-1]/mu_lat/skin**2)**2 )
#     print('Строим ', name, '...')
#     ax.plot(freq, eta,'o-',color = colors[i-1], label=name+' мм')
#     ax.plot(freq_ext[freq_ext>cutoff[i-1]], eta_t_high[freq_ext>cutoff[i-1]],'--',color = colors[i-1])
#     ax.plot(freq_ext[freq_ext<cutoff[i-1]], eta_t_low[freq_ext<cutoff[i-1]],'--',color = colors[i-1])

# steel
cutoff = [16,2.56,0.65]
freq_ext = np.arange(20, 5000, 1)
for i in range(4, 7):
    name = sheet.col_values(i*3)[0]
    Ve = removeEmptyStrings(sheet.col_values(i*3)[3:])
    Ue = removeEmptyStrings(sheet.col_values(i*3+1)[3:])
    eta = removeEmptyStrings(sheet.col_values(i*3+2)[3:])

    skin = c/np.sqrt(4*np.pi**2*sigma_st*mu_st*freq_ext)
    radius = R_IN + d_lat[i-4]
    mda = mu_st*skin/radius
    amd = 1/mda
    eta_t_high = 1/6*np.exp(d_lat[i-4]/skin)*np.sqrt((mda + amd + 3)**2 + (amd - mda)**2)
    eta_t_low = np.sqrt( (1+2/3*d_lat[i-4]/radius*(mu_st-1)**2/mu_st)**2 + (2/3*radius*d_lat[i-4]/mu_st/skin**2)**2 )
    print('Строим ', name, '...')
    ax.plot(freq, eta,'o-',color = colors[i-4], label=name+' мм')
    ax.plot(freq_ext[freq_ext>cutoff[i-4]], eta_t_high[freq_ext>cutoff[i-4]],'--',color = colors[i-4])
    ax.plot(freq_ext[freq_ext<cutoff[i-4]], eta_t_low[freq_ext<cutoff[i-4]],'--',color = colors[i-4])

    # print(sheet.col_values(i*3))


ax.set_xlabel(r'Частота $f$, Гц')
ax.set_ylabel('$|\eta_m|$')
ax.grid(which='both')
ax.set_yscale('log')
ax.set_xscale('log')
plt.legend(fancybox = False,shadow = False, framealpha = 1)
# plt.savefig('imgs/graphs/steel.png',dpi=600)
plt.show()
