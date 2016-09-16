execfile('/home/rumbaugh/radmon_var_chisq_test.py')
import numpy as np

load1608_1 = np.loadtxt('/home/rumbaugh/B1608_files/1608_season1.dat')
ltime1_orig = load1608_1[:,0].copy()
Aflux1,Bflux1,Cflux1,Dflux1,Aerr1,Berr1,Cerr1,Derr1 = load1608_1[:,1].copy(),load1608_1[:,2].copy(),load1608_1[:,3].copy(),load1608_1[:,4].copy(),load1608_1[:,5].copy(),load1608_1[:,6].copy(),load1608_1[:,7].copy(),load1608_1[:,8].copy()
season1len = len(ltime1_orig)
load1608_2 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_season2.dat')
ltime2_orig = load1608_2[:,0].copy()
Aflux2,Bflux2,Cflux2,Dflux2,Aerr2,Berr2,Cerr2,Derr2 = load1608_2[:,1].copy(),load1608_2[:,2].copy(),load1608_2[:,3].copy(),load1608_2[:,4].copy(),load1608_2[:,5].copy(),load1608_2[:,6].copy(),load1608_2[:,7].copy(),load1608_2[:,8].copy()
season2len = len(ltime2_orig)
load1608_3 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime3_orig = load1608_3[:,0].copy()
Aflux3,Bflux3,Cflux3,Dflux3,Aerr3,Berr3,Cerr3,Derr3 = load1608_3[:,1].copy(),load1608_3[:,2].copy(),load1608_3[:,3].copy(),load1608_3[:,4].copy(),load1608_3[:,5].copy(),load1608_3[:,6].copy(),load1608_3[:,7].copy(),load1608_3[:,8].copy()
season3len = len(ltime3_orig)

ltime1,ltime2,ltime3 = ltime1_orig - ltime1_orig[0],ltime2_orig - ltime1_orig[0],ltime3_orig - ltime1_orig[0]

images = ['A','B','C','D']

data_dict = {1: {'flux': dict(zip(images,[Aflux1,Bflux1,Cflux1,Dflux1])), 'err': dict(zip(images,[Aerr1,Berr1,Cerr1,Derr1])), 'time': ltime1}, 2: {'flux': dict(zip(images,[Aflux2,Bflux2,Cflux2,Dflux2])), 'err': dict(zip(images,[Aerr2,Berr2,Cerr2,Derr2])), 'time': ltime2}, 3: {'flux': dict(zip(images,[Aflux3,Bflux3,Cflux3,Dflux3])), 'err': dict(zip(images,[Aerr3,Berr3,Cerr3,Derr3])), 'time': ltime3}}

for season in [1,2,3]:
    print 'Season %i\n'%season
    ltime = data_dict[season]['time']
    for img in images:
        S,Serr = data_dict[season]['flux'][img],data_dict[season]['err'][img]
        g = np.where((S > 0)&(Serr>0))[0]
        csq,prob = calc_chi_sqrd(S[g],Serr[g],calcprob=True)
        print '\n%s: %f - %f\n'%(img,prob,csq/len(g))
