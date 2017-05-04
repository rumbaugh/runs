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

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
crd=crd[:100]
drop,baseline=np.abs(crd['glo']-crd['ghi']),np.abs(crd['mjdlo']-crd['mjdhi'])/(1+crd['z'])
matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=13.5
dbids,evqdbids,longdbids=crd['DBID'][drop>1],crd['DBID'][drop>2],crd['DBID'][(baseline>3400)&(drop>1)]
radecs,evqradecs,longradecs=np.zeros(len(dbids),dtype='|S24'),np.zeros(len(evqdbids),dtype='|S24'),np.zeros(len(longdbids),dtype='|S24')
for i in range(0,len(dbids)):
    grd=np.where('%s_SDSScutout'%dbids[i]==crrd['dbid'])[0][0]
    rah,ram,ras=deg2hms(crrd['ra'][grd])
    decd,decm,decs=deg2dms(crrd['dec'][grd])
    radecs[i]='J%02i%02i%04.1f%+02i%02i%4.1f'%(rah,ram,ras,decd,decm,decs)
plot_DB_lightcurves(dbids,'/home/rumbaugh/DR7_EVQ_lightcurves.5.4.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False,sdsscutoutradec=radecs,plotspread=True)
