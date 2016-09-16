import numpy as np
from pycrates import read_file
from coords.chandra import cel_to_chandra


execfile('/home/rumbaugh/set_spec_dict.py')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])


for field in targets:
    if field=='cl1604':
        crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=ACSspecloaddict)
    else:
        crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    gq=np.where((crs['Q']==-1)|(crs['Q']>2.5))[0]
    XYout=np.zeros((len(gq),2))
    try:
        myfile=read_file('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_full.hdrmod.img'%(field,field,field))
    except:
        myfile=read_file('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_full.img'%(field,field,field))
    key_names=myfile.get_keynames()
    key_vals=[ myfile.get_key_value(x) for x in key_names ]
    keywords = dict(zip(key_names, key_vals ))
    for i in range(0,len(gq)):
        tmpXY=cel_to_chandra(keywords,crs['ra'][gq[i]],crs['dec'][gq[i]])
        XYout[i][0],XYout[i][1]=tmpXY['x'][0],tmpXY['y'][0]
    np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_XY_speccoords.dat'%(field,field,field),XYout,fmt='%f %f')
