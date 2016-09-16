import numpy as np
import pyfits as py
import os

obsid_dict={'rcs0224': [4987,3181],'rxj0910':[2227,2452],'cl1604':[6933,7343,6932]}

for field in ['rcs0224','rxj0910','cl1604']:
    os.chdir('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field))
    oid=obsid_dict[field][0]
    crr=py.open('../../raw/%i/primary/acis%i.evt2.fits.gz'%(oid,oid))
    hdur=crr[1]
    hdrr=hdur.header
    for band in ['soft','hard','full']:
        os.system('cp %s_%s.img bkup_%s_%s.img'%(field,band,field,band))
        cr=py.open('%s_%s.img'%(field,band))
        hdu=cr[0]
        hdr=hdu.header
        hdr['DEC_NOM']=hdrr['DEC_NOM']
        hdr['RA_NOM']=hdrr['RA_NOM']
        hdr['DEC_PNT']=hdrr['DEC_PNT']
        hdr['RA_PNT']=hdrr['RA_PNT']
        hdr['ROLL_NOM']=hdrr['ROLL_NOM']
        hdr['ROLL_PNT']=hdrr['ROLL_PNT']
        cr.writeto('%s_%s.hdrmod.img'%(field,band),clobber=True)

