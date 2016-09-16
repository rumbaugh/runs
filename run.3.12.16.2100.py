import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

R95=1#placeholder value
binwid=64

#psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/k_Imp_test.3.7.16.pdf')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','X','Y'),'formats':('|S24','i8','i8')})

crobs=np.loadtxt('/home/rumbaugh/Chandra/obs_properties.dat',dtype={'names':('obsid','field','name','chip','PI','exp','RAh','RAm','RAs','Decd','Decm','Decs','nH'),'formats':('i8','|S12','|S24','|S8','|S24','f8','i8','i8','f8','i8','i8','f8','f8')})

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
FILEGETPSF=open('/home/rumbaugh/runs/run.3.12.16.2100','w')
FILEGETPSF.write("cd /home/rumbaugh/Chandra/ImperialPipeline/ImperialPipe\nexport PSFTAB='/home/rumbaugh/Chandra/ImperialPipeline/ImperialPipe/PSF/psftable.fits'\n")
#fig=figure(1)
ks=np.zeros(len(targets))
for field in targets:
    hdu=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    data=hdu[1].data
    gk=np.where(crk['field']==field)[0][0]
    gobs=np.where(crobs['field']==field)[0]
    exptime=np.sum(crobs['exp'][gobs])*10000.
    g0=np.where(cr0['field']==field)[0][0]
    x0,y0=cr0['X'][g0],cr0['Y'][g0]
    for band in ['soft','hard','full']:
        ktmp=crk['k_%s'%band][gk]
        hduimg=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.img'%(field,field,field,band))
        tmpdimg=hduimg[0].data
        numadd0,numadd1=binwid-np.shape(tmpdimg)[0]%binwid,binwid-np.shape(tmpdimg)[1]%binwid
        dimg=np.append(tmpdimg,np.zeros((numadd0,np.shape(tmpdimg)[1])),axis=0)
        dimg=np.append(dimg,np.zeros((np.shape(dimg)[0],numadd1)),axis=1)
        binimgtmp=dimg.reshape(np.shape(dimg)[0]/binwid,binwid,np.shape(dimg)[0]/binwid,binwid)
        binimg=binimgtmp.sum(axis=3).sum(axis=1)
        physX,physY=x0+np.arange(binwid/2,np.shape(dimg)[0],binwid),y0+np.arange(binwid/2,np.shape(dimg)[0],binwid)
        XYout=np.zeros((np.shape(binimg)[0]**2,3))
        XYout[:,0]=np.arange(0,np.shape(binimg)[0]**2)
        ind1,ind2=np.arange(np.shape(binimg)[0]**2,dtype='i8')%np.shape(binimg)[0],np.arange(np.shape(binimg)[0]**2,dtype='i8')/np.shape(binimg)[0]
        XYout[:,1],XYout[:,2]=physX[ind1],physY[ind2]
        np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/XYout_%s.3.12.16.dat'%(field,field,band),XYout,fmt='%i %i %i')
        if field in ['rcs0224','rxj0910','cl1604']:
            FILEGETPSF.write('./getpsf %s /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/XYout_%s.3.12.16.dat infmt=sky afile=/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.hdrmod.img\nmv getpsfout.dat /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.getpsfout.dat\n'%(band,field,field,band,field,field,field,band,field,field,field,band))
        else:
            FILEGETPSF.write('./getpsf %s /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/XYout_%s.3.12.16.dat infmt=sky afile=/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.img\nmv getpsfout.dat /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.getpsfout.dat\n'%(band,field,field,band,field,field,field,band,field,field,field,band))
        Slim=3*ktmp/exptime*(1+np.sqrt(0.75*binimg*np.pi*R95))#Need to figure out what R95 should really be
#psfpdf.close()    
FILEGETPSF.close()
