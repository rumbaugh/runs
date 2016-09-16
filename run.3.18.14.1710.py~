execfile("/home/rumbaugh/LoadVLA_2001.py")


date = '3.5.14'

for lens in ['1030','1127','1152','0712']:
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
    plt.title('A-B Flux Ratios')
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.xlabel('Fractional Deviation From Mean Flux Ratio')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/fluxratios_AB.%s.%s.png'%(lens,date))
    print '%s:\nMean: %f\nMedian: %f\nStd: %f\n'%(lens,np.average(pdfm_fr),np.median(pdfm_fr),np.std(pdfm_fr))
