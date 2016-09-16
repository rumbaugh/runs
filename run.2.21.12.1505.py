execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/biweight.py")
execfile("/home/rumbaugh/DStest.py")
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

try:
    skipMC
except NameError:
    skipMC = 1
try:
    writeMC
except NameError:
    writeMC = 1

names2 = np.array(['RXJ1757','RXJ1821','Cl0910+5422'])
names = np.array(['nep200','nep5281','cl0910'])

BCGinds = np.array([3,4,8])
crBCG = read_file("/home/rumbaugh/BCGpositions.2.15.12.dat")
BCGzs = copy_colvals(crBCG,'col7')

ymaxes = np.array([11,11,8]) 

for i in range(0,len(names)):
    cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    RA = copy_colvals(cr,'col2')
    Dec = copy_colvals(cr,'col3')
    z = copy_colvals(cr,'col4')
    vels = copy_colvals(cr,'col5')
    delta = np.zeros(len(z))
    avg_v = c*biweight_loc(z)
    avg_z = avg_v/c
    #sig = np.std(vels)
    sig = biweight_scale(vels)
    zsig = sig*(1+avg_z)/c
    if skipMC == 0:
        Del,P,delta = DStest(RA,Dec,z,vel_in=vels)
        if writeMC == 1:
            FILEt = open('/home/rumbaugh/temp/DStest.%s.tempdata.dat'%(names[i]),'w')
            FILEt.write('%f\n%f\n'%(P,Del))
            for iw in range(0,len(delta)): FILEt.write('%f\n'%(delta[iw]))
            FILEt.close()
    else:
        crt = read_file('/home/rumbaugh/temp/DStest.%s.tempdata.dat'%(names[i]))
        tempcol = copy_colvals(crt,'col1')
        P,Del = tempcol[0],tempcol[1]
        delta = tempcol[2:len(tempcol)]
    gBCG = np.where((BCGzs[BCGinds[i]] + 0.00004 > z) & (BCGzs[BCGinds[i]] - 0.00004 < z))
    gBCG = gBCG[0]
    BCGvel = vels[gBCG]
    print '%s:\n sig = %f using %i gals\n Del = %f - P = %f\n'%(names[i],sig,len(z),Del,P)
    pylab.xlabel('R.A. (J2000)')
    pylab.ylabel('Dec. (J2000)')
    for j in range(0,len(delta)):
        circsize = 25*m.exp(delta[j])
        if ((z[j] > avg_z-zsig) & (z[j] < avg_z+zsig)): 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color='red')
        elif ((z[j] < avg_z-sig/c) & (z[j] > avg_z+sig/c)): 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color=html_orng,linestyle='dashed')
        else: 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color='blue',linestyle='dotted')
    pylab.savefig('/home/rumbaugh/DSplot.%s.2.21.12.png'%(names2[i]))
    pylab.close('all')
    pylab.xlabel("Relative Recessional Velocity (km s$^{-1}$)")
    pylab.ylabel("Num. of Galaxies")
    pylab.xlim(-2250,2250)
    ymax = ymaxes[i]
    pylab.ylim(0,ymax)
    pylab.hist(vels,bins=9,facecolor='none',range=[-2250,2250])
    tempgaussx = np.arange(3200)*4500.0/3200-2250
    tempgaussy = np.zeros(3200)
    for it in range(0,3200): tempgaussy[it] = 500*(len(vels)/(sig*m.sqrt(2*m.pi)))*m.exp(-0.5*(tempgaussx[it]/sig)**2)
    pylab.plot(tempgaussx,tempgaussy,color='blue')
    BCGx = np.array([BCGvel,BCGvel,BCGvel+100,BCGvel,BCGvel-100,BCGvel,BCGvel])
    BCGy = np.array([ymax-1,ymax-2,ymax-1.75,ymax-2,ymax-1.75,ymax-2,ymax-1])
    pylab.plot(BCGx,BCGy,color='red')
    pylab.savefig('/home/rumbaugh/veldist.%s.2.21.12.png'%(names2[i]))
    pylab.close('all')

    
