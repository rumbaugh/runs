import numpy as np

crt = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')

FILE = open('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/season_lens.txt','w')
FILE.write('#pair avg_season_length delay_frac min_season_len max_season_len\n')
season_len = np.zeros(100)
for pair in range(1,101):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/Nickrung0_pair%i.txt'%pair)
    ltime = cr[:,0]
    g = np.where(ltime[1:]-ltime[:-1]>50)[0]
    season_tmp = np.zeros(len(g))
    for i in range(0,len(g)):
        if i == 0:
            season_tmp[i] = ltime[g[0]]-ltime[0]
        else:
            season_tmp[i] = ltime[g[i]]-ltime[g[i-1]+1]
    season_len[pair-1] = np.average(season_tmp)
    FILE.write('%3i %5.1f %5.3f %5.1f %5.1f\n'%(pair,season_len[pair-1],crt[pair-1]/season_len[pair-1],np.min(season_tmp),np.max(season_tmp)))
FILE.close()
