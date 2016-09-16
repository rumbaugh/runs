execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/scale_estimators.py")
execfile("/home/rumbaugh/DStest.py")
execfile('/home/rumbaugh/angconvert.py')
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

def sigclip(data,mean,sig,sigthresh=3.0):
    gsc = np.where((data < mean + sigthresh*sig) & (data > mean - sigthresh*sig))
    gsc = gsc[0]
    #if ccnt == 6:
    #    print mean,sig,data[gsc]
    return gsc

degree_symbol = unichr(176)
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'
html_pink = '#FF00FF'

zlb = [0.82,0.65,0.68,0.805,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.83,0.96,0.96,1.2]

try:
    skipMC
except NameError:
    skipMC = 1
try:
    writeMC
except NameError:
    writeMC = 1

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
#files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.T08needstoberedone.nodups.cat']
files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','newcats/FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','newcats/FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','newcats/FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.plusT08.nodups.cat']
RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.383771,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.471189,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])
names2 = np.array(['RXJ1757','RXJ1821','Cl0910+5422'])
#names = np.array(['nep200','nep5281','cl0910'])

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])

BCGfile = '/home/rumbaugh/BCGpositions.2.15.12.dat'
crBCG = read_file(BCGfile)
BCGRA = copy_colvals(crBCG,'col2')
BCGDec = copy_colvals(crBCG,'col3')
BCGzs = copy_colvals(crBCG,'col7')
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7
ccnt = 0

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
ymaxes = np.array([20,20,20,20,20,20,20,20,20]) 
#ccnt = np.array([2,3,6])
ccnt=0
FILEo = open('/home/rumbaugh/DStest_output.5.1.12.dat','w')
FILE3 = open('/home/rumbaugh/veldisp_output.5.1.12.dat','w')
for i in range(0,len(names)):
    #cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    #royID = copy_colvals(cr,'col1')
    #RA = copy_colvals(cr,'col2')
    #Dec = copy_colvals(cr,'col3')
    #z = copy_colvals(cr,'col4')
    #vels = copy_colvals(cr,'col5')
    if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
    if i == 5: ccnt += 1
    sfile = '/home/rumbaugh/%s'%(files[ccnt])
    crs = read_file(sfile)
    sID = copy_colvals(crs,'col1')
    sslit = copy_colvals(crs,'col3')
    smask = copy_colvals(crs,'col2')
    sRA = copy_colvals(crs,'col4')
    sDec = copy_colvals(crs,'col5')
    sLFCrB = copy_colvals(crs,'col6')
    sLFCiB = copy_colvals(crs,'col7')
    RA,Dec = np.copy(sRA),np.copy(sDec)
    if ((i == 5) | (i == 6)):
        ACSRA = copy_colvals(crs,'col14')
        ACSDec = copy_colvals(crs,'col15')
        sf606 = copy_colvals(crs,'col17')
        sf814 = copy_colvals(crs,'col18')
        srB,siB = np.copy(sf606),np.copy(sf814)
    else:
        srB,siB = np.copy(sLFCrB),np.copy(sLFCiB)
    szB = copy_colvals(crs,'col8')
    z = copy_colvals(crs,'col9')
    sz = np.copy(z)
    #vels = sz*3*10**5
    sq = copy_colvals(crs,'col11')
    q = np.copy(sq)
    g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]))
    if names[i] == "RXJ1757": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((smask != 'N200M1') | (sslit != 64)) & ((smask != 'N200M1') | (sslit != 67)) & ((smask != 'N200M1') | (sslit != 80)) & ((smask != 'N200M1') | (sslit != 83)))
    if names[i] == "RXJ1821": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((z < 0.80721891) | (z > 0.80721901)))
    if names[i] == "Cl1604A": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC2_06516") | (z > 0.9)))
    if names[i] == "Cl1604B": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC1_01472") | (z < 0.87)))
    g = g[0]
    dists = np.zeros(len(g))
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],RGalPeakRA[i],RGalPeakDec[i])
    gRGP = np.where(dists < srchdist[i])
    gRGP = gRGP[0]
    vels = (z[g[gRGP]]-biweight_loc(z[g[gRGP]]))*c/(1+z[g[gRGP]])
    avg_v = biweight_loc(vels)
    #sig = np.std(vels)
    #print 'a'
    sig = biweight_scale(vels)
    prevRGP = 9999
    gRGPtemp = np.arange(len(gRGP))
    meanRGP = biweight_loc(vels)
    velstemp = np.copy(vels)
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velstemp,meanRGP,sig)
        velstemp = (z[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velstemp[gRGPtemp])
        sig,sige = biweight_scale(velstemp[gRGPtemp],ConfInv=1)
        #if ccnt == 6: print meanRGP,sig,velstemp[gRGPtemp]
    #print np.sort(sID[g[gRGP[gRGPtemp]]])
    znew = sz[g[gRGP[gRGPtemp]]]
    RAnew = RA[g[gRGP[gRGPtemp]]]
    Decnew = Dec[g[gRGP[gRGPtemp]]]
    srBnew = srB[g[gRGP[gRGPtemp]]]
    siBnew = siB[g[gRGP[gRGPtemp]]]
    szBnew = szB[g[gRGP[gRGPtemp]]]
    #print sID[g[gRGP[gRGPtemp]]]
    for isid in range(0,len(gRGPtemp)):
        gsid = np.where(sID[g[gRGP[gRGPtemp]]] == sID[g[gRGP[gRGPtemp[isid]]]])
        gsid = gsid[0]
        #if len(gsid) > 1.1: print sID[g[gRGP[gRGPtemp[gsid]]]],smask[g[gRGP[gRGPtemp[gsid]]]],sslit[g[gRGP[gRGPtemp[gsid]]]]
    vels = np.copy(velstemp)
    avg_z = biweight_loc(z[g[gRGP[gRGPtemp]]])
    zsig = sig*(1+avg_z)/c
    #print 'b'
    gq = np.where(sq > 2.2)
    if names[i] == "RXJ1757": gq = np.where((sq > 2.2) & ((smask != 'N200M1') | (sslit != 64)) & ((smask != 'N200M1') | (sslit != 67)) & ((smask != 'N200M1') | (sslit != 80)) & ((smask != 'N200M1') | (sslit != 83)))
    if names[i] == "RXJ1821": gq = np.where((sq > 2.2) & ((z < 0.80721891) | (z > 0.80721901)))
    if names[i] == "Cl1604A": gq = np.where((sq > 2.2) & ((sID != "LFC_SC2_06516") | (z > 0.9)))
    if names[i] == "Cl1604B": gq = np.where((sq > 2.2) & ((sID != "LFC_SC1_01472") | (z < 0.87)))
    gq = gq[0]
    dists2 = np.zeros(len(gq))
    for j in range(0,len(gq)): dists2[j] = SphDist(sRA[gq[j]],sDec[gq[j]],RGalPeakRA[i],RGalPeakDec[i])
    gd2 = np.where(dists2 < srchdist[i])
    velstemp2 =  (z[gq]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[gq])
    #velstemp2 =  (z[gq]-np.average(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[gq])
    if names[i] != "RXJ1821": 
        gRGP2 = np.where((velstemp2 < 3000) & (velstemp2 > -3000) & (dists2 < srchdist[i]))
        gRGP2 = gRGP2[0]
        gRGPtemp = np.arange(len(gRGP2))
        meanRGP = biweight_loc(velstemp2[gRGP2])
        velstemp2 = velstemp2[gRGP2]
        sig = biweight_scale(velstemp2)
        prevRGP=9999
        while len(gRGPtemp) < prevRGP:
            prevRGP = len(gRGPtemp)
            gRGPtemp = sigclip(velstemp2,meanRGP,sig)
            velstemp2 = (z[gq[gRGP2]]-biweight_loc(sz[gq[gRGP2[gRGPtemp]]]))*(3.0*10**5)/(1+sz[gq[gRGP2]])
            meanRGP = biweight_loc(velstemp2[gRGPtemp])
            sig = biweight_scale(velstemp2[gRGPtemp])
        np.sort(sID[gq[gRGP2[gRGPtemp]]])
        znew = sz[gq[gRGP2[gRGPtemp]]]
        srBnew = srB[gq[gRGP2[gRGPtemp]]]
        siBnew = siB[gq[gRGP2[gRGPtemp]]]
        szBnew = szB[gq[gRGP2[gRGPtemp]]]
        RAnew = RA[gq[gRGP2[gRGPtemp]]]
        Decnew = Dec[gq[gRGP2[gRGPtemp]]]
        vels = np.copy(velstemp2)
        sig,sige = biweight_scale(velstemp2[gRGPtemp],ConfInv=1,ConfInvTrials=10000)
    delta = np.zeros(len(gRGPtemp))
    if skipMC == 0:
        Del,P,delta = DStest(RAnew,Decnew,znew,vel_in=vels[gRGPtemp])
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
        FILEo.write('%s %f %f %i\n'%(names[i],P,Del,len(gRGPtemp)))
    #print 'c'
    gBCG = np.where((BCGzs[i] + 0.00004 > znew) & (BCGzs[i] - 0.00004 < znew))
    gBCG = gBCG[0]
    if len(gBCG) > 1: gBCG = gBCG[0]
    BCGvel = vels[gRGPtemp[gBCG]]
    #print '%s:\n sig = %f +/- %f \nusing %i gals\n Del = %f - P = %f\n'%(names[i],sig,sige,len(gRGPtemp),Del,P)
    #print biweight_loc(znew)
    matplotlib.rcParams['figure.figsize'] = [7,7]
    fig = matplotlib.figure.Figure()
    pylab.xlabel('R.A. (J2000)')
    pylab.ylabel('Dec. (J2000)')
    pylab.title(names[i])
    if names[i] == 'RXJ1821':
        pylab.xlim(275.50004353025524,275.28195646974466)
        pylab.ylim(68.43,68.51)
        xlocs = (np.arange(4)+1)*360.0/24/60/60*15+275.25
        xlabs = np.array(['18$^{h}$21$^{m}$15$^{s}$','30$^{s}$','45$^{s}$','22$^{m}$00$^{s}$'])
        ylocs = (np.arange(5)+1)/60.0+68+25/60.0
        ylabs = np.array(['68' + degree_symbol + "26'","27'","28'","29'","30'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == "RXJ1757":
        pylab.xlim(269.45285292808654,269.22714707191341)
        pylab.ylim(66.482,66.572)
        xlocs = (np.arange(4)+0)*360.0/24/60/60*15+269.25
        xlabs = np.array(['17$^{h}$57$^{m}$00$^{s}$','15$^{s}$','30$^{s}$','45$^{s}$'])
        ylocs = (np.arange(6)+0)/60.0+66+29/60.0
        ylabs = np.array(['68' + degree_symbol + "29'","30'","31'","32'","33'","34'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == "RXJ0910+5422":
        pylab.xlim(137.74503696960534,137.62496303039467)
        pylab.ylim(54.337,54.407)
        xlocs = (np.arange(6))*360.0/24/60/60*5+(9+10.5/60)*360.0/24
        xlabs = np.array(['9$^{h}$10$^{m}$30$^{s}$','35$^{s}$','40$^{s}$','45$^{s}$','50$^{s}$','55$^{s}$'])
        ylocs = (np.arange(4)+1)/60.0+54+20/60.0
        ylabs = np.array(['54' + degree_symbol + "21'","22'","23'","24'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'Cl1324+3011':
        pylab.xlim(201.24428157607926,201.15171842392076)
        pylab.ylim(30.16,30.240)
        xlocs = (np.arange(4))*360.0/24/60/60*5+360/24.0*(13+(24+40/60.0)/60.0)
        xlabs = np.array(['13$^{h}$24$^{m}$40$^{s}$','45$^{s}$','50$^{s}$','55$^{s}$'])
        ylocs = (np.arange(5))/60.0+30+10/60.0
        ylabs = np.array(['30' + degree_symbol + "10'","11'","12'","13'","14'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'Cl1324+3013':
        pylab.xlim(201.12749900191645,201.05750099808355)
        pylab.ylim(30.19,30.25001)
        xlocs = (np.arange(4))*360.0/24/60/60*5+360/24.0*(13+(24+15/60.0)/60.0)
        xlabs = np.array(['13$^{h}$24$^{m}$15$^{s}$','20$^{s}$','25$^{s}$','30$^{s}$'])
        ylocs = (np.arange(4))/60.0+30+12/60.0
        ylabs = np.array(['30' + degree_symbol + "12'","13'","14'","15'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'Cl1324+3059':
        pylab.xlim(201.24083216890253,201.15916783109745)
        pylab.ylim(30.93,31.000001)
        xlocs = (np.arange(4))*360.0/24/60/60*5+360/24.0*(13+(24+40/60.0)/60.0)
        xlabs = np.array(['13$^{h}$24$^{m}$40$^{s}$','45$^{s}$','50$^{s}$','55$^{s}$'])
        ylocs = (np.arange(5))/60.0+30+56/60.0
        ylabs = np.array(['30' + degree_symbol + "56'","57'","58'","59'",'31' + degree_symbol + "00'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'Cl1604A':
        pylab.xlim(241.12760150518022,241.05239849481978)
        pylab.ylim(43.06,43.115)
        xlocs = (np.arange(4))*360.0/24/60/60*5+360/24.0*(16+(4+15/60.0)/60.0)
        xlabs = np.array(['16$^{h}$04$^{m}$15$^{s}$','20$^{s}$','25$^{s}$','30$^{s}$'])
        ylocs = (np.arange(3))/60.0+43+4/60.0
        ylabs = np.array(['43' + degree_symbol + "04'","5'","6'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'Cl1604B':
        pylab.xlim(241.1615867973577,241.04841320264234)
        pylab.ylim(43.1925,43.2750001)
        xlocs = (np.arange(5))*360.0/24/60/60*5+360/24.0*(16+(4+15/60.0)/60.0)
        xlabs = np.array(['16$^{h}$04$^{m}$15$^{s}$','20$^{s}$','25$^{s}$','30$^{s}$','35$^{s}$'])
        ylocs = (np.arange(5))/60.0+43+12/60.0
        ylabs = np.array(['43' + degree_symbol + "12'","13'","14'","15'","16'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    if names[i] == 'RXJ0910+5419':
        pylab.xlim(137.575,137.46)
        pylab.ylim(54.277696380347031,54.344803619652971)
        xlocs = (np.arange(5))*360.0/24/60/60*5+360/24.0*(9+(9+55/60.0)/60.0)
        xlabs = np.array(['9$^{h}$09$^{m}$55$^{s}$','9$^{h}$10$^{m}$00$^{s}$','5$^{s}$','10$^{s}$','15$^{s}$'])
        ylocs = (np.arange(4))/60.0+54+17/60.0
        ylabs = np.array(['54' + degree_symbol + "17'","18'","19'","20'"])
        pylab.yticks(ylocs,ylabs)
        pylab.xticks(xlocs,xlabs)
    for j in range(0,len(delta)):
        circsize = 25*m.exp(1.0*delta[j])
        if ((znew[j] > avg_z-zsig) & (znew[j] < avg_z+zsig)): 
            tx = pylab.cos(pylab.linspace(0,2*m.pi,50)).tolist()
            ty = pylab.sin(pylab.linspace(0,2*m.pi,50)).tolist()
            xy1 = zip(tx,ty)
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors='red')
        elif ((znew[j] < avg_z-zsig)):
            #pylab.scatter(RAnew[j],Decnew[j],s=circsize,facecolors=html_teal,edgecolor='black')
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
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy2,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy3,0),facecolors='none',edgecolors=html_teal)
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy4,0),facecolors='none',edgecolors=html_teal)
        else:
            tx = pylab.cos(pylab.linspace(0,2*m.pi,50)).tolist()
            ty = pylab.sin(pylab.linspace(0,2*m.pi,50)).tolist()
            xy1 = zip(tx,ty)
            pylab.scatter(RAnew[j],Decnew[j],s=0.25*circsize,marker=(xy1,0),facecolors='none',edgecolors='blue',linestyle='dotted')
    pylab.scatter([BCGRA[i]],[BCGDec[i]],marker='x',edgecolors='blue',s=75,lw=2)
    pylab.scatter([centerRAs[i]],[centerDecs[i]],marker='s',edgecolors=html_brwn,facecolors='none',s=75,lw=2)
    pylab.scatter([RGalPeakRA[i]],[RGalPeakDec[i]],marker='d',edgecolors=html_purp,facecolors='none',s=75,lw=2)
    pylab.savefig('/home/rumbaugh/DSplot.%s.5.1.12.png'%(names[i]))
    pylab.close('all')
    #print 'd'
    #nep5281newcnt = 0
    #garr = np.zeros(len(vels),dtype='int8')
    #isnew = np.zeros(len(vels))
    #for iv in range(0,len(vels)):
        #gat = np.where((sz + 0.00004 > z[iv]) & (sz - 0.00004 < z[iv]))
        #gat = np.where(sID == royID[iv])
        #if i == 1: gat = np.where(sID == str(int(royID[iv])))
        #gat = gat[0]
        #if len(gat) == 0: sys.exit("Couldn't find galaxy redshift in spectroscopic file")
        #if len(gat) > 1.1: sys.exit("Multiple matches to galaxy redshift tin spectroscopic file")
    #    if len(gat) == 0: 
    #        if i != 1:
    #            sys.exit("Couldn't find galaxy ID in spectroscopic file")
    #        else:
    #            nep5281newcnt += 1
    #            isnew[iv] = 1
    #            if nep5281newcnt > 4.1: sys.exit("Found more than 4 new 5281 members")
    #    if len(gat) > 1.1: 
    #        gat2 = np.where((sz[gat] + 0.00004 > z[iv]) & (sz[gat] - 0.00004 < z[iv]))
    #        gat2 = gat2[0]
    #        if len(gat2) == 0: sys.exit("Multiple matches to galaxy ID, but no matches to redshift, in spectroscopic file")
    #        if len(gat2) > 1.1: 
                #sys.exit("Multiple matches to galaxy ID and redshift in spectroscopic file")
    #            print "%s: Multiple matches to galaxy ID (%s) and redshift in spectroscopic file\niB = (%f,%f)\nrB = (%f,%f)\n"%(names2[i],sID[gat[0]],siB[gat[0]],siB[gat[1]],srB[gat[0]],srB[gat[1]])
    #            if len(gat2) > 2.1: sys.exit("More than 2 matches to galaxy ID and redshift in spectroscopic file")
    #    if isnew[iv] == 0: garr[iv] = gat[0]
    #    if len(gat) > 1.1: garr[iv] = gat[gat2[0]]
    #print 'e'
    if ccnt != 6:
        gred = np.where((srBnew-siBnew > rsb[ccnt]-rsm[ccnt]*siBnew-rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        gred = np.where((siBnew-szBnew > rsb[ccnt]-rsm[ccnt]*szBnew-rsNSTD[ccnt]*rsSTD[ccnt]))
    if ccnt != 6:
        gblu = np.where((srBnew-siBnew < rsb[ccnt]-rsm[ccnt]*siBnew-rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        gblu = np.where((siBnew-szBnew < rsb[ccnt]-rsm[ccnt]*szBnew-rsNSTD[ccnt]*rsSTD[ccnt]))
    #print 'f'
    gblu = gblu[0]
    gred = gred[0]
    pylab.xlabel("Relative Recessional Velocity (km s$^{-1}$)")
    pylab.ylabel("Num. of Galaxies")
    pylab.xlim(-2250,2250)
    ymax = ymaxes[i]
    pylab.ylim(0,ymax)
    pylab.hist(vels[gRGPtemp],bins=9,facecolor='none',range=[-2250,2250])
    if ((len(gblu) >= 8) & (len(gred) >= 8)):
        pylab.hist(vels[gRGPtemp[gblu]],bins=9,facecolor='none',edgecolor='blue',range=[-2250,2250])
        pylab.hist(vels[gRGPtemp[gred]],bins=9,facecolor='none',edgecolor='red',range=[-2250,2250])
    #print 'g'
    enoughBoR = 0
    if ((len(gblu) >= 8) & (len(gred) >= 8)): 
        enoughBoR = 1
        blusig = biweight_scale(vels[gRGPtemp[gblu]])
        redsig = biweight_scale(vels[gRGPtemp[gred]])
        blumean = biweight_loc(vels[gRGPtemp[gblu]])
        redmean = biweight_loc(vels[gRGPtemp[gred]])
    #print names[i],len(gblu),len(gred),names[i]
    tempgaussx = np.arange(3200)*4500.0/3200-2250
    tempgaussy = np.zeros(3200)
    for it in range(0,3200): tempgaussy[it] = 500*(len(vels[gRGPtemp])/(sig*m.sqrt(2*m.pi)))*m.exp(-0.5*(tempgaussx[it]/sig)**2)
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
    pylab.savefig('/home/rumbaugh/veldist.redblu.%s.5.1.12.png'%(names[i]))
    pylab.close('all')
    FILEidl1 = open('/home/rumbaugh/temp/idl_clusprops.%s.5.1.12.dat'%(names[i]),'w')
    if enoughBoR == 1:
        FILEidl1.write('%f %f %f %f'%(sig,blusig,redsig,BCGvel))
        print names[i],blusig,redsig
    else:
        FILEidl1.write('%f %f %f %f'%(sig,-1,-1,BCGvel))
    FILEidl1.close()
    FILEidl2 = open('/home/rumbaugh/temp/idl_vels.%s.5.1.12.dat'%(names[i]),'w')
    for iidl in range(0,len(gRGPtemp)):
        isblu = 0
        if ccnt == 6:
            if siBnew[iidl]-szBnew[iidl] < rsb[ccnt]-rsm[ccnt]*szBnew[iidl]-rsNSTD[ccnt]*rsSTD[ccnt]: isblu = 1
        else:
            if srBnew[iidl]-siBnew[iidl] < rsb[ccnt]-rsm[ccnt]*siBnew[iidl]-rsNSTD[ccnt]*rsSTD[ccnt]: isblu = 1
        #if isnew[iidl] == 1: isblu = 2
        FILEidl2.write('%f %f %i\n'%(vels[gRGPtemp[iidl]],delta[iidl],isblu))
    FILEidl2.close()
    if enoughBoR == 1:
        FILE3.write("%s %f %f %f %i %i\n"%(names[i],sig,blusig,redsig,len(gblu),len(gred)))
    else:
        FILE3.write("%s %f %f %f %i %i\n"%(names[i],sig,0,0,len(gblu),len(gred)))
FILEo.close()
FILE3.close()
    

    
