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
zL_pairs=np.zeros((2,tsize**2))
zL_pairs[0],zL_pairs[1]=np.repeat(zcens,len(Lcens)),np.tile(Lcens,len(zcens))
richness=np.zeros(zL_pairs[0])
for i,z,L in zip(np.arange(len(richness)),zL_pairs[0],zL_pairs[1]):
    richness[i]=len(np.where((np.abs(bhz-z)<=0.5*zsize)&(np.abs(bhL-L)<=0.5*Lsize))[0])
plt.contour(zL_pairs[0],zL_pairs[1],richness)
plt.scatter(bhz[ggd],bhL[ggd],color='r')
plt.scatter(bhz[gegd],bhL[gegd],color='magenta',marker='x')
plt.xlabel('Redshift')
plt.ylabel(r'$log\left(L_{BOL}\right)')
plt.xlim(zmin,zmax)
plt.ylim(Lmin,Lmax)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/L-z_plot.DR7_CLQ_candidates.3.2.17.png')
