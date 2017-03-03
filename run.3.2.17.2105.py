execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')

crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.dat',dtype={'names':('DBID','drop'),'formats':('|S32','f8')},skiprows=1)

good_dbids=crmd['DBID'][crmd['drop']>=2]

outcr=np.zeros((len(good_dbids),),dtype={'names':('DBID','MaxDrop','CLQFlag'),'formats':('|S32','f8','i8')})
outcr['DBID'],outcr['MaxDrop']=good_dbids,crmd['drop'][crmd['drop']>=2]
np.savetxt('/home/rumbaugh/DR7_CLQ_candidate_flags.dat',outcr,fmt='%24s %.4f %2i',header='DatabaseID MaxMagDrop Flag',comments='')
