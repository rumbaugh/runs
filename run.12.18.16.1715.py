import numpy as np
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
outputdir='/home/rumbaugh/var_database'
DB_path='/home/rumbaugh/var_database'

#lsdict={'names':('DESJ','rah','ram','ras','decd','decm','decs','tif'),'formats':
#('|S4','i8','i8','f8','i8','i8','f8','|S4')}
#delims=(4,2,2,4,3,2,4,4)
#crls=np.genfromtxt('',dtype=lsdict,delimiter=delims)
#lsfilenames=np.loadtxt('',dtype='|S30')

#crdescutin=np.loadtxt('/home/rumbaugh/radecname_forDEScutouts.csv',delimiter=',DEScutout_DBID_',dtype={'names':('radec','DBID'),'formats':('|S20','i8')})
#crdescutout=np.loadtxt('/home/rumbaugh/descuts/results/12-5-16/matched_12-5-16.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})


#lsras,lsdecs=hms2deg(crls['rah'],crls['ram'],crls['ras']),dms2deg(crls['decd'],crls['decm'],crls['decs'])


crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_sig_DBID.12.18.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

outcr=np.zeros((len(good_dbids),),dtype={'names':('DBID','CID','tID','dr7ID','RA','DEC','Intflag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})
outcr['DBID']=good_dbids
for DBID,i in zip(good_dbids,np.arange(len(good_dbids))):
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    gdes,gsdss,gposs=np.where(survey=='DES')[0],np.where(survey=='SDSS')[0],np.where(survey=='POSS')[0]
    if len(gdes)>0:
        try:
            cid=cr['SurveyCoaddID'][gdes[0]]
        except:
            cid=cr['SurveyCoaddID'][gdes]
        outcr['CID'][i]=cid
    if len(gposs)>0:
        try:
            cid=cr['SurveyCoaddID'][gposs[0]]
        except:
            cid=cr['SurveyCoaddID'][gposs]
        outcr['tID'][i]=cid
    if len(gsdss)>0:
        try:
            cid=cr['SurveyCoaddID'][gsdss[0]]
        except:
            cid=cr['SurveyCoaddID'][gsdss]
        outcr['dr7ID'][i]=cid
    try:
        mRA,mDec=np.median(cr['RA']),np.median(cr['DEC'])
    except:
        mRA,mDec=np.array([cr['RA']])[0],np.array([cr['DEC']])[0]
    outcr['RA'][i],outcr['DEC'][i]=mRA,mDec
np.savetxt('/home/rumbaugh/changinglookAGNcandidates_index.12.18.16.dat',outcr,fmt='%6i %16i %16i %10i %9.5f %9.5f %2i',header='DatabaseID CoaddObjectsID thingid sdr7id RA Dec IntFlag')
