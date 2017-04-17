execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import pyfits as py
import time

clqsize=16

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

try:
    crp=np.loadtxt('/home/rumbaugh/primarydbid_table.4.14.17.1600.dat',dtype='|S48')
    PrimaryDBID={crp[:,0][x]: crp[:,1][x] for x in np.arange(len(crp))}
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
    np.savetxt('/home/rumbaugh/primarydbid_table.4.14.17.1600.dat',poutcr,fmt='%s %s')
    end=time.time()
    print 'First loop took %f'%(end-st)

gmf_dr7=np.where(data['SDSSNAME']!='-1')[0]


cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.28.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
cr=cr[gdr]
crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.17.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8')})
drop,baseline=np.abs(crd['glo']-crd['ghi']),np.abs(crd['mjdlo']-crd['mjdhi'])
try:
    gmf=np.loadtxt('/home/rumbaugh/gmf_table.4.10.17.1440.dat',dtype='i8')
except:
    print 'Starting second loop...'
    st=time.time()
    gmf=np.zeros(len(cr),dtype='i8')
    for i in range(0,len(gmf)):
        #PDBID=PrimaryDBID_dict[cr['DBID'][i]]
        #gp=np.where(data['DatabaseID']==PDBID)[0]
        gp=np.where(data['DatabaseID']==cr['DBID'][i])[0]
        gmf[i]=gp[0]
    np.savetxt('/home/rumbaugh/gmf_table.4.10.17.1440.dat',gmf,fmt='%i')
    end=time.time()
    print 'Second loop took %f'%(end-st)
medu,medg,medr,medi,medz=data['med_SDSS_u'][gmf],data['med_SDSS_g'][gmf],data['med_SDSS_r'][gmf],data['med_SDSS_i'][gmf],data['med_SDSS_z'][gmf]
medu_all,medg_all,medr_all,medi_all,medz_all=data['med_SDSS_u'][gmf_dr7],data['med_SDSS_g'][gmf_dr7],data['med_SDSS_r'][gmf_dr7],data['med_SDSS_i'][gmf_dr7],data['med_SDSS_z'][gmf_dr7]

crmd=cr[drop>1]
gmf_md=gmf[drop>1]

good_dbids=crmd['DBID'][drop>1]
gooddrops=np.abs(crmd['drop'])[drop>1]

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
gl=np.where(bhdata['LOGLBOL']>0)[0]
bhdata=bhdata[gl]
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
bhmagu,bhmagg,bhmagr,bhmagi,bhmagz,bhmagwise1,bhmagwise2,bhmagwise3,bhmagwise4=bhdata['UGRIZ'][:,0],bhdata['UGRIZ'][:,1],bhdata['UGRIZ'][:,2],bhdata['UGRIZ'][:,3],bhdata['UGRIZ'][:,4],bhdata['WISE1234'][:,0],bhdata['WISE1234'][:,1],bhdata['WISE1234'][:,2],bhdata['WISE1234'][:,3]
glc=np.where(cdata['LOGLBOL']>0)[0]
cdata=cdata[glc]
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']
cmagu,cmagg,cmagr,cmagi,cmagz,cmagwise1,cmagwise2,cmagwise3,cmagwise4=cdata['UGRIZ'][:,0],cdata['UGRIZ'][:,1],cdata['UGRIZ'][:,2],cdata['UGRIZ'][:,3],cdata['UGRIZ'][:,4],cdata['WISE1234'][:,0],cdata['WISE1234'][:,1],cdata['WISE1234'][:,2],cdata['WISE1234'][:,3]
bhdbid,cdbid=np.array(bhname,copy=True,dtype='|S24'),np.array(cname,copy=True,dtype='|S24')
for i in range(0,len(bhname)):
    try:
        bhdbid[i]=PrimaryDBID_dict['DR7BH%s'%bhname[i]]
    except:
        bhdbid[i]='DR7BH%s'%bhname[i]
for i in range(0,len(cname)):
    try:
        cdbid[i]=PrimaryDBID_dict['DR7BH%s'%cname[i]]
    except:
        cdbid[i]='DR7BH%s'%cname[i]

#try:
#    crcon=np.loadtxt('/home/rumbaugh/control_DBIDs.3.24.17.1040.dat',dtype={'names':('DBID','gdb'),'formats':('|S24','i8')})
#    cDBIDs,cgdb=crcon['DBID'],crcon['gdb']
#except:
#    print 'Starting third loop...'
#    st=time.time()
#    cDBIDs,cgdb=np.zeros(len(cz),dtype='|S24'),np.zeros(len(cz),dtype='i8')
#    for i in range(0,len(cgdb)):
#        cgdb[i]=np.where(crdb['DatabaseID']==PrimaryDBID_dict['DR7BH%s'%cname[i]])[0][0]
#        cDBIDs[i]=crdb['DatabaseID'][cgdb[i]]
#    conoutcr=np.zeros((len(cgdb),),dtype={'names':('DBID','gdb'),'formats':('|S24','i8')})
#    conoutcr['DBID'],conoutcr['gdb']=cDBIDs,cgdb
#    np.loadtxt('/home/rumbaugh/control_DBIDs.3.24.17.1040.dat',conoutcr,fmt='%s %i')
#    end=time.time()
#    print 'Third loop took %f'%(end-st)

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=18

