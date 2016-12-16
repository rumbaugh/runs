import numpy as np
import os

cr=np.loadtxt('/home/rumbaugh/MQ_SDSS_platemjdfiber.csv',delimiter=',',dtype='i8')

outcr=np.zeros(np.shape(cr)[0],dtype='|S120')
for i in range(0,len(outcr)):
    if cr[i][0]<1963:
        redux='26'
    elif cr[i][0]<3140:
        redux='103'
    elif cr[i][0]<4190:
        redux='104'
    else:
        redux='v5_7_0'
    outcr[i]='wget https://dr12.sdss.org/sas/dr12/sdss/spectro/redux/%s/spectra/%i/spec-%i-%i-%i.fits'%(redux,cr[i][0],cr[i][0],cr[i][1],cr[i][2])
np.savetxt('/home/rumbaugh/runs/run.12.16.16.1730.sh',outcr,fmt='|S200')
os.system('chmod +x /home/rumbaugh/runs/run.12.16.16.1730.sh')
