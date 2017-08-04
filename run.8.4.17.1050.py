import numpy as np
import pyfits as py
import pandas as pd

hdu=py.open('/data2/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

badids,dbids,olddbids,flags=np.zeros(0,dtype='i8'),np.zeros(0,dtype='|S30'),np.zeros(0,dtype='|S40'),np.zeros(0,dtype='i8')
for i in range(0,len(data)):
    DBID,oldDBID=data['DatabaseID'][i],data['OldDatabaseID'][i]
    try:
        hdutmp=py.open('/data2/rumbaugh/var_database/Y3A1/{}/LC.fits'.format(DBID))
    except:
        try:
            hdutmp=py.open('/data2/rumbaugh/var_database/Y3A1/{}/LC.fits'.format(oldDBID))
            flags=np.append(flags,0)
        except:
            flags=np.append(flags,-1)
        badids,dbids,olddbids=np.append(badids,i),np.append(dbids,DBID),np.append(olddbids,oldDBID)
df=pd.DataFrame({x:y for x,y in zip(['id','DBID','oldDBID','flag'],[badids,dbids,olddbids,flags])})
df.to_csv('/data2/rumbaugh/badids.csv')
