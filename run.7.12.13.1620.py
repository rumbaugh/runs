import pyfits,numpy
import numpy as np
import sys

execfile('/home/rumbaugh/LRIS_files_dict_master.py')

#postive shift means second image is higher than first
shift_dict = {'0435_slit1': {'blue': {'top': 37}, 'red': {'top': 18}}, '0435_slit2': {'blue': {'top': -75}, 'red': {'top': -38}}}

indir = "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/" 

for mask in ['0435_slit3']:
    for color in ['blue','red']:
        for side in ['top']:
            shift = 0
            #shift = shift_dict[mask][color][side]
            dataList = []
            i = 0
            for img in files_dict[mask][color]['images']:
                filesci='%s%s_%s_%s_%i_bgsub.fits'%(indir,mask,color,side,img)
                filevar='%s%s_%s_%s_%i_var.fits'%(indir,mask,color,side,img)
                var = pyfits.open(filevar)[0].data.copy()[0]
                var[numpy.isnan(var)] = 1e30
                sci = pyfits.open(filesci)[0].data.copy()[0]
                if i == 0: scicoadd,varcoadd = numpy.zeros((np.shape(var)[0]-int(numpy.fabs(shift)),np.shape(var)[1])),numpy.zeros((np.shape(var)[0]-int(numpy.fabs(shift)),np.shape(var)[1]))
                for row in range(0,np.shape(varcoadd)[0]):
                    if ((i == 1) & (shift > 0)):
                        scicoadd[row] += sci[row+shift]
                        varcoadd[row] += var[row+shift]
                    elif ((i == 0) & (shift < 0)):
                        scicoadd[row] += sci[row-shift]
                        varcoadd[row] += var[row-shift]
                    else:
                        scicoadd[row] += sci[row]
                        varcoadd[row] += var[row]
                i += 1
            header = pyfits.open(filesci)[0].header.copy()
            outname = "%s%s_%s_%s_coadd_bgsub.fits"%(indir,mask,color,side)
            newfile = pyfits.PrimaryHDU(data=scicoadd,header=header)
            newfile.writeto(outname,clobber=True)
            header = pyfits.open(filevar)[0].header.copy()
            outname = "%s%s_%s_%s_coadd_bgsub.weight.fits"%(indir,mask,color,side)
            newfile = pyfits.PrimaryHDU(data=varcoadd,header=header)
            newfile.writeto(outname,clobber=True)
 

