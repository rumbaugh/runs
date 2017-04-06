execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pyfits as py
import time

clqsize=16

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
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

#cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','S1','S2','S82','flag'),'formats':('|S24','f8','|S4','|S4','i8','i8')},skiprows=1)

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
cr=cr[gdr]
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

crmd=cr[np.abs(cr['drop'])>1]
gmf_md=gmf[np.abs(cr['drop'])>1]

good_dbids=crmd['DBID'][np.abs(crmd['drop'])>1]
gooddrops=np.abs(crmd['drop'])[np.abs(crmd['drop'])>1]

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

plt.figure(1)
plt.clf()
bhgr,bhug=bhmagg-bhmagr,bhmagu-bhmagg
cgr,cug=cmagg-cmagr,cmagu-cmagg
ggdgr,ggdug=bhmagg[ggd]-bhmagr[ggd],bhmagu[ggd]-bhmagg[ggd]
gegdgr,gegdug=bhmagg[gegd]-bhmagr[gegd],bhmagu[gegd]-bhmagg[gegd]
geegdgr,geegdug=bhmagg[geegd]-bhmagr[geegd],bhmagu[geegd]-bhmagg[geegd]
con_pairs,con_richness=calc_contour(cgr,cug,-0.25,1,-0.4,1.25,subdivisions=2,tsize=consize+1)
evq_pairs,evq_richness=calc_contour(ggdgr,ggdug,-0.25,1,-0.4,1.25,subdivisions=2,tsize=consize)
Ccon=plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b')
Cevq=plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r')
plt.clf()
conlevels,evqlevels=np.arange(Ccon.levels[0],Ccon.levels[-2]+0.001,(Ccon.levels[-2]-Ccon.levels[0])/(nlevels-1)),np.arange(Cevq.levels[0],Cevq.levels[-2]+0.001,(Cevq.levels[-2]-Cevq.levels[0])/(nlevels-1))
#plt.scatter(bhgr,bhug,color='k',s=1,edgecolor='None',marker='.')
plt.scatter(cgr,cug,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdgr,ggdug,color='red',s=gdsize,edgecolor='None',marker='.')
plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b',levels=conlevels)
plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r',levels=evqlevels)
#plt.scatter(gegdgr,gegdug,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
#plt.scatter(geegdgr,geegdug,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.xlabel(r'$g-r$')
plt.ylabel(r'$u-g$')
plt.xlim(-0.25,1)
plt.ylim(-0.4,1.25)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/u-g_vs_g-r.DR7_CLQ_candidates.3.25.17.png')

plt.figure(1)
plt.clf()
bhri,bhgr=bhmagr-bhmagi,bhmagg-bhmagr
cri,cgr=cmagr-cmagi,cmagg-cmagr
ggdri,ggdgr=bhmagr[ggd]-bhmagi[ggd],bhmagg[ggd]-bhmagr[ggd]
gegdri,gegdgr=bhmagr[gegd]-bhmagi[gegd],bhmagg[gegd]-bhmagr[gegd]
geegdri,geegdgr=bhmagr[geegd]-bhmagi[geegd],bhmagg[geegd]-bhmagr[geegd]
#plt.scatter(bhri,bhgr,color='k',s=1,edgecolor='None',marker='.')
con_pairs,con_richness=calc_contour(cgr,cri,-0.25,0.65,-0.225,0.8,subdivisions=2,tsize=consize+1)
evq_pairs,evq_richness=calc_contour(ggdgr,ggdri,-0.25,0.65,-0.225,0.8,subdivisions=2,tsize=consize)
Ccon=plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b')
Cevq=plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r',levels=evqlevels)
plt.clf()
conlevels,evqlevels=np.arange(Ccon.levels[0],Ccon.levels[-2]+0.001,(Ccon.levels[-2]-Ccon.levels[0])/(nlevels-1)),np.arange(Cevq.levels[0],Cevq.levels[-2]+0.001,(Cevq.levels[-2]-Cevq.levels[0])/(nlevels-1))
plt.scatter(cri,cgr,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdri,ggdgr,color='red',s=gdsize,edgecolor='None',marker='.')
plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b',levels=conlevels)
plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r',levels=evqlevels)
#plt.scatter(gegdri,gegdgr,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
#plt.scatter(geegdri,geegdgr,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.xlabel(r'$g-r$')
plt.ylabel(r'$r-i$')
plt.xlim(-0.25,0.65)
plt.ylim(-0.225,0.8)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/r-i_vs_g-r.DR7_CLQ_candidates.3.25.17.png')


