execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import pyfits as py

clqsize=16

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

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

gmf_dr7=np.where(data['SDSSNAME']!='-1')[0]

#cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','S1','S2','S82','flag'),'formats':('|S24','f8','|S4','|S4','i8','i8')},skiprows=1)

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)


gmf=np.zeros(len(cr),dtype='i8')
for i in range(0,len(gmf)):
    #PDBID=PrimaryDBID_dict[cr['DBID'][i]]
    #gp=np.where(data['DatabaseID']==PDBID)[0]
    gp=np.where(data['DatabaseID']==cr['DBID'][i])[0]
    gmf[i]=gp[0]
medu,medg,medr,medi,medz=data['med_SDSS_u'][gmf],data['med_SDSS_g'][gmf],data['med_SDSS_r'][gmf],data['med_SDSS_i'][gmf],data['med_SDSS_z'][gmf]
medu_all,medg_all,medr_all,medi_all,medz_all=data['med_SDSS_u'][gmf_dr7],data['med_SDSS_g'][gmf_dr7],data['med_SDSS_r'][gmf_dr7],data['med_SDSS_i'][gmf_dr7],data['med_SDSS_z'][gmf_dr7]

crmd=cr[np.abs(cr['drop'])>1]
gmf_md=gmf[np.abs(cr['drop'])>1]

good_dbids=crmd['DBID'][crmd['flag']==0]
extra_good_dbids=crmd['DBID'][(crmd['flag']==0)&(crmd['drop']>1.5)]
extra_extra_good_dbids=crmd['DBID'][(crmd['flag']==0)&(crmd['drop']>2)]

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
gl=np.where(bhdata['LOGLBOL']>0)[0]
bhdata=bhdata[gl]
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
glc=np.where(cdata['LOGLBOL']>0)[0]
cdata=cdata[gl]
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']

ggd=np.zeros(len(good_dbids),dtype='i8')
for i in range(0,len(ggd)): ggd[i]=np.where(bhname==good_dbids[i][5:])[0][0]
gegd=np.zeros(len(extra_good_dbids),dtype='i8')
for i in range(0,len(gegd)): gegd[i]=np.where(bhname==extra_good_dbids[i][5:])[0][0]
geegd=np.zeros(len(extra_extra_good_dbids),dtype='i8')
for i in range(0,len(geegd)): geegd[i]=np.where(bhname==extra_extra_good_dbids[i][5:])[0][0]


execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

plt.figure(1)
plt.clf()
plt.plot(np.sort(np.abs(cr['drop'])),(np.arange(len(cr))+1.)/len(cr),lw=2,color='k')
plt.xlabel('Magnitude Change')
plt.ylabel('Cumulative Fraction')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/MagDropPlot.CLQ_candidates.DR7.3.24.17.png')

plt.figure(1)
plt.clf()
plt.plot(np.sort(cr['Baseline']),(np.arange(len(cr))+1.)/len(cr),lw=2,color='k')
plt.xlabel('Maximum Change Baseline (days)')
plt.ylabel('Cumulative Fraction')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/MaxChangeBaselinePlot.CLQ_candidates.DR7.3.24.17.png')

plt.figure(1)
plt.clf()
plt.scatter(np.abs(cr['drop'][np.abs(cr['drop'])>1]),bhL[ggd])
plt.xlabel('Magnitude Drop')
plt.ylabel(r'$log\left(L_{BOL}\right)$')
#plt.xlim(zmin,zmax)
#plt.ylim(Lmin,Lmax)
plt.xlim(0.99,3.2)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdrop-lum_plot.DR7_CLQ_candidates.3.24.17.png')


execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

plt.figure(1)
plt.clf()
#Lmin,Lmax,zmin,zmax=np.min(bhL),np.max(bhL),np.min(bhz),np.max(bhz)
#tsize=30
#Lbnds,zbnds=np.linspace(Lmin,Lmax,tsize+1),np.linspace(zmin,zmax,tsize+1)
#zcens,Lcens=0.5*(zbnds[:-1]+zbnds[1:]),0.5*(Lbnds[:-1]+Lbnds[1:])
#zsize,Lsize=zcens[1]-zcens[0],Lcens[1]-Lcens[0]
#zL_pairs=np.meshgrid(zcens,Lcens)
#richness=np.zeros(np.shape(zL_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhz,cur_bhL=zL_pairs[0][i][j],zL_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhz-bhz)<=0.5*zsize)&(np.abs(cur_bhL-bhL)<=0.5*Lsize))[0])
plt.scatter(bhz,bhL,s=2,edgecolor='None',marker='.',color='k')
plt.scatter(cz,cL,s=8,edgecolor='None',marker='.',color='b')
#plt.contour(zL_pairs[0],zL_pairs[1],richness,color='k')
plt.scatter(bhz[ggd],bhL[ggd],color='green',s=clqsize)
plt.scatter(bhz[gegd],bhL[gegd],color='magenta',s=clqsize+2)
plt.scatter(bhz[geegd],bhL[geegd],color='red',s=clqsize+4)
plt.xlabel('Redshift')
plt.ylabel(r'$log\left(L_{BOL}\right)$')
#plt.xlim(zmin,zmax)
#plt.ylim(Lmin,Lmax)
plt.xlim(0,3.5)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/L-z_plot.DR7_CLQ_candidates.3.24.17.png')

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')


