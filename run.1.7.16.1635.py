import numpy as np
execfile("/home/rumbaugh/angconvert.py")

cr=np.loadtxt('/home/rumbaugh/R12_T8.dat',delimiter=',',dtype={'names':('field','num','rah','ram','ras','decd','decm','decs','z','fluxS','fluxH','fluxF','sig'),'formats':('|S8','i8','i8','i8','f8','i8','i8','f8','f8','f8','f8','f8','f8')})

ra,dec=hms2deg(cr['rah'],cr['ram'],cr['ras']),dms2deg(cr['decd'],cr['decm'],cr['decs'])

outarr=np.zeros((len(ra),len(cr.dtype.names)+2))

#outarr[:,0],outarr[:,1],outarr[:,2],outarr[:,3],outarr[:,4],outarr[:,5],outarr[:,6],outarr[:,7],outarr[:,8],outarr[:,9],outarr[:,10],outarr[:,11],outarr[:,12],outarr[:,13] = cr['field'],ra,dec,cr['rah'],cr['ram'],cr['ras'],cr['decd'],cr['decm'],cr['decs'],cr['z'],cr['fluxS'],cr['fluxH'],cr['fluxF'],cr['sig']

FILE=open('/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8.dat','w')
FILE.write('# field RA Dec RAH RAM RAS DecD DecM DecS redshift soft_flux hard_flux full_flux significance\n')
for i in range(0,len(ra)):
    FILE.write('%8s %2i  %10.6f  %10.6f  %02i %02i %05.2f %02i %02i %05.2f %6.4f %f %f %f %f\n'%(cr['field'][i],cr['num'][i],ra[i],dec[i],cr['rah'][i],cr['ram'][i],cr['ras'][i],cr['decd'][i],cr['decm'][i],cr['decs'][i],cr['z'][i],cr['fluxS'][i],cr['fluxH'][i],cr['fluxF'][i],cr['sig'][i]))

#np.savetxt('/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8.dat',outarr,fmt='%8s  %10.6f  %10.6f  %02i %02i %02i %5.2f %02i %02i %5.2f %6.4f %f %f %f %f',header='# field RA Dec RAH RAM RAS DecD DecM DecS redshift soft_flux hard_flux full_flux significance')

FILE.close()
