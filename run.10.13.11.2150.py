import matplotlib
import matplotlib.pylab as pylab
import math as m
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/plotcircle.py")
execfile("/home/rumbaugh/angconvert.py")

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'


try:
    rslim
except NameError:
    rslim = 0.01

try:
    cradmult
except NameError:
    cradmult = 0.5

try:
    Ilim
except NameError:
    Ilim = 23.5
try:
    Imin
except NameError:
    Imin = 19.5

try:
    arstep
except NameError:
    arstep = 0.0001

def switch5(arr5):
    arr5[0],arr5[1],arr5[2],arr5[3],arr5[4] = arr5[1],arr5[3],arr5[0],arr5[4],arr5[2]
    return arr5

lumlims = np.array([24.2,24.5,24,24.8,24])

path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])

pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])


zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])

crcr = read_file('/home/rumbaugh/paperstuff/clusters.z+pos+mpc.5.13.11.dat')
struc = get_colvals(crcr,'col1')
cnam = get_colvals(crcr,'col2')
clusz = get_colvals(crcr,'col3')
clusdis = get_colvals(crcr,'col14')
clusH = get_colvals(crcr,'col15')*0.7
clusRA = get_colvals(crcr,'col4')
clusDec = get_colvals(crcr,'col5')
mpc = get_colvals(crcr,'col6')
mpccm = get_colvals(crcr,'col7')
crads = cradmult*0.7*mpc/60
r200 = 2*clusdis/(m.sqrt(200)*clusH)
crads = cradmult*0.7*mpc/60
totinclus_proj = 0
totinclus = 0
totinclusP = 0
for i in range(0,5):
    pfile = '%s/%s'%(path,pfiles[i])
    crp = read_file(pfile)
    pID = get_colvals(crp,'col1')
    if i == 0:
        pRA = get_colvals(crp,'col3')
        pDec = get_colvals(crp,'col4')
        pR = get_colvals(crp,'col5')
        pI = get_colvals(crp,'col6')
        pZ = get_colvals(crp,'col7')
    elif i == 3:
        crp = read_file('/home/rumbaugh/Download/ACS_merged.F606W+F814W_deep.all.coll.nh.dat')
        pRA = get_colvals(crp,'col1')
        pDec = get_colvals(crp,'col2')
        pI = get_colvals(crp,'col4')
    else:
        pRA = get_colvals(crp,'col2')
        pDec = get_colvals(crp,'col3')
        pR = get_colvals(crp,'col4')
        pI = get_colvals(crp,'col5')
        pZ = get_colvals(crp,'col6')

#    FILE = open('/home/rumbaugh/notincluscores.%s.spec.dat'%(names[i]),'w')
    sfile = '%s/%s'%(path,files[i])
    crs = read_file(sfile)
    sid = get_colvals(crs,'col1')
    smask = get_colvals(crs,'col2')
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sR = get_colvals(crs,'col6')
    sq = get_colvals(crs,'col11')
    sz = get_colvals(crs,'col9')
#    if i == 3:
#        sR = get_colvals(crs,'col17')
#        sI = get_colvals(crs,'col18')
    
