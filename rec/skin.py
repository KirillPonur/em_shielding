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
freq = np.array(sheet.col_values(0)[3:])
# colors = ['ro-','ko-','bo-']
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
freq_ext = np.arange(0, 10000, 0.1)

c = 299792458  # m/s
# sigma = 1.5*10**(17)
# mu = 1
sigma = 0.7*10**(17)
mu = 500
omega = 2*np.pi*freq_ext

skin = c/np.sqrt(2*np.pi*sigma*mu*omega)

ax.plot(freq_ext,skin*100)

ax.plot(freq_ext,[0.2]*len(freq_ext),label = '2 мм')
ax.plot(freq_ext,[0.5]*len(freq_ext),label = '5 мм')
ax.plot(freq_ext,[1]*len(freq_ext),label = '10 мм')

# for i in range(1,4):
#     name = sheet.col_values(i*3)[0]
#     Ve = removeEmptyStrings(sheet.col_values(i*3)[3:])
#     Ue = removeEmptyStrings(sheet.col_values(i*3+1)[3:])
#     eta = removeEmptyStrings(sheet.col_values(i*3+2)[3:])


#     print('Строим ',name,'...')
#     ax.plot(freq,eta,colors[i-1],label = name)

# print(sheet.col_values(i*3))


ax.set_xlabel(r'Частота f, Гц')
ax.set_ylabel('$\delta$, см')
ax.grid(which='both')
# ax.set_yscale('log')
ax.set_xscale('log')
plt.legend()
# plt.savefig('imgs/graphs/lat.png',dpi=600)
plt.show()
