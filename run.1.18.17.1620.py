import numpy as np
import healpy as hp
import easyaccess as ea
import time

con=ea.connect()

hps='4445, 4446, 4447, 4444, 5130, 5128, 5122, 4439, 4438'
st=time.time()
for i in range(0,1):
    YQ='SELECT * FROM MCARRAS2.Y1A1_HPIX WHERE HPIX in (%s)'%hps
    ydf=con.query_to_pandas(YQ)
mt=time.time()
print 'Y1A1 time taken: %f seconds'%(mt-st)
for i in range(0,1):
    YQ='SELECT * FROM DES_ADMIN.Y3A1_COADD_OBJECT_HPIX WHERE HPIX_16384 in (%s)'%hps
    ydf=con.query_to_pandas(YQ)
et=time.time()

print 'Y3A1 time taken: %f seconds'%(et-mt)
