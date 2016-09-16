import numpy as np
execfile('/home/rumbaugh/SphDist.py')

tol=1./3600.

speccat='/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/FINAL.nep5281.deimos.gioia.aug2013.nodups.cat'
photcat='/home/rumbaugh/Chandra/photcats/rxj1821_rizdata.corr.gz'


specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}
refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79]}, \
             'rxj1821': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':[0.818,0.8,0.83]}, \
             'cl0849': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':[1.261,1.25,1.28]}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':[1.050,1,1.1]}, \
             'cl0023': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':[0.845,0.82,0.87]}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':[0.845,0.82,0.87]}, \
             'cl1604': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':[0.900,0.84,0.96]}, \
             'cl1350': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.dec2015.nodups.cat', 'loaddict': '','z':[0.804,0.79,0.81]}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':[0.985,0.97,1.]}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':[0,0,0]}, \
             'rcs0224': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':[0.772,0.76,0.79]}, \
             'rxj1221': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.dec2015.nodups.cat', 'loaddict': '','z':[0.700,0.69,0.71]}, \
             'rxj1716': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':[0.813,0.8,0.83]}, \
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':[1.110,1.08,1.15]}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':[0.691,0.68,0.71]}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':[0,0,0]}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':[0.959,0.94,0.97]}, \
             'rxj1053': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1053.dec2015.BCDXtargetsonly.nodups.cat', 'loaddict': '','z':[1.140,1.1,1.15]}}

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])


FILE=open('/home/rumbaugh/checkNN.1.6.15.dat','w')

for field in targets:
    print field
    speccat='/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file']
    photcat='/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    crs=np.loadtxt(speccat,dtype=specloaddict)
    crp=np.loadtxt(photcat,dtype=refdict)
    pra,pdec,sra,sdec=crp['ra'],crp['dec'],crs['ra'],crs['dec']
    BMcnt=0
    totBM=0
    NMcnt=0
    for i in range(0,len(sra)):
        gtmp=np.where((np.abs(sra[i]-pra)/np.cos(sdec[i])<tol)&(np.abs(sdec[i]-pdec)<tol))[0]
        if len(gtmp)==0: 
            print 'Nothing within %f as for object %i'%(tol*3600,i)
            FILE.write('%7s %7s %10.6f %10.6f %7s %10.6f %10.6f\n'%(field,crs['ID'][i],sra[i],sdec[i],'NONE',-1,-1))
            NMcnt+=1
            continue
        disttmp=SphDist(sra[i],sdec[i],pra[gtmp],pdec[gtmp])
        gas=np.argsort(disttmp)
        FILE.write('%7s %7s %10.6f %10.6f %7s %10.6f %10.6f\n'%(field,crs['ID'][i],sra[i],sdec[i],crp['ID'][gtmp[gas[0]]],pra[gtmp[gas[0]]],pdec[gtmp[gas[0]]]))
        if ((crs['ID'][i] != crp['ID'][gtmp[gas[0]]])): 
            try:
                if crs['ID'][i] == 'F%05i'%int(crp['ID'][gtmp[gas[0]]]): continue
            except:
                pass
            BMcnt+=1
            totBM+=1
            if BMcnt<10:
                print '%s matched to %s'%(crs['ID'][i],crp['ID'][gtmp[gas[0]]])
        else:
            if BMcnt>=10:
                print '%i bad matches in a row'%BMcnt
            BMcnt=0
    if BMcnt>10:
        print '%i bad matches in a row'%BMcnt
    print '%i total bad matches, %i no matches out of %i'%(totBM,NMcnt,len(sra))
FILE.close()
