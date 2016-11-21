import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])


outputdir='/home/rumbaugh/var_database'
crt=np.loadtxt('/home/rumbaugh/MILLIQUAS_INY1A1TILE.tab',dtype={'names':('SP_ROWNUM','RA','DEC','TILENAME'),'formats':('i8','f8','f8','|S30')},skiprows=1)
cr=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EPOCHG','EPOCHR','EPOCHI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_SDSS','G_SDSS','G_SDSS_ERR','R_SDSS','R_SDSS_ERR','I_SDSS','I_SDSS_ERR'),'formats':('f8','f8','|S2','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S2','f8','f8','|S2','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8')})
#cr=np.loadtxt('MILLIQUAS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
crm=np.loadtxt('MQ_DR13_MATCH_INY1A1TILE.csv',skiprows=1,delimiter=',',dtype={'names':('numrow','thingid','objid','ra','dec','mjd_g','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
IDs=np.unique(crm['numrow'])
gID=IDs-1
cr = np.loadtxt('/home/rumbaugh/MILLIQUAS_INY1A1TILE_WNAME.tab',skiprows=1,dtype={'names':('NUMROW','MQ_ROWNUM','RA','DEC','OBJNAME','TILENAME'),'formats':('i8','i8','f8','f8','|S30','|S30')})
crout=np.zeros(len(gID),dtype={'names':('RA','DEC'),'formats':('f8','f8')})
crout['RA'],crout['DEC']=cr['RA'][gID],cr['DEC'][gID]
np.savetxt('/home/rumbaugh/MQ_Y1A1_POTDOS_RADEC.csv',crout,fmt='%f,%f')
crout2=np.zeros(len(gID),dtype={'names':('name','ra','dec'),'formats':('i8','f8','f8')})
crout2['name'],crout2['ra'],crout2['dec']=IDs,cr['RA'][gID],cr['DEC'][gID]
np.savetxt('/home/rumbaugh/MQ_Y1A1_POTDOS_numrowradec.tab',crout2,fmt='%i %f %f')
