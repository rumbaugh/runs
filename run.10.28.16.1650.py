import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
#nside=16384
nside=64

cr=np.loadtxt('milliquas_y1a1_match.tab',dtype={'names':('MQ','ra','dec','hpix','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1)
hpix=hp.ang2pix(nside,(90-cr['dec'])*np.pi/180.,cr['ra']*np.pi/180)
b=np.bincount(hpix)
hpixb=np.nonzero(b)
b,hpixb=b[b>0],hpixb[0]


HPang=np.array(hp.pix2ang(nside,hpixb))
HPra,HPdec=HPang[1]*180/np.pi,90-HPang[0]*180/np.pi
opacs=b*0.5/np.max(b)
for ra,dec,op in zip(HPra,HPdec,opacs): scatter(ra,dec,color='b',s=2,alpha=op)
