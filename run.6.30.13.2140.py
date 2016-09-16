import numpy as np
import spec_simple as ss
import lris_extract as le
import os

execfile("/home/rumbaugh/slit_name_dict_master.py")

tdict = {1: ''}
tdict2 = {1: ''}
for i in range(1,10): tdict[i+1] = ' Line %i'%(i+1)
for i in range(1,10): tdict2[i+1] = '_line%i'%(i+1)

for mask in ['miki22.f','miki21.f','miki04.f','miki04_B','miki04_A','miki03_B','miki03_A','miki21D.','miki16B.','bc3.file','bc3B.fil','miki21C.','M0744_A','M0744_B','M0417_B','M1115_A','miki10.f','miki22_z','miki21_B','miki16B.']:
    osv = os.chdir('%s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    for color in ['red','blue']:
        if mask == 'miki16B.':
            sides = ['top']
        else:
            sides = ['top','bottom']
        for side in sides:
            for slit in slit_name_dict[mask][color][side]:
                line = 1
                plotfile = 'spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(mask,slit,color,side)
                tmp = np.loadtxt(plotfile)
                numlines = (np.shape(tmp)[1]-1)/2
                for line in range(1,numlines+1):
                    title = '%s G%s %s %s%s'%(mask,slit,color,side,tdict[line])
                    w,f,v = ss.read_spectrum(plotfile,line=line)
                    try:
                        w,f,v = ss.smooth_boxcar(plotfile,10,varwt=True,title=title,line=line,output=True,clear=True)
                        xlim([w[0],w[len(w)-1]])
                        ylbt,yubt = le.sig_clip(f,sigthresh=5.)
                        ylim(ylbt,yubt)
                        savefig('plots/smoothedplot.%s_%s_%s_%s%s_coadd_bgsub.png'%(mask,slit,color,side,tdict2[line]))
                    except:
                        try:
                            w,f,v = ss.smooth_boxcar(plotfile,7,varwt=True,title=title,line=line,output=True,clear=True)
                            xlim([w[0],w[len(w)-1]])
                            ylbt,yubt = le.sig_clip(f,sigthresh=5.)
                            ylim(ylbt,yubt)
                            savefig('plots/smoothedplot.%s_%s_%s_%s%s_coadd_bgsub.png'%(mask,slit,color,side,tdict2[line]))
                        except:
                            pass
                            
