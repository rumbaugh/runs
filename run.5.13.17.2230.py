import numpy as np
import pyfits as py
execfile('/home/rumbaugh/pythonscripts/calc_SF_Xray.py')

CPath='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE'

R,wid=5,500

cr_peaks=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.init_smooth_peaks.dat',dtype={'names':('field','cluster','RA','Dec','ImageX','ImageY'),'formats':('|S15','|S15','f8','f8','f8','f8')})
crcc=np.loadtxt("/home/rumbaugh/cc_out_clusters.2.1.16.dat",dtype={'names':('ID','z','omegaM','omegaVac','H0','age(Gyr)','zage(Gyr)','LTT(Gyr)','comov.rad.dist.(Mpc)','comov.rad.dist.(Gyr)','comov.vol.(Gpc^3)','DA(Mpc)','DA(Gyr)','kpc_DA','DL(Mpc)','DL(Gyr)','DistMod','E(z)','4piDL^2(Gpc^2)','4piDL^2(cm^2)'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

for i in range(0,len(cr_peaks)):
    clus,field,xcen,ycen=cr_peaks['cluster'][i],cr_peaks['field'][i],cr_peaks['ImageX'][i]-1,cr_peaks['ImageY'][i]-1
    hdu=py.open('%s/%s/proc/%s/%s_soft_nops.vig_corr.img'%(CPath,field,field,field))
    data=hdu[0].data
    inArr=data[int(np.round(ycen))-wid:int(np.round(ycen))+wid+1,int(np.round(xcen))-wid:int(np.round(xcen))+wid+1]
    SFarr=calc_SF_Xray(inArr)
    np.savetxt('%s/%s/proc/%s/%s.SFarr_%s_soft.wid_%i.R_%i.dat'%(CPath,field,field,field,clus,wid,R),SFarr)
