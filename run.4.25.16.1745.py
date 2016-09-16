import numpy as np
import matplotlib.pyplot as plt

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7'}


for field in reffile_dict.keys():
    cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.4.23.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8')})
    print field,len(np.where(((np.abs(cr['z_spec']-cr['z_spec_adam'])>0.001)&(cr['z_spec_adam']>-0.5)))[0]),len(np.where((cr['z_spec_adam']<0)&(cr['z_spec']>0)&(cr['Q']>2.5))[0])
    
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(cr['z_spec_adam'],cr['z_spec'],color='k',s=2)
    plt.xlabel('z_spec (adam)')
    plt.ylabel('z_spec (spec cat)')
    plt.legend()
    plt.savefig('/home/rumbaugh/Chandra/plots/adam_specz_test.%s.4.23.16.png'%field)