plt.figure(1)
plt.clf()
bhW1W2,bhrW1=bhmagwise1-bhmagwise2,bhmagr-bhmagwise1
cW1W2,crW1=cmagwise1-cmagwise2,cmagr-cmagwise1
ggdW1W2,ggdrW1=bhmagwise1[ggd]-bhmagwise2[ggd],bhmagr[ggd]-bhmagwise1[ggd]
gegdW1W2,gegdrW1=bhmagwise1[gegd]-bhmagwise2[gegd],bhmagr[gegd]-bhmagwise1[gegd]
geegdW1W2,geegdrW1=bhmagwise1[geegd]-bhmagwise2[geegd],bhmagr[geegd]-bhmagwise1[geegd]
con_pairs,con_richness=calc_contour(cW1W2,crW1,0.1,1.75,2.25,6.25,subdivisions=2,tsize=consize+1)
evq_pairs,evq_richness=calc_contour(ggdW1W2,ggdrW1,0.1,1.75,2.25,6.25,subdivisions=2,tsize=consize)
Ccon=plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b')
Cevq=plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r')
#plt.scatter(bhW1W2,bhrW1,color='k',s=1,edgecolor='None',marker='.')
conlevels,evqlevels=np.arange(Ccon.levels[0],Ccon.levels[-2]+0.001,(Ccon.levels[-2]-Ccon.levels[0])/(nlevels-1)),np.arange(Cevq.levels[0],Cevq.levels[-2]+0.001,(Cevq.levels[-2]-Cevq.levels[0])/(nlevels-1))
plt.clf()
plt.scatter(cW1W2,crW1,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdW1W2,ggdrW1,color='red',s=gdsize,edgecolor='None',marker='.')
#plt.scatter(gegdW1W2,gegdrW1,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
#plt.scatter(geegdW1W2,geegdrW1,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.contour(con_pairs[0],con_pairs[1],con_richness,ls='dashed',colors='b',levels=conlevels)
plt.contour(evq_pairs[0],evq_pairs[1],evq_richness,colors='r',levels=evqlevels)
plt.xlabel('W1-W2')
plt.ylabel(r'$r-$W1')
plt.xlim(0.1,1.75)
plt.ylim(2.25,6.25)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/W1-W2_vs_r-W1.DR7_CLQ_candidates.3.25.17.png')

cug,cgr,cri,ciz,czW1,cW1W2,cW2W3,cW3W4=cmagu-cmagg,cmagg-cmagr,cmagr-cmagi,cmagi-cmagz,cmagz-cmagwise1,cmagwise1-cmagwise2,cmagwise2-cmagwise3,cmagwise3-cmagwise4
ggdug,ggdgr,ggdri,ggdiz,ggdzW1,ggdW1W2,ggdW2W3,ggdW3W4=bhmagu[ggd]-bhmagg[ggd],bhmagg[ggd]-bhmagr[ggd],bhmagr[ggd]-bhmagi[ggd],bhmagi[ggd]-bhmagz[ggd],bhmagz[ggd]-bhmagwise1[ggd],bhmagwise1[ggd]-bhmagwise2[ggd],bhmagwise2[ggd]-bhmagwise3[ggd],bhmagwise3[ggd]-bhmagwise4[ggd]
ggdz=bhz[ggd]


def calc_runmed(color,z,width,divisions=100,zmin=None,zmax=None):
    if zmin==None: zmin=np.min(z)
    if zmax==None: zmax=np.max(z)
    zcens=np.linspace(zmin,zmax,divisions)
    runmed=np.zeros(len(zcens))
    for i in range(0,len(zcens)):
        runmed[i]=np.median(color[np.abs(z-zcens[i])<width])
    return zcens,runmed
#matplotlib.rcParams['figure.figsize']=[16,18]
matplotlib.rcParams['axes.linewidth']=3
gs1=gs.GridSpec(4,2)
gs1.update(hspace=0)
plt.figure(figsize=(16,24))
plt.clf()
for ccolor,evqcolor,colorlabel,colorname,i in zip([cug,cgr,cri,ciz,czW1,cW1W2,cW2W3,cW3W4],[ggdug,ggdgr,ggdri,ggdiz,ggdzW1,ggdW1W2,ggdW2W3,ggdW3W4],['$u-g$','$g-r$','$r-i$','$i-z$','$z-$W1','W1-W2','W2-W3','W3-W4'],['u-g','g-r','r-i','i-z','z-W1','W1-W2','W2-W3','W3-W4'],np.arange(8)):
    #ax=plt.subplot2grid((2,10),(0,6),colspan=4,
    ax1=plt.subplot(gs1[2*i-7*(i/4)])
    ax1.tick_params(which='major',length=8,width=2,labelsize=14)
    ax1.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.axis('on')
    if i%4<3: ax1.set_xticklabels([])
    if colorname in ['z-W1','W1-W2','W2-W3','W3-W4']:
        gc,gevq=np.where((ccolor>0)&(ccolor<6.8))[0],np.where((evqcolor>0)&(evqcolor<6.8))[0]
    else:
        gc,gevq=np.arange(len(ccolor)),np.arange(len(evqcolor))
    plt.scatter(cz[gc],ccolor[gc],color='k',marker='.',edgecolor='None')
    plt.scatter(ggdz[gevq],evqcolor[gevq],color='red',marker='.',edgecolor='None')
    zcens_con,runmed_con=calc_runmed(ccolor[gc],cz[gc],0.25,zmax=3.5)
    zcens_evq,runmed_evq=calc_runmed(evqcolor[gevq],ggdz[gevq],0.25,zmax=3.5)
    plt.plot(zcens_con,runmed_con,c='cyan',ls='dashed',lw=2)
    plt.plot(zcens_evq,runmed_evq,c='pink',ls='dashed',lw=2)
    if i%4==3:ax1.set_xlabel('Redshift',fontsize=16)
    ax1.set_ylabel(colorlabel,fontsize=16)
    plt.xlim(0,4.4)
    plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/zcolor_plots.4.6.17.png')
