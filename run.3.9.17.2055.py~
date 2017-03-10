execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crmd=np.loadtxt('/home/rumbaugh/DR7_CLQ_candidate_flags.dat',dtype={'names':('DBID','drop','flag'),'formats':('|S32','f8','i8')},skiprows=1)

good_dbids=crmd['DBID'][crmd['flag']==1]

plot_DB_lightcurves(good_dbids,'/home/rumbaugh/DR7_CLQ_candidates_cut.lightcurves.3.2.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1')
