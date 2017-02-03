import numpy as np
import easyaccess as ea
import matplotlib.pyplot as plt
con=ea.connect()

try:
    crmd
except NameError:
    crmd=np.loadtxt('/home/rumbaugh/sdssposs_y3a1_match.csv',dtype={'names':('SP_ROWNUM','RA','DEC','HPIX','COADD_OBJECTS_ID'),'formats':('i8','f8','f8','i8','i8')},delimiter=',',skiprows=1)

crm=crmd[crmd['COADD_OBJECTS_ID']!=0]
dists=np.zeros(len(crm))
for i in range(0,len(crm)):
    cid,ra,dec=crm['COADD_OBJECTS_ID'][i],crm['RA'][i],crm['DEC'][i]
    qry='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE COADD_OBJECT_ID=%i'%cid
    DF=con.query_to_pandas(qry)
    dists[i]=np.sqrt((ra-DF['RA'][0])**2+(dec-DF['DEC'][0])**2)

plt.figure(1)
plt.clf()
plt.hist(dists*3600,range=(0,3),bins=30)
plt.savefig('/home/rumbaugh/SP_match_test_y3a1.dist_hist.png')
