execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.dat',dtype={'names':('DBID','drop'),'formats':('|S32','f8')},skiprows=1)

good_dbids=crmd['DBID'][crmd['drop']>=2]

plot_DB_lightcurves(good_dbids,'/home/rumbaugh/DR7_CLQ_candidates.lightcurves.3.2.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1')
