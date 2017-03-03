execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crmd=np.loadtxt('/home/rumbaugh/DR7_CLQ_candidate_flags.dat',dtype={'names':('DBID','drop','flag'),'formats':('|S32','f8','i8')},skiprows=1)

good_dbids=crmd['DBID'][crmd['flag']>0]
extra_good_dbids=crmd['DBID'][crmd['flag']>1]

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
gl=np.where(bhdata['LOGLBOL']>0)[0]
bhdata=bhdata[gl]
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']

ggd=np.zeros(len(good_dbids),dtype='i8')
for i in range(0,len(ggd)): ggd[i]=np.where(bhname==good_dbids[i][5:])[0][0]
gegd=np.zeros(len(extra_good_dbids),dtype='i8')
for i in range(0,len(gegd)): gegd[i]=np.where(bhname==extra_good_dbids[i][5:])[0][0]


execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

plt.figure(1)
plt.clf()
Lmin,Lmax,zmin,zmax=np.min(bhL),np.max(bhL),np.min(bhz),np.max(bhz)
tsize=30
Lbnds,zbnds=np.linspace(Lmin,Lmax,tsize+1),np.linspace(zmin,zmax,tsize+1)
zcens,Lcens=0.5*(zbnds[:-1]+zbnds[1:]),0.5*(Lbnds[:-1]+Lbnds[1:])
zsize,Lsize=zcens[1]-zcens[0],Lcens[1]-Lcens[0]
#zL_pairs=np.zeros((2,tsize**2))
#zL_pairs[0],zL_pairs[1]=np.repeat(zcens,len(Lcens)),np.tile(Lcens,len(zcens))
#richness=np.zeros(len(zL_pairs[0]))
zL_pairs=np.meshgrid(zcens,Lcens)
richness=np.zeros(np.shape(zL_pairs[0]))
for i in np.arange(tsize):
    for j in np.arange(tsize):
        cur_bhz,cur_bhL=zL_pairs[0][i][j],zL_pairs[1][i][j]
        richness[i][j]=len(np.where((np.abs(cur_bhz-bhz)<=0.5*zsize)&(np.abs(cur_bhL-bhL)<=0.5*Lsize))[0])
plt.contour(zL_pairs[0],zL_pairs[1],richness)
plt.scatter(bhz[ggd],bhL[ggd],color='r',s=48)
plt.scatter(bhz[gegd],bhL[gegd],color='magenta',marker='x',s=64)
plt.xlabel('Redshift')
plt.ylabel(r'$log\left(L_{BOL}\right)$')
#plt.xlim(zmin,zmax)
#plt.ylim(Lmin,Lmax)
plt.xlim(0,3.5)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/L-z_plot.DR7_CLQ_candidates.3.2.17.png')

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')


bhOIII,bhHB,bhFe=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']
bhOIIIorig,bhHBorig,bhFeorig=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']

ggs=np.where((bhHB>0)&(bhFe>0))[0]
bhOIII,bhHB,bhFe=bhOIII[ggs],bhHB[ggs],bhFe[ggs]

plt.figure(1)
plt.clf()
HBmin,HBmax,Femin,Femax=np.min(bhHB),np.max(bhHB),np.min(bhFe),np.max(bhFe)
tsize=30
HBbnds,Febnds=np.linspace(HBmin,HBmax,tsize+1),np.linspace(Femin,Femax,tsize+1)
Fecens,HBcens=0.5*(Febnds[:-1]+Febnds[1:]),0.5*(HBbnds[:-1]+HBbnds[1:])
Fesize,HBsize=Fecens[1]-Fecens[0],HBcens[1]-HBcens[0]
#zHB_pairs=np.zeros((2,tsize**2))
#zHB_pairs[0],zHB_pairs[1]=np.repeat(zcens,len(HBcens)),np.tile(HBcens,len(zcens))
#richness=np.zeros(len(zHB_pairs[0]))
FeHB_pairs=np.meshgrid(Fecens,HBcens)
richness=np.zeros(np.shape(FeHB_pairs[0]))
for i in np.arange(tsize):
    for j in np.arange(tsize):
        cur_bhFe,cur_bhHB=FeHB_pairs[0][i][j],FeHB_pairs[1][i][j]
        richness[i][j]=len(np.where((np.abs(cur_bhFe-bhFe)<=0.5*Fesize)&(np.abs(cur_bhHB-bhHB)<=0.5*HBsize))[0])
plt.contour(FeHB_pairs[0],FeHB_pairs[1],richness)
plt.scatter(bhFeorig[ggd],bhHBorig[ggd],color='r',s=48)
plt.scatter(bhFeorig[gegd],bhHBorig[gegd],color='magenta',marker='x',s=64)
plt.xlabel('Redshift')
plt.ylabel(r'$log\left(HB_{BOHB}\right)$')
#plt.xlim(Femin,Femax)
#plt.ylim(HBmin,HBmax)
plt.xlim(0,1000)
plt.ylim(0,10000)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/HB-Fe_plot.DR7_CLQ_candidates.3.2.17.png')
