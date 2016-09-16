import numpy as np
import math as m
import time
import sys
execfile("/home/rumbaugh/PowerRatios.py")

st = time.time()

print 'Note that this script needs to be run on gravlens\n'

try:
    aperture
except NameError:
    aperture = 0.5

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

imcensY = np.array([768.422,720.375,2236.0,1380.492,815.5,798.656,1986.469,1117.562,1501.609])
imcensX = np.array([1349.594,2021.5,1525.25,774.523,873.5,1283.375,1219.219,1523.375,871.5])

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

for i in range(0,len(names)):
    if i < len(names)-2.1:
        xfile = '/scratch/rumbaugh/ciaotesting/%s/master/acis%s.img.500-2000.nops.fits'%(strucs[i],chandraIDs[i])
        if i == 3: xfile = '/scratch/rumbaugh/ciaotesting/%s/master/RXJ1757.img.500-2000.nops.fits'%(strucs[i])
        if ((i == 5) | (i == 6)): '/scratch/rumbaugh/ciaotesting/Cl1604/6932/acis%.img.500-2000.nops.fits'%(chandraIDs[i])
    else:
        xfile = '/home/rumbaugh/ChandraData/0910/master/acis%s.img.500-2000.nops.fits'%(chandraIDs[i])
    cr = read_file(xfile)
    pvals = copy_piximgvals(cr)
    pvshape = np.shape(pvals)
    cp1 = time.time()
    tp0 = P_0(pvals,imcensX[i],imcensY[i],srchdist[i])
    tp2 = P_m(pvals,2,imcensX[i],imcensY[i],srchdist[i])
    tp3 = P_m(pvals,3,imcensX[i],imcensY[i],srchdist[i])
    tp4 = P_m(pvals,4,imcensX[i],imcensY[i],srchdist[i])
    tp02 = P_0(pvals,imcensX[i],imcensY[i],srchdist[i]*0.5)
    tp22 = P_m(pvals,2,imcensX[i],imcensY[i],srchdist[i]*0.5)
    tp32 = P_m(pvals,3,imcensX[i],imcensY[i],srchdist[i]*0.5)
    tp42 = P_m(pvals,4,imcensX[i],imcensY[i],srchdist[i]*0.5)
    print '%s - 0.5 Mpc\nP_2/P_0: %E\nP_3/P_0: %E\nP_4/P_0: %E\n%s - 0.25 Mpc\nP_2/P_0: %E\nP_3/P_0: %E\nP_4/P_0: %E\n\n'%(names[i],tp2/tp0,tp3/tp0,tp4/tp0,names[i],tp22/tp02,tp32/tp02,tp42/tp02)
        
