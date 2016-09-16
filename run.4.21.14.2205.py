execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")
execfile("/home/rumbaugh/LinReg.py")


try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '4.21.14'

try:
    ylimits
except NameError:
    ylimits = None

FILE = open('/home/rumbaugh/EVLA/light_curves/flux_ratios.4.21.14.dat','w')

for lens in ['0414','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    if lens == '0414':
        A1flux,A2flux,Bflux,Cflux = flux_arr[0],flux_arr[1],flux_arr[2],flux_arr[3]
        A1err,A2err,Berr,Cerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2],flux_err_arr[3]
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    gAonly = np.where(ltime < 1946-1839)[0]
    if lens != '0414':
        BAfluxratio = np.mean(Aflux[g])/np.mean(Bflux[g])
        #BAfr_err = np.sqrt(np.sum(Aerr[g]**2)/(len(g)/np.mean(Bflux[g]))**2+np.sum(Berr[g]**2)*(np.mean(Aflux[g])/len(g)/(np.mean(Bflux[g]))**2)**2)
        BAfr_err =BAfluxratio*((np.sqrt(np.sum(Aerr[g]**2))/len(g)/np.mean(Aflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
        FILE.write('%s BA     whole %f %f\n'%(lens,BAfluxratio,BAfr_err))
        BAfluxratio = np.mean(Aflux[gAonly])/np.mean(Bflux[gAonly])
        #BAfr_err = np.sqrt(np.sum(Aerr[gAonly]**2)/(len(gAonly)/np.mean(Bflux[gAonly]))**2+np.sum(Berr[gAonly]**2)*(np.mean(Aflux[gAonly])/len(gAonly)/(np.mean(Bflux[gAonly]))**2)**2)
        BAfr_err =BAfluxratio*((np.sqrt(np.sum(Aerr[gAonly]**2))/len(gAonly)/np.mean(Aflux[gAonly]))**2+(np.sqrt(np.sum(Berr[gAonly]**2))/len(gAonly)/np.mean(Bflux[gAonly]))**2)
        FILE.write('%s BA     Aonly %f %f\n'%(lens,BAfluxratio,BAfr_err))
    else:
        fluxdict = {0: A1flux, 1: A2flux, 2: Cflux}
        errdict = {0: A1err, 1: A2err, 2: Cerr}
        imgname = {0: 'A1', 1: 'A2', 2: 'C'}
        for img in [0,1,2]:
            tflux = fluxdict[img]
            tferr = errdict[img]
            fluxratio = np.mean(tflux[g])/np.mean(Bflux[g])
            #fr_err = np.sqrt(np.sum(tferr[g]**2)/(len(g)/np.mean(Bflux[g]))**2+np.sum(Berr[g]**2)*(np.mean(tflux[g])/len(g)/(np.mean(Bflux[g]))**2)**2)
            fr_err =fluxratio*((np.sqrt(np.sum(tferr[g]**2))/len(g)/np.mean(tflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
            FILE.write('%s B%2s    whole %f %f\n'%(lens,imgname[img],fluxratio,fr_err))
            fluxratio = np.mean(tflux[gAonly])/np.mean(Bflux[gAonly])
            #fr_err = np.sqrt(np.sum(tferr[gAonly]**2)/(len(gAonly)/np.mean(Bflux[gAonly]))**2+np.sum(Berr[gAonly]**2)*(np.mean(tflux[gAonly])/len(gAonly)/(np.mean(Bflux[gAonly]))**2)**2)
            fr_err =fluxratio*((np.sqrt(np.sum(tferr[gAonly]**2))/len(gAonly)/np.mean(tflux[gAonly]))**2+(np.sqrt(np.sum(Berr[gAonly]**2))/len(gAonly)/np.mean(Bflux[gAonly]))**2)
            FILE.write('%s B%2s    Aonly %f %f\n'%(lens,imgname[img],fluxratio,fr_err))
    #Aerr /= np.mean(Aflux[g])
    #Aflux /= np.mean(Aflux[g])
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()
Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)
ltime = (ltime-ltime[0])/86400.

g = np.arange(len(Aflux))
BAfluxratio = np.mean(Aflux)/np.mean(Bflux)
#BAfr_err = np.sqrt(np.sum(Aerr**2)/(len(g)/np.mean(Bflux))**2+np.sum(Berr**2)*(np.mean(Aflux)/len(g)/(np.mean(Bflux))**2)**2)
BAfr_err =BAfluxratio*((np.sqrt(np.sum(Aerr[g]**2))/len(g)/np.mean(Aflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
FILE.write('1938 BA     whole %f %f\n'%(BAfluxratio,BAfr_err))
BAfluxratio = np.mean(Cflux)/np.mean(Bflux)
#BAfr_err = np.sqrt(np.sum(Cerr**2)/(len(g)/np.mean(Bflux))**2+np.sum(Berr**2)*(np.mean(Cflux)/len(g)/(np.mean(Bflux))**2)**2)
BAfr_err =BAfluxratio*((np.sqrt(np.sum(Cerr[g]**2))/len(g)/np.mean(Cflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
FILE.write('1938 BC     whole %f %f\n'%(BAfluxratio,BAfr_err))
FILE.close()
