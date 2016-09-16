execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')


try:
    errstd
except NameError:
    errstd = 7.5

try:
    ntrials
except NameError:
    ntrials = 50


for i in range(0,ntrials):
    stime = np.arange(220.,550.,3.)
    F_dict = GenerateMockCurve(stime,errstd=errstd,return_lc_params=True)
    if np.mean(F_dict['flux'] > 100000):
        print F_dict
        print '\n\n'
