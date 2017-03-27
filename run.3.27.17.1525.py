import numpy
import matplotlib.pyplot as plt
import numpy as np
execfile('/home/rumbaugh/pythonscripts/StructureFunction.py')
outputdir='/home/rumbaugh/var_database/Y3A1'
DBdir='/home/rumbaugh/var_database/Y3A1'
nbins=10


hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]
crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm=crm[gdr]

crmd=crm[np.abs(crm['drop'])>1]

hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']

gc=np.zeros(len(cdata),dtype='i8')
for i in range(0,len(gc)): 
    try:
        gc[i]=np.where(crdb['SDSSNAME']==cname[i])[0][0]
    except IndexError:
        gc[i]=-1
gc=gc[gc>-1]


DBIDs=crdb['DatabaseID'][gc]
DBIDs=np.intersect1d(DBIDs,crdb['DatabaseID'][np.abs(crm['drop'])>1])
DBIDs=DBIDs[:20]
print DBIDs

#DBIDs=['MQ200905','MQ197739','MQ199828','MQ198719','MQ198646']

DBdir='/home/rumbaugh/var_database/Y3A1'

for DBID in DBIDs:
    cr=np.loadtxt('%s/%s/SF.tab'%(DBdir,DBID),dtype={'names':('tau','SF1','SF2','SF3','SF4','SF5','IQRN'),'formats':('f8','f8','f8','f8','f8','f8','f8')})

    plt.figure(1)
    plt.clf()
    color_arr=['magenta','red','blue','green','cyan']
    for i in np.arange(1,6): plt.loglog(cr['tau'],cr['SF%i'%i],lw=2,c=color_arr[i-1],label='SF%i'%i)
    plt.loglog(cr['tau'],cr['IQRN'],lw=2,c='orange',label='IQRN')
    plt.legend()
    plt.xlabel(r'$\Delta t$')
    plt.ylabel('Structure Function')
    plt.savefig('/home/rumbaugh/testplot_SF.%s.png'%DBID)
