import os
import time
names=np.array(['0910','0910','Cl1324','Cl1324','Cl1324','Cl1604','Cl1604','NEP5281','RXJ1757'])
cnames = np.array(["RXJ0910+5422","RXJ0910+5419",'Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','NEP5281','RXJ1757'])
n_ids = np.array(['acis2227+2452','acis2227+2452','acis9403+9840','acis9404+9836','acis9404+9836','acis6932','acis6932','acis10444+10924','RXJ1757'])
 
xcen=np.array([4010,4656,4091,3915,4667,4012,3946,3886,4100])
ycen=np.array([4360,3975,4920,3447,3623,3415,4600,4114,4352])

rpath = '/home/rumbaugh/ChandraData'

st = time.time()
#for i in range(0,1):
for i in range(1,len(names)):
    print cnames[i]
    #os.system('dmcopy "%s/%s/master/%s.img.500-2000.nops.fits[x=%i:%i,y=%i:%i]" %s/%s/master/%s.cut.5.11.12.fits clob+'%(rpath,names[i],n_ids[i],xcen[i]-250,xcen[i]+250,ycen[i]-250,ycen[i]+250,rpath,names[i],cnames[i]))
    #print time.time()-st
    #os.system("csmooth infile=%s/%s/master/%s.cut.5.11.12.fits outfile=%s/%s/master/%s.csmooth.5.11.12.fits outsigfile=%s/%s/master/%s.csmooth_sig.5.11.12.fits sclmode=compute outsclfile=%s/%s/master/%s.csmooth_scls.5.11.12.fits sclmap='' conmeth=fft conkerneltype=gauss sclmin=INDEF sclmax=INDEF sigmin=4 sigmax=5 clob+"%(rpath,names[i],cnames[i],rpath,names[i],cnames[i],rpath,names[i],cnames[i],rpath,names[i],cnames[i]))
    #print time.time()-st
    os.system("dmstat %s/%s/master/%s.csmooth.5.11.12.fits centroid=yes | tee %s/%s/master/%s.csmooth.centroid.dat"%(rpath,names[i],cnames[i],rpath,names[i],cnames[i]))
    #print time.time()-st
#print "Elapsed time: %i seconds"%(time.time()-st)
#FILE = open('/home/rumbaugh/run.5.11.12.1450.elapsetime.txt','w')
#FILE.write('%f'%(time.time()-st))
#FILE.close()