matplotlib.rcParams['axes.linewidth']=4
matplotlib.rcParams['font.size']=18
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(crmd['Baseline']/(1.+data['redshift'][gmf_md]),range=(0,4400),bins=22,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(np.sort(crmd['Baseline']/(1.+data['redshift'][gmf_md])),(np.arange(len(crmd))+1.)/len(crmd),lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (Restframe days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,4400)
ax2.set_xlim(0,4400)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/MaxChangeBaselinePlot.RF.DR7_EVQs.4.17.17.png')

corr_weights=np.zeros(len(crmd))

for buff in [0,100,300,600]:
    crb=np.loadtxt('/home/rumbaugh/DetFracRF.buff_%i.4.10.17.dat'%buff)
    detepochs=np.append(np.append(0.,crb[:,1]),6000.)
    for i in range(0,len(a[1])-1):
        lb,ub=a[1][i],a[1][i+1]
        gb=np.where((detepochs>lb)&(detepochs<ub))[0]
        gw=np.where((crmd['Baseline']/(1.+data['redshift'][gmf_md])>lb)&(crmd['Baseline']/(1.+data['redshift'][gmf_md])<ub))[0]
        bounds=0.5*(np.append(detepochs[gb[0]-1],detepochs[gb])+np.append(detepochs[gb],detepochs[gb[-1]+1]))
        if bounds[0]>lb:
            bounds,gb=np.append(lb,bounds),np.append(gb[0]-1,gb)
        else:
            bounds[0]=lb
        if bounds[-1]<ub:
            bounds,gb=np.append(bounds,ub),np.append(gb,gb[-1]+1)
        else:
            bounds[-1]=ub
        corr_weights[gw]=np.sum(crb[:,0][gb-1]*(bounds[1:]-bounds[:-1]))/(a[1][i+1]-a[1][i])
    
    fig=plt.figure(1)
    fig.clf()
    plt.clf()
    plt.rc('axes',linewidth=2)
    ax=fig.add_subplot(1,1,1)
    ax2=ax.twinx()
    ax.tick_params(which='major',length=12,width=3,labelsize=17)
    ax.tick_params(which='minor',length=6,width=2,labelsize=17)
    ax2.tick_params(which='major',length=12,width=3,labelsize=17)
    ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
    a=ax.hist(crmd['Baseline']/(1.+data['redshift'][gmf_md]),range=(0,4400),bins=22,color='k',edgecolor='k',facecolor='None',lw=2)
    b=ax2.plot(np.sort(crmd['Baseline']/(1.+data['redshift'][gmf_md])),(np.arange(len(crmd))+1.)/len(crmd),lw=2,color='r')
    a2=ax.hist(crmd['Baseline']/(1.+data['redshift'][gmf_md]),weights=1./corr_weights,range=(0,4400),bins=22,color='k',edgecolor='k',facecolor='None',ls='dashed',lw=2)
    ax.set_xlabel('Maximum Change Baseline (Restframe days)')
    ax.set_ylabel(r'N$_{obj}$')
    ax2.set_ylabel('Cumulative Fraction')
    #ax.axhline(lw=4,color='k')
    #ax.axvline(lw=4,color='k')
    #ax2.axhline(lw=4,color='k')
    #ax2.axvline(lw=4,color='k')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(3)
    ax.set_xlim(0,4400)
    ax2.set_xlim(0,4400)
    ax2.set_ylim(0,1)
    fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/MaxChangeBaselinePlot.RF.DR7_EVQs.corr_wbuff_%i.4.17.17.png'%buff)


crbs=np.array([np.loadtxt('/home/rumbaugh/DetFracRF.buff_%i.4.10.17.dat'%x) for x in [0,100,300,600]])#,dtype='object'])
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
colarr=['k','r','green','cyan']
lsarr=['solid','dashed','dotted','-.']
for b,ib in zip([0,100,300,600],np.arange(4)):
    if b==0:
        label='No buffer'
    else:
        label='Buffer=%i days'%b
    plt.plot(crbs[ib][:,1],crbs[ib][:,0],color=colarr[ib],ls=lsarr[ib],lw=2,label=label)
plt.legend(loc='upper right',frameon=False)
plt.xlim(0,4400)
plt.xlabel('Maximum Change Baseline (restframe days)')
plt.ylabel('Detection Fraction')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/MaxChangeBaselinePlot.DetFrac_comp.baselines.4.17.17.png')
