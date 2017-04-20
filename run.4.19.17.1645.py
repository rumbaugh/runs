import numpy as np
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.19.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','DBID'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24')})
drop,baseline=np.abs(crd['glo']-crd['ghi']),np.abs(crd['mjdlo']-crd['mjdhi'])/(1+crd['z'])
matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14
evqdbids,longdbids=crd['DBID'][drop>2],crd['DBID'][baseline>3400]
plot_DB_lightcurves(evqdbids,'/home/rumbaugh/DR7_mag2+_lightcurves.4.19.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False)
plot_DB_lightcurves(longbids,'/home/rumbaugh/DR7_baseline3400+_lightcurves.4.19.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False)

