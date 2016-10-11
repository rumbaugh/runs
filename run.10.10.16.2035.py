import numpy as np
import easyaccess as ea
con=ea.connect()

q1="SELECT HPIX FROM MILLIQUAS_HPIX"
DF1=con.query_to_pandas(q1)
hpixs=np.unique(np.array(DF1['HPIX']))

numinpix=np.zeros(len(hpixs),dtype='i8')
for ihp,hpix in zip(np.arange(len(hpixs)),hpixs):
    if hpix!=hpixs[ihp]:
        print 'oops'
        break
    q2='SELECT COUNT(HPIX) FROM MCARRAS2.Y1A1_HPIX WHERE HPIX=%i'%hpix
    DF2=con.query_to_pandas(q2)
    numinpix[ihp]=DF2['COUNT(HPIX)'][0]
outcr=np.zeros((len(hpixs),2))
outcr[:,0],outcr[:,1]=hpixs,numinpix
np.savetxt('/home/rumbaugh/milliquas_num_in_hpix.tab',outcr,fmt='%i %i',header='HPIX NUMINHPIX',comments='')
