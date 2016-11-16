import numpy as np
import angconvert as ang

cr = np.loadtxt('/home/rumbaugh/MILLIQUAS_INY1A1TILE.csv',skiprows=1,delimiter=',',dtype={'names':('NUMROW','MQ_ROWNUM','RA','DEC','TILENAME'),'formats':('i8','i8','f8','f8','|S30')})

rah,ram,ras=ang.deg2hms(cr['RA'])
decd,decm,decs=ang.deg2dms(cr['DEC'])
crout=np.zeros(len(cr),dtype={'names':('NUMROW','MQ_ROWNUM','RA','DEC','OBJNAME','TILENAME'),'formats':('i8','i8','f8','f8','|S30','|S30')})
crout['NUMROW'],crout['MQ_ROWNUM'],crout['RA'],crout['DEC'],crout['TILENAME']=cr['NUMROW'],cr['MQ_ROWNUM'],cr['RA'],cr['DEC'],cr['TILENAME']
for i in range(0,len(cr)):
    crout['OBJNAME'][i]='DESJ%02i%02i%04.1f%+03i%02i%04.1f'%(rah[i],ram[i],ras[i],decd[i],decm[i],decs[i])
np.savetxt('/home/rumbaugh/MILLIQUAS_INY1A1TILE_WNAME.tab',crout,fmt='%6i %8i %9.5f %9.5f %21s %s',header='NUMROW MQ_ROWNUM RA DEC OBJNAME TILENAME')
