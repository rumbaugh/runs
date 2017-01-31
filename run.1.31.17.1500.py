import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/set_spec_dict.py')

def read_spec_file(field):
    fname='/home/rumbaugh/Chandra/speccats/%s'%spec_dict[field]['file']
    if field=='cl1604':
        loaddict=ACSspecloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
    else:
        loaddict=specloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11)
    crspec=np.genfromtxt(fname,dtype=loaddict,usecols=uc)
    return crspec

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))

cosmocalc(cr['z'],outfile='/home/rumbaugh/cc_out_clus.1.28.17.dat',ids=cr['cluster'])

field='cl0849'
gcr,gx=np.where(cr['field']=='Cl0849')[0],np.where(crx['field']==field)[0]
crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.
crspec=read_spec_file(field)
gspecz=np.where((crspec['Q']>2.5)&(crspec['z']>spec_dict[field]['z'][1])&(crspec['z']<spec_dict[field]['z'][2]))[0]

plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(crspec['ra'][gspecz],crspec['dec'][gspecz],color='b',s=4)
plt.scatter(cr['RA'][gcr],cr['Dec'][gcr],marker='+',color='green',s=250,lw=2)
for i in gcr:
    phi=np.linspace(0,2*np.pi,500)
    r_Mpc=1./Mpc[i]/60./60.
    xdummy,ydummy=r_Mpc*np.cos(phi),r_Mpc*np.sin(phi)
    plt.plot(cr['RA'][i]+xdummy,cr['Dec'][i]+ydummy,color='k',lw=1,ls='dashed')
    plt.text(cr['RA'][i]+10./3600/np.cos(cr['Dec'][i]*np.pi/180.),cr['Dec'][i]+20./3600,'%s'%(cr['cluster'][i]),color='k')
plt.scatter(crx['RA'][gx],crx['DEC'][gx],marker='x',color='red',s=300,lw=2)
for i in gx:
    plt.text(crx['RA'][i]+10./3600/np.cos(crx['DEC'][i]*np.pi/180.),crx['DEC'][i]-50./3600,'%s'%(crx['cluster'][i]),color='magenta')
xlim=plt.xlim()
plt.xlim(xlim[1],xlim[0])
plt.xlabel('R.A.')
plt.ylabel('Dec.')
plt.savefig('/home/rumbaugh/Chandra/plots/center_comp.cl0849.1.31.17.png')
