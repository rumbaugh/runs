import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/PowerRatios.py")

st = time.time()

print 'Note that this script needs to be run on gravlens\n'

try:
    aperture
except NameError:
    aperture = 0.5

crp1 = read_file("/home/rumbaugh/p1_cens.2.2.12.dat")
p1censx = copy_colvals(crp1,'col2')
p1censy = copy_colvals(crp1,'col3')

ncnts = np.array([212,108,96,298,670,219,69,258,456])
apsizes = np.array([50,80,80,50,60,75,50,50,50])
regsizes = np.array([(250*250-200*200),(250*250-200*200),(300*300-260*260),(240*240-200*200),200*200,100*100,(250*250-200*200),(250*250-200*200),(250*250-200*200)])

bgcnts = np.array([1044,1044,971,882,1740,1740,1048,2312,2312])

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

imcensYold = np.array([768.422,720.375,2236.0,1380.492,815.5,798.656,1986.469,1117.562,1501.609])
imcensXold = np.array([1349.594,2021.5,1525.25,774.523,873.5,1283.375,1219.219,1523.375,871.5])

imcensY,imcensX = np.zeros(len(names)),np.zeros(len(names))
for i in range(0,len(imcensY)):
    imcensY[i] = p1censy[i+1]
    imcensX[i] = p1censx[i+1]

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
#centerRAs = np.array([((16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24])
#centerDecs = np.array([43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])
#1 Mpc = 3.06*0.7 Arcmin
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7*aperture*60
crn = read_file('/home/rumbaugh/temp.powrat.2.15.12.dat')
tp0s,tp2s,tp4s,tp3s,tp02s,tp22s,tp42s,tp32s,tp0vs,tp2vs,tp4vs,tp3vs,tp02vs,tp22vs,tp42vs,tp32vs = copy_colvals(crn,'col1'),copy_colvals(crn,'col2'),copy_colvals(crn,'col3'),copy_colvals(crn,'col4'),copy_colvals(crn,'col5'),copy_colvals(crn,'col6'),copy_colvals(crn,'col7'),copy_colvals(crn,'col8'),copy_colvals(crn,'col9'),copy_colvals(crn,'col10'),copy_colvals(crn,'col11'),copy_colvals(crn,'col12'),copy_colvals(crn,'col13'),copy_colvals(crn,'col14'),copy_colvals(crn,'col15'),copy_colvals(crn,'col16')
crn = read_file('/home/rumbaugh/temp.powrat_2.2.15.12.dat')
tp0s2,tp2s2,tp4s2,tp3s2,tp02s2,tp22s2,tp42s2,tp32s2,tp0vs2,tp2vs2,tp4vs2,tp3vs2,tp02vs2,tp22vs2,tp42vs2,tp32vs2 = copy_colvals(crn,'col1'),copy_colvals(crn,'col2'),copy_colvals(crn,'col3'),copy_colvals(crn,'col4'),copy_colvals(crn,'col5'),copy_colvals(crn,'col6'),copy_colvals(crn,'col7'),copy_colvals(crn,'col8'),copy_colvals(crn,'col9'),copy_colvals(crn,'col10'),copy_colvals(crn,'col11'),copy_colvals(crn,'col12'),copy_colvals(crn,'col13'),copy_colvals(crn,'col14'),copy_colvals(crn,'col15'),copy_colvals(crn,'col16')
tp0s,tp2s,tp4s,tp3s,tp02s,tp22s,tp42s,tp32s,tp0vs,tp2vs,tp4vs,tp3vs,tp02vs,tp22vs,tp42vs,tp32vs = np.append(tp0s,tp0s2),np.append(tp2s,tp2s2),np.append(tp3s,tp3s2),np.append(tp4s,tp4s2),np.append(tp02s,tp02s2),np.append(tp22s,tp22s2),np.append(tp32s,tp32s2),np.append(tp42s,tp42s2),np.append(tp0vs,tp0vs2),np.append(tp2vs,tp2vs2),np.append(tp3vs,tp3vs2),np.append(tp4vs,tp4vs2),np.append(tp02vs,tp02vs2),np.append(tp22vs,tp22vs2),np.append(tp32vs,tp32vs2),np.append(tp42vs,tp42vs2)

inds1 = np.arange(9)
width = 0.2

p2errs,p3errs,p4errs,p22errs,p32errs,p42errs = np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names))
p2errsL,p3errsL,p4errsL,p22errsL,p32errsL,p42errsL = np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names)),np.zeros(len(names))

