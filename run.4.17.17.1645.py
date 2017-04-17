execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.14.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','DBID'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24')})

crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.28.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82'),'formats':('|S32','f8','|S8','|S8','i8')},skiprows=1)

crmd=crmd[crdb['SDSSNAME']!='-1']
crmd=crmd[np.abs(crd['ghi']-crd['glo'])>1]
print len(crmd)
gdbids=np.array(['MQ206171','MQ208717','MQ213230','MQ209259','MQ212075','MQ211918','MQ214934','MQ214802','MQ214532','MQ215548','MQ216346'])
plot_DB_lightcurves(gdbids,'/home/rumbaugh/testSN_lightcurves.4.17.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',zoominband='g',calc_outliers=True,outlier_window=100,load_macleod=True,connectpoints=False)