bhOIII,bhHB,bhFe=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']
bhOIIIorig,bhHBorig,bhFeorig=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']

ggs=np.where((bhHB>0)&(bhFe>0))[0]
bhOIII,bhHB,bhFe=bhOIII[ggs],bhHB[ggs],bhFe[ggs]

plt.figure(1)
plt.clf()
#HBmin,HBmax,Femin,Femax=np.min(bhHB),np.max(bhHB),np.min(bhFe),np.max(bhFe)
#HBmin,HBmax,Femin,Femax=0,10000,0,200
#tsize=30
#HBbnds,Febnds=np.linspace(HBmin,HBmax,tsize+1),np.linspace(Femin,Femax,tsize+1)
#Fecens,HBcens=0.5*(Febnds[:-1]+Febnds[1:]),0.5*(HBbnds[:-1]+HBbnds[1:])
#Fesize,HBsize=Fecens[1]-Fecens[0],HBcens[1]-HBcens[0]
#zHB_pairs=np.zeros((2,tsize**2))
#zHB_pairs[0],zHB_pairs[1]=np.repeat(zcens,len(HBcens)),np.tile(HBcens,len(zcens))
#richness=np.zeros(len(zHB_pairs[0]))
#FeHB_pairs=np.meshgrid(Fecens,HBcens)
#richness=np.zeros(np.shape(FeHB_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhFe,cur_bhHB=FeHB_pairs[0][i][j],FeHB_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhFe-bhFe)<=0.5*Fesize)&(np.abs(cur_bhHB-bhHB)<=0.5*HBsize))[0])
plt.scatter(bhFe,bhHB,s=2,edgecolor='None',marker='.',color='k')
#plt.contour(FeHB_pairs[0],FeHB_pairs[1],richness,color='k')
ggz,gegz,geegz=np.where((bhFeorig[ggd]>0)&(bhHBorig[ggd]>0))[0],np.where((bhFeorig[gegd]>0)&(bhHBorig[gegd]>0))[0],np.where((bhFeorig[geegd]>0)&(bhHBorig[geegd]>0))[0]
plt.scatter(bhFeorig[ggd[ggz]],bhHBorig[ggd[ggz]],color='green',s=clqsize)
plt.scatter(bhFeorig[gegd[gegz]],bhHBorig[gegd[gegz]],color='magenta',s=clqsize+2)
plt.scatter(bhFeorig[geegd[geegz]],bhHBorig[geegd[geegz]],color='red',s=clqsize+4)
plt.xlabel('EW(Fe)')
plt.ylabel(r'FWHM(H$\beta$)')
#plt.xlim(Femin,Femax)
#plt.ylim(HBmin,HBmax)
plt.xlim(0,200)
plt.ylim(0,10000)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/HB-Fe_plot.DR7_CLQ_candidates.3.24.17.png')


