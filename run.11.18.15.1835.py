import numpy as np
import os
import psf
import caldb4
cdb = caldb4.Caldb(telescope="CHANDRA", product="REEF")
reef = cdb.search[0]
reef = reef.split('[')[0]
pdata = psf.psfInit(reef)

tfile='/home/rumbaugh/Chandra/7914/temp_tfile.txt'
pfile='/home/rumbaugh/Chandra/7914/temp_pfile.txt'

Ra_aim,Dec_aim=5.9623443990511,4.3820249628906


mdata=np.loadtxt('/home/rumbaugh/Chandra/7914/photometry/7914.xray_phot.soft_hard_full.dat')

mra,mdec=mdata[:,0],mdata[:,1]

for i in range(0,len(mra)):
    ra,dec=mra[i],mdec[i]
    dum=os.system("dmcoords acis7914.img.500-8000.fits opt=cel ra=%s dec=%s asolfile=acis7914.asol.fits.gz"%(ra,dec))
    dum=os.system('pget dmcoords theta >> %s'%tfile)
    dum=os.system('pget dmcoords phi >> %s'%pfile)
    
crp,crt=np.loadtxt(pfile),np.loadtxt(tfile)
FILE=open("/home/rumbaugh/Chandra/7914/chandra_psf_file.7914.dat",'w')
FILE.write("# ra dec theta phi r90_1.497 r90_2.3 r90_4.51 r95_1.497 r95_2.3 r95_4.51\n")
for i in range(0,len(mra)):
    r90_bot=psf.psfSize(pdata,1.25,crt[i],crp[i],0.9)
    r90_soft=psf.psfSize(pdata,1.497,crt[i],crp[i],0.9)
    r90_mid=psf.psfSize(pdata,2.3,crt[i],crp[i],0.9)
    r90_hard=psf.psfSize(pdata,4.51,crt[i],crp[i],0.9)
    r95_bot=psf.psfSize(pdata,1.25,crt[i],crp[i],0.95)
    r95_soft=psf.psfSize(pdata,1.497,crt[i],crp[i],0.95)
    r95_mid=psf.psfSize(pdata,2.3,crt[i],crp[i],0.95)
    r95_hard=psf.psfSize(pdata,4.51,crt[i],crp[i],0.95)
    FILE.write('%9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f\n'%(mra[i],mdec[i],crt[i],crp[i],r90_bot,r90_soft,r90_mid,r90_hard,r95_bot,r95_soft,r95_mid,r95_hard))
FILE.close()

