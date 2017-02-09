import numpy as np

cr=np.loadtxt('/home/rumbaugh/MQ_SDSS_DR13_match_y3a1.csv',skiprows=1,dtype={'names':('numrow','thingid','objid','ra','dec','mjd_g','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},delimiter=',')

crms=np.loadtxt('/home/rumbaugh/milliquas_y3a1_match_only.csv',skiprows=1,delimiter=',',dtype={'names':('numrow','mq_rownum','ra','dec','hpix','cid')})

MQdict={crms['numrow'][x]: crms['mq_rownum'][x] for x in np.arange(len(crms))}
CIDdict={crms['numrow'][x]: crms['cid'][x] for x in np.arange(len(crms))}

outcr=np.zeros(len(cr,),dtype={'names':('numrow','cid','MQ','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
outcr['numrow'],outcr['thingid'],outcr['objid'],outcr['ra'],outcr['dec'],outcr['mjd_g'],outcr['run'],outcr['rerun'],outcr['stripe'],outcr['psfmag_u'],outcr['psfmag_g'],outcr['psfmag_r'],outcr['psfmag_i'],outcr['psfmag_z'],outcr['psfmagerr_u'],outcr['psfmagerr_g'],outcr['psfmagerr_r'],outcr['psfmagerr_i'],outcr['psfmagerr_z']=cr['numrow'],cr['thingid'],cr['objid'],cr['ra'],cr['dec'],cr['mjd_g'],cr['run'],cr['rerun'],cr['stripe'],cr['psfmag_u'],cr['psfmag_g'],cr['psfmag_r'],cr['psfmag_i'],cr['psfmag_z'],cr['psfmagerr_u'],cr['psfmagerr_g'],cr['psfmagerr_r'],cr['psfmagerr_i'],cr['psfmagerr_z']
outcr['ray3a1'],outcr['decy3a1']=0,0
outcr['MQ'],outcr['cid']=np.array([MQdict[x] for x in cr['numrow']]),np.array([CIDdict[x] for x in cr['numrow']])

np.savetxt('/home/rumbaugh/milliquas_lightcurve_entries_SDSS.y3a1.tab',outcr,fmt='%i %i %i %f %f %i %i %f %f %f %i %i %i %f %f %f %f %f %f %f %f %f %f',header='numrow cid MQ ray3a1 decy3a1 objid thingid mjd_g ra dec run rerun stripe psfmag_u psfmag_g psfmag_r psfmag_i psfmag_z psfmagerr_u psfmagerr_g psfmagerr_r psfmagerr_i psfmagerr_z',comments='')
