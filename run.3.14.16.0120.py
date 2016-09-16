import numpy as np
execfile("/home/rumbaugh/makeCMD.py")


execfile("/home/rumbaugh/set_spec_dict.py")


date='3.13.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

FILERS=open('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.%s.dat'%date,'w')
FILERS.write('# field r-i_intercept slope sigma numsigs\n')
zarr=np.linspace(0.1,2,191)

zarr=np.linspace(0.1,2,191)

ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
#ARed[zarr<0.628],ARed[zarr>1/1.794+0.628]=0.424,0
#BRed[zarr<0.628],BRed[zarr>1/1.794+0.628]=0,0.576
#ABlue[zarr<0.679],ABlue[zarr>1/1.824+0.679]=0.45,0
#BBlue[zarr<0.679],BBlue[zarr>1/1.824+0.679]=0,0.55
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}
for field in targets[np.argsort(zlist)]:
    if field[:6] in ['cl1604','cl1324']:
        numsigs=2
    else: 
        numsigs=3
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    outfile='%s/%s_clus_CMD_nofit.%s.dat'%(curdir,field,date)
    plotfile='/home/rumbaugh/Chandra/plots/CMD_comp_color.nofit.%s_clus.%s.png'%(field,date)
    y0,m,sig=makeCMD(field,plotfile=plotfile,outputfile=outfile,dofit=False,param_colors=True,ierrmax=99,param_dict=param_dict,absmags=True)
    FILERS.write('%12s %6.3f %8.5f %7.4f %i\n'%(field,y0,m,sig,numsigs))
FILERS.close()
psfpdf.close()
