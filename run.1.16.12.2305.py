import numpy as np
import math as m
import matplotlib
import matplotlib.pylab as pylab
import random as rand
execfile('/home/rumbaugh/FindCloseSources.py')
execfile('/home/rumbaugh/angconvert.py')

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.0])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.1])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22,])
cDs = np.array([26,52,35,29,57,39,22,56,7])
#centerRAs = np.array([((16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24])
#centerDecs = np.array([43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.84,0.89861,0.86531,1.1,1.1])
#1 Mpc = 3.06*0.7 Arcmin
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7

cnt = 1
for i in range(0,len(names)):
    if ((i == 3) | (i == 4) | (i == 5) | (i == 7)): cnt += 1
    if i == 7: cnt = 6
    sfile = '/home/rumbaugh/%s'%(files[cnt])
    cr = read_file(sfile)

    RA = get_colvals(cr,'col4')
    Dec = get_colvals(cr,'col5')
    #ACSRA = get_colvals(cr,'col14')
    #ACSDec = get_colvals(cr,'col15')
    #f606 = get_colvals(cr,'col16')
    #f814 = get_colvals(cr,'col17')
    LFCrB = get_colvals(cr,'col6')
    LFCiB = get_colvals(cr,'col7')
    zB = get_colvals(cr,'col8')
    z = get_colvals(cr,'col9')
    q = get_colvals(cr,'col11')

