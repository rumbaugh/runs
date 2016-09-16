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
#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
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
zlb = [0.82,0.65,0.68,0.80,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.84,0.96,0.96,1.2]

cnt = 1
for i in range(0,len(names)):
    if ((i == 3) | (i == 4) | (i == 5) | (i == 7)): cnt += 1
    if i == 5: cnt += 1
    sfile = '/home/rumbaugh/%s'%(files[cnt])
    cr = read_file(sfile)

    RA = get_colvals(cr,'col4')
    Dec = get_colvals(cr,'col5')
    if ((i == 5) | (i == 6)):
        ACSRA = get_colvals(cr,'col14')
        ACSDec = get_colvals(cr,'col15')
        f606 = get_colvals(cr,'col17')
        f814 = get_colvals(cr,'col18')
    LFCrB = get_colvals(cr,'col6')
    LFCiB = get_colvals(cr,'col7')
    zB = get_colvals(cr,'col8')
    z = get_colvals(cr,'col9')
    q = get_colvals(cr,'col11')
    iB = LFCiB
    rB = LFCrB
    if ((i == 5) | (i == 6)):
        iB = f814
        rB = f606

    #g = np.where((q > 2.2) & (z > 0.84) & (z < 0.96) & (iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
    g = np.where((q > 2.2) & (iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
    g = g[0]

    gall = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i]*60,RA[g],Dec[g],0)
    gz = np.where((z[g[gall]] > zlb[cnt]) & (z[g[gall]] < zub[cnt]))
    gz = gz[0]
    tempstars = np.zeros(len(gz))
    for jjj in range(0,len(gz)):
        tempstars[jjj] = 60*SphDist(RA[g[gall[gz[jjj]]]],Dec[g[gall[gz[jjj]]]],centerRAs[i],centerDecs[i])
    gr = np.where(rB[g[gall[gz]]]-iB[g[gall[gz]]] > rsb[cnt]-rsm[cnt]*iB[g[gall[gz]]]-rsNSTD[cnt]*rsSTD[cnt])
    gr = gr[0]
    RAcen = np.sum(RA[g[gall[gz]]]/iB[g[gall[gz]]])/np.sum(1.0/iB[g[gall[gz]]])
    Deccen = np.sum(Dec[g[gall[gz]]]/iB[g[gall[gz]]])/np.sum(1.0/iB[g[gall[gz]]])
    RAcennw = np.sum(RA[g[gall[gz]]])/len(gz)
    Deccennw = np.sum(Dec[g[gall[gz]]])/len(gz)
    RAcen_r = np.sum(RA[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])/np.sum(1.0/iB[g[gall[gz[gr]]]])
    Deccen_r = np.sum(Dec[g[gall[gz[gr]]]]/iB[g[gall[gz[gr]]]])/np.sum(1.0/iB[g[gall[gz[gr]]]])
    RAcen_rnw = np.sum(RA[g[gall[gz[gr]]]])/len(gr)
    Deccen_rnw = np.sum(Dec[g[gall[gz[gr]]]])/len(gr)
    RAstrs = np.array(['12345678901234567890',' ', ' '])
    Decstrs = np.array(['12345678901234567890',' ', ' '])
    for ia in range(0,3):
        if ia == 0: pos = RAcennw
        if ia == 1: pos = RAcen
        if ia == 2: pos = RAcen_r
        rah,ram,ras = dec2hms(pos)
        ex0m,ex0s = '',''
        if ram < 10: ex0m = '0'
        if ras < 10: ex0s = '0'
        RAstrs[ia] = '%3i:%s%i:%s%f'%(rah,ex0m,ram,ex0s,ras)
    for ia in range(0,3):
        if ia == 0: pos = Deccennw
        if ia == 1: pos = Deccen
        if ia == 2: pos = Deccen_r
        decd,decm,decs = dec2dms(pos)
        ex0m,ex0s = '',''
        if decm < 10: ex0m = '0'
        if decs < 10: ex0s = '0'
        Decstrs[ia] = '%3i:%s%i:%s%f'%(decd,ex0m,decm,ex0s,decs)
        
    print '\n%s - \nUnweighted mean: (%f,%f) - using %i gal\nWeighted mean: (%f,%f) - using %i gal\nUnweighted mean, red: (%f,%f) - using %i gal\nWeighted mean, red: (%f,%f) - using %i gal\n'%(names[i],RAcennw,Deccennw,len(gz),RAcen,Deccen,len(gz),RAcen_rnw,Deccen_rnw,len(gr),RAcen_r,Deccen_r,len(gr))
                  
             
    
    

