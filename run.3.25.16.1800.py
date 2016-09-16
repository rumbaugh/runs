import numpy as np
execfile('/home/rumbaugh/set_spec_dict.py')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

for field in targets: 
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    print '%s - %.2f & %.2f & %.2f \n Members: %i\n'%(field,spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2],len(gq))
