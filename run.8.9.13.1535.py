execfile('/home/rumbaugh/slit_name_dict_master.py')

import os

tdict,tdict2 = {x: ' Line %i'%(x) for x in range(1,10)},{x: '_line%i'%(x) for x in range(1,10)}
tdict[1],tdict2[1] = '',''

for mask in slit_name_dict:
    try:
        os.chdir('%s%s'%(slit_name_dict[mask]['redux_dir'],mask))
        for color in ['red','blue']:
            for side in slit_name_dict[mask][color]:
                for slit in slit_name_dict[mask][color][side]:
                    try:
                        cr = np.loadtxt('spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(mask,slit,color,side))
                        if np.shape(cr)[1] > 3:
                            lines = (np.shape(cr)[1]-1)/2
                            for line in range(1,lines+1):
                                np.savetxt('spec_output/outspec.%s_%s_%i_%s_%s_coadd_bgsub.dat'%(mask,slit,line,color,side),cr[:,[0,2*line-1,2*line]],'%f %f %f')
                    except IOError:
                        pass
    except OSError:
        pass
