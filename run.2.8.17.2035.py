import numpy as np
cr=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})
outcr2=np.zeros((len(cr),4))
outcr2[:,0],outcr2[:,1],outcr2[:,2],outcr2[:,3]=np.arange(len(cr)),cr['SDR7ID'],cr['ra'],cr['dec']
np.savetxt('/home/rumbaugh/SP_radec.tab',outcr2,fmt='%i %i %f %f',header='NUMROW SDR7ID RA DEC',comments='')
np.savetxt('/home/rumbaugh/SP_radec.csv',outcr2,fmt='%i,%i,%f,%f',header='NUMROW,SDR7ID,RA,DEC',comments='')
