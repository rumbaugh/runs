import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import os

os.chdir('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/cl0023/proc/cl0023')


hdu=py.open('SRCv1/cl0023_srclist_v1.fits')
data=hdu[1].data

SF,SNC=data['Soft_flux']*10**16,data['Soft_net_cts']
SF,SNC=SF[SF>0],SNC[SF>0]
