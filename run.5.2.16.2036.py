import numpy as np
#import pyfits as py
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/set_spec_dict.py')
#import matplotlib.pyplot as plt
#import matplotlib.backends.backend_pdf as bpdf

R95=1#placeholder value
binwid=64

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

#psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/Lum_lim.5.2.16.pdf')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','X','Y'),'formats':('|S24','i8','i8')})

crobs=np.loadtxt('/home/rumbaugh/Chandra/obs_properties.dat',dtype={'names':('obsid','field','name','chip','PI','exp','RAh','RAm','RAs','Decd','Decm','Decs','nH'),'formats':('i8','|S12','|S24','|S8','|S24','f8','i8','i8','f8','i8','i8','f8','f8')})

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
#fig=plt.figure(1)
ks=np.zeros(len(targets))
for field in targets:
    crSlim=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_flatSlim.5.2.16.dat'%(field,field,field))

    #calc_dict={'z': spec_dict[field]['z'][0]*np.ones(np.shape(crSlim)[0]), 'nh': nh_dict[field]*np.ones(np.shape(crSlim)[0]), 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':crSlim}
    calc_dict={'z': spec_dict[field]['z'][0], 'nh': nh_dict[field], 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':crSlim}

    lums=calc_Xray_lums(calc_dict,loadonce=True)
    np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.2.16.dat'%(field,field,field),lums,fmt='%E %E %E')

        
#Sarea=np.arange(1,np.shape(crSlim)[0]+1)*(binwid/60.)**2
        #fig.clf()
        #plt.rc('axes',linewidth=2)
        #plt.fontsize = 14
        #plt.tick_params(which='major',length=8,width=2,labelsize=14)
        #plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        #ax=fig.add_subplot(1,1,1)
        #ax.plot(
        #ax.set_xlabel("Flux (10^15 erg/s)")
        #ax.set_ylabel("N(<S)")
        #ax.set_title('%s - %s'%(field,band))
        #xlim=plt.xlim()
        #ylim=plt.ylim()
        #ax.loglog([100000,100000],[100000,100001])
        #ax.set_xlim(xlim)
        #ax.set_ylim(ylim)
        #fig.savefig(psfpdf,format='pdf')
#psfpdf.close()
