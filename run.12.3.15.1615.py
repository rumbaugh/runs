import numpy as np

cr=np.loadtxt('/home/rumbaugh/Chandra/7914/photometry/7914.xray_phot_imp.soft_hard_full.dat')

ra,dec,fluxs,fluxh,fluxf=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]

g=np.argsort(ra)

rah=np.floor(ra*24/360.)
ram=np.floor((ra*24/360.-rah)*60)
ras=((ra*24/360.-rah)*60-ram)*60

decd=np.floor(dec)
decm=np.floor((dec-decd)*60)
decs=((dec-decd)*60-decm)*60

for i in g:
    print '%3i %3i %02i %05.2f %3i %02i %05.2f %7.2f %7.2f %7.2f'%(i,rah[i],ram[i],ras[i],decd[i],decm[i],decs[i],10**17*fluxs[i],10**17*fluxh[i],10**17*fluxf[i])
