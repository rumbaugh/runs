execfile('/home/rumbaugh/check_Imp_wavdetect_regs.py')
import os

date='1.19.16'


targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

for field in targets[:3]:
    for band in ['soft','hard','full']:
        outreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.reg'%(field,field,field,band)
        os.system('cp /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.reg /home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/bkup_%s_PS_masks_%s.reg'%(field,field,field,band,field,field,field,band))
        crr=np.loadtxt(outreg,dtype='|S128')
        
        np.savetxt(outreg,np.concatenate((['# Region file format: DS9 version 4.1','global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1','fk5'],crr)),fmt='%s')
