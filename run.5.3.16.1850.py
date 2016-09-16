import numpy as np




fields=['cl0023','rxj1716']
bands=['soft','hard','full']
netcnts=np.zeros(2)

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
gks={x:np.where(crk['field']==x)[0][0] for x in fields}

for s in [1,2]:
    FILE=open('/home/rumbaugh/sample%s_aperphot.dat'%s,'w')
    FILE.write('# sample band netcnts netcnts_err srccnts bkgcnts srcarea bkgarea num_src\n')
    for sample in ['cut','nocut']:
        srccnts,bkgcnts,netcnts,ncntserr={x:0. for x in bands},{x:0. for x in bands},{x:0. for x in bands},{x:0. for x in bands}
        srcarea,bkgarea={x:0. for x in bands},{x:0. for x in bands}
        for j,band in zip(np.arange(3),bands):
            numsrc=0
            for field in fields:
                cro=np.loadtxt('/home/rumbaugh/sample%i_%s.image_cut.w_PSF.reg'%(s,field),skiprows=3,dtype='|S256')
                print len(cro)
                crpnc=np.loadtxt('/home/rumbaugh/sample%i_%s.phys_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
                crinc=np.loadtxt('/home/rumbaugh/sample%i_%s.image_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
                crnc=np.loadtxt('/home/rumbaugh/sample%i_%s.image_nocut.w_PSF.reg'%(s,field),skiprows=1,dtype='|S256')
                load_data('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.img'%(field,field,field,band))
                if sample=='cut':
                    cr=np.copy(cro)
                else:
                    cr=np.copy(crnc)
                numsrc+=len(cr)
                for i in range(0,len(cr)):
                    tmpstr=cr[i].split(' #')
                    srccnts[band]+=calc_data_sum2d(tmpstr[0])
                load_data('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s_nops.img'%(field,field,field,band))
                for i in range(0,len(cr)):
                    tmpstr=cr[i].split(' #')
                    tmpstr=tmpstr[0].split(',')
                    tmpra,tmpangle=tmpstr[0].split('('),tmpstr[4].split(')')
                    ra,dec,rA,rB,ang=float(tmpra[1]),float(tmpstr[1]),float(tmpstr[2]),float(tmpstr[3]),float(tmpangle[0])
                    srcarea[band]+=np.pi*rA*rB
                    annA_inner,annA_outer,annB_inner,annB_outer=rA*1.5,rA*2.5,rB*1.5,rB*2.5
                    bkgarea[band]+=np.pi*annA_outer*annB_outer-np.pi*annA_inner*annB_inner
                    bkgcnts[band]+=calc_data_sum2d('ellipse(%f,%f,%f,%f,%f)'%(ra,dec,annA_outer,annB_outer,ang))-calc_data_sum2d('ellipse(%f,%f,%f,%f,%f)'%(ra,dec,annA_inner,annB_inner,ang))
            netcnts[band]=srccnts[band]-bkgcnts[band]*srcarea[band]/bkgarea[band]
            ncntserr[band]=np.sqrt(srccnts[band]+bkgcnts[band]*(srcarea[band]/bkgarea[band])**2)
            print '\n%i (%s) - \nnetcnts: %.1f +/- %.1f\nsrccnts: %.1f\nbkgcnts: %.1f\n'%(s,band,netcnts[band],ncntserr[band],srccnts[band],bkgcnts[band])
            FILE.write('%5s %4s %.2f %.2f %.2f %.2f %.2f %.2f %i\n'%(sample,band,netcnts[band],ncntserr[band],srccnts[band],bkgcnts[band],srcarea[band],bkgarea[band],numsrc))
    FILE.close()
