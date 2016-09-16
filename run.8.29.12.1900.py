import numpy as np
#import matplotlib
#import matplotlib.pylab as pylab
import math as m

try:
    t3013
except NameError:
    t3013 = 3

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
#namespec = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/spec_10444+10924.pi","/home/rumbaugh/ChandraData/RXJ1757/master/spec_RXJ1757_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9403+9840.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9836.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9826_3013.4.24.11.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932a.3.28.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932b.3.28.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_2_grp.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_1_grp.pi"])
namespec = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/spec_10444+10924_grp.pi","/home/rumbaugh/ChandraData/RXJ1757/master/spec_RXJ1757_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9403+9840_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9836_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9826_3013.4.24.11_grp.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932a.3.28_grp.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932b.3.28_grp.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_2_grp.pi","/home/rumbaugh/ChandraData/0910/master/spec/spec_2227+2452_full_1_grp.pi"])
namef = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/acis10444+10924.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/RXJ1757/master/RXJ1757.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.vig_corr.nops.fits"])

nharr = np.array([5.66,4.07,1.15,1.16,1.16,7.57,7.57,2.05,2.05])/100.0
rsarr = np.array([0.84,0.69,0.69,0.76,0.76,0.898,0.866,1.1,1.1])
#rsarr = np.array([0.818,0.692,0.696,0.755,0.697,0.898,0.866,1.101,1.103])
times = np.array([49548.501183658,46451.792387024,48391.890220549,50399.00069391,50399.00069391,49478.092354796,49478.092354796,171046.89083577,171046.89083577])
cnt2flux = np.zeros(len(nharr))
cnt2flux2 = np.zeros(len(nharr))
ncnts = np.array([670,298,96,212,108,219,69,436])
ncnts = np.array([670,298,96,212,108,219,69,436])

Temps = np.array([4.95,3.75,4.71,3.71,t3013,3.50,1.64,4.5,2.5])

crc = read_file("/home/rumbaugh/cc_out.6.29.12.nh.dat")
#crc = read_file("/home/rumbaugh/cosmocalc_out.9.7.11.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
mpccm = get_colvals(crc,'col13')*0.7
lumdists = get_colvals(crc,'col9')/0.7
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
fourpiDL2 = 1e-57*get_colvals(crc,'col10')/(0.7*0.7)
tcnts = np.zeros(len(nharr))
netcnts = np.zeros(len(nharr))
bgcnts = np.zeros(len(nharr))
lums = np.zeros(len(nharr))
fluxs = np.zeros(len(nharr))
fluxs2 = np.zeros(len(nharr))
lumerr = np.zeros(len(nharr))

Abunds = np.array([0.1,0.2,0.25,0.27,0.28,0.29,0.295,0.299,0.3,0.301,0.305,0.31,0.32,0.3,0.35,0.4,0.5])

for i in range(0,len(names)):
    load_pha(str(namespec[i]))
    #ungroup()
    #notice(0.5,5.0)
    notice(0.3,8.0)
    set_model(xsraymond.rs*xswabs.abs1)
    #rs.kT = Temps[i]
    rs.kT = 3
    rs.redshift = rsarr[i]
    rs.Abundanc = 0.3
    rs.norm = 1.0
    abs1.nh = nharr[i]
    freeze(abs1.nh)
    thaw(rs.norm)
    time = times[i]
    #set_stat('cash')
    subtract()
    #group_counts(20)
    ungroup() #the referee thinks it should be ungrouped, i am testing how this affects the fits
    fit()
    freeze(rs.norm)
    projection()
    print Temps[i]
