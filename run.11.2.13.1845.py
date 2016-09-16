import numpy as np
import os

band = ['F390W','F555W','F814W']
infiles = ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J073728.44+321618.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']

#ralist = (7.+(37.+((28.4+np.array([0.04,0.034,0.034]))/60))/60)*360./24
#declist = 32+(16.+(18.6/60))/60*np.ones(3)

ralist = (7.+(37.+((28.4+np.array([0.072,0.05,0.05]))/60))/60)*360./24
declist = 32+(16.+(17+np.array([0.92,2.5,2.5]))/60)/60
sighi = [15., 50., 50.]
execfile('/home/rumbaugh/pythonscripts/make_3panel_mod.py')