#iB = f814
#rB = f606
    iB = LFCiB
    rB = LFCrB

    #g = np.where((q > 2.2) & (z > 0.84) & (z < 0.96) & (iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
    g = np.where((q > 2.2) & (iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
    g = g[0]

    gall = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i]*60,RA[g],Dec[g],0)
    gz = np.where((z[g[gall]] > centerzs[i]-0.02) & (z[g[gall]] < centerzs[i]+0.02))
    #if i == 1: gz = np.where(z[g[gall]] > -1)
    if i == 1: gz = np.where((z[g[gall]] > 0.65) & (z[g[gall]] < 0.76))
    gz = gz[0]
    tempstars = np.zeros(len(gz))
    for jjj in range(0,len(gz)):
        tempstars[jjj] = 60*SphDist(RA[g[gall[gz[jjj]]]],Dec[g[gall[gz[jjj]]]],centerRAs[i],centerDecs[i])
    gr = np.where(rB[g[gall[gz]]]-iB[g[gall[gz]]] > rsb[cnt]-rsm[cnt]*iB[g[gall[gz]]]-rsNSTD[cnt]*rsSTD[cnt])
    gr = gr[0]
    gb = np.where((rB[g[gall[gz]]]-iB[g[gall[gz]]] < rsb[cnt]-rsm[cnt]*iB[g[gall[gz]]]-rsNSTD[cnt]*rsSTD[cnt]))
    gb = gb[0]
    RAcen = np.sum(RA[g[gall[gz]]]/iB[g[gall[gz]]])/np.sum(1.0/iB[g[gall[gz]]])
    Deccen = np.sum(Dec[g[gall[gz]]]/iB[g[gall[gz]]])/np.sum(1.0/iB[g[gall[gz]]])
    RAcen_r = np.sum(RA[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])/np.sum(1.0/iB[g[gall[gz[gr]]]])
    Deccen_r = np.sum(Dec[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])/np.sum(1.0/iB[g[gall[gz[gr]]]])
    RAcen_b = np.sum(RA[g[gall[gz[gb]]]]/iB[g[gall[gz[gb]]]])/np.sum(1.0/iB[g[gall[gz[gb]]]])
    Deccen_b = np.sum(Dec[g[gall[gz[gb]]]]/iB[g[gall[gz[gb]]]])/np.sum(1.0/iB[g[gall[gz[gb]]]])
    RAcen_rnw = np.sum(RA[g[gall[gz[gr]]]])/len(gr)
    Deccen_rnw = np.sum(Dec[g[gall[gz[gr]]]])/len(gr)
    RAcen_bnw = np.sum(RA[g[gall[gz[gb]]]])/len(gb)
    Deccen_bnw = np.sum(Dec[g[gall[gz[gb]]]])/len(gb)
    diff = 60*SphDist(RAcen_r,Deccen_r,RAcen_b,Deccen_b)
    diffnw = 60*SphDist(RAcen_rnw,Deccen_rnw,RAcen_bnw,Deccen_bnw)
    diffdist = np.zeros(1000)
    diffdistnw = np.zeros(1000)
    odiff = 60*SphDist(RAcen,Deccen,centerRAs[i],centerDecs[i])
    pylab.scatter(RA[g[gall[gz[gr]]]],Dec[g[gall[gz[gr]]]],color='red')
    pylab.scatter(RA[g[gall[gz[gb]]]],Dec[g[gall[gz[gb]]]],color='blue')
    pylab.savefig('/home/rumbaugh/spatplot.bycolor.%s.png'%(names[i]))
    pylab.close('all')
    for j in range(0,1000):
        rint = rand.randint(0,len(gr)+len(gb)-1)
        if rint < len(gr):
            tempRAcr = (np.sum(RA[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])-RA[g[gall[gz[gr[rint]]]]]/iB[g[gall[gz[gr[rint]]]]])/(np.sum(1.0/iB[g[gall[gz[gr]]]])-1.0/iB[g[gall[gz[gr[rint]]]]])
            tempRAcrnw = (np.sum(RA[g[gall[gz[gr]]]])-RA[g[gall[gz[gr[rint]]]]])/(len(gr)-1)
            tempDcr = (np.sum(Dec[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])-Dec[g[gall[gz[gr[rint]]]]]/iB[g[gall[gz[gr[rint]]]]])/(np.sum(1.0/iB[g[gall[gz[gr]]]])-1.0/iB[g[gall[gz[gr[rint]]]]])
            tempDcrnw = (Deccen_rnw*len(gr)-Dec[g[gall[gz[gr[rint]]]]])/(len(gr)-1)
            tempRAcb = RAcen_b
            tempRAcbnw = RAcen_bnw
            tempDcb = Deccen_b
            tempDcbnw = Deccen_bnw
        else:
            
            tempRAcr = RAcen_r
            tempRAcrnw = RAcen_rnw
            tempDcr = Deccen_r
            tempDcrnw = Deccen_rnw
            tempRAcb = (np.sum(RA[g[gall[gz[gb]]]]/iB[g[gall[gz[gb]]]])-RA[g[gall[gz[gb[rint-len(gr)]]]]]/iB[g[gall[gz[gb[rint-len(gr)]]]]])/(np.sum(1.0/iB[g[gall[gz[gb]]]])-1.0/iB[g[gall[gz[gb[rint-len(gr)]]]]])
            tempRAcbnw = (np.sum(RA[g[gall[gz[gb]]]])-RA[g[gall[gz[gb[rint-len(gr)]]]]])/(len(gb)-1)
            tempDcb = (np.sum(Dec[g[gall[gz[gb]]]]/iB[g[gall[gz[gb]]]])-Dec[g[gall[gz[gb[rint-len(gr)]]]]]/iB[g[gall[gz[gb[rint-len(gr)]]]]])/(np.sum(1.0/iB[g[gall[gz[gb]]]])-1.0/iB[g[gall[gz[gb[rint-len(gr)]]]]])
        diffdist[j] = 60*SphDist(tempRAcr,tempDcr,tempRAcb,tempDcb)
        diffdistnw[j] = 60*SphDist(tempRAcrnw,tempDcrnw,tempRAcbnw,tempDcbnw)
    sortdiffdist = np.sort(diffdist)
    sortdiffdistnw = np.sort(diffdistnw)
    RAcenh,RAcenm,RAcens = dec2hms(RAcen)
    Deccenh,Deccenm,Deccens = dec2dms(Deccen)
    numgals = len(gz)
    output = 0
    probblue = len(gb)*1.0/len(gz)
    execfile("/home/rumbaugh/runs/run.1.17.12.1545.py")
    percx = np.searchsorted(sort_diff_un_tot,odiff)
    perc = np.searchsorted(sort_diff_un,diff)
    percnw = np.searchsorted(sort_diff_un,diffnw)
    print '%s\nOverall Opt. Center: (%i %i %4.1f,%i %i %4.1f)\nOpt-Xray Offset (as): %f   Perc: %f\nNum. of Blue/Red Gals: (%i,%i)\nRed Center: (%f,%f)\nBlue Center: (%f,%f)\nDifference in as: %f +%f/-%f\nPercentile: %f\nNo Weights\nRed Center: (%f,%f)\nBlue Center: (%f,%f)\nDifference in as: %f +%f/-%f\nPercentile: %f\n'%(names[i],RAcenh,RAcenm,RAcens,Deccenh,Deccenm,Deccens,odiff,percx/100.0,len(gb),len(gr),RAcen_r,Deccen_r,RAcen_b,Deccen_b,diff,(sortdiffdist[np.searchsorted(sortdiffdist,diff)+333])-diff,diff-(sortdiffdist[np.searchsorted(sortdiffdist,diff)-333]),perc/100.0,RAcen_rnw,Deccen_rnw,RAcen_bnw,Deccen_bnw,diffnw,(sortdiffdistnw[np.searchsorted(sortdiffdistnw,diffnw)+333])-diffnw,diffnw-(sortdiffdistnw[np.searchsorted(sortdiffdistnw,diffnw)-333]),percnw/100.0)
    if i == 0:
        allstardist = tempstars
    else:
        allstardist = np.append(allstardist,tempstars)
pylab.hist(allstardist,bins=20)
pylab.savefig('/home/rumbaugh/allstardisthist.png')
pylab.close('all')
           
                  
             
    
    

