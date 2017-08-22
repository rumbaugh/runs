import numpy as np
import pyfits as py
import os
import scipy.ndimage.filters as filt

beta=2./3.
rc=180. #kpc

width=100
x,y=np.arange(-width/2,width/2+1),np.arange(-width/2,width/2+1)
xy=np.meshgrid(x,y)
cr=np.loadtxt('/home/rumbaugh/cc_out.1.26.16.dat',dtype={'names':('ID','z','omegaM','omegaVac','H0','age(Gyr)','zage(Gyr)','LTT(Gyr)','comov.rad.dist.(Mpc)','comov.rad.dist.(Gyr)','comov.vol.(Gpc^3)','DA(Mpc)','DA(Gyr)','kpc_DA','DL(Mpc)','DL(Gyr)','DistMod','E(z)','4piDL^2(Gpc^2)','4piDL^2(cm^2)'),'formats':('|S32','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

fields=cr['ID']
kpcDA=cr['kpc_DA']

for i in range(0,len(fields)):
    field=fields[i]
    print field
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    #outfile='%s/betaprofile.z_%.2f.beta_%.2f.rc_%3.0fkpc.fits'%(curdir,cr['z'][i],beta,rc)
    #outerrfile='%s/betaprofile_squared.z_%.2f.beta_%.2f.rc_%3.0fkpc.fits'%(curdir,cr['z'][i],beta,rc)
    outfile='%s/%s_conv.z_%.2f.beta_%.2f.rc_%3.0fkpc.fits'%(curdir,field,cr['z'][i],beta,rc)
    outerrfile='%s/%s_conv_err.z_%.2f.beta_%.2f.rc_%3.0fkpc.fits'%(curdir,field,cr['z'][i],beta,rc)
    rc_as=rc/kpcDA[i]
    kern=(1.+(np.sqrt((xy[0])**2+(xy[1])**2)/(rc_as/0.492))**2)**(-3*beta+0.5)
    kern2=kern**2
    for band in ['soft','hard','full']:
        print band
        infits='%s/%s_full.img'%(curdir,field)
        dum=os.system('cp %s %s/bkup2_%s_full.img'%(infits,curdir,field))
        hdu=py.open(infits)
        data=np.copy(hdu[0].data)
        hdr = hdu[0].header.copy()
        hdu.close()
        conv=filt.convolve(data,kern,mode='constant')
        converr=np.sqrt(filt.convolve(data**2,kern2,mode='constant'))
        py.PrimaryHDU(conv,hdr).writeto(outfile,clobber=True)
        py.PrimaryHDU(conv2,hdr).writeto(outerrfile,clobber=True)
    
