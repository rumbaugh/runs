import numpy as np

crt = np.loadtxt('sim_ltcurve_testing/Nicktruth.txt')

FILE = open('sim_ltcurve_testing/Nick/season_lens.txt','w')
FILE.write('#pair season_length delay_frac\n')
season_len = np.zeros(100)
for pair in range(1,101):
    cr = np.loadtxt('sim_ltcurve_testing/Nick/Nick_pair%i.txt'%pair)
    ltime = cr[:,0]
    season_len[pair-1] = ltime[-1]-ltime[0]
    FILE.write('%3i %5.1f %5.3f\n'%(pair,season_len[pair-1],crt[pair-1]/season_len[pair-1]))
FILE.close()
