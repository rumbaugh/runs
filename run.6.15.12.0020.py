import numpy as np

try:
    ntrials
except NameError:
    ntrials = 10000

execfile("/home/rumbaugh/KStest.py")
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

for i in range(0,len(names)):
    FILE=open('/home/rumbaugh/temp/idl_clusprops.%s.5.31.12.dat'%(names[i]),'w')
    cr1 = read_file("/home/rumbaugh/temp/idl_clusprops.%s.4.10.12.dat"%(names[i]))
    sig = copy_colvals(cr1,'col1')
    blusig,redsig,BCGvel=copy_colvals(cr1,'col2'),copy_colvals(cr1,'col3'),copy_colvals(cr1,'col4')
    cr = read_file("/home/rumbaugh/temp/idl_vels.%s.4.10.12.dat"%(names[i]))
    vels = copy_colvals(cr,'col1')
    isblu = copy_colvals(cr,'col3')
    vsort = np.sort(vels)
    randvels = np.random.normal(0.0,sig,ntrials)
    cdf_norm = np.zeros(len(vsort))
    for j in range(0,len(vsort)):
        g = np.where(randvels < vsort[j])
        cdf_norm[j] = len(g[0])*1.0/ntrials
    maxdif,KSprob = KStest1var(vsort,cdf_norm)
    print '%s - KS result: %f\n'%(names[i],KSprob)
