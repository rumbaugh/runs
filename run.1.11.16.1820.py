import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/angconvert.py")
execfile('/home/rumbaugh/SphDist.py')

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.1.5.16.dat',dtype=indict)


oldfile='/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8_wflux.dat'

olddict={'names':('field','num','RA','Dec','RAH','RAM','RAS','DecD','DecM','DecS','redshift','soft_lum','hard_lum','full_lum','soft_ncnts','hard_ncnts','full_ncnts','soft_flux','hard_flux','full_flux','significance'),'formats':('|S32','i8','f8','f8','i8','i8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

cro=np.loadtxt(oldfile,dtype=olddict)
#oldra,olddec=hms2deg(cro['RA']),dms2deg(cro['dec'])
oldra,olddec=cro['RA'],cro['Dec']

nncS,nfS,nlS,nncH,nfH,nlH,nncF,nfF,nlF=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
oncS,ofS,olS,oncH,ofH,olH,oncF,ofF,olF=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)

for i in range(0,len(crn['RA'])):
    disttmp=SphDist(crn['RA'][i],crn['Dec'][i],oldra,olddec)*60
    gas=np.where(disttmp<5)[0]
    if len(gas)>0:
        gas=gas[0]
        nncS,nfS,nlS,nncH,nfH,nlH,nncF,nfF,nlF=np.append(nncS,crn['ncnts_soft'][i]),np.append(nfS,crn['flux_soft'][i]),np.append(nlS,crn['lum_soft'][i]),np.append(nncH,crn['ncnts_hard'][i]),np.append(nfH,crn['flux_hard'][i]),np.append(nlH,crn['lum_hard'][i]),np.append(nncF,crn['ncnts_full'][i]),np.append(nfF,crn['flux_full'][i]),np.append(nlF,crn['lum_full'][i])
        oncS,ofS,olS,oncH,ofH,olH,oncF,ofF,olF=np.append(oncS,cro['soft_ncnts'][i]),np.append(ofS,cro['soft_flux'][i]),np.append(olS,cro['soft_lum'][i]),np.append(oncH,cro['hard_ncnts'][i]),np.append(ofH,cro['hard_flux'][i]),np.append(olH,cro['hard_lum'][i]),np.append(oncF,cro['full_ncnts'][i]),np.append(ofF,cro['full_flux'][i]),np.append(olF,cro['full_lum'][i])
        print '%10s %2i - %02i:%02i:%05.2f %02i:%02i:%05.2f  z: %.3f\nSoft Band Lum.   - New: %8.3f Old: %8.3f P.D.: %8.3f\nSoft Band Flux.  - New: %8.3f Old: %8.3f P.D.: %8.3f\nSoft Band NCnts. - New: %8.3f Old: %8.3f P.D.: %8.3f\nHard Band Lum.   - New: %8.3f Old: %8.3f P.D.: %8.3f\nHard Band Flux.  - New: %8.3f Old: %8.3f P.D.: %8.3f\nHard Band NCnts. - New: %8.3f Old: %8.3f P.D.: %8.3f\nFull Band Lum.   - New: %8.3f Old: %8.3f P.D.: %8.3f\nFull Band Flux.  - New: %8.3f Old: %8.3f P.D.: %8.3f\nFull Band NCnts. - New: %8.3f Old: %8.3f P.D.: %8.3f\n'%(cro['field'][gas],cro['num'][gas],cro['RAH'][gas],cro['RAM'][gas],cro['RAS'][gas],cro['DecD'][gas],cro['DecM'][gas],cro['DecS'][gas],crn['redshift'][i],1E-42*crn['lum_soft'][i],cro['soft_lum'][gas],(1E-42*crn['lum_soft'][i]-cro['soft_lum'][gas])*100./cro['soft_lum'][gas],1E16*crn['flux_soft'][i],1E16*cro['soft_flux'][gas],(1E16*crn['flux_soft'][i]-1E16*cro['soft_flux'][gas])*100.*1E-16/cro['soft_flux'][gas],crn['ncnts_soft'][i],cro['soft_ncnts'][gas],(crn['ncnts_soft'][i]-cro['soft_ncnts'][gas])*100./cro['soft_ncnts'][gas],1E-42*crn['lum_hard'][i],cro['hard_lum'][gas],(1E-42*crn['lum_hard'][i]-cro['hard_lum'][gas])*100./cro['hard_lum'][gas],1E16*crn['flux_hard'][i],1E16*cro['hard_flux'][gas],(1E16*crn['flux_hard'][i]-1E16*cro['hard_flux'][gas])*100.*1E-16/cro['hard_flux'][gas],crn['ncnts_hard'][i],cro['hard_ncnts'][gas],(crn['ncnts_hard'][i]-cro['hard_ncnts'][gas])*100./cro['hard_ncnts'][gas],1E-42*crn['lum_full'][i],cro['full_lum'][gas],(1E-42*crn['lum_full'][i]-cro['full_lum'][gas])*100./cro['full_lum'][gas],1E16*crn['flux_full'][i],1E16*cro['full_flux'][gas],(1E16*crn['flux_full'][i]-1E16*cro['full_flux'][gas])*100.*1E-16/cro['full_flux'][gas],crn['ncnts_full'][i],cro['full_ncnts'][gas],(crn['ncnts_full'][i]-cro['full_ncnts'][gas])*100./cro['full_ncnts'][gas])

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='k')
plt.hist(x_zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='r')
plt.xlabel('Redshift')
plt.ylabel('Number of sources')
plt.title(field)
plt.savefig('/home/rumbaugh/Chandra/plots/z_hist_zoom.%s.%s.png'%(field,date))
