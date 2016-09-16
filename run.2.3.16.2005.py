execfile('/home/rumbaugh/mkBgRegScript.py')

dum=os.system("ds9 &")

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

for field in ['cl1604']:
    for band in ['soft','hard','full']:
        fitsfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.img'%(field,field,field,band)
        inreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.reg'%(field,field,field,band)
        outreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.bkg'%(field,field,field,band)
        mkBgReg(inreg,outreg,fitsfile=fitsfile,startds9=False)
        dtgts=ds9_targets()
        ds9targ=dtgts[-1][8:]
        d=DS9(ds9targ)
        d.set('regions delete all')
        d.set('regions load %s'%inreg)
        inreg2='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_PS_masks_%s.chandra.reg'%(field,field,field,band)
        d.set('regions save %s'%inreg2)
        cr=np.loadtxt(inreg2,skiprows=3,dtype='|S256')
        np.savetxt(inreg2,cr,fmt='%s')

