import numpy as np
execfile("/home/rumbaugh/angconvert.py")
execfile('/home/rumbaugh/SphDist.py')

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.1.5.16.dat',dtype=indict)


oldfile='/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8.dat'

olddict={'names':('field','num','RA','Dec','RAH','RAM','RAS','DecD','DecM','DecS','redshift','soft_lum','hard_lum','full_lum','significance'),'formats':('|S32','i8','f8','f8','i8','i8','f8','i8','i8','f8','f8','f8','f8','f8','f8')}

cro=np.loadtxt(oldfile,dtype=olddict)
#oldra,olddec=hms2deg(cro['RA']),dms2deg(cro['dec'])
oldra,olddec=cro['RA'],cro['Dec']

for i in range(0,len(crn['RA'])):
    disttmp=SphDist(crn['RA'][i],crn['Dec'][i],oldra,olddec)*60
    gas=np.where(disttmp<5)[0]
    if len(gas)>0:
        gas=gas[0]
        print '%10s %2i - %02i:%02i:%05.2f %02i:%02i:%05.2f  z: %.3f\nSoft Band Lum. - New: %6.3f Old: %6.3f P.D.: %8.3f\nHard Band Lum. - New: %6.3f Old: %6.3f P.D.: %8.3f\nFull Band Lum. - New: %6.3f Old: %6.3f P.D.: %8.3f\n'%(cro['field'][gas],cro['num'][gas],cro['RAH'][gas],cro['RAM'][gas],cro['RAS'][gas],cro['DecD'][gas],cro['DecM'][gas],cro['DecS'][gas],crn['redshift'][i],1E-42*crn['lum_soft'][i],cro['soft_lum'][gas],(1E-42*crn['lum_soft'][i]-cro['soft_lum'][gas])*100./cro['soft_lum'][gas],1E-42*crn['lum_hard'][i],cro['hard_lum'][gas],(1E-42*crn['lum_hard'][i]-cro['hard_lum'][gas])*100./cro['hard_lum'][gas],1E-42*crn['lum_full'][i],cro['full_lum'][gas],(1E-42*crn['lum_full'][i]-cro['full_lum'][gas])*100./cro['full_lum'][gas])
