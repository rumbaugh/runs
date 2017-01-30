import numpy as np
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')

def read_spec_file(field):
    fname=spec_dict[field]
    if field=='cl1604':
        loaddict=ACSspecloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
    else:
        loaddict=specloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11)
    crspec=np.genfromtxt(fname,dtype=loaddict,usecols=uc)
    return crspec

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','blg','bkg-','blg+','r500','r500NC','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

cosmocalc(cr['z'],outfile='/home/rumbaugh/cc_out_clus.1.28.17.dat',ids=cr['cluster'])

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.

for clus in crf['cluster']:
    gcr=np.where(cr['cluster']==clus)[0]
    Mpc_am=1./Mpc[gcr]/60.
    field=cr['field'][gcr]
    crspec=read_spec_file(field)
    gspecz=np.where((crspec['z']>spec_dict[field]['z'][1])&(crspec['z']<spec_dict[field]['z'][2]))[0]
    tdists=SphDist(crspec['ra'][gspecz],crspec['dec'][gspecz],cr['RA'][gcr],cr['Dec'][gcr])
    gclose=np.where(tdists<Mpc_am)[0]
    allzs=crspec['z'][gspecz][gclose]
    allsig=CalcVelDisp(allzs)
    print clus,allsig
