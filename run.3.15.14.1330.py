execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")

try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '3.15.14'

try:
    ylimits
except NameError:
    ylimits = 0.001

for pair in range(1,101):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/Nick_pair%i.txt'%pair)
    ltime,Aflux,Bflux = cr[:,0],cr[:,1],cr[:,3]
    Aerr,Berr = cr[:,2],cr[:,4]
    ltime = (ltime-ltime[0])#/86400
    plt.clf()
    plt.errorbar(ltime,Aflux,Aerr)
    plt.scatter(ltime,Aflux)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/Nick/lightcurve_plot.Nick_pair%i.png'%pair)
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    plt.clf()
    plt.errorbar(ltime,Aflux,Aerr)
    plt.scatter(ltime,Aflux)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/Nick/norm_lightcurve_plot.Nick_pair%i.png'%pair)
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/Nickrung0_pair%i.txt'%pair)
    ltime,Aflux,Bflux = cr[:,0],cr[:,1],cr[:,3]
    Aerr,Berr = cr[:,2],cr[:,4]
    ltime = (ltime-ltime[0])#/86400
    plt.clf()
    plt.errorbar(ltime,Aflux,Aerr)
    plt.scatter(ltime,Aflux)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/lightcurve_plot.Nickrung0_pair%i.png'%pair)
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    plt.clf()
    plt.errorbar(ltime,Aflux,Aerr)
    plt.scatter(ltime,Aflux)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/norm_lightcurve_plot.Nickrung0_pair%i.png'%pair)
