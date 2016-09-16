date = '7.7.14'

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
outfile = '/mnt/data2/rumbaugh/Fermi/output/0218/disp_out.daily_lc.D_2.%s.dat'%(date)

calc_disp_delay(Sfull[g],Sfull[g],ltime[g],ltime[g],Sfullerr[g],Sfullerr[g],maxtime,timestep,minmu,maxmu,mustep,'D_2',delta=delta,mintime=mintime,dispmatrix=True,outfile=outfile)
for delta in np.arange(18)+2.5:
    outfile = '/mnt/data2/rumbaugh/Fermi/output/0218/disp_out.daily_lc.%s.delta_%4.1f.%s.dat'%(disp_type,delta,date)
    calc_disp_delay(Sfull[g],Sfull[g],ltime[g],ltime[g],Sfullerr[g],Sfullerr[g],maxtime,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta,mintime=mintime,dispmatrix=True,outfile=outfile)
