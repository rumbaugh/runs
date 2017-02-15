import numpy as np

crmq=np.loadtxt('/home/rumbaugh/milliquas_y3a1_match_wtiles.csv',dtype={'names':('MQ_ROWNUM','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','f8','f8','i8','i8','|S32')},delimiter=',',skiprows=1)
crsp=np.loadtxt('/home/rumbaugh/sdssposs_y3a1_match_wtiles.csv',dtype={'names':('SP_ROWNUM','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','f8','f8','i8','i8','|S32')},delimiter=',',skiprows=1)
crbh=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match_wtiles.csv',dtype={'names':('SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','f8','f8','i8','i8','|S32')},delimiter=',',skiprows=1)

crout=np.zeros((0,),dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S32','|S32','f8','f8','i8','i8','|S32')})

gnm=np.where(crmq['COADD_OBJECTS_ID']==0)[0]
crmqnomatch=np.zeros((len(gnm),),dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S32','|S32','f8','f8','i8','i8','|S32')})
crmqnomatch['SP_ROWNUM'],crmqnomatch['SDSS_NAME']='0','0'
crmqnomatch['MQ_ROWNUM'],crmqnomatch['RA'],crmqnomatch['DEC'],crmqnomatch['TILENAME']=crmq['MQ_ROWNUM'][gnm],crmq['RA'][gnm],crmq['DEC'][gnm],crmq['TILENAME'][gnm]
crout=np.concatenate((crout,crmqnomatch),axis=0)

gnm=np.where(crsp['COADD_OBJECTS_ID']==0)[0]
crspnomatch=np.zeros((len(gnm),),dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S32','|S32','f8','f8','i8','i8','|S32')})
crspnomatch['MQ_ROWNUM'],crspnomatch['SDSS_NAME']='0','0'
crspnomatch['SP_ROWNUM'],crspnomatch['RA'],crspnomatch['DEC'],crspnomatch['TILENAME']=crsp['SP_ROWNUM'][gnm],crsp['RA'][gnm],crsp['DEC'][gnm],crsp['TILENAME'][gnm]
crout=np.concatenate((crout,crspnomatch),axis=0)

gnm=np.where(crbh['COADD_OBJECTS_ID']==0)[0]
crbhnomatch=np.zeros((len(gnm),),dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S32','|S32','f8','f8','i8','i8','|S32')})
crbhnomatch['SP_ROWNUM'],crbhnomatch['MQ_ROWNUM']='0','0'
crbhnomatch['SDSS_NAME'],crbhnomatch['RA'],crbhnomatch['DEC'],crbhnomatch['TILENAME']=crbh['SDSS_NAME'][gnm],crbh['RA'][gnm],crbh['DEC'][gnm],crbh['TILENAME'][gnm]
crout=np.concatenate((crout,crbhnomatch),axis=0)


crmq,crsp,crbh=crmq[crmq['COADD_OBJECTS_ID']>0],crsp[crsp['COADD_OBJECTS_ID']>0],crbh[crbh['COADD_OBJECTS_ID']>0]

cidlist=np.unique(np.concatenate((crmq['COADD_OBJECTS_ID'],crsp['COADD_OBJECTS_ID'],crbh['COADD_OBJECTS_ID'])))

matchcr=np.zeros((len(cidlist),),dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S32','|S32','f8','f8','i8','i8','|S32')})
matchcr['COADD_OBJECTS_ID']=cidlist
matchcr['TILENAME']='None'
matchcr['SDSS_NAME'],matchcr['SP_ROWNUM'],matchcr['MQ_ROWNUM']='0','0','0'

for cid,i in zip(cidlist,np.arange(len(cidlist))):
    gmq,gsp,gbh=np.where(crmq['COADD_OBJECTS_ID']==cid)[0],np.where(crsp['COADD_OBJECTS_ID']==cid)[0],np.where(crbh['COADD_OBJECTS_ID']==cid)[0]
    if len(gsp)>0:
        gsp=gsp[0]
        matchcr['RA'][i],matchcr['DEC'][i],matchcr['HPIX'][i],matchcr['TILENAME'][i]=crsp['RA'][gsp],crsp['DEC'][gsp],crsp['HPIX'][gsp],crsp['TILENAME'][gsp]
        matchcr['SP_ROWNUM'][i]=crsp['SP_ROWNUM'][gsp]
    if len(gbh)>0:
        gbh=gbh[0]
        matchcr['RA'][i],matchcr['DEC'][i],matchcr['HPIX'][i]=crbh['RA'][gbh],crbh['DEC'][gbh],crbh['HPIX'][gbh]
        if matchcr['TILENAME'][i]=='None':matchcr['TILENAME'][i]=crbh['TILENAME'][gbh]
        matchcr['SDSS_NAME'][i]=crbh['SDSS_NAME'][gbh]
    if len(gmq)>0:
        gmq=gmq[0]
        matchcr['RA'][i],matchcr['DEC'][i],matchcr['HPIX'][i]=crmq['RA'][gmq],crmq['DEC'][gmq],crmq['HPIX'][gmq]
        if matchcr['TILENAME'][i]=='None':matchcr['TILENAME'][i]=crmq['TILENAME'][gmq]
        matchcr['MQ_ROWNUM'][i]=crmq['MQ_ROWNUM'][gmq]

outcr=np.concatenate((matchcr,crout),axis=0)
np.savetxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',outcr,fmt='%32s %32s %32s %f %f %i %i %32s',header='MQ_ROWNUM SP_ROWNUM SDSS_NAME RA DEC HPIX COADD_OBJECTS_ID TILENAME',comments='')
