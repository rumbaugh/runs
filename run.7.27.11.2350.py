execfile("/home/rumbaugh/LeastSquares.py")

names = np.array(['RXJ1757','NEP5281','Cl1324','Cl0023','Cl1604','composite'])
paths = np.array(['/scratch/rumbaugh/ciaotesting/RXJ1757/master/','/scratch/rumbaugh/ciaotesting/NEP5281/master/','/scratch/rumbaugh/ciaotesting/Cl1324/master/','/scratch/rumbaugh/ciaotesting/Cl0023/7914/','/scratch/rumbaugh/ciaotesting/Cl1604/master/','/home/rumbaugh/CDF/'])
nrL = np.array([5e-15,1e-14,5e-15])
nrH = np.array([1e-14,4e-14,4e-14])

S_0 = 1e-14

FILE = open("/home/rumbaugh/LFC/test.logNlogS.powlaw.fit.dat","w")
for i in range(0,len(names)):
    cr = read_file(paths[i] + "src_flux_sort.N_sort.Nerr." + names[i] + ".hard.lst")
    S = get_colvals(cr,'col1')
    N = get_colvals(cr,'col2')
    Nerr = get_colvals(cr,'col3')
    x = np.zeros(len(S))
    for j in range(0,len(S)): x[j] = m.log(S[j]/S_0)
    y = np.zeros(len(S))
    for j in range(0,len(y)): y[j] = m.log(N[j])
    dy = y*Nerr/N
    print '\nFit %s to k(S/S_0)^alpha, S_0 = %5.3E\n'%(names[i],S_0)
    Ssort = np.sort(S)
    gk0 = np.searchsorted(Ssort,S_0)
    gk = len(S) - gk0
    print S[gk],S[gk-2],N[gk],N[gk-1],Nerr[gk],Nerr[gk-1]
    k_0 = (S_0 - S[gk-1])*(N[gk]-N[gk-1])/(S[gk]-S[gk-1]) + N[gk-1]
    k_0_err = m.sqrt((Nerr[gk-1]*(S[gk]-S_0)/(S[gk]-S[gk-1]))**2 + (Nerr[gk]*(S_0-S[gk-1])/(S[gk]-S[gk-1]))**2)
    k0kreferr = m.sqrt((k_0_err/275.0)**2 + (22.0*k_0/(275*275))**2)
    FILE.write('%9s %5.1f %5.1f %4.2f %4.2f '%(names[i],k_0,k_0_err,k_0/275.0,k0kreferr))
    for ir in range(0,3):
        gg = np.where((S >= nrL[ir]))
        gg = gg[0]
        g = np.where(S[gg] <= nrH[ir])
        g = g[0]
        a,b,da,db = LQFitYErr(x[gg[g]],y[gg[g]],dy[gg[g]])
        k = m.exp(a)
        alpha = b
        dk = m.exp(a)*da
        kkrerr = m.sqrt((dk/275)**2 + (22.0*k/(275*275))**2)
        print 'Fit Range (ergs/s/cm^2): %3.1E - %3.1E'%(nrL[ir],nrH[ir])
        print 'k     = %6.1f    Error in k     = %5.1f'%(k,dk)
        print 'alpha = %6.3f    Error in alpha = %5.3f'%(alpha,db)
        print 'k/k_ref = %4.2f  Error in k/k_ref = %4.2f\n'%(k/275.0,kkrerr)
        FILE.write('%6.1f %5.1f %6.3f %5.3f %4.2f %4.2f '%(k,dk,alpha,db,k/275.0,kkrerr))
    FILE.write("\n")
FILE.close()
