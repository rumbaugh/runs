import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/LFC_color_param.py')

crf=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S32')
crpre=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S6')

z=np.linspace(0.1,2,191)
for year in np.arange(1,14):
    gy=np.where(crpre=='graz%02i'%year)[0]
    FILEB=open('/home/rumbaugh/LFC_color_param/LFC_color_param_output_graz%02i_ABlue.dat'%year,'w')
    FILEB.write('# Filename A(Blue):')
    for zi in z: FILEB.write(' %4.2f'%zi)
    FILEB.write('\n')
    FILER=open('/home/rumbaugh/LFC_color_param/LFC_color_param_output_graz%02i_ARed.dat'%year,'w')
    FILER.write('# Filename A(Red): ')
    for zi in z: FILER.write(' %4.2f'%zi)
    FILER.write('\n')
    for SED in crf[gy]:
        curcr=np.loadtxt(SED)
        w,S=np.copy(curcr[:,0]),np.copy(curcr[:,1])
        Ablue,Ared=np.zeros(len(z)),np.zeros(len(z))
        FILEB.write('%s'%(SED))
        FILER.write('%s'%(SED))
        for i in range(0,len(z)): 
            Ablue[i],Ared[i]=find_color_param(w,S,z[i])
            FILEB.write(' %f'%(Ablue[i]))
            FILER.write(' %f'%(Ared[i]))
        FILEB.write('\n')
        FILER.write('\n')
    FILER.close()
    FILEB.close()
