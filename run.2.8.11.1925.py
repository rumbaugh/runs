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
cens = np.array(['1','1','4093.65,4920.99','3445.91,3445.91'])

nh = 0.0115
temp2 = ''
for i in range(3,4):
    cen = cens[i]
    bgA = bnds[i] + 10
    bgB = bnds[i] + 20
    load_data('%s/%s.img.500-2000.nops.fits'%(paths[i],names[i]))
    set_coord('physical')
    cnts1 = calc_data_sum2d('circle(%s,%i)'%(cen,bnds[i]))-(bnds[i])**2*calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(cen,bgB,cen,bgA))/(bgB**2-bgA**2)
    load_data('%s/%s.img.2000-8000.nops.fits'%(paths[i],names[i]))
    set_coord('physical')
    cnts2 = calc_data_sum2d('circle(%s,%i)'%(cen,bnds[i]))-(bnds[i])**2*calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(cen,bgB,cen,bgA))/(bgB**2-bgA**2)
    ncnts = cnts1+cnts2
    fourpiDl2 = (1/0.7/0.7)*1.310e+57
    DL = 3294/0.7
    load_pha('%s%s/spec_%s_full_grp.pi'%(path,pathspec[i],namespec[i]))
    rmf1 = unpack_rmf('%s%s/spec_%s_full.wrmf'%(path,pathspec[i],namespec[i]))
    arf1 = unpack_arf('%s%s/spec_%s_full.warf'%(path,pathspec[i],namespec[i]))
    notice(0.5,8.0)
    paramprompt()
    set_model(xswabs.abs1*xsraymond.rs)
    abs1.nh = nh
    time = times[i]
    freeze(abs1.nh)
    rs.kT = temps[i]
    rs.redshift = 0.76
    rs.Abundanc = 0.3
    flb = 0.5/(1.76)
    fub = 8.0/1.76
    n1 = calc_model_sum(0.5,0.8)
    rs.norm = 1.0/n1
    calc_model_sum(0.5,0.8)
    fake_pha(1,arf1,rmf1,time)
    eflx = calc_energy_flux(0.5,8.0)
    n2 = calc_model_sum(0.5,8.0)
    abs1.nh = 0.0
    fake_pha(1,arf1,rmf1,time)
    eflx2 = calc_energy_flux(flb,fub)
    cnt2flux = time*eflx2
    print "Count rate to unabsorbed flux conversion for " + names[i] + ": " + str(cnt2flux)
    flux = ncnts*cnt2flux/time
    lum = flux*fourpiDl2
    print lum
    
