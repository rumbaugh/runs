import numpy as np
import pyfits as py

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

data=data[data['SDSSNAME']!='-1']

for band in ['g','r','i','z','Y']:
    print 'Median number of epochs for %s: %f'%(band,np.median(data['Epochs_DES_%s'%band]))