#    gsz = np.where((sz > zlb[i]) & (sz < zub[i]) & ((sq > 2.2) | (sq < -0.1)))
    gsz = np.where(((sq > 2.2) | (sq < -0.1)))
    gsz = gsz[0]


    if i == 0:
        #Cl1324
        intemp = np.zeros(len(sDec))
        intemp_proj = np.zeros(len(sDec))
	intempP = np.zeros(len(pRA))
        for j in range(0,3):
            Cind = j+5
            inclus_proj = 0
            inclus = 0
            inclusP = 0
            RAprev,Decprev = 999.,999.
            for k in range(0,len(intemp)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[k],sDec[k])
                if ((sI[k] < lumlims[i]) & (diststemp < crads[Cind]*60)): 
                    intemp_proj[k] += 1
                    if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus_proj += 1
                    if ((clusz[Cind] - sz[k] > -rslim) & (clusz[Cind] - sz[k] < rslim) & (sq[k] > 2.2)): 
                        intemp[k] += 1
                        if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus += 1
                RAprev,Decprev = sRA[k],sDec[k]
            for k in range(0,len(intempP)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[k],pDec[k])
                if diststemp < crads[Cind]*60:  
                    if pI[k] < lumlims[i]: intempP[k] += 1
                    if pI[k] < lumlims[i]: inclusP += 1
            print "Cluster %s %s:\nPhoto in clus: %i\nProj. Spec. in clus: %i\nConfirmed in clus: %i"%(struc[Cind],cnam[Cind],inclusP,inclus_proj,inclus)
            if j > 0.1:
                totinclus += inclus
                totinclusP += inclusP
                totinclus_proj += inclus_proj
    if i == 1:
        #NEP5281
        Cind = 4
        for j in range(0,1):
            intemp = np.zeros(len(sDec))
            intempP = np.zeros(len(pRA))
            intemp_proj = np.zeros(len(sDec))
            inclus_proj = 0
            inclus = 0
            inclusP = 0
            RAprev,Decprev = 999.,999.
            for k in range(0,len(intemp)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[k],sDec[k])
                if ((sI[k] < lumlims[i]) & (diststemp < crads[Cind]*60)): 
                    intemp_proj[k] += 1
                    if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus_proj += 1
                    if ((clusz[Cind] - sz[k] > -rslim) & (clusz[Cind] - sz[k] < rslim) & (sq[k] > 2.2)): 
                        intemp[k] += 1
                        if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus += 1
                RAprev,Decprev = sRA[k],sDec[k]
            for k in range(0,len(intempP)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[k],pDec[k])
                if diststemp < crads[Cind]*60:  
                    if pI[k] < lumlims[i]: intempP[k] += 1
                    if pI[k] < lumlims[i]: inclusP += 1
            print "Cluster %s %s:\nPhoto in clus: %i\nProj. Spec. in clus: %i\nConfirmed in clus: %i"%(struc[Cind],cnam[Cind],inclusP,inclus_proj,inclus)
            totinclus += inclus
            totinclusP += inclusP
            totinclus_proj += inclus_proj
            for k in range(0,len(intemp)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[k],sDec[k])
                if diststemp < crads[Cind]*60: 
                    if ((clusz[Cind] - sz[k] > -rslim) & (clusz[Cind] - sz[k] < rslim)): intemp[k] += 1
    if i == 3:
        #Cl1604
        intemp = np.zeros(len(sDec))
        intemp_proj = np.zeros(len(sDec))
	intempP = np.zeros(len(pRA))
        for j in range(0,4):
            Cind = j+10
            inclus_proj = 0
            inclus = 0
            inclusP = 0
            RAprev,Decprev = 999.,999.
            for k in range(0,len(intemp)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[k],sDec[k])
                if ((sI[k] < lumlims[i]) & (diststemp < crads[Cind]*60)): 
                    intemp_proj[k] += 1
                    if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus_proj += 1
                    if ((clusz[Cind] - sz[k] > -rslim) & (clusz[Cind] - sz[k] < rslim) & (sq[k] > 2.2)): 
                        intemp[k] += 1
                        if ((m.fabs(sRA[k] - RAprev) > 0.001) | (m.fabs(sDec[k] - Decprev) > 0.001)): inclus += 1
                RAprev,Decprev = sRA[k],sDec[k]
            for k in range(0,len(intempP)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[k],pDec[k])
                if diststemp < crads[Cind]*60:  
                    if pI[k] < lumlims[i]: intempP[k] += 1
                    if pI[k] < lumlims[i]: inclusP += 1
            print "Cluster %s %s:\nPhoto in clus: %i\nProj. Spec. in clus: %i\nConfirmed in clus: %i"%(struc[Cind],cnam[Cind],inclusP,inclus_proj,inclus)
            totinclus += inclus*1.0
            totinclusP += inclusP*1.0
            totinclus_proj += inclus_proj*1.0
    if i == 4:
        #RXJ1757
        Cind = len(clusRA)-1
        for j in range(0,1):
            intemp = np.zeros(len(gsz))
            intempP = np.zeros(len(pRA))
            for k in range(0,len(intemp)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsz[k]],sDec[gsz[k]])
                if diststemp < crads[Cind]*60: 
                    if ((clusz[Cind] - sz[gsz[k]] > -rslim) & (clusz[Cind] - sz[gsz[k]] < rslim)): intemp[k] += 1
    notinclus = np.where(intemp < 0.11)
    notinclus = notinclus[0]
    inclus = np.where(intemp > 0.11)
    inclus = inclus[0]
#    pylab.scatter(sRA[gsz[notinclus]],sDec[gsz[notinclus]],color='blue',s=10)
 #   pylab.scatter(sRA[gsz[inclus]],sDec[gsz[inclus]],color='red',s=8)
 #   pylab.savefig('/home/rumbaugh/testfig.%s.10.5.11.png'%(names[i]))
#    pylab.close('all')
   # for j in range(0,len(notinclus)): FILE.write('%s\n'%(sid[gsz[notinclus[j]]]))
  #  FILE.close()
print totinclus*1.0/totinclus_proj*totinclusP,m.sqrt(totinclus*(totinclusP/totinclus_proj)**2+totinclusP*(totinclus/totinclus_proj)**2+totinclus_proj*(totinclus/(totinclus_proj**2)*totinclusP)**2)
