import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

R95=1#placeholder value
binwid=64

psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/cumnetcnts.3.14.16.pdf')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','X','Y'),'formats':('|S24','i8','i8')})

crobs=np.loadtxt('/home/rumbaugh/Chandra/obs_properties.dat',dtype={'names':('obsid','field','name','chip','PI','exp','RAh','RAm','RAs','Decd','Decm','Decs','nH'),'formats':('i8','|S12','|S24','|S8','|S24','f8','i8','i8','f8','i8','i8','f8','f8')})

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
fig=plt.figure(1)
ks=np.zeros(len(targets))
FILE=open('/home/rumbaugh/Chandra/cumnetcnts.3.14.16.dat','w')
FILE.write('# field soft hard full (omega in deg^2)\n')
for field in targets:
    hdu=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    data=hdu[1].data
    gk=np.where(crk['field']==field)[0][0]
    gobs=np.where(crobs['field']==field)[0]
    exptime=np.sum(crobs['exp'][gobs])*10000.
    g0=np.where(cr0['field']==field)[0][0]
    x0,y0=cr0['X'][g0],cr0['Y'][g0]
    FILE.write('%12s'%(field))
    for band in ['soft','hard','full']:
        FILEtmp=open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_cumnetcnts.%s.3.14.16.dat'%(field,field,field,band),'w')
        FILEtmp.write('# ra dec omega NS\n')
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
        ind1,ind2=np.arange(np.shape(binimg)[0]**2,dtype='i8')/np.shape(binimg)[0],np.arange(np.shape(binimg)[0]**2,dtype='i8')%np.shape(binimg)[0]
        XYout[:,1],XYout[:,2]=physX[ind1],physY[ind2]
        np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/XYout_%s.3.12.16.dat'%(field,field,band),XYout,fmt='%i %i %i')
        crpsf=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.getpsfout.dat'%(field,field,field,band))
        A95=np.pi*crpsf[:,18]*crpsf[:,19]
        A95=A95.reshape(np.shape(binimg))
        Slim=3*ktmp/exptime*(1+np.sqrt(0.75*binimg*np.pi*A95/(64.*0.492/.492)**2))
        NS=0.
        zcnt=0
        gord=np.argsort(data['%s%s_flux'%(band[0].upper(),band[1:])])
        guse=np.zeros(0,dtype='i8')
        for i in reversed(gord):
            omega=(64*0.492/3600.)**2*len(Slim[((Slim<=data['%s%s_flux'%(band[0].upper(),band[1:])][i])&(binimg>0))])
            if omega>0:
                NS+=1./omega
                guse=np.append(guse,i)
                FILEtmp.write('%9.5f %9.5f %f %f\n'%(data['RA'][i],data['Dec'][i],omega,NS))
            else:
                zcnt+=1
        print '%s - %s: zero count - %i'%(field,band,zcnt)
        FILE.write(' %f'%NS)
        FILEtmp.close()
        crpt=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_cumnetcnts.%s.3.14.16.dat'%(field,field,field,band),usecols=(1,2,3))
        fig.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        ax=fig.add_subplot(1,1,1)
        ax.scatter(data['%s%s_flux'%(band[0].upper(),band[1:])][guse]*10**15,crpt[:,2],s=6)
        ax.set_xlabel("Flux (10^15 erg/s)")
        ax.set_ylabel("N(<S)")
        ax.set_title('%s - %s'%(field,band))
        xlim=plt.xlim()
        ylim=plt.ylim()
        ax.loglog([100000,100000],[100000,100001])
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        fig.savefig(psfpdf,format='pdf')
    FILE.write('\n')
FILE.close()
psfpdf.close()
