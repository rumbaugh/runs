import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/LFC_color_param.py')

zarr=np.linspace(0.1,2,191)

cols=()
for i in range(0,len(zarr)): cols=cols+(i+2,)
crcp=np.loadtxt('/home/rumbaugh/LFC_color_param/comb_LFC_param_UVs.graz13.2.23.16.dat',usecols=cols)
Acomb=crcp[-1]
param_dict={'Acomb':Acomb,'z':zarr}
F_Acomb=interp1d(param_dict['z'],param_dict['Acomb'],kind='linear',bounds_error=False,fill_value=0)

crf=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S32')
crpre=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S6')

gz=np.arange(40,141)
z=np.linspace(0.5,1.5,101)
A_z=F_Acomb(z)
B_z=1-A_z
year = 13
gy=np.where(crpre=='graz%02i'%year)[0]
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
safeLB=950
safeUB=32000
crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13][gz]*3.086E22
cc_z=crcc[:,0][gz]

for SED,iSED in zip(crf[gy],np.arange(len(gy))):
    curcr=np.loadtxt(SED)
    w,S=np.copy(curcr[:,0]),np.copy(curcr[:,1])
    mblue,mred=np.zeros(len(z)),np.zeros(len(z))
    for i in range(0,len(z)): 
        A,B=A_z[i],B_z[i]
        gdl=np.argsort(np.abs(z-cc_z))[0]
        obs_r,obs_i,obs_z=calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='r',D_L=D_L[gdl]),calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='i',D_L=D_L[gdl]),calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='z',D_L=D_L[gdl])
        m_b=-2.5*np.log10(A*obs_r+B*(obs_i))-48.6
        m_r=-2.5*np.log10(A*obs_i+B*obs_z)-48.6
        mblue[i],mred[i]=m_b,m_r
    

    if iSED%4==0:plt.plot(z,mblue-mred)
plt.xlabel('Redshift')
plt.ylabel('m_blue-m_red')
plt.savefig('/home/rumbaugh/LFC_color_param/LFC_color_param.zfunc.2.23.16.png')
