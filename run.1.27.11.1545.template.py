import os
import numpy as np
import time
import gc

execfile("/home/rumbaugh/FindCloseSources.py")

def FindPeaks(imgvals):
    imshp = imgvals.shape
    peaks = np.zeros(0)
    xs,ys = np.zeros(0),np.zeros(0)
    g = np.where(imgvals > (0.4*imgvals.max()+0.6*imgvals.mean()))
    for i in range(0,len(g[0][:])):
    	x = g[0][i]
	y = g[1][i]
	t = imgvals[x][y]
    	sxmax = x + 20
    	if sxmax >= imshp[0]: imshp[0]-1
    	sxmin = x - 20
   	if sxmin < 0: sxmin = 0
        symax = y + 20
        if symax >= imshp[1]: symax = imshp[1]-1
        symin = y-20
        if symin < 0: symin=0
        tt = imgvals[sxmin:sxmax,symin:symax]
        if t >= tt.max(): 
            peaks,xs,ys = np.append(peaks,t),np.append(xs,x),np.append(ys,y)
    return peaks,xs,ys
    

rArr = ['18.83','27.27','35.1']


dataspace2d([1024,1024])
set_model(beta2d.b1 + const2d.C)
b1.xpos = 512
b1.ypos = 512
b1.alpha = 2.064
b1.r0 = 27.27
C.c0 = tempc0

ccArr = [4,5.5,7]


#FILE = open("/home/rumbaugh/COSMOS/analysis/peak.list.Pos_r_27.27.conv_r_" + r + ".c_0.004x" + str(cc) + ".1.16.11.dat","w")
FILE = open("/home/rumbaugh/COSMOS/analysis/FPerroranal/tempname/test.spat.error.1.25.11_temp1.dat","w")
st = time.time()
cc = tempcc
b1.ampl = cc*C.c0
r = tempr
b1.r0 = r
for i in range(0,100):
    fake()
    save_image("AtempP.fits",clobber="yes")
    os.system('aconvolve AtempP.fits conv.tempOP.' + str(r) + '.fits "file:/home/rumbaugh/COSMOS/beta_models/beta.alpha_2.064.r_' + str(r) + '.300x300.fits" edges=wrap method=fft clob+')
    convfile = "conv.tempOP." + str(r) + ".fits"
    imcr = read_file(convfile)
    imgvals = get_piximgvals(imcr)
    gP = np.where(imgvals == imgvals.max())
    dist = m.sqrt((gP[0] - 512)**2 + (gP[1]-512)**2)
    FILE.write('%4i %4i %f\n'%(gP[0],gP[1],dist))
FILE.close()
print time.time()-st

exit()
