execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pyfits as py
import time

clqsize=16

hdu=py.open('/home/rumbaugh/var_database/Y3A1/old_masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

try:
    crp=np.loadtxt('/home/rumbaugh/primarydbid_table.3.24.17.1040.dat',dtype='|S48')
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
    np.savetxt('/home/rumbaugh/primarydbid_table.3.24.17.1040.dat',poutcr,fmt='%s %s')
    end=time.time()
    print 'First loop took %f'%(end-st)

gmf_dr7=np.where(data['SDSSNAME']!='-1')[0]

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.19.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24')})

#cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
drop=np.abs(cr['glo']-cr['ghi'])
try:
    gmf=np.loadtxt('/home/rumbaugh/gmf_table.3.24.17.1040.dat',dtype='i8')
except:
    print 'Starting second loop...'
    st=time.time()
    gmf=np.zeros(len(cr),dtype='i8')
    for i in range(0,len(gmf)):
        #PDBID=PrimaryDBID_dict[cr['DBID'][i]]
        #gp=np.where(data['DatabaseID']==PDBID)[0]
        gp=np.where(data['DatabaseID']==cr['DBID'][i])[0]
        gmf[i]=gp[0]
    np.savetxt('/home/rumbaugh/gmf_table.3.24.17.1040.dat',gmf,fmt='%i')
    end=time.time()
    print 'Second loop took %f'%(end-st)
medu,medg,medr,medi,medz=data['med_SDSS_u'][gmf],data['med_SDSS_g'][gmf],data['med_SDSS_r'][gmf],data['med_SDSS_i'][gmf],data['med_SDSS_z'][gmf]
medu_all,medg_all,medr_all,medi_all,medz_all=data['med_SDSS_u'][gmf_dr7],data['med_SDSS_g'][gmf_dr7],data['med_SDSS_r'][gmf_dr7],data['med_SDSS_i'][gmf_dr7],data['med_SDSS_z'][gmf_dr7]

crmd=cr[np.abs(drop)>1]
gmf_md=gmf[np.abs(drop)>1]
dropmd=drop[drop>1]

good_dbids=crmd['DBID'][np.abs(dropmd)>1]
gooddrops=np.abs(dropmd)[np.abs(dropmd)>1]

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


print 'Starting good_id loops...'
try: 
    gkeep
except NameError:
    st=time.time()
    ggd=np.zeros(len(good_dbids),dtype='i8')
    gkeep=np.ones(len(good_dbids),dtype='bool')
    for i in range(0,len(ggd)): 
        ggddb=np.where(good_dbids[i]==crdb['DatabaseID'])[0][0]
        try:
            ggd[i]=np.where(bhname==crdb['SDSSNAME'][ggddb])[0][0]
        except IndexError:
            gkeep[i]=0
    good_dbids,ggd,gooddrops=good_dbids[gkeep],ggd[gkeep],gooddrops[gkeep]
    extra_good_dbids=good_dbids[gooddrops>1.5]
    extra_extra_good_dbids=good_dbids[gooddrops>2]
    gegd=np.zeros(len(extra_good_dbids),dtype='i8')
    for i in range(0,len(gegd)): 
        gegddb=np.where(extra_good_dbids[i]==crdb['DatabaseID'])[0][0]
        gegd[i]=np.where(bhname==crdb['SDSSNAME'][gegddb])[0][0]
    geegd=np.zeros(len(extra_extra_good_dbids),dtype='i8')
    for i in range(0,len(geegd)): 
        geegddb=np.where(crdb['DatabaseID']==extra_extra_good_dbids[i])[0][0]
        geegd[i]=np.where(bhname==crdb['SDSSNAME'][geegddb])[0][0]
    end=time.time()
    print 'good_id loops took %f'%(end-st)


execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')


bhOIII,bhHB,bhFe=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']
bhOIIIorig,bhHBorig,bhFeorig=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']

ggs=np.where((bhHB>0)&(bhFe>0))[0]
bhOIII,bhHB,bhFe=bhOIII[ggs],bhHB[ggs],bhFe[ggs]


csize=4
gdsize=4
consize=12
nlevels=4


def calc_contour(A,B,Amin=None,Amax=None,Bmin=None,Bmax=None,tsize=30,subdivisions=None):
    if Amin==None: Amin=np.min(A)
    if Amax==None: Amax=np.min(A)
    if Bmin==None: Bmin=np.min(B)
    if Bmax==None: Bmax=np.min(B)
    Abnds,Bbnds=np.linspace(Amin,Amax,tsize+1),np.linspace(Bmin,Bmax,tsize+1)
    Bcens,Acens=0.5*(Bbnds[:-1]+Bbnds[1:]),0.5*(Abnds[:-1]+Abnds[1:])
    Bsize,Asize=Bcens[1]-Bcens[0],Acens[1]-Acens[0]
    Bcens,Acens=np.linspace(Bcens[0],Bcens[-1],(len(Bcens)-1)*subdivisions+1),np.linspace(Acens[0],Acens[-1],(len(Acens)-1)*subdivisions+1)
    #AB_pairs=np.zeros((2,tsize**2))
    #AB_pairs[0],AB_pairs[1]=np.repeat(Acens,len(Bcens)),np.tile(Bcens,len(Acens))
    #richness=np.zeros(len(AB_pairs[0]))
    AB_pairs=np.meshgrid(Acens,Bcens)
    richness=np.zeros(np.shape(AB_pairs[0]))
    for i in np.arange(np.shape(richness)[-1]):
        for j in np.arange(np.shape(richness)[-1]):
            cur_A,cur_B=AB_pairs[0][i][j],AB_pairs[1][i][j]
            richness[i][j]=len(np.where((np.abs(cur_B-B)<=0.5*Bsize)&(np.abs(cur_A-A)<=0.5*Asize))[0])
    return AB_pairs,richness
    #plt.contour(AB_pairs[0],AB_pairs[1],richness,color='k')


cug,cgr,cri,ciz,czW1,cW1W2,cW2W3,cW3W4=cmagu-cmagg,cmagg-cmagr,cmagr-cmagi,cmagi-cmagz,cmagz-cmagwise1,cmagwise1-cmagwise2,cmagwise2-cmagwise3,cmagwise3-cmagwise4
ggdug,ggdgr,ggdri,ggdiz,ggdzW1,ggdW1W2,ggdW2W3,ggdW3W4=bhmagu[ggd]-bhmagg[ggd],bhmagg[ggd]-bhmagr[ggd],bhmagr[ggd]-bhmagi[ggd],bhmagi[ggd]-bhmagz[ggd],bhmagz[ggd]-bhmagwise1[ggd],bhmagwise1[ggd]-bhmagwise2[ggd],bhmagwise2[ggd]-bhmagwise3[ggd],bhmagwise3[ggd]-bhmagwise4[ggd]
ggdz=bhz[ggd]


def calc_runmed(color,z,width,divisions=100,zmin=None,zmax=None,highz=None,highwid=None):
    if zmin==None: zmin=np.min(z)
    if zmax==None: zmax=np.max(z)
    zcens=np.linspace(zmin+width,zmax-width,divisions)
    runmed=np.zeros(len(zcens))
    if ((highz!=None)&(highwid!=None)):
        for i in np.arange(len(zcens))[zcens<highz]:
            runmed[i]=np.median(color[np.abs(z-zcens[i])<width])
        for i in np.arange(len(zcens))[zcens>=highz]:
            runmed[i]=np.median(color[np.abs(z-zcens[i])<highwid])
    else:
        for i in range(0,len(zcens)):
            runmed[i]=np.median(color[np.abs(z-zcens[i])<width])
    return zcens,runmed
#matplotlib.rcParams['figure.figsize']=[16,18]
matplotlib.rcParams['axes.linewidth']=3
gs1=gs.GridSpec(4,2)
gs1.update(hspace=0)
plt.figure(figsize=(16,19))
plt.clf()
#for ccolor,evqcolor,colorlabel,colorname,i,lb,ub in zip([cug,cgr,cri,ciz,czW1,cW1W2,cW2W3,cW3W4],[ggdug,ggdgr,ggdri,ggdiz,ggdzW1,ggdW1W2,ggdW2W3,ggdW3W4],['$u-g$','$g-r$','$r-i$','$i-z$','$z-$W1','W1-W2','W2-W3','W3-W4'],['u-g','g-r','r-i','i-z','z-W1','W1-W2','W2-W3','W3-W4'],np.arange(8),[-0.49,-0.3,-0.35,-0.6,2.01,0.05,1.8,1.8],[4.49,1.49,0.9,0.95,5.45,1.9,4.99,4.8]):
for ccolor,evqcolor,cband1,cband2,evqband1,evqband2,colorlabel,colorname,i,lb,ub in zip([cug,cgr,cri,ciz,czW1,cW1W2,cW2W3,cW3W4],[ggdug,ggdgr,ggdri,ggdiz,ggdzW1,ggdW1W2,ggdW2W3,ggdW3W4],[cmagu,cmagg,cmagr,cmagi,cmagz,cmagwise1,cmagwise2,cmagwise3],[cmagg,cmagr,cmagi,cmagz,cmagwise1,cmagwise2,cmagwise3,cmagwise4],[bhmagu[ggd],bhmagg[ggd],bhmagr[ggd],bhmagi[ggd],bhmagz[ggd],bhmagwise1[ggd],bhmagwise2[ggd],bhmagwise3[ggd]],[bhmagg[ggd],bhmagr[ggd],bhmagi[ggd],bhmagz[ggd],bhmagwise1[ggd],bhmagwise2[ggd],bhmagwise3[ggd],bhmagwise4[ggd]],['u - g','g - r','r - i','i - z','z - W1','W1 - W2','W2 - W3','W3 - W4'],['u - g','g - r','r - i','i - z','z - W1','W1 - W2','W2 - W3','W3 - W4'],np.arange(8),[-0.49,-0.3,-0.35,-0.59,2.01,0.05,1.8,1.8],[4.49,1.49,0.9,0.95,5.45,1.9,4.99,4.8]):
    #ax=plt.subplot2grid((2,10),(0,6),colspan=4,
    ax1=plt.subplot(gs1[2*i-7*(i/4)])
    ax1.tick_params(which='major',length=8,width=2,labelsize=16)
    ax1.tick_params(which='minor',length=4,width=1.5,labelsize=16)
    plt.axis('on')
    ax1.set_xticks([1,2,3,4])
    ax1.set_xticks([0.5,1.5,2.5,3.5],minor=True)
    if i%4<3:
        ax1.set_xticklabels([])
    else:
        ax1.set_xticklabels(['1','2','3','4'])
    
    if colorname in ['z-W1','W1-W2','W2-W3','W3-W4']:
        gc,gevq=np.where((ccolor>0)&(ccolor<6.8)&(cband1>0)&(cband1<30)&(cband2>0)&(cband2<30))[0],np.where((evqcolor>0)&(evqcolor<6.8)&(evqband1>0)&(evqband1<30)&(evqband2>0)&(evqband2<30))[0]
    else:
        gc,gevq=np.where((cband1>0)&(cband1<30)&(cband2>0)&(cband2<30))[0],np.where((evqband1>0)&(evqband1<30)&(evqband2>0)&(evqband2<30))[0]
    plt.scatter(cz[gc],ccolor[gc],color='silver',marker='.',edgecolor='None')
    plt.scatter(ggdz[gevq],evqcolor[gevq],color='pink',marker='.',edgecolor='None')
    zcens_con,runmed_con=calc_runmed(ccolor[gc],cz[gc],0.125,zmax=3.5,highz=2.2,highwid=0.3)
    zcens_evq,runmed_evq=calc_runmed(evqcolor[gevq],ggdz[gevq],0.125,zmax=3.5,highz=2.2,highwid=0.3)
    plt.plot(zcens_con,runmed_con,c='black',lw=3,label='Control')
    plt.plot(zcens_evq,runmed_evq,c='red',ls='dashed',lw=3,label='EVQ')
    if i%4==3:ax1.set_xlabel('Redshift',fontsize=20)
    ax1.set_ylabel(colorlabel,fontsize=20)
    plt.xlim(0,4.4)
    plt.ylim(lb,ub)
    if i==0: 
        leg=plt.legend(loc='upper left',frameon=False,prop={'size':24})
        for text in leg.get_texts():
            if text.properties()['text']!='EVQ': text.set_color('silver')
            if text.properties()['text']=='EVQ': text.set_color('pink')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/zcolor_plots.6.22.17.png')
