import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

targets=np.array(["cl1324_north","cl1324_south","rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053"])
for field in targets:
    cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_lum_limit_alt.dat'%(field,field,field))

    sigma=cr[:,7]
    Ltrue,Lobs=cr[:,8],cr[:,9]
    logLT,logLO=np.log10(Ltrue),np.zeros(len(Lobs))
    logLO[Lobs>0]=np.log10(Lobs[Lobs>0])
    logLO[Lobs<1E30]=rand.normal(40,0.1,len(Lobs[Lobs<1E30]))

    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(logLT,logLO)
    plt.scatter(logLT[sigma<2],logLO[sigma<2],color='r')
    plt.xlabel('True Lx')
    plt.ylabel('Obs Lx')
    plt.xlim(42,44.5)
    plt.title(field)
    plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_lum_test.lum_comp.%s.6.24.16.png'%field)
