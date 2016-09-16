import numpy as np

fields=['cl0023','rxj1716']

netcnts=np.zeros(2)

for s in [1,2]:
    srccnts,bkgcnts=0.,0.
    srcarea,bkgarea=0.,0.
    for field in fields:
        load_data('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_full.img'%(field,field,field))
        cr=np.loadtxt('/home/rumbaugh/sample%i_%s.phys_cut.w_PSF.reg'%(s,field),skiprows=2,dtype='|S256')
        FILE=open('/home/rumbaugh/sample%i_%s.phys_bkg.w_PSF.reg'%(s,field),'w')
        FILE.write('physical\n')
        for i in range(0,len(cr)):
            tmpstr=cr[i].split(' #')
            srccnts+=calc_data_sum2d(tmpstr[0])
        load_data('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_full_nops.img'%(field,field,field))
        for i in range(0,len(cr)):
            tmpstr=cr[i].split(' #')
            tmpstr=tmpstr[0].split(',')
            tmpra,tmpangle=tmpstr[0].split('('),tmpstr[4].split(')')
            ra,dec,rA,rB,ang=float(tmpra[1]),float(tmpstr[1]),float(tmpstr[2]),float(tmpstr[3]),float(tmpangle[0])
            srcarea+=np.pi*rA*rB
            annA_inner,annA_outer,annB_inner,annB_outer=rA*1.5,rA*2.5,rB*1.5,rB*2.5
            bkgarea+=np.pi*annA_outer*annB_outer-np.pi*annA_inner*annB_inner
            bkgcnts+=calc_data_sum2d('ellipse(%f,%f,%f,%f,%f)'%(ra,dec,annA_outer,annB_outer,ang))-calc_data_sum2d('ellipse(%f,%f,%f,%f,%f)'%(ra,dec,annA_inner,annB_inner,ang))
            FILE.write('ellipse(%f,%f,%f,%f,%f)\nellipse(%f,%f,%f,%f,%f) # color=red\n'%(ra,dec,annA_outer,annB_outer,ang,ra,dec,annA_inner,annB_inner,ang))
        FILE.close()
    netcnts[s-1]=srccnts-bkgcnts*srcarea/bkgarea
    ncntserr=np.sqrt(srccnts+bkgcnts*(srcarea/bkgarea)**2)
    print '\n%i - \nnetcnts: %.1f +/- %.1f\nsrccnts: %.1f\nbkgcnts: %.1f\n'%(s,netcnts[s-1],ncntserr,srccnts,bkgcnts)
