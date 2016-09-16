import numpy as np

for field in ['Cl0023','Cl1324','Cl1604','RXJ1821','RXJ1757']:
    cr=np.loadtxt('/home/rumbaugh/Chandra/old_xray_photcats/%s.xray_phot.soft_hard_full.dat'%field,usecols=[0,1])
    ra,dec=cr[:,0],cr[:,1]
    FILE=open('/home/rumbaugh/Chandra/old_xray_photcats/regions/%s.xray_phot.soft_hard_full.reg'%field,'w')
    FILE.write('# Region file format: DS9 version 4.1\nglobal color=magenta dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    for i in range(0,len(ra)):
        FILE.write('circle(%f,%f,3.00")\n'%(ra[i],dec[i]))
    FILE.close()
