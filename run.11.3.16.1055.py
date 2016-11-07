import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
#nside=16384
nside=64
sdict={16:16,64:4}
        
DESbands=np.array(['g','r','i','z','Y'])
SDSSbands=np.array(['u','g','r','i','z'])
    
fname='/home/rumbaugh/Downloads/milliquas.txt'
mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}
delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)
cr=np.genfromtxt(fname,dtype=mdict,delimiter=delims)
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist(cr['Z'][np.isnan(cr['Z'])==False],range=(0,5),bins=20)
plt.savefig('/home/rumbaugh/DBplots/zhist_plot.milliquas_full.png')
