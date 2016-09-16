import numpy as np
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")

date='3.6.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

FILERS=open('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.%s.dat'%date,'w')
FILERS.write('# field r-i_intercept slope sigma numsigs\n')
zarr=np.linspace(0.1,2,191)
field='cl1604'
numsigs=2
curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
outfile='%s/%s_clus_CMD_ACS_nofit.%s.dat'%(curdir,field,date)
plotfile='/home/rumbaugh/Chandra/plots/CMD_ACS.nofit.%s_clus.%s.png'%(field,date)
y0,m,sig=makeCMD(field,plotfile=plotfile,outputfile=outfile,dofit=False,ierrmax=99999,useACS=True)
FILERS.write('%12s %6.3f %8.5f %7.4f %i\n'%(field,y0,m,sig,numsigs))
FILERS.close()
