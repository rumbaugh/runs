import numpy as np
import pyfits as py
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

mhdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
mdata=mhdu[1].data
mdists=SphDist(mdata['RA_SDSS'],mdata['DEC_SDSS'],mdata['RA_DES'],mdata['DEC_DES'])*60
mdists2=SphDist(mdata['RA_POSS'],mdata['DEC_POSS'],mdata['RA_DES'],mdata['DEC_DES'])*60
print np.max(mdists),np.max(mdists2)

for i in range(0,len(mdata)):
    DBID=mdata['DatabaseID'][i]
    hdu=py.open('/home/rumbaugh/var_database/Y3A1/{}/LC.fits'.format(DBID))
    data=hdu[1].data
    if len(data)>0:
        dists=SphDist(data['RA'],data['DEC'],data["RA"][0],data['DEC'][0])*60
        mdiststmp=SphDist(data['RA'],data['DEC'],mdata["RA_DES"][i],mdata['DEC_DES'][i])*60
        if (np.max(dists)>10)|(np.max(mdiststmp)>10):
            print '\nDBID - {}:'.format(DBID)
            print np.max(dists),np.max(mdiststmp)
    
