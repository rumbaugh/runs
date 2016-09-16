execfile("/home/rumbaugh/Dispersion.py")
import matplotlib.pyplot as plt
date = '5.12.14'

try:
    maxtime
except NameError:
    maxtime = 100
mintime = -1*maxtime
try:
    timestep
except NameError:
    timestep = 0.5
try:
    minmu
except NameError:
    minmu = 0.9
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    mustep
except NameError:
    mustep = 0.001
try:
    disp_type
except NameError:
    disp_type = 'D_4_2'
try:
    delta
except NameError:
    delta = 10.5

import pyfits as py
hdu = py.open('/mnt/data2/rumbaugh/Fermi/data/0218/S30218+35_86400.lc')
d = hdu[1].data
ltime = (d['START']-d['START'][0])/86400
g = np.where((ltime > 350) & (ltime < 525))[0]
Sfull = d['FLUX_100_300000']
Sfullerr = d['ERROR_100_300000']
outfile = '/mnt/data2/rumbaugh/Fermi/plots/0218/fermi_lc.0218.FLUX_100_300000.daily_binning.png'
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(ltime,Sfull,Sfullerr,c='r')
plt.scatter(ltime,Sfull,c='r')
plt.xlabel('Time (days)',fontsize=14)
plt.ylabel('Flux')
plt.title('0218 Lightcurve - Daily binning')
plt.savefig(outfile)

outfile = '/mnt/data2/rumbaugh/Fermi/plots/0218/fermi_lc.0218.FLUX_100_300000.daily_binning.flaring_period.png'
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(ltime[g],Sfull[g],Sfullerr[g],c='r')
plt.scatter(ltime[g],Sfull[g],c='r')
plt.xlabel('Time (days)',fontsize=14)
plt.ylabel('Flux')
plt.title('0218 Lightcurve - Daily binning')
plt.savefig(outfile)
