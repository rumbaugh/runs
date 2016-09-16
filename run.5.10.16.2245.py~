import numpy as np
import pyfits as py
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/set_spec_dict.py')
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

R95=1#placeholder value
binwid=64

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/Lum_lim.5.2.16.pdf')

#targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','X','Y'),'formats':('|S24','i8','i8')})

crobs=np.loadtxt('/home/rumbaugh/Chandra/obs_properties.dat',dtype={'names':('obsid','field','name','chip','PI','exp','RAh','RAm','RAs','Decd','Decm','Decs','nH'),'formats':('i8','|S12','|S24','|S8','|S24','f8','i8','i8','f8','i8','i8','f8','f8')})

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
fig=plt.figure(1)
ks=np.zeros(len(targets))
carr=['blue','red','green','cyan','magenta','brown','gray']
lsarr=['dashed','dotted','solid']
for field,ifld in zip(targets,np.arange(0,len(targets))): 
    if field=='cl1324':
        crLum1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_north','cl1324_north','cl1324_north'))
        crLum2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_south','cl1324_south','cl1324_south'))
        crLum=np.append(crLum1,crLum2,axis=0)
    else:
        crLum=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%(field,field,field))
    gn0=np.where(crLum>0)[0]
    Sarea=np.arange(1,np.shape(crLum[gn0])[0]+1)*(binwid/60.)**2
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        ax.plot(np.log10(np.sort(crLum[gn0][:,ib])),Sarea,color=carr[ib],lw=2,ls=lsarr[ib],label=band)
    ax.set_xlabel("Log[3-sigma Luminosity Limit (erg/s)]")
    ax.set_ylabel("Area (sq. arcmin)")
    plt.legend(loc='lower right')
    ax.set_title(field)
    #xlim=plt.xlim()
    #ylim=plt.ylim()
    #ax.set_xlim(xlim)
    #ax.set_ylim(ylim)
    fig.savefig(psfpdf,format='pdf')
fig=plt.figure(2)
plt.clf()  
for field,ifld in zip(targets,np.arange(0,len(targets))):  
    if field=='cl1324':
        crLum1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_north','cl1324_north','cl1324_north'))
        crLum2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_south','cl1324_south','cl1324_south'))
        crLum=np.append(crLum1,crLum2,axis=0)
    else:
        crLum=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%(field,field,field))
    gn0=np.where(crLum>0)[0]
    Sarea=np.arange(1,np.shape(crLum[gn0])[0]+1)*(binwid/60.)**2
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    band,ib='full',2
    ax.plot(np.log10(np.sort(crLum[gn0][:,ib])),Sarea,color=carr[ifld%len(carr)],lw=2,ls=lsarr[ifld%len(lsarr)],label=field)
    ax.set_xlabel("Log[3-sigma Luminosity Limit (erg/s)]")
    ax.set_ylabel("Area (sq. arcmin)")
    plt.legend(loc='upper left')
    ax.set_title('Full band comparison')
    plt.xlim(41,45)
fig.savefig(psfpdf,format='pdf')

fig=plt.figure(3)
plt.clf()  
for field,ifld in zip(targets,np.arange(0,len(targets))):  
    if field=='cl1324':
        crLum1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_north','cl1324_north','cl1324_north'))
        crLum2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%('cl1324_south','cl1324_south','cl1324_south'))
        crLum=np.append(crLum1,crLum2,axis=0)
    else:
        crLum=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lim_lums.5.3.16.dat'%(field,field,field))
    crLum*=2./3.
    gn0=np.where(crLum>0)[0]
    Sarea=np.arange(1,np.shape(crLum[gn0])[0]+1)*(binwid/60.)**2
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    band,ib='full',2
    ax.plot(np.log10(np.sort(crLum[gn0][:,ib])),Sarea,color=carr[ifld%len(carr)],lw=2,ls=lsarr[ifld%len(lsarr)],label=field)
    ax.set_xlabel("Log[2-sigma Luminosity Limit (erg/s)]")
    ax.set_ylabel("Area (sq. arcmin)")
    plt.legend(loc='upper left')
    ax.set_title('Full band comparison')
    plt.xlim(41,45)
fig.savefig(psfpdf,format='pdf')
psfpdf.close()
