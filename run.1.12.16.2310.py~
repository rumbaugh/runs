import numpy as np
execfile("/home/rumbaugh/angconvert.py")
execfile('/home/rumbaugh/SphDist.py')

stol=2.5


cr=np.loadtxt('/home/rumbaugh/R12_T8.dat',delimiter=',',dtype={'names':('field','num','rah','ram','ras','decd','decm','decs','z','fluxS','fluxH','fluxF','sig'),'formats':('|S8','i8','i8','i8','f8','i8','i8','f8','f8','f8','f8','f8','f8')})

ra,dec=hms2deg(cr['rah'],cr['ram'],cr['ras']),dms2deg(cr['decd'],cr['decm'],cr['decs'])

outarr=np.zeros((len(ra),len(cr.dtype.names)+2))

#outarr[:,0],outarr[:,1],outarr[:,2],outarr[:,3],outarr[:,4],outarr[:,5],outarr[:,6],outarr[:,7],outarr[:,8],outarr[:,9],outarr[:,10],outarr[:,11],outarr[:,12],outarr[:,13] = cr['field'],ra,dec,cr['rah'],cr['ram'],cr['ras'],cr['decd'],cr['decm'],cr['decs'],cr['z'],cr['fluxS'],cr['fluxH'],cr['fluxF'],cr['sig']

FILE=open('/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8_wflux.dat','w')
FILE.write('# field RA Dec RAH RAM RAS DecD DecM DecS redshift soft_lum hard_lum full_lum soft_ncnts hard_ncnts full_ncnts soft_flux hard_flux full_flux significance\n')
for i in range(0,len(ra)):
    nncS,nfS,nncH,nfH,nncF,nfF=0.,0.,0.,0.,0.,0.
    field=cr['field'][i].lower()
    if field == 'cl1324':
        if ra[i]>30.56:
            field='cl1324_north'
        else:
            field='cl1324_south'
        cr_op=np.loadtxt('/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(obsid_dict[field],obsid_dict[field]))
    elif field != 'cl1604':
        cr_op=np.loadtxt('/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(obsid_dict[field],obsid_dict[field]))
    else:
        crtmp1,crtmp2=np.loadtxt('/home/rumbaugh/Chandra/6932/photometry/6932.xray_phot.soft_hard_full.dat'),np.loadtxt('/home/rumbaugh/Chandra/6933+7343/photometry/6933+7343.xray_phot.soft_hard_full.dat')
        cr_op=np.append(crtmp1,crtmp2,axis=0)
    oldra,olddec,oldfluxS,oldfluxH,oldfluxF,oldncntsS,oldncntsH,oldncntsF=cr_op[:,0],cr_op[:,1],cr_op[:,2],cr_op[:,3],cr_op[:,4],cr_op[:,5],cr_op[:,6],cr_op[:,7]
    gtmp=np.where((np.abs(oldra-ra[i])/np.cos(dec[i])<stol)&(np.abs(olddec-dec[i])<stol))[0]
    if len(gtmp)!=0: 
        disttmp=SphDist(oldra[gtmp],olddec[gtmp],ra[i],dec[i])
        gas=np.argsort(disttmp)
        gz=gtmp[gas[:1]]
        nncS,nncH,nncF,nfS,nfH,nfF=oldncntsS[gz],oldncntsH[gz],oldncntsF[gz],oldfluxS[gz],oldfluxH[gz],oldfluxF[gz]
    FILE.write('%8s %2i  %10.6f  %10.6f  %02i %02i %05.2f %02i %02i %05.2f %6.4f %f %f %f %f %f %f %E %E %E %f\n'%(cr['field'][i],cr['num'][i],ra[i],dec[i],cr['rah'][i],cr['ram'][i],cr['ras'][i],cr['decd'][i],cr['decm'][i],cr['decs'][i],cr['z'][i],cr['fluxS'][i],cr['fluxH'][i],cr['fluxF'][i],nncS,nncH,nncF,nfS,nfH,nfF,cr['sig'][i]))

#np.savetxt('/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8.dat',outarr,fmt='%8s  %10.6f  %10.6f  %02i %02i %02i %5.2f %02i %02i %5.2f %6.4f %f %f %f %f',header='# field RA Dec RAH RAM RAS DecD DecM DecS redshift soft_flux hard_flux full_flux significance')

FILE.close()
