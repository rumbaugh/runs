import pyfits as py
import numpy as np

bands=['g','r','i','z']

SNfields=np.array(['C1','C2','C3','E1','E2','S1','S2','X1','X2','X3'])
outcr=np.zeros((0,),dtype={'names':('COADD_OBJECT_ID','RA','DEC','MJD','MAG_PSF','MAG_PSF_ERROR','MAG_AUTO','MAG_AUTO_ERROR','BAND','SN_FIELD','FLAGS'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','|S4','|S4','i8')})
np.savetxt('/home/rumbaugh/Eric_LC_Y3A1_abridged.tab',outcr,header='COADD_OBJECT_ID RA DEC MJD MAG_PSF MAG_PSF_ERROR BAND FLAGS',comments='')

for SN in SNfields:
    FILE=open('/home/rumbaugh/runs/run.3.6.17.1810_%s.py'%SN,'w')
    FILE.write('import numpy as np\nimport pyfits as py\nSN=%s\n'%SN)
    FILE.write("bands=['g','r','i','z']")
    FILE.write('\n')
    FILE.write("hdu=py.open('/home/rumbaugh/%s_lc.fits'%SN)")
    FILE.write('\n')
    FILE.write("data=hdu[1].data")
    FILE.write('\n')
    FILE.write("outcr_dict= {b: np.zeros((len(data)*np.shape(data['LC_MJD_%s'%b.upper()])[1],),dtype={'names':('COADD_OBJECT_ID','RA','DEC','MJD','MAG_PSF','MAG_PSF_ERROR','BAND','FLAGS'),'formats':('i8','f8','f8','f8','f8','f8','|S4','i8')}) for b in bands}")
    FILE.write('\n')
    FILE.write("for b in bands:")
    FILE.write('\n')
    FILE.write("    outcr_dict[b]['BAND']=b")
    FILE.write('\n')
    FILE.write("    outcr_dict[b]['COADD_OBJECT_ID'],outcr_dict[b]['RA'],outcr_dict[b]['DEC'],outcr_dict[b]['FLAGS'] = np.repeat(data['COADD_OBJECT_ID'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['RA'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['DEC'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['FLAGS_%s'%b.upper()],np.shape(data['LC_MJD_%s'%b.upper()])[1])")
    FILE.write('\n')
    FILE.write("    outcr_dict[b]['MJD'],outcr_dict[b]['MAG_PSF'],outcr_dict[b]['MAG_PSF_ERROR']=data['LC_MJD_%s'%b.upper()].flatten(),data['LC_MAG_PSF_%s'%b.upper()].flatten(),data['LC_MAGERR_PSF_%s'%b.upper()].flatten()")
    FILE.write('\n')
    FILE.write("    outcr_dict[b]=outcr_dict[b][outcr_dict[b]['MJD']!=0]")
    FILE.write('\n')
    FILE.write("outcr=np.concatenate((outcr_dict['g'],outcr_dict['r'],outcr_dict['i'],outcr_dict['z']),axis=0)")
    FILE.write('\n')
    FILE.write("np.savetxt('/home/rumbaugh/Eric_LC_%s.tab'%SN,outcr,fmt='%i %f %f %f %f %f %4s %i')")
    FILE.close()
