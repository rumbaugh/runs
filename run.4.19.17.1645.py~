import numpy as np
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

gmf=np.loadtxt('/home/rumbaugh/gmf_table.4.10.17.1440.dat',dtype='i8')

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
try:
    crp=np.loadtxt('/home/rumbaugh/primarydbid_table.4.18.17.1735.dat',dtype='|S48')
    PrimaryDBID_dict={crp[:,0][x]: crp[:,1][x] for x in np.arange(len(crp))}
except:
    print 'Starting first loop...'
    st=time.time()
    gdb=np.where(crdb['SDSSNAME']!='-1')[0]
    PrimaryDBID_dict={}
    for i in range(0,len(gdb)):
        PrimaryDBID=crdb['DatabaseID'][gdb[i]]
        AllDBIDs = crdb['DBIDS'][gdb[i]]
        AllDBIDs=AllDBIDs.split(';')
        for DBID in AllDBIDs:
            if DBID[:2]=='DR': PrimaryDBID_dict[DBID]=PrimaryDBID
        try:
            PrimaryDBID_dict[DBID]
        except KeyError:
            print "Couldn't find DBID for "+PrimaryDBID
    poutcr=np.zeros((len(gdb),),dtype={'names':('key','val'),'formats':('|S48','|S48')})
    pkeys=PrimaryDBID_dict.keys()
    for i in range(0,len(gdb)): poutcr['key'][i],poutcr['val'][i]=pkeys[i],PrimaryDBID_dict[pkeys[i]]
    np.savetxt('/home/rumbaugh/primarydbid_table.4.18.17.1735.dat',poutcr,fmt='%s %s')
    end=time.time()
    print 'First loop took %f'%(end-st)

bhdbid=np.array(bhname,copy=True,dtype='|S24')
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
dists2=dists[data['RA_DES'][gmf]>0]
matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=18
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.hist(dists2,range=(0,2),bins=100,lw=2)
plt.xlabel('Separation (arcseconds)')
plt.ylabel('Number of Objects')
plt.xlim(0,2)
plt.savefig('/home/rumbaugh/DR7_DES_spatial_sep.hist.png')

gfar=np.arange(len(crdb))[(dists>0.5)&(data['RA_DES'][gmf]>0)]
fardbids=crdb['DatabaseID'][gfar]


outcr=np.zeros((len(fardbids),),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','|S64')})
outcr_radec=np.zeros((len(gfar),2))
outcr['RA'],outcr['DEC'],outcr['Name']=data['RA_DES'][gmf[gfar]],data['DEC_DES'][gmf[gfar]],crdb['DatabaseID'][gfar]
outcr_radec[:,0],outcr_radec[:,1]=data['RA_DES'][gmf[gfar]],data['DEC_DES'][gmf[gfar]]
np.savetxt('/home/rumbaugh/radecname_forDEScutouts.4.18.17.csv',outcr,fmt='%f,%f,%s')
np.savetxt('/home/rumbaugh/radec_forDEScutouts.4.18.17.csv',outcr_radec,fmt='%f,%f')

outcr=np.zeros((len(fardbids),),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','|S64')})
outcr_radec=np.zeros((len(gfar),2))
outcr['RA'],outcr['DEC'],outcr['Name']=bhdata['RA'][gbh[gfar]],bhdata['DEC'][gbh[gfar]],crdb['DatabaseID'][gfar]
outcr_radec[:,0],outcr_radec[:,1]=bhdata['RA'][gbh[gfar]],bhdata['DEC'][gbh[gfar]]
np.savetxt('/home/rumbaugh/radecname_forSDSScutouts.4.18.17.csv',outcr,fmt='%f,%f,%s_SDSScutout')
np.savetxt('/home/rumbaugh/radec_forSDSScutouts.4.18.17.csv',outcr_radec,fmt='%f,%f')

matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14
plot_DB_lightcurves(fardbids,'/home/rumbaugh/DR7_largesep_lightcurves.4.18.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,load_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False)

