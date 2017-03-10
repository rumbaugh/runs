execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.8.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82'),'formats':('|S32','f8','|S8','|S8','i8')},skiprows=1)

good_dbids=crmd['DBID'][np.abs(crmd['drop'])>=1]

plot_DB_lightcurves(good_dbids,'/home/rumbaugh/DR7_CLQ_candidates.lightcurves.3.8.17.pdf',DBdir='/home/rumbaugh/var_database/Y3A1')

outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','MaxDrop','SurvST','SurvEnd','S82','Flag'),'formats':('|S64','f8','|S8','|S8','i8','i8')})

outcr['DatabaseID'],outcr['MaxDrop'],outcr['SurvST'],outcr['SurvEnd'],outcr['S82']=crmd['DBID'],crmd['drop'],crmd['Surv1'],crmd['Surv2'],crmd['S82']
outcr=outcr[np.abs(crmd['drop'])>=1]

np.savetxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',outcr,fmt='%24s %6.3f %4s %4s %i %2i',header='DatabaseID MaxMagDrop SurveyInit SurveyFinal Stripe82 Flag',comments='')
