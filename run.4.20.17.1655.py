import numpy as np
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]
crrd=np.loadtxt('/home/rumbaugh/radecname_forSDSScutouts.4.20.17.csv',dtype={'names':('ra','dec','dbid'),'formats':('f8','f8','|S64')},delimiter=',')

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.19.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24')})
drop,baseline=np.abs(crd['glo']-crd['ghi']),np.abs(crd['mjdlo']-crd['mjdhi'])/(1+crd['z'])
matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=13.5
dbids,evqdbids,longdbids=crd['DBID'][drop>1],crd['DBID'][drop>2],crd['DBID'][(baseline>3400)&(drop>1)]
radecs,evqradecs,longradecs=np.zeros(len(dbids)),np.zeros(len(evqdbids)),np.zeros(len(longdbids))
for i in range(0,len(dbids)):
    grd=np.where('%s_SDSScutout'%dbids[i]==crrd['dbid'])[0][0]
    rah,ram,ras=deg2hms(crrd['ra'][grd])
    decd,decm,decs=deg2dms(crrd['dec'][grd])
    radecs[i]='J%02i%02i%04.1f%+02i%02i%4.1f'%(rah,ram,ras,decd,decm,decs)
for i in range(0,len(evqdbids)):
    grd=np.where('%s_SDSScutout'%evqdbids[i]==crrd['dbid'])[0][0]
    rah,ram,ras=deg2hms(crrd['ra'][grd])
    decd,decm,decs=deg2dms(crrd['dec'][grd])
    evqradecs[i]='J%02i%02i%04.1f%+02i%02i%4.1f'%(rah,ram,ras,decd,decm,decs)
for i in range(0,len(longdbids)):
    grd=np.where('%s_SDSScutout'%longdbids[i]==crrd['dbid'])[0][0]
    rah,ram,ras=deg2hms(crrd['ra'][grd])
    decd,decm,decs=deg2dms(crrd['dec'][grd])
    longradecs[i]='J%02i%02i%04.1f%+02i%02i%4.1f'%(rah,ram,ras,decd,decm,decs)
print radecs,evqradecs,longradecs
plot_DB_lightcurves(dbids,'/home/rumbaugh/DR7_EVQ_lightcurves.4.20.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False,sdsscutoutradec=radecs)
plot_DB_lightcurves(evqdbids,'/home/rumbaugh/DR7_mag2+_lightcurves.4.20.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False,sdsscutoutradec=evqradecs)
plot_DB_lightcurves(longdbids,'/home/rumbaugh/DR7_baseline3400+_lightcurves.4.19.20.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False,sdsscutoutradec=longradecs)