for i in range(0,len(names)):
    p2errs[i] = m.sqrt(tp2vs[i]/(tp0s[i]**2)+tp0vs[i]*tp2s[i]**2/(tp0s[i]**4))
    if p2errs[i] > tp2s[i]/tp0s[i]:
        p2errsL[i] = tp2s[i]/tp0s[i]-10**(-10)
    else:
        p2errsL[i] = p2errs[i]
    p3errs[i] = m.sqrt(tp3vs[i]/(tp0s[i]**2)+tp0vs[i]*tp3s[i]**2/(tp0s[i]**4))
    if p3errs[i] > tp3s[i]/tp0s[i]:
        p3errsL[i] = tp3s[i]/tp0s[i]-10**(-10)
    else:
        p3errsL[i] = p3errs[i]
    p3errs[i] = m.sqrt(tp4vs[i]/(tp0s[i]**2)+tp0vs[i]*tp4s[i]**2/(tp0s[i]**4))
    if p4errs[i] > tp4s[i]/tp0s[i]:
        p4errsL[i] = tp4s[i]/tp0s[i]-10**(-10)
    else:
        p4errsL[i] = p4errs[i]
    p22errs[i] = m.sqrt(tp22vs[i]/(tp02s[i]**2)+tp02vs[i]*tp22s[i]**2/(tp02s[i]**4))
    if p22errs[i] > tp22s[i]/tp02s[i]:
        p22errsL[i] = tp22s[i]/tp02s[i]-10**(-10)
    else:
        p22errsL[i] = p22errs[i]
    p32errs[i] = m.sqrt(tp32vs[i]/(tp02s[i]**2)+tp02vs[i]*tp32s[i]**2/(tp02s[i]**4))
    if p32errs[i] > tp32s[i]/tp02s[i]:
        p32errsL[i] = tp32s[i]/tp02s[i]-10**(-10)
    else:
        p32errsL[i] = p32errs[i]
    p42errs[i] = m.sqrt(tp42vs[i]/(tp02s[i]**2)+tp02vs[i]*tp42s[i]**2/(tp02s[i]**4))
    if p42errs[i] > tp42s[i]/tp02s[i]:
        p42errsL[i] = tp42s[i]/tp02s[i]-10**(-10)
    else:
        p42errsL[i] = p42errs[i]


pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp2s/tp0s, tp3s/tp0s, xerr=[p2errsL,p2errs],yerr=[p3errsL,p3errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp2s[i]/tp0s[i],1.1*tp3s[i]/tp0s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_2$/P$_0$')
pylab.ylabel('P$_3$/P$_0$')
pylab.title('Power Ratios within 0.5 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p2vp3.0.5_mpc.2.15.12.png')
pylab.close('all')

pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp2s/tp0s, tp4s/tp0s, xerr=[p2errsL,p2errs],yerr=[p4errsL,p4errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp2s[i]/tp0s[i],1.1*tp4s[i]/tp0s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_2$/P$_0$')
pylab.ylabel('P$_4$/P$_0$')
pylab.title('Power Ratios within 0.5 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p2vp4.0.5_mpc.2.15.12.png')
pylab.close('all')

pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp3s/tp0s, tp4s/tp0s, xerr=[p3errsL,p3errs],yerr=[p4errsL,p4errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp3s[i]/tp0s[i],1.1*tp4s[i]/tp0s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_3$/P$_0$')
pylab.ylabel('P$_4$/P$_0$')
pylab.title('Power Ratios within 0.5 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p3vp4.0.5_mpc.2.15.12.png')
pylab.close('all')

pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp22s/tp02s, tp32s/tp02s, xerr=[p22errsL,p22errs],yerr=[p32errsL,p32errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp22s[i]/tp02s[i],1.1*tp32s[i]/tp02s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_2$/P$_0$')
pylab.ylabel('P$_3$/P$_0$')
pylab.title('Power Ratios within 0.25 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p2vp3.0.25_mpc.2.15.12.png')
pylab.close('all')

pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp22s/tp02s, tp42s/tp02s, xerr=[p22errsL,p22errs],yerr=[p42errsL,p42errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp22s[i]/tp02s[i],1.1*tp42s[i]/tp02s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_2$/P$_0$')
pylab.ylabel('P$_4$/P$_0$')
pylab.title('Power Ratios within 0.25 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p2vp4.0.25_mpc.2.15.12.png')
pylab.close('all')

pylab.xlim(10**-9,10**-5)
pylab.ylim(10**-9,10**-5)
pylab.loglog(np.arange(3),np.zeros(3))
pylab.errorbar(tp32s/tp02s, tp42s/tp02s, xerr=[p32errsL,p32errs],yerr=[p42errsL,p42errs],fmt='ro')
for i in range(0,len(names)):
    pylab.text(1.1*tp32s[i]/tp02s[i],1.1*tp42s[i]/tp02s[i],names[i],color='black',weight='extra bold')

pylab.xlabel('P$_3$/P$_0$')
pylab.ylabel('P$_4$/P$_0$')
pylab.title('Power Ratios within 0.25 Mpc')
pylab.savefig('/home/rumbaugh/powerratios.p3vp4.0.25_mpc.2.15.12.png')
pylab.close('all')
FILEN.close()
