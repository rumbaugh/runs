execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/angconvert.py")

try:
    cradmult
except NameError:
    cradmult = 2

try:
    Ilim
except NameError:
    Ilim = 23.5
try:
    Imin
except NameError:
    Imin = 19.5

path = '/home/rumbaugh/LFC'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
pathm = '/scratch/rumbaugh/ciaotesting'
mfiles = np.array(['FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat'])

zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])

avg0023Bz = 0.5*(0.844500+0.82860)#B1 is lower redshift

crcr = read_file('/home/rumbaugh/clusters.z+pos+mpc.5.13.11.dat')
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
numclus = np.array([3,1,4,7,1])
Cinds = np.array([5,4,0,10,16])
mpc *= 0.7

for i in range(0,5):
    mfile = '%s/%s/%s/%s'%(pathm,names[i],'master',path2)
    crm = read_file(mfile)
    mRAX = get_colvals(crm,'col2')
    mDecX = get_colvals(crm,'col3')
    nm = get_colvals(crm,'col5')
    mRA = get_colvals(crm,'col6')
    mDec = get_colvals(crm,'col7')

    msfile = '%s/%s'%(path,mfiles[i])
    crms = read_file(msfile)
    msRA = get_colvals(crms,'col4')
    msDec = get_colvals(crms,'col5')
    msR = get_colvals(crms,'col6')
    msI = get_colvals(crms,'col7')
    msZ = get_colvals(crms,'col8')
    msq = get_colvals(crms,'col11')
    msz = get_colvals(crms,'col9')
    msRAX = get_colvals(crms,'col14')
    msDecX = get_colvals(crms,'col15')
   # if i == 3: 
   #     print msRAX
   #     print msDecX
   #     print msRA
   #     print msDec

    gz = np.where((msz > zlb[i]) & (msz < zub[i]))
    gz = gz[0]
    gq = np.where((msq[gz] > 2.3))
    gq = gq[0]
    for j in range(0,len(gq)):
        mindis = 99999.0
        for k in range(0,numclus[i]):
            Cind = Cinds[i]+k
            if i == 4: Cind = len(clusRA)-1
            distemp = SphDist(msRA[gz[gq[j]]],msDec[gz[gq[j]]],clusRA[Cind],clusDec[Cind])
            flag = 0
            if ((j == 2) & (k == 1) & (msz[gz[gq[j]]] > avg0023Bz)): flag == 1
            if ((j == 2) & (k == 2) & (msz[gz[gq[j]]] < avg0023Bz)): flag == 1
            if ((distemp < mindis) & (flag == 0)):
                mindis = distemp
                zdiff = msz[gz[gq[j]]]-clusz[Cind]
            #if ((i == 3) & ((j == 1) | (j == 4))): print '%f %f %f %f %f %f'%(distemp,mindis,msRA[gz[gq[j]]],msDec[gz[gq[j]]],clusRA[Cind],clusDec[Cind])
        print '%7.5f %7.5f %7.5f'%(msz[gz[gq[j]]],mindis/mpc[Cind],zdiff)
