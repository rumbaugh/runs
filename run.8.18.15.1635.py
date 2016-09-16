import numpy as np
import os
import pyfits as py
import copy

os.chdir('/home/rumbaugh/KAST/rusu_run_8.15/Raw')

for i in np.arange(3000,3156):
    infile='r%i.fits'%i
    outfile='r%i_fixedhdr.fits'%i
    cr=py.open(infile)
    hdr=py.getheader(infile)
    data=cr[0].data.copy()
    temphdr=copy.deepcopy(hdr)
    hkeys=np.array(hdr.keys())
    csyind=np.where(hkeys=='CSYER2')[0][0]
    csyind2=np.where(hkeys=='CSYER1')[0][0]
    if csyind2<csyind:csyind=csyind2
    for j in range(0,61): temphdr.pop(csyind)
    py.PrimaryHDU(data,temphdr).writeto(outfile,checksum=True)
