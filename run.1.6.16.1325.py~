import numpy as np
import pyfits as py

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1053","rxj1716"])

basedir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE'

for target in targets[:-2]:
    curdir='%s/%s/proc/%s'%(basedir,target,target)
    infile='%s/SRCv1/%s_srclist_v1.fits'%(curdir,target)
    outfile='%s/%s_xray_phot.dat'%(curdir,target)
    hdu=py.open(infile)
    data=hdu[1].data
    raX,decX,netcnts_corrX_soft,netcnts_corrX_hard,netcnts_corrX_full=data['RA'],data['Dec'],data['Soft_net_cts'],data['Hard_net_cts'],data['Full_net_cts']
    dataout=np.zeros((len(raX),5))
    dataout[:,0],dataout[:,1],dataout[:,2],dataout[:,3],dataout[:,4]=raX,decX,netcnts_corrX_soft,netcnts_corrX_hard,netcnts_corrX_full
    np.savetxt(outfile,dataout,fmt='%f %f %E %E %E')
