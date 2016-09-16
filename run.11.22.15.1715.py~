import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/Imperial.PSFAngle.rows.pdf')


crp=py.open('/home/rumbaugh/Downloads/psftable.fits')
d=crp[1].data
ang=d['PSF95'][:,2]
xin=d['X']
yin=d['Y']
fig=figure(1)
for i in range(0,211):
    fig.clf()
    ax=fig.add_subplot(1,1,1)
    ax.plot(yin[211*i:211*(i+1)],ang[211*i:211*(i+1)])
    ax.scatter(yin[211*i:211*(i+1)],ang[211*i:211*(i+1)],s=6)
    ax.set_xlabel('CCD Y')
    ax.set_ylabel('PSF Angle')
    ax.set_title('CCD X = %.1f'%xin[211*i])
    ax.set_xlim(yin[0]-5,yin[210]+5)
    ax.set_ylim(-5,185)
    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
