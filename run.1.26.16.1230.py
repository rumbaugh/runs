import numpy as np

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

for field in targets:
    for band in ['soft','hard','full']:
        inreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.chandra.reg'%(field,field,field,band)
        try:
            cr=np.loadtxt(inreg,dtype='|S256')
            print 'It worked?'
        except ValueError:
            cr=np.loadtxt(inreg,skiprows=3,dtype='|S256')
            if ((cr[0][0]!='e')&(cr[0][0]!='c')):
                if cr[2]=='physical':
                    print 'What?'
            print 'saving %s'%field
            np.savetxt(inreg,cr[3:],fmt='%s')
        print field,cr[:5]
            
