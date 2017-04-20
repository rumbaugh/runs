import numpy as np

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

numflagobj,numflags,numgflags=0,0,0
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): 
        continue
    elif np.shape(cr)==():
        if cr['Survey']=='DES':
            if cr['BAND']=='g':
                if cr['FLAG']>3:
                    numflagonj+=1
                    numflags+=1
                    if cr['MAGERR']<0.15:
                        print '%s:\nFlagged good epochs: %i\nFlagged epochs:%i\n'%(DBID,1,1)
                        numgflags+=1
                    else:
                        print '%s:\nFlagged good epochs: %i\nFlagged epochs:%i\n'%(DBID,0,1)
    else:
        g=np.where((cr['Survey']=='DES')&(cr['BAND']=='g'))[0]
        if len(g)>0:
            gflag,ggflag=np.where(cr['FLAG'][g]>3)[0],np.where((cr['FLAG'][g]>3)&(cr['MAGERR'][g]<0.15))[0]
            if len(gflag)>0:
                numflagobj+=1
                numflags+=len(gflag)
                numgflags+=len(ggflag)
                print '%s:\nFlagged good epochs: %i\nFlagged epochs:%i\n'%(DBID,len(ggflag),len(gflag))
