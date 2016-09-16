import numpy as np
import matplotlib.pyplot as plt

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604"}

cr=np.loadtxt('/home/rumbaugh/Chandra/coadds.allORELSE.mostly.magcut.EWnD4000.winfillcorrHd.cat',dtype={'names':('field','file','z','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S12','|S64','f8','f8','f8','f8','f8','f8','f8','f8')})

crbf=np.loadtxt('/home/rumbaugh/Chandra/Blue_fracs.5.11.16.dat',dtype={'names':('field','BF','num','BF_cut','num_cut'),'formats':('|S24','f8','f8','f8','f8')})
crbfz=np.loadtxt('/home/rumbaugh/Chandra/Blue_fracs.w_photz.5.11.16.dat',dtype={'names':('field','BF','num','BF_cut','num_cut','BF_photz','num_photz'),'formats':('|S24','f8','i8','f8','i8','f8','f8')})
gbf=np.zeros(len(cr['field']),dtype='i8')
for i in range(0,len(cr['field'])):
    gbf[i]=np.where(target_dir[cr['field'][i]]==crbf['field'])[0]
gbfz=np.zeros(len(cr['field']),dtype='i8')
for i in range(0,len(cr['field'])):
    if target_dir[cr['field'][i]] in crbfz['field']: 
        gbfz[i]=np.where(target_dir[cr['field'][i]]==crbfz['field'])[0]


#plt.figure(1)
#plt.clf()
#plt.rc('axes',linewidth=2)
#plt.fontsize = 14
#plt.tick_params(which='major',length=8,width=2,labelsize=14)
#plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
#plt.scatter(cr['Hd'],crbf['BF_cut'][gbf],color='r',s=32)
#xlim=plt.xlim()
#xrng=xlim[1]-xlim[0]
#plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'])): 
    print '%s: %f'%(cr['field'][i],crbf['BF_cut'][gbf[i]])
#    plt.text(cr['Hd'][i]+xrng/50.,crbf['BF_cut'][gbf[i]],cr['field'][i],color='b')
#    if target_dir[cr['field'][i]] in crbfz['field']: plt.arrow(cr['Hd'][i],crbf['BF_cut'][gbf][i],0,crbfz['BF_photz'][gbfz[i]]-crbf['BF_cut'][gbf][i],color='r',lw=2,width=0.005,head_length=0.01)
#plt.axvline(-4,lw=2,color='k',ls='dashed')
#plt.ylabel('Blue Fraction')
#plt.xlabel(r'EW(H$\delta$) (angstroms)')
#plt.title('Cut at -20.9')
#plt.savefig('/home/rumbaugh/Chandra/plots/coadds.Hd_vs_bluefrac_photoz.png')

