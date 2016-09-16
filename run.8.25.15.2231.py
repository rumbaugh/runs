import numpy as np
import pyfits as py
import copy
import os
os.chdir('/home/rumbaugh/KAST/Science')
execfile('/home/rumbaugh/KAST/FindCosmicRays.py')
crls = np.loadtxt('/home/rumbaugh/KAST/Science/sci_fits_list.txt',dtype='string')
stepsize=21

for i in range(0,len(crls)):
    if len(crls[i]) == 13:
        color=crls[i][4]
        num = crls[i][5:8]
        outmask='CRmask_transpose-%s%s.skysub.fits'%(color,num)
        infile='transpose_sci-%s%s.skysub.fits'%(color,num)
        FindCosmicRays(infile,outmask,stepsize)
        outmask='CRmask-%s%s.skysub.fits'%(color,num)
        FindCosmicRays(infile,outmask,stepsize,transpose=True)
