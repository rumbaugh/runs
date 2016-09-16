import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m

try:
    t3013
except NameError:
    t3013 = 3

#5281,1757,1324+3059,1324+3011,1604A,1604B
names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
namespec = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/spec_10444+10924.pi","/home/rumbaugh/ChandraData/RXJ1757/master/spec_RXJ1757_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9403+9840.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9836.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9826_3013.4.24.11.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932a.3.28.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932b.3.28.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_2_grp.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_1_grp.pi"])
namef = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/acis10444+10924.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/RXJ1757/master/RXJ1757.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.vig_corr.nops.fits"])


xcens = np.array([3885.5130391,4099.7827296,4090.65,3915.3138561,4667.3138561,4011.5271805,3945.5271805,4009.28,4656.28])
ycens = np.array([4114.342391,4351.7991,4919.99,3446.91,3622.91,3414.8217815,4599.8217815,4359.77,3974.77])
#above are new centers using new smoothing

ann_arr = np.arange(51)*5+25
area_arr = np.zeros(len(ann_arr))
area_arr[0] = m.pi*ann_arr[0]*ann_arr[0]
for i in range(1,len(ann_arr)): area_arr[i] = m.pi*(ann_arr[i]*ann_arr[i]-ann_arr[i-1]*ann_arr[i-1])

ncnts = np.array([670,298,96,212,108,219,69,436,258])

Temps = np.array([4.95,3.75,4.71,3.71,t3013,3.50,1.64,4.5,2.52])
TerrU = np.array([0.99,1.00,10,1.44,10,1.82,0.65,1.07,0.59])
TerrD = np.array([0.74,0.68,2.95,0.94,2.99,1.08,0.45,0.78,0.47])
sigma = np.array([921,652,880,914,819,619,811,675,1028])
sigerr = np.array([76,123,124,137,242,96,76,190,140])

lineslope = (m.log(2146)-m.log(308))/(m.log(20))
lineb = m.log(308)
expb = 308.0
lineX = (np.arange(10000)+5)*(10.0/10000)
lineY = expb*lineX**lineslope

anninner = np.array([120,100,160,100,160,150,100,100,100])*1.0
annouter1 = anninner + 100
annouter2 = anninner + 150

#nharr = np.array([5.66,4.07,1.15,1.16,1.23,1.23])
#I need to use Dale's value forit to be compatible
nharr = np.array([5.66,4.07,1.15,1.16,1.16,7.57,7.57,2.05,2.05])/100.0
rsarr = np.array([0.84,0.69,0.69,0.76,0.76,0.898,0.866,1.1,1.1])
times = np.array([49548.501183658,46451.792387024,48391.890220549,50399.00069391,50399.00069391,49478.092354796,49478.092354796,171046.89083577,171046.89083577])
cnt2flux = np.zeros(len(nharr))
cnt2flux2 = np.zeros(len(nharr))

crc = read_file("/home/rumbaugh/cc_out.6.29.12.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Hz = np.append(Hz,Hz[len(Hz)-1])
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
mpc = np.append(mpc,mpc[len(mpc)-1])
mpccm = get_colvals(crc,'col13')*0.7
mpccm = np.append(mpccm,mpccm[len(mpccm)-1])
lumdists = get_colvals(crc,'col9')/0.7
lumdists = np.append(lumdists,lumdists[len(lumdists)-1])
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
fourpiDL2 = 1e-57*get_colvals(crc,'col10')/(0.7*0.7)
fourpiDL2 = np.append(fourpiDL2,fourpiDL2[len(fourpiDL2)-1])
tcnts = np.zeros(len(nharr))
netcnts = np.zeros(len(nharr))
bgcnts = np.zeros(len(nharr))
lums = np.zeros(len(nharr))
fluxs = np.zeros(len(nharr))
fluxs2 = np.zeros(len(nharr))
lumerr = np.zeros(len(nharr))

cnts_arr = np.zeros(len(ann_arr))

for i in range(0,len(sigma)):
    load_data(str(namef[i]))
    set_coord('physical')
    set_model(beta2d.b)
    r200 = 2*(mpc[i]*60)*2*sigma[i]/(m.sqrt(200)*Hz[i])
    b.xpos = xcens[i]
    b.ypos = ycens[i]
    b.r0 = 2*0.18*(mpc[i]*60)
    b.alpha = 1.5
    netcnts[i] = calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,anninner[i])) - (calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,annouter2[i]))-calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,annouter1[i])))*anninner[i]**2/(annouter2[i]**2-annouter1[i]**2)
    bgcnts[i] = (calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,annouter2[i]))-calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,annouter1[i])))
    cperc = calc_source_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,anninner[i]))/calc_source_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,r200))
    for j in range(0,len(ann_arr)):
        cnts_arr[j] = calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,ann_arr[j]))
    SB_arr = cnts_arr/area_arr
    tcnts[i] = netcnts[i]/cperc
    tcerr = m.sqrt(ncnts[i])/cperc
    flux = tcnts[i]*cnt2flux[i]/time
    flux2 = ncnts[i]*cnt2flux2[i]/time
    fluxs[i] = flux2*1e14
    fluxs2[i] = flux*1e14
    ferr = tcerr*cnt2flux[i]/time
    #lums[i] = flux*4*m.pi*lumdistmod[i]**2*10**5*Ez[i]
    #lumerr[i] = ferr*4*m.pi*lumdistmod[i]**2*10**5*Ez[i]
    lums[i] = flux*fourpiDL2[i]/Ez[i]*1e14
    lumerr[i] = ferr*fourpiDL2[i]/Ez[i]*1e14
    #lums in units of 10^43 ergs/s
    pylab.scatter(ann_arr*0.5,SB_arr*4)
    pylab.savefig('/home/rumbaugh/DE_counts_profile.%s.9.25.12.png'%names[i])
    pylab.close()

    
