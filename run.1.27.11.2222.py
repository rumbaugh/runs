import numpy as np
import math as m
import os

names = np.array(['367','5602','5604','3571','3460','6249','7759','7761','1644','5194','5794','4763','4807','5193','8176','3572','3419'])

mergednames= np.array(['7757+363','427+3461','419+1629','423+424'])

path = '/scratch/rumbaugh/ciaotesting'

ann = np.arange(149)
ann = 2*ann+4

cnts = np.zeros(149)
FILE2 = open("/home/rumbaugh/COSMOS/conv.centers.12.28.11.dat","w")
for i in range(0,len(mergednames)):
    if i == 3: 
        ost = os.system('dmstat %s/merged/conv.beta.%s.12.9.10.fits verbose=0'%(path,mergednames[i]))
    else:
        ost = os.system('dmstat %s/merged/conv.beta.1.24.11.%s.fits verbose=0'%(path,mergednames[i]))
    ost = os.system('pget dmstat out_max_loc | tee temp.txt')
    cr = read_file('temp.txt')
    centemp = get_colvals(cr,'col1')
    centemp = centemp[0]
    FILE2.write('%s %s\n'%(mergednames[i],centemp))
    load_data('%s/merged/%s.fits'%(path,mergednames[i]))
    set_coord("physical")
    cnts[0] += calc_data_sum2d('circle(%s,4)'%(centemp))/(m.pi*(16))
    for r in range(1,len(ann)):
        cnts[r] += calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(centemp,ann[r],centemp,ann[r-1]))/(m.pi*(ann[i]**2-ann[i-1]**2))
for i in range(0,len(names)):
    ost = os.system('dmstat %s/%s/conv.beta.12.4.10.fits verbose=0'%(path,names[i]))
    ost = os.system('pget dmstat out_max_loc | tee temp.txt')
    cr = read_file('temp.txt')
    centemp = get_colvals(cr,'col1')
    centemp = centemp[0]
    FILE2.write('%s %s\n'%(names[i],centemp))
    load_data('%s/%s/acis%s.img.500-2000.S07.nops.norand.fits'%(path,names[i],names[i]))
    set_coord("physical")
    cnts[0] += calc_data_sum2d('circle(%s,4)'%(centemp))/(m.pi*(16))
    for r in range(1,len(ann)):
        cnts[r] += calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(centemp,ann[r],centemp,ann[r-1]))/(m.pi*(ann[i]**2-ann[i-1]**2))
cnts /= (len(names)+len(mergednames)*1.0)
FILE=open("/home/rumbaugh/COSMOS/full.spat.anal.1.27.11.dat",'w')
for i in range(0,len(cnts)):
    FILE.write('%3i %10.7f\n'%(ann[i],cnts[i]))
FILE.close()
FILE2.close()
    
