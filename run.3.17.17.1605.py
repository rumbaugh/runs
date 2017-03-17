execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','flag'),'formats':('|S32','f8','|S8','|S8','i8','i8')},skiprows=1)

plot_DB_lightcurves(crmd['DBID'],'/home/rumbaugh/DR7_EVQ_lightcurves.3.17.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1',outlierflags=crmd['flag'])
