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
    date = '8.15.14'

try:
    ylimits
except NameError:
    ylimits = None

try:
    timestep
except NameError:
    timestep = 0.5

try:
    maxtime
except NameError:
    maxtime = 105

try: 
    maxtimeA
except NameError:
    maxtimeA = 60

def iter_fluxratio(Aflux,Bflux,ltime,maxtime,timestep):
    steps = 2*(int(np.floor(maxtime/timestep)))+1
    BA_FR_arr = np.zeros(steps)
    for tau,i in zip((np.arange(steps)-steps/2)*timestep,np.arange(steps)):
        if tau > 0:
            overlapA,overlapB = np.where(ltime+tau<np.max(ltime))[0],np.where(ltime>tau+np.min(ltime))[0]
        elif tau < 0:
            overlapA,overlapB = np.where(ltime+tau>np.min(ltime))[0],np.where(ltime<np.max(ltime)+tau)[0]
        else:
            overlapA,overlapB = np.arange(len(ltime)),np.arange(len(ltime))
        BA_FR_arr[i] = np.mean(Aflux[overlapA])/np.mean(Bflux[overlapB])
    return BA_FR_arr

FILE = open('/home/rumbaugh/EVLA/light_curves/flux_ratios.8.15.14.dat','w')

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
        print lens
        BAfluxratio = np.mean(Aflux[g])/np.mean(Bflux[g])
        BAfr_err =BAfluxratio*((np.sqrt(np.sum(Aerr[g]**2))/len(g)/np.mean(Aflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
        BA_FR_arr = iter_fluxratio(Aflux[g],Bflux[g],ltime[g],maxtime,timestep)
        sarr = np.sort(BA_FR_arr)
        print np.max(BA_FR_arr)-np.min(BA_FR_arr),sarr[int((0.5+0.682689*0.5)*len(sarr))]-sarr[int((0.5-0.682689*0.5)*len(sarr))]
        FILE.write('%s BA     whole %f %f %f\n'%(lens,BAfluxratio,BAfr_err,np.max(BA_FR_arr)-np.min(BA_FR_arr)))
        BAfluxratio = np.mean(Aflux[gAonly])/np.mean(Bflux[gAonly])
        BAfr_err =BAfluxratio*((np.sqrt(np.sum(Aerr[gAonly]**2))/len(gAonly)/np.mean(Aflux[gAonly]))**2+(np.sqrt(np.sum(Berr[gAonly]**2))/len(gAonly)/np.mean(Bflux[gAonly]))**2)
        BA_FR_arr = iter_fluxratio(Aflux[gAonly],Bflux[gAonly],ltime[gAonly],maxtime,timestep)
        sarr = np.sort(BA_FR_arr)
        print np.max(BA_FR_arr)-np.min(BA_FR_arr),sarr[int((0.5+0.682689*0.5)*len(sarr))]-sarr[int((0.5-0.682689*0.5)*len(sarr))]
        FILE.write('%s BA     Aonly %f %f %f\n'%(lens,BAfluxratio,BAfr_err,np.max(BA_FR_arr)-np.min(BA_FR_arr)))
    else:
        fluxdict = {0: A1flux, 1: A2flux, 2: Cflux}
        errdict = {0: A1err, 1: A2err, 2: Cerr}
        imgname = {0: 'A1', 1: 'A2', 2: 'C'}
        print lens
        for img in [0,1,2]:
            tflux = fluxdict[img]
            tferr = errdict[img]
            fluxratio = np.mean(tflux[g])/np.mean(Bflux[g])
            #fr_err = np.sqrt(np.sum(tferr[g]**2)/(len(g)/np.mean(Bflux[g]))**2+np.sum(Berr[g]**2)*(np.mean(tflux[g])/len(g)/(np.mean(Bflux[g]))**2)**2)
            fr_err =fluxratio*((np.sqrt(np.sum(tferr[g]**2))/len(g)/np.mean(tflux[g]))**2+(np.sqrt(np.sum(Berr[g]**2))/len(g)/np.mean(Bflux[g]))**2)
            BA_FR_arr = iter_fluxratio(tflux[g],Bflux[g],ltime[g],maxtime,timestep)
            sarr = np.sort(BA_FR_arr)
            print np.max(BA_FR_arr)-np.min(BA_FR_arr),sarr[int((0.5+0.682689*0.5)*len(sarr))]-sarr[int((0.5-0.682689*0.5)*len(sarr))]
            FILE.write('%s B%2s    whole %f %f %f\n'%(lens,imgname[img],fluxratio,fr_err,np.max(BA_FR_arr)-np.min(BA_FR_arr)))
            fluxratio = np.mean(tflux[gAonly])/np.mean(Bflux[gAonly])
            #fr_err = np.sqrt(np.sum(tferr[gAonly]**2)/(len(gAonly)/np.mean(Bflux[gAonly]))**2+np.sum(Berr[gAonly]**2)*(np.mean(tflux[gAonly])/len(gAonly)/(np.mean(Bflux[gAonly]))**2)**2)
            fr_err =fluxratio*((np.sqrt(np.sum(tferr[gAonly]**2))/len(gAonly)/np.mean(tflux[gAonly]))**2+(np.sqrt(np.sum(Berr[gAonly]**2))/len(gAonly)/np.mean(Bflux[gAonly]))**2)
            BA_FR_arr = iter_fluxratio(tflux[gAonly],Bflux[gAonly],ltime[gAonly],maxtime,timestep)
            sarr = np.sort(BA_FR_arr)
            print np.max(BA_FR_arr)-np.min(BA_FR_arr),sarr[int((0.5+0.682689*0.5)*len(sarr))]-sarr[int((0.5-0.682689*0.5)*len(sarr))]
            FILE.write('%s B%2s    Aonly %f  %f %f\n'%(lens,imgname[img],fluxratio,fr_err,np.max(BA_FR_arr)-np.min(BA_FR_arr)))
    #Aerr /= np.mean(Aflux[g])
    #Aflux /= np.mean(Aflux[g])
