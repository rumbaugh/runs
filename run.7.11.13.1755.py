import pyfits,numpy
import numpy as np
import sys


#postive shift means second image is higher than first
shift_dic = {'0435_slit1': {'blue': {'top': 37}, 'red': {'top': 18}}, '0435_slit2': {'blue': {'top': -75}, 'red': {'top': -38}}}

indir = "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/" 
outname = 'test_0435_slit2_blue_top_coadd_bgsub.fits'

mask,color,side = '0435_slit2','blue','top'

shift = -75

#scicoadd,varcoadd=numpy.zeros(1),numpy.zeros(1)
dataList = []
i = 0
for img in [256,257]:
    filesci='%s%s_%s_%s_%i_bgsub.fits'%(indir,mask,color,side,img)
    filevar='%s%s_%s_%s_%i_var.fits'%(indir,mask,color,side,img)
    var = pyfits.open(filevar)[0].data.copy()[0]
    if i == 0:
        scicoadd,varcoadd = numpy.zeros((np.shape(var)[0]-int(numpy.fabs(shift)),np.shape(var)[1])),numpy.zeros((np.shape(var)[0]-int(numpy.fabs(shift)),np.shape(var)[1]))
    var[numpy.isnan(var)] = 1e30
    sci = pyfits.open(filesci)[0].data.copy()[0]
    #sci[numpy.isnan(sci)] = 0
    #if (scicoadd.all() == 0):
    #    scicoadd=numpy.zeros_like(sci)
    #    varcoadd=numpy.zeros_like(sci)
    #scicoadd=scicoadd+sci/var
        
    #dataList.append(sci)
    #varcoadd=varcoadd+var
    for row in range(0,np.shape(varcoadd)[0]):
        if i == 1:
            scicoadd[row] += sci[row]
            varcoadd[row] += var[row]
        else:
            scicoadd[row] += sci[row-shift]
            varcoadd[row] += var[row-shift]
    i += 1
#final = scicoadd/varcoadd
#final = numpy.median(numpy.array(dataList), axis=0)
header = pyfits.open(filevar)[0].header.copy()
outname = indir+outname+"_coadd.fits"
newfile = pyfits.PrimaryHDU(data=scicoadd,header=header)
newfile.writeto(outname,clobber=True)
 

