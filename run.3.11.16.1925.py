import numpy as np
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
date='3.11.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

for field in targets:
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    if field=='cl1604':
        crs=np.loadtxt(scat,dtype=ACSspecloaddictwnotes)
    else:
        try:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes)
        except:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
    notes=crs['notes']
    g=np.where(notes=='-')[0]
    print field
    print 'Number of -: %i'%len(g)
