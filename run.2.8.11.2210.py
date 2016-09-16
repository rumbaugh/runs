import os
import numpy as np
import math as m

names = np.array(['RXJ1757','acis10444+10924','acis9403+9840','acis9404+9836'])
paths = np.array(['/scratch/rumbaugh/ciaotesting/RXJ1757/master','/scratch/rumbaugh/ciaotesting/NEP5281/master','/scratch/rumbaugh/ciaotesting/Cl1324/master','/scratch/rumbaugh/ciaotesting/Cl1324/master'])
zz = np.array(['RXJ1757','10444+10924','9403+9840','9404+9836'])
pbk = np.array(['acis11999','acis10444','acis9840','../9836/acis9836'])
full = np.array(['full','full','full','full_2'])
bnds = np.array([300,300,250,200])
temps = np.array([1,1,1.8,0.9])

path = '/home/rumbaugh/ChandraData/'
pathspec = np.array(['NEP5281/10444+10924/spec','RXJ1757/master/spec','Cl1324/master/spec','Cl1324/master/spec'])
fields = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324'])
namespec = np.array(['10444+10924','RXJ1757','9403+9840','9404+9836'])
nharr = np.array([0.0566,0.0407,0.0115,0.0115])
z = np.array([0.82,0.69,0.76,0.76])
times = np.array([50000,50000,48391.890220549,50399.00069391])


nh = 0.0115
temp2 = ''
cen2 = '4584.3139,3388.91'
cen1 = '4631.314,3641'
bgcen = '4346.314,3644.9'
for i in range(3,4):
    ostemp = os.system('dmstat %s/conv.beta.12.15.10%s.fits verbose=0'%(paths[i],temp2))
    temp2 = '_2'
    ostemp = os.system('pget dmstat out_max_loc | tee temp1.txt')
    cr1 = read_file("temp1.txt")
    centemp = get_colvals(cr1,'col1')
    cen = centemp[0]
    bgA = bnds[i] + 10
    bgB = bnds[i] + 20
    load_data('%s/%s.img.500-2000.nops.fits'%(paths[i],names[i]))
    set_coord('physical')
    cnts1 = calc_data_sum2d('circle(%s,%i)'%(cen,bnds[i]))-(bnds[i])**2*calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(cen,bgB,cen,bgA))/(bgB**2-bgA**2)
    if i == 3:
        cnts1S = calc_data_sum2d('circle(%s,100)'%(cen1))-(100)**2*calc_data_sum2d('circle(%s,60)'%(bgcen))/(3600)
        cnts1B = calc_data_sum2d('circle(%s,100)'%(cen2))-(100)**2*calc_data_sum2d('circle(%s,60)'%(bgcen))/(3600)
    load_data('%s/%s.img.2000-8000.nops.fits'%(paths[i],names[i]))
    set_coord('physical')
    cnts2 = calc_data_sum2d('circle(%s,%i)'%(cen,bnds[i]))-(bnds[i])**2*calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(cen,bgB,cen,bgA))/(bgB**2-bgA**2)
    ncnts = cnts1+cnts2
    print 'Net counts for main cluster in %s: %f\n'%(names[i],ncnts)
    if i == 3:
        cnts2S = calc_data_sum2d('circle(%s,190)'%(cen1))-(190)**2*calc_data_sum2d('circle(%s,60)'%(bgcen)/(360))
        cnts2B = calc_data_sum2d('circle(%s,100)'%(cen2))-(100)**2*calc_data_sum2d('circle(%s,60)'%(bgcen)/(360))
    ncntsS = cnts2S+cnts1S
    ncntsB = cnts2B+cnts1B
    print ncntsS,ncntsB
