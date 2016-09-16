import numpy as np
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')

def plot_red_and_blue(infile,outfile=None,smooth_width=5,fact=7,xl=(3360,8250),yl=(-200,3200),z=None):
    figure(1)
    figsize(25,8)
    clf()
    w,f,v = np.array([]),np.array([]),np.array([])
    pcol = 'r'
    for color in ['red','blue']:
        print infile[color]
        if color=='blue':
            figure(2)
            wt,ft,vt = smooth_boxcar(infile[color],smooth_width,output=True,clear=False,plotvar=False,customcolors=pcol)
            ft,vt=ft*fact,vt*fact
            figure(1)
            smooth_boxcar(None,smooth_width,w_in=wt,f_in=ft,v_in=vt,output=False,clear=False,plotvar=False,customcolors=pcol)
        else:
            wt,ft,vt = smooth_boxcar(infile[color],smooth_width,output=True,clear=False,plotvar=False,customcolors=pcol)
        w,f,v = np.append(w,wt),np.append(f,ft),np.append(v,vt)
        pcol = 'b'
        xlim(xl)
        ylim(yl)
        figsize(25,8)
        if z!=None:
            mark_spec_absorption(z,w,f)
            mark_spec_emission(z,w,f,showz=False)
    if outfile != None:
        savefig(outfile)
    return w,f,v
    
        
