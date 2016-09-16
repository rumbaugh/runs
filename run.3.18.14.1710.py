execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")


date = '3.18.14'

for lens in ['0414','1030','1127','1152','0712','1938']:
    if lens == '1938':
        ltime,zAflux,zBflux,Aflux,Bflux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()
        ltime = (ltime-ltime[0])/86400
        g = np.arange(len(ltime))
    else:
        ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

        Aflux,Bflux = flux_arr[0],flux_arr[1]
        Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
        ltime = (ltime-ltime[0])#/86400
        g = np.arange(len(ltime))[:len(ltime)-10]

    fluxratio = Aflux/Bflux
    pdfm_fr = (fluxratio-np.average(fluxratio))/np.average(fluxratio)
    plt.figure(1)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.clf()
    plt.hist(pdfm_fr)#,bins=nbins,range=trange)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.xlabel('Fractional Deviation From Mean Flux Ratio')
    plt.ylabel('Number of Observations')
    if lens == '0414':
        plt.title('A1-A2 Flux Ratio')
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/fluxratios_A1A2.%s.%s.png'%(lens,date))
    elif lens == '1938':
        plt.title('C1-C2 Flux Ratio')
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/fluxratios_C1C2.%s.%s.png'%(lens,date))
    else:
        plt.title('A-B Flux Ratio')
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/fluxratios_AB.%s.%s.png'%(lens,date))
    print '%s:\nMean: %f\nMedian: %f\nStd: %f\n'%(lens,np.average(pdfm_fr),np.median(pdfm_fr),np.std(pdfm_fr))
