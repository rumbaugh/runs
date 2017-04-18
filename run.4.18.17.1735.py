import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

gmf=np.loadtxt('/home/rumbaugh/gmf_table.4.10.17.1440.dat',dtype='i8')

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
crp=np.loadtxt('/home/rumbaugh/primarydbid_table.4.14.17.1600.dat',dtype='|S48')
PrimaryDBID={crp[:,0][x]: crp[:,1][x] for x in np.arange(len(crp))}
bhdbid,cdbid=np.array(bhname,copy=True,dtype='|S24'),np.array(cname,copy=True,dtype='|S24')
for i in range(0,len(bhname)):
    try:
        bhdbid[i]=PrimaryDBID_dict['DR7BH%s'%bhname[i]]
    except:
        bhdbid[i]='DR7BH%s'%bhname[i]
gbh=np.zeros(len(gmf),dtype='i8')
for i in range(0,len(gmf)):
    gbh[i]=np.where(bhdbid==crdb['DatabaseID'][i])[0][0]
dists=SphDist(bhdata['RA'][gbh],bhdata['DEC'][gbh],data['RA_DES'][gmf],data['DEC_DES'][gmf])*60
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=18
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.hist(dists,range(0,2),bins=20,lw=2)
plt.xlabel('Separation (arcseconds)')
plt.ylabel('Number of Objects')
plt.xlim(0,2)
plt.savefig('/home/rumbaugh/DR7_DES_spatial_sep.hist.png')