plt.figure(1)
plt.clf()
bhri,bhz=medr_all-medi_all,medu_all-medg_all
plt.scatter(medr_all-medi_all,medu_all-medg_all,color='k',s=2,edgecolor='None',marker='.')
#rimin,rimax,zmin,zmax=np.min(medr_all-medi_all),np.max(medr_all-medi_all),np.min(medu_all-medg_all),np.max(medu_all-medg_all)
#tsize=30
#ribnds,zbnds=np.linspace(rimin,rimax,tsize+1),np.linspace(zmin,zmax,tsize+1)
#zcens,ricens=0.5*(zbnds[:-1]+zbnds[1:]),0.5*(ribnds[:-1]+ribnds[1:])
#zsize,risize=zcens[1]-zcens[0],ricens[1]-ricens[0]
#zri_pairs=np.meshgrid(zcens,ricens)
#richness=np.zeros(np.shape(zri_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhz,cur_bhri=zri_pairs[0][i][j],zri_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhz-bhz)<=0.5*zsize)&(np.abs(cur_bhri-bhri)<=0.5*risize))[0])
#plt.contour(zri_pairs[0],zri_pairs[1],richness,color='k')
plt.scatter(medr[np.abs(cr['drop'])>1]-medi[np.abs(cr['drop'])>1],medu[np.abs(cr['drop'])>1]-medg[np.abs(cr['drop'])>1],color='green',s=clqsize/2)
plt.scatter(medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medi[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],color='magenta',s=clqsize/2+2)
plt.scatter(medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medi[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],color='red',s=clqsize/2+4)
plt.xlabel('r-i')
plt.ylabel('u-g')
plt.xlim(-0.5,1.2)
plt.ylim(-0.5,4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/u-g_vs_r-i.DR7_CLQ_candidates.3.24.17.png')


plt.figure(1)
plt.clf()
bhri,bhz=medr_all-medi_all,medu_all-medg_all
plt.scatter(medg_all-medr_all,medu_all-medg_all,color='k',s=2,edgecolor='None',marker='.')
#rimin,rimax,zmin,zmax=np.min(medg_all-medr_all),np.max(medg_all-medr_all),np.min(medu_all-medg_all),np.max(medu_all-medg_all)
#tsize=30
#ribnds,zbnds=np.linspace(rimin,rimax,tsize+1),np.linspace(zmin,zmax,tsize+1)
#zcens,ricens=0.5*(zbnds[:-1]+zbnds[1:]),0.5*(ribnds[:-1]+ribnds[1:])
#zsize,risize=zcens[1]-zcens[0],ricens[1]-ricens[0]
#zri_pairs=np.meshgrid(zcens,ricens)
#richness=np.zeros(np.shape(zri_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhz,cur_bhri=zri_pairs[0][i][j],zri_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhz-bhz)<=0.5*zsize)&(np.abs(cur_bhri-bhri)<=0.5*risize))[0])
#plt.contour(zri_pairs[0],zri_pairs[1],richness)
plt.scatter(medg[np.abs(cr['drop'])>1]-medr[np.abs(cr['drop'])>1],medu[np.abs(cr['drop'])>1]-medg[np.abs(cr['drop'])>1],color='green',s=clqsize/2)
plt.scatter(medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],color='magenta',s=clqsize/2+2)
plt.scatter(medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],color='red',s=clqsize/2+4)
plt.xlabel('g-r')
plt.ylabel('u-g')
plt.xlim(-0.5,1.2)
plt.ylim(-0.5,4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/u-g_vs_g-r.DR7_CLQ_candidates.3.24.17.png')



plt.figure(1)
plt.clf()
bhL,bhug=medr_all-medi_all,medu_all-medg_all
plt.scatter(bhug,bhL,color='k',s=2,edgecolor='None',marker='.')
#ugmin,ugmax,Lmin,Lmax=np.min(medu_all-medg_all),np.max(medu_all-medg_all),np.min(bhL),np.max(bhL)
#tsize=30
#ugbnds,Lbnds=np.linspace(ugmin,ugmax,tsize+1),np.linspace(Lmin,Lmax,tsize+1)
#Lcens,ugcens=0.5*(Lbnds[:-1]+Lbnds[1:]),0.5*(ugbnds[:-1]+ugbnds[1:])
#Lsize,ugsize=Lcens[1]-Lcens[0],ugcens[1]-ugcens[0]
#Lug_pairs=np.meshgrid(ugcens,Lcens)
#richness=np.zeros(np.shape(Lug_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhL,cur_bhug=Lug_pairs[0][i][j],Lug_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhL-bhL)<=0.5*Lsize)&(np.abs(cur_bhug-bhug)<=0.5*ugsize))[0])
#plt.contour(Lug_pairs[0],Lug_pairs[1],richness,color='k')
plt.scatter(medg[np.abs(cr['drop'])>1]-medr[np.abs(cr['drop'])>1],medu[np.abs(cr['drop'])>1]-medg[np.abs(cr['drop'])>1],color='green',s=clqsize/2)
plt.scatter(medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>1.5)],color='magenta',s=clqsize/2+2)
plt.scatter(medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medr[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],medu[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)]-medg[(np.abs(cr['drop'])>1)&(np.abs(cr['drop'])>2)],color='red',s=clqsize/2+4)
plt.xlabel('g-r')
plt.ylabel('u-g')
plt.xlim(-0.5,1.2)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/u-g_vs_L.DR7_CLQ_candidates.3.24.17.png')