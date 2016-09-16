import numpy as np
execfile("/home/rumbaugh/makeCMD.py")

date='2.8.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

FILERS=open('/home/rumbaugh/Chandra/RS_fits.%s.dat'%date,'w')
FILERS.write('# field r-i_intercept slope sigma numsigs\n')

for field in targets[0:-2]:
    if field[:6] in ['cl1604','cl1324']:
        numsigs=2
    else: 
        numsigs=3
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    outfile='%s/%s_clus_CMD.%s.dat'%(curdir,field,date)
    plotfile='%s/%s_clus_CMD.%s.png'%(curdir,field,date)
    y0,m,sig=makeCMD(field,plotfile=plotfile,outputfile=outfile)
    FILERS.write('%12s %6.3f %8.5f %7.4f %i\n'%(field,y0,m,sig,numsigs))
FILERS.close()
