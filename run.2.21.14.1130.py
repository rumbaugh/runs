import numpy as np

slits = np.array([761,85,324,628,211])

for slit in slits:
    mask = '0435m2'
    if slit == 211: mask = '0435m3'
    for color in ['red','blue']:
        try:
            cr = np.loadtxt('/home/rumbaugh/tmp0435/outspec.%s_%i_%s.dat'%(mask,slit,color))
            FILE = open('/home/rumbaugh/tmp0435/outspec.%s_%i_%s.dat'%(mask,slit,color),'w')
            FILE.write('#wavelength rel_flux flux_err\n')
            for i in range(0,np.shape(cr)[0]):
                FILE.write('%7.2f %9.3f %9.3f\n'%(cr[i][0],cr[i][1],cr[i][2]))
            FILE.close()
        except:
            pass
