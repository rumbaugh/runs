import numpy as np
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
outputdir='/home/rumbaugh/var_database/Y3A1'
cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.8.17.dat',dtype={'names':('DatabaseID','drop','SI','SF','S82'),'formats':('|S24','f8','|S4','|S4','i8')},skiprows=1)

maxdists=np.zeros(len(cr))

for i,DBID in zip(np.arange(len(cr)),cr['DatabaseID']):
    crlc=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if len(crlc)>0:
        dists=60*SphDist(crlc['RA'][0],crlc['DEC'][0],crlc['RA'],crlc['DEC'])
        maxdists[i]=np.max(dists)


