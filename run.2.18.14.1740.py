import numpy as np
import spec_simple as ss

def plot_red_and_blue(mask,slit,side,line=1,indir=None,smooth_width=7,ret_of=False):
    clf()
    if indir == None: indir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/'
    titledict = {x: ' line%i'%x for x in np.arange(10)+1}
    linedict = {x: '_line%i'%x for x in np.arange(10)+1}
    titledict[1],linedict[1] = '',''
    w,f,v = np.array([]),np.array([]),np.array([])
    pcol = 'r'
    for color in ['red','blue']:
    #plotfile,title,outfile = '%s/%s/spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(indir,mask,mask,slit,color,side),'%s %s %s %s%s'%(mask,slit,color,side,titledict[line]),'%s/plots/lineplot.%s_%s_%s_%s%s_coadd_bgsub.png'%(indir,mask,slit,color,side,linedict[line])
        if mask == '0435m2':
            plotfile,title,outfile = '%s/0435m2_revised/slits/spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(indir,mask,slit,color,side),'%s %s'%(mask,slit),'%s/0435m2_revised/slits/plots/lineplot.%s_%s_coadd_bgsub.png'%(indir,mask,slit)
        else:
            plotfile,title,outfile = '%s/%s/spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(indir,mask,mask,slit,color,side),'%s %s'%(mask,slit),'%s/%s/plots/lineplot.%s_%s_coadd_bgsub.png'%(indir,mask,mask,slit)
        wt,ft,vt = ss.smooth_boxcar(plotfile,smooth_width,line=line,title=title,output=True,clear=False,plotvar=False,customcolors=pcol)
        w,f,v = np.append(w,wt),np.append(f,ft),np.append(v,vt)
        pcol = 'b'
    if ret_of:
        return w,f,v,outfile
    else:
        return w,f,v
    
        
