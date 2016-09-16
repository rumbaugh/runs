import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/Imperial.PSFAngle.cols.pdf')


crp=py.open('/home/rumbaugh/Downloads/psftable.fits')
d=crp[1].data
ang=d['PSF95'][:,2]
xin=d['X']
yin=d['Y']
fig=figure(1)
for i in range(0,211):
    fig.clf()
    ax=fig.add_subplot(1,1,1)
    ax.plot(xin[np.arange(0,211*211,211)],ang[np.arange(i,211*211,211)])
    ax.scatter(xin[np.arange(0,211*211,211)],ang[np.arange(i,211*211,211)],s=6)
    ax.set_xlabel('CCD X')
    ax.set_ylabel('PSF Angle')
    ax.set_title('CCD Y = %.1f'%yin[i])
    ax.set_xlim(xin[0]-5,xin[-1]+5)
    ax.set_ylim(-5,185)
    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
