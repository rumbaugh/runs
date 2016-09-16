import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')

spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9404,9836,9840]}, \
             'cl1324_north': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9840]}, \
             'cl1324_south': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9404,9836]}, \
             'rxj1821': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':[0.818,0.8,0.83], 'obsids': [10444,10924]}, \
             'cl0849': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':[1.261,1.25,1.28], 'obsids': [927,1708]}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':[1.050,1,1.1], 'obsids': []}, \
             'cl0023': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':[0.845,0.82,0.87], 'obsids': [7914]}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':[0.845,0.82,0.87], 'obsids': []}, \
             'cl1604': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':[0.900,0.84,0.96], 'obsids': [6932,6933,7343]}, \
             'cl1350': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.dec2015.nodups.cat', 'loaddict': '','z':[0.804,0.79,0.81], 'obsids': [2229]}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':[0.985,0.97,1.], 'obsids': []}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':[0,0,0], 'obsids': []}, \
             'rcs0224': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':[0.772,0.76,0.79], 'obsids': [3181,4987]}, \
             'rxj1221': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.dec2015.nodups.cat', 'loaddict': '','z':[0.700,0.69,0.71], 'obsids': [1662]}, \
             'rxj1716': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':[0.813,0.8,0.83], 'obsids': [548]}, \
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':[1.110,1.08,1.15], 'obsids': [2227,2452]}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':[0.691,0.68,0.71], 'obsids': [10443,11999]}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':[0,0,0], 'obsids': []}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':[0.959,0.94,0.97], 'obsids': [4161]}, \
             'rxj1053': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1053.dec2015.BCDXtargetsonly.nodups.cat', 'loaddict': '','z':[1.140,1.1,1.15], 'obsids': [4936]}}

cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh'),'formats':('|S24','|S24','f8','f8','f8','f8')})
testfield,testclus=np.zeros(np.shape(cr)[0],dtype='|S24'),np.zeros(np.shape(cr)[0],dtype='|S24')
for i in range(0,len(testclus)):
    testfield[i]=cr['field'][i].lower()
    testclus[i]=cr['cluster'][i].lower()
testfield2,testclus2=np.zeros(np.shape(cr2)[0],dtype='|S24'),np.zeros(np.shape(cr2)[0],dtype='|S24')
for i in range(0,len(testclus2)):
    testfield2[i]=cr2['field'][i].lower()
    testclus2[i]=cr2['cluster'][i].lower()

cfields,ras,decs,zs=np.append(testfield2,testfield[-4:]),np.append(cr2['ra'],cr['ra'][-4:]),np.append(cr2['dec'],cr['dec'][-4:]),np.append(cr2['z'],cr['z'][-4:])


infile='/home/rumbaugh/combined_match_catalog.1.19.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

cosmocalc(zs,outfile='/home/rumbaugh/cc_out_clus.2.9.16.dat',ids=cfields)

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.2.9.16.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Mpc = kpc/1000.

FILE=open('/home/rumbaugh/Chandra/clustocentric_dists.dat','w')
FILE.write('# field number RA Dec dist\n')
clusdist=np.ones(len(crx['RA']))*-1
for i in range(0,len(crx['RA'])):
    g=np.where(((cfields==crx['field'][i].lower())|(cfields==crx['field'][i][:6].lower()))&(np.abs(crx['redshift'][i]-zs)<=0.01))[0]
    if len(g)>0:
        tmpdist=60*SphDist(crx['RA'][i],crx['Dec'][i],ras[g],decs[g])
        #print tmpdist
        gas=np.argsort(tmpdist)[0]
        gind=g[gas]
        clusdist[i]=tmpdist[gas]*Mpc[gind]
        #print tmpdist[gas],Mpc[gind]
    FILE.write('%12s %2i %9.5f %9.5f %f\n'%(crx['field'][i],crx['number'][i],crx['RA'][i],crx['Dec'][i],clusdist[i]))
FILE.close()

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}
allclusdist=np.zeros(0)
for field in targets: 
    crs=np.loadtxt('/home/rumbaugh/Chandra/speccats/%s_spec.cat'%field,dtype=specloaddict)
    g=np.where(((cfields==field)|(cfields==field[:6].lower())))[0]
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    tmpallclusdist=np.ones(len(gq))*-1
    for i in range(0,len(gq)):
        g2=np.where(np.abs(crs['z'][gq[i]]-zs[g])<=0.01)[0]
        if len(g2)>0:
            tmpdist=60*SphDist(crs['ra'][gq[i]],crs['dec'][gq[i]],ras[g[g2]],decs[g[g2]]) 
            gas=np.argsort(tmpdist)[0]
            gind=g[g2[gas]]
            tmpallclusdist[i]=tmpdist[gas]*Mpc[gind]
    allclusdist=np.append(allclusdist,tmpallclusdist)
allclusdist[((allclusdist<0)|(allclusdist>3.1))]=3.1

crd=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists.dat',usecols=(1,2,3,4))

ccd=crd[:,3]
ccd[ccd>3.1]=3.1
ccd[ccd<0]=3.1

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
n1=plt.hist(ccd,bins=7,range=(0,3.5),color='r')
n2=plt.hist(allclusdist,bins=7,range=(0,3.5),color='b',alpha=0.3,weights=20*np.ones(len(allclusdist))*1./len(allclusdist))
plt.xlabel('Clustocentric Distance (Mpc)')
plt.ylabel('Number of sources')
date='2.10.16'
plt.ylim(0,20)
plt.savefig('/home/rumbaugh/Chandra/plots/clustocentric_distance.%s.png'%(date))
for i in range(0,len(n1[0])):
    print 'Percent of sources in range %3.1f to %3.1f Mpc:\nAGN: %4.1f%%  All: %4.1f%%\n'%(n1[1][i],n1[1][i+1],n1[0][i]*100./np.sum(n1[0]),n2[0][i]*100./np.sum(n2[0]))

a,b=KStest(ccd,allclusdist)

print a,b

a,b=KStest(ccd[ccd<=3],allclusdist[allclusdist<=3])

print a,b
