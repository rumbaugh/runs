import numpy as np
import math as m
import matplotlib
import matplotlib.pylab as pylab
import random as rand
execfile('/home/rumbaugh/FindCloseSources.py')

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0])
#1 Mpc = 3.06*0.7 Arcmin
srchdist = 3.06*0.7

names = np.array(['Cl1604A','Cl1604B'])
centerRAs = np.array([(16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24])
centerDecs = np.array([43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60])
centerzs = np.array([0.89861,0.86531])

cr = read_file("FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat")

RA = get_colvals(cr,'col4')
Dec = get_colvals(cr,'col5')
ACSRA = get_colvals(cr,'col14')
ACSDec = get_colvals(cr,'col15')
f606 = get_colvals(cr,'col16')
f814 = get_colvals(cr,'col17')
LFCrB = get_colvals(cr,'col6')
LFCiB = get_colvals(cr,'col7')
zB = get_colvals(cr,'col8')
z = get_colvals(cr,'col9')
q = get_colvals(cr,'col11')

#iB = f814
#rB = f606
iB = LFCiB
rB = LFCrB

g = np.where((q > 2.2) & (z > 0.84) & (z < 0.96) & (iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
g = g[0]

for i in range(0,len(names)):
    gall = FindCloseSources(centerRAs[i],centerDecs[i],srchdist*60,ACSRA[g],ACSDec[g],0)
    gz = np.where((z[g[gall]] > centerzs[i]-0.02) & (z[g[gall]] < centerzs[i]+0.02))
    gz = gz[0]
    gr = np.where(rB[g[gall[gz]]]-iB[g[gall[gz]]] > rsb[4]-rsm[4]*iB[g[gall[gz]]]-rsNSTD[4]*rsSTD[4])
    gr = gr[0]
    gb = np.where((rB[g[gall[gz]]]-iB[g[gall[gz]]] < rsb[4]-rsm[4]*iB[g[gall[gz]]]-rsNSTD[4]*rsSTD[4]))
    gb = gb[0]
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
    print '%s\nRed Center: (%f,%f)\nBlue Center: (%f,%f)\nDifference in as: %f\nNo Weights\nRed Center: (%f,%f)\nBlue Center: (%f,%f)\nDifference in as: %f\n'%(names[i],RAcen_r,Deccen_r,RAcen_b,Deccen_b,diff,RAcen_rnw,Deccen_rnw,RAcen_bnw,Deccen_bnw,diffnw)
           
                  
             
    
    

