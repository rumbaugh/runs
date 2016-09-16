execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/biweight.py")
execfile("/home/rumbaugh/DStest.py")
execfile('/home/rumbaugh/angconvert.py')
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

degree_symbol = unichr(176)
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'
html_pink = '#FF00FF'

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


rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
ymaxes = np.array([11,11,8]) 
ccnt = np.array([2,3,6])

for i in range(0,len(names)):
    cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    royID = copy_colvals(cr,'col1')
    RA = copy_colvals(cr,'col2')
    Dec = copy_colvals(cr,'col3')
    z = copy_colvals(cr,'col4')
    vels = copy_colvals(cr,'col5')
    delta = np.zeros(len(z))
    avg_v = c*biweight_loc(z)
    avg_z = avg_v/c
    #sig = np.std(vels)
    #print 'a'
    sig = biweight_scale(vels)
    zsig = sig*(1+avg_z)/c
    crs = read_file('/home/rumbaugh/%s'%(files[ccnt[i]]))
    sID = copy_colvals(crs,'col1')
    sLFCrB = copy_colvals(crs,'col6')
    sLFCiB = copy_colvals(crs,'col7')
    szB = copy_colvals(crs,'col8')
    sz = copy_colvals(crs,'col9')
    siB = sLFCiB
    srB = sLFCrB
    #print 'b'
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
    #print 'c'
    gBCG = np.where((BCGzs[BCGinds[i]] + 0.00004 > z) & (BCGzs[BCGinds[i]] - 0.00004 < z))
    gBCG = gBCG[0]
    BCGvel = vels[gBCG]
    print '%s:\n sig = %f using %i gals\n Del = %f - P = %f\n'%(names[i],sig,len(z),Del,P)
    pylab.xlabel('R.A. (J2000)')
    pylab.ylabel('Dec. (J2000)')
    if i == 1:
        pylab.xlim(275.50004353025524,275.28195646974466)
        pylab.ylim(68.43,68.51)
        xlocs = (np.arange(4)+1)*360.0/24/60/60*15+275.25
        xlabs = np.array(['18$^{h}$21$^{m}$15$^{s}$','30$^{s}$','45$^{s}$','22$^{m}$00$^{s}$'])
        ylocs = (np.arange(5)+1)/60.0+68+25/60.0
        ylabs = np.array(['68' + degree_symbol + "26'","27'","28'","29'","30'"])
    if i == 0:
        pylab.xlim(269.45285292808654,269.22714707191341)
        pylab.ylim(66.49,66.58)
        xlocs = (np.arange(4)+0)*360.0/24/60/60*15+269.25
        xlabs = np.array(['17$^{h}$57$^{m}$00$^{s}$','15$^{s}$','30$^{s}$','45$^{s}$'])
        ylocs = (np.arange(5)+0)/60.0+66+30/60.0
        ylabs = np.array(['68' + degree_symbol + "30'","31'","32'","33'","34'"])
    if i == 2:
        pylab.xlim(137.73651039108756,137.63348960891244)
        pylab.ylim(54.34,54.4)
        xlocs = (np.arange(2)+4)*360.0/24/60/60*10+137.5
        xlabs = np.array(['9$^{h}$10$^{m}$30$^{s}$','40$^{s}$'])
        ylocs = (np.arange(4)+1)/60.0+54+20/60.0
        ylabs = np.array(['54' + degree_symbol + "21'","22'","23'","24'"])
    pylab.yticks(ylocs,ylabs)
    pylab.xticks(xlocs,xlabs)
    for j in range(0,len(delta)):
        circsize = 25*m.exp(delta[j])
        if ((z[j] > avg_z-zsig) & (z[j] < avg_z+zsig)): 
            tx = pylab.cos(pylab.linspace(0,2*m.pi,50)).tolist()
            ty = pylab.sin(pylab.linspace(0,2*m.pi,50)).tolist()
            xy1 = zip(tx,ty)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors='red')
        elif ((z[j] < avg_z-sig/c)):
            #pylab.scatter(RA[j],Dec[j],s=circsize,facecolors=html_teal,edgecolor='black')
            tr = m.sqrt(circsize/m.pi)
            tx = [0] + pylab.cos(pylab.linspace(0,2*m.pi*0.25,50)).tolist()
            ty = [0] + pylab.sin(pylab.linspace(0,2*m.pi*0.25,50)).tolist()
            xy1 = zip(tx,ty)
            tx = [0] + pylab.cos(pylab.linspace(2*m.pi*0.25,2*m.pi*0.5,50)).tolist()
            ty = [0] + pylab.sin(pylab.linspace(2*m.pi*0.25,2*m.pi*0.5,50)).tolist()
            xy2 = zip(tx,ty)
            tx = [0] + pylab.cos(pylab.linspace(2*m.pi*0.5,2*m.pi*0.75,50)).tolist()
            ty = [0] + pylab.sin(pylab.linspace(2*m.pi*0.5,2*m.pi*0.75,50)).tolist()
            xy3 = zip(tx,ty)
            tx = [0] + pylab.cos(pylab.linspace(2*m.pi*0.75,2*m.pi,50)).tolist()
            ty = [0] + pylab.sin(pylab.linspace(2*m.pi*0.75,2*m.pi,50)).tolist()
            xy4 = zip(tx,ty)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy2,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy3,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy4,0),facecolors='none',edgecolors=html_teal)
        else:
            tx = pylab.cos(pylab.linspace(0,2*m.pi,50)).tolist()
            ty = pylab.sin(pylab.linspace(0,2*m.pi,50)).tolist()
            xy1 = zip(tx,ty)
            pylab.scatter(RA[j],Dec[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors='blue',linestyle='dotted')
    pylab.savefig('/home/rumbaugh/DSplot.%s.2.21.12.png'%(names2[i]))
    pylab.close('all')
    #print 'd'
    nep5281newcnt = 0
    garr = np.zeros(len(vels),dtype='int8')
    isnew = np.zeros(len(vels))
    for iv in range(0,len(vels)):
        #gat = np.where((sz + 0.00004 > z[iv]) & (sz - 0.00004 < z[iv]))
        gat = np.where(sID == royID[iv])
        if i == 1: gat = np.where(sID == str(int(royID[iv])))
        gat = gat[0]
        #if len(gat) == 0: sys.exit("Couldn't find galaxy redshift in spectroscopic file")
        #if len(gat) > 1.1: sys.exit("Multiple matches to galaxy redshift tin spectroscopic file")
        if len(gat) == 0: 
            if i != 1:
                sys.exit("Couldn't find galaxy ID in spectroscopic file")
            else:
                nep5281newcnt += 1
                isnew[iv] = 1
                if nep5281newcnt > 4.1: sys.exit("Found more than 4 new 5281 members")
        if len(gat) > 1.1: 
            gat2 = np.where((sz[gat] + 0.00004 > z[iv]) & (sz[gat] - 0.00004 < z[iv]))
            gat2 = gat2[0]
            if len(gat2) == 0: sys.exit("Multiple matches to galaxy ID, but no matches to redshift, in spectroscopic file")
            if len(gat2) > 1.1: 
                #sys.exit("Multiple matches to galaxy ID and redshift in spectroscopic file")
                print "%s: Multiple matches to galaxy ID (%s) and redshift in spectroscopic file\niB = (%f,%f)\nrB = (%f,%f)\n"%(names2[i],sID[gat[0]],siB[gat[0]],siB[gat[1]],srB[gat[0]],srB[gat[1]])
                if len(gat2) > 2.1: sys.exit("More than 2 matches to galaxy ID and redshift in spectroscopic file")
        if isnew[iv] == 0: garr[iv] = gat[0]
        if len(gat) > 1.1: garr[iv] = gat[gat2[0]]
    #print 'e'
    if ccnt[i] != 6:
        gred = np.where((srB[garr]-siB[garr] > rsb[ccnt[i]]-rsm[ccnt[i]]*siB[garr]-rsNSTD[ccnt[i]]*rsSTD[ccnt[i]]) & (isnew == 0))
    else:
        gred = np.where((siB[garr]-szB[garr] > rsb[ccnt[i]]-rsm[ccnt[i]]*szB[garr]-rsNSTD[ccnt[i]]*rsSTD[ccnt[i]]) & (isnew == 0))
    if ccnt[i] != 6:
        gblu = np.where((srB[garr]-siB[garr] < rsb[ccnt[i]]-rsm[ccnt[i]]*siB[garr]-rsNSTD[ccnt[i]]*rsSTD[ccnt[i]]) & (isnew == 0))
    else:
        gblu = np.where((siB[garr]-szB[garr] < rsb[ccnt[i]]-rsm[ccnt[i]]*szB[garr]-rsNSTD[ccnt[i]]*rsSTD[ccnt[i]]) & (isnew == 0))
    #print 'f'
    gblu = gblu[0]
    gred = gred[0]
    pylab.xlabel("Relative Recessional Velocity (km s$^{-1}$)")
    pylab.ylabel("Num. of Galaxies")
    pylab.xlim(-2250,2250)
    ymax = ymaxes[i]
    pylab.ylim(0,ymax)
    pylab.hist(vels,bins=9,facecolor='none',range=[-2250,2250])
    if ((len(gblu) >= 8) & (len(gred) >= 8)):
        pylab.hist(vels[gblu],bins=9,facecolor='none',edgecolor='blue',range=[-2250,2250])
        pylab.hist(vels[gred],bins=9,facecolor='none',edgecolor='red',range=[-2250,2250])
    #print 'g'
    if ((len(gblu) >= 8) & (len(gred) >= 8)): 
        blusig = biweight_scale(vels[gblu])
        redsig = biweight_scale(vels[gred])
        blumean = biweight_loc(vels[gblu])
        redmean = biweight_loc(vels[gred])
    tempgaussx = np.arange(3200)*4500.0/3200-2250
    tempgaussy = np.zeros(3200)
    for it in range(0,3200): tempgaussy[it] = 500*(len(vels)/(sig*m.sqrt(2*m.pi)))*m.exp(-0.5*(tempgaussx[it]/sig)**2)
    pylab.plot(tempgaussx,tempgaussy,color='cyan')
    tempgaussy = np.zeros(3200)
    for it in range(0,3200): tempgaussy[it] = 500*(len(gblu)/(blusig*m.sqrt(2*m.pi)))*m.exp(-0.5*((tempgaussx[it]-blumean)/blusig)**2)
    if ((len(gblu) >= 8) & (len(gred) >= 8)): pylab.plot(tempgaussx,tempgaussy,color='blue')
    tempgaussy = np.zeros(3200)
    for it in range(0,3200): tempgaussy[it] = 500*(len(gred)/(redsig*m.sqrt(2*m.pi)))*m.exp(-0.5*((tempgaussx[it]-redmean)/redsig)**2)
    #print 'h'
    if ((len(gblu) >= 8) & (len(gred) >= 8)): pylab.plot(tempgaussx,tempgaussy,color='red')
    BCGx = np.array([BCGvel,BCGvel,BCGvel+100,BCGvel,BCGvel-100,BCGvel,BCGvel])
    BCGy = np.array([ymax-1,ymax-2,ymax-1.75,ymax-2,ymax-1.75,ymax-2,ymax-1])
    pylab.plot(BCGx,BCGy,color='red')
    pylab.savefig('/home/rumbaugh/veldist.redblu.%s.2.21.12.png'%(names2[i]))
    pylab.close('all')
    FILEidl1 = open('/home/rumbaugh/temp/idl_clusprops.%s.2.21.12.dat'%(names2[i]),'w')
    FILEidl1.write('%f %f %f %f'%(sig,blusig,redsig,BCGvel))
    FILEidl1.close()
    FILEidl2 = open('/home/rumbaugh/temp/idl_vels.%s.2.21.12.dat'%(names2[i]),'w')
    for iidl in range(0,len(z)):
        isblu = 0
        if srB[garr[iidl]]-siB[garr[iidl]] < rsb[ccnt[i]]-rsm[ccnt[i]]*siB[garr[iidl]]-rsNSTD[ccnt[i]]*rsSTD[ccnt[i]]: isblu = 1
        if isnew[iidl] == 1: isblu = 2
        FILEidl2.write('%f %f %i\n'%(vels[iidl],delta[iidl],isblu))
    FILEidl2.close()
    

    
