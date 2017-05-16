import numpy as np
execfile('/home/rumbaugh/pythonscripts/PowerRatios.py')

wid,smR=500,5

CPath='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE'

cr_peaks=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.init_smooth_peaks.dat',dtype={'names':('field','cluster','RA','Dec','ImageX','ImageY'),'formats':('|S15','|S15','f8','f8','f8','f8')})
cr_peaks=cr_peaks[:-1]

crcc=np.loadtxt("/home/rumbaugh/cc_out_clusters.2.1.16.dat",dtype={'names':('ID','z','omegaM','omegaVac','H0','age(Gyr)','zage(Gyr)','LTT(Gyr)','comov.rad.dist.(Mpc)','comov.rad.dist.(Gyr)','comov.vol.(Gpc^3)','DA(Mpc)','DA(Gyr)','kpc_DA','DL(Mpc)','DL(Gyr)','DistMod','E(z)','4piDL^2(Gpc^2)','4piDL^2(cm^2)'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

kpcs=crcc['kpc_DA']
Hz=crcc['E(z)']*crcc['H0']

kpc_dict={crcc['ID'][x]: kpcs[x] for x in np.arange(len(kpcs))}
outcr=np.zeros((len(cr_peaks),),dtype={'names':('field','clus','xcen','ycen','P3','P4','P3err','P4err'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8')})
outcr['field'],outcr['clus'],outcr['xcen'],outcr['ycen']=cr_peaks['field'],cr_peaks['cluster'],cr_peaks['ImageX'],cr_peaks['ImageY']
for i in range(0,len(cr_peaks)):
    clus,field,xcen0,ycen0=cr_peaks['cluster'][i],cr_peaks['field'][i],cr_peaks['ImageX'][i]-1,cr_peaks['ImageY'][i]-1
    kpc=kpc_dict[clus]
    R_Mpc=500./kpc/.492
    xcen,ycen=xcen0-int(np.round(xcen0))+wid-1,ycen0-int(np.round(ycen0))+wid-1
    SF_arr=np.loadtxt('%s/%s/proc/%s/%s.SFarr_%s_soft.wid_%i.R_%i.dat'%(CPath,field,field,field,clus,wid,smR))
    P3,P4=PowerRatio(SF_arr,3,R_Mpc,xcen,ycen),PowerRatio(SF_arr,4,R_Mpc,xcen,ycen)
    outcr['P3'][i],outcr['P4'][i]=P3,P4
np.savetxt('/home/rumbaugh/Chandra/ORELSE.power_ratios.dat',outcr,fmt='%12s %12s %10.5f %10.5f %f %f %f %f',header='field cluster ImageX ImageY P3 P4 P3err P4err')
