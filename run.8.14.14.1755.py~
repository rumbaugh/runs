import numpy as np
import matplotlib.pylab as plt

execfile("/home/rumbaugh/radmon_var_chisq_test.py")

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0054

try:
    dayoffset
except NameError:
    dayoffset = 0.2

FILE = open('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/chisq_results_Aconfig.8.14.14.dat','w')
FILE.write("# lens img1 chisq1 red_chisq1 P1 img2 chisq2 red_chisq2 P2 img3 chisq3 red_chisq3 P3 img4 chisq4 red_chisq4 P4")


lens_dict = {'0414': {'name': 'MG0414','images': 4}, '0712': {'name': 'B0712','images': 4}, '1030': {'name': 'J1030','images': 2}, '1127': {'name': 'B1127','images': 2}, '1152': {'name': 'B1152','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,2],CSO2cr[:,2]

CSO1day -= CSO1day[0]
CSO2day -= CSO2day[0]

CSO1S[CSO1day>1946-1839]=0

g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g])*CSOnorm,color=color_arr[0])
plt.plot(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g])*CSOnorm,color=color_arr[0],lw=2,ls=ls_arr[0])
plt.scatter(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g])*CSOnorm,color=color_arr[1])
plt.plot(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g])*CSOnorm,color=color_arr[1],lw=2,ls=ls_arr[1])
plt.title('Normalized CSO Lightcurves')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.legend(('CSO1244','CSO1400'),loc=2)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.lc_norm_plot.9.11.13.png')


for lens in lens_dict:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    nimg = lens_dict[lens]['images']
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    days = cr[:,0]-cr[0][0]
    for img in range(0,nimg):
        S = cr[:,img+1]
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=56)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=58)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=42)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #print np.mean(CSOnorm)
        plt.scatter(days[g],S[g]/CSOnorm,color=color_arr[img])
        plt.plot(days[g],S[g]/CSOnorm,color=color_arr[img])
    if lens == '0414':
        plt.legend(('A1','A2','B','C'),loc=2)
    elif lens == '0712':
        plt.legend(('A','B','C','D'),loc=2)
    else:
        plt.legend(('A','B'),loc=2)
    plt.title('Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Flux')
    plt.xlim(1810-cr[0][0],2090-cr[0][0])
    #plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_plot.9.11.13.png'%lens)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    testlegs = []
    chisq_arr,prob_arr = np.zeros(4),np.zeros(4)
    if lens!= '0712': FILE.write("\n%4s "%lens)
    for img in range(0,nimg):
        S = cr[:,img+1]
        rms = cr[:,nimg+img+1]
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=56)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=58)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=42)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #if img == 0: 
        #    meanS0 = np.mean(S[g]*CSOnorm)
        #else:
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
        Smean = np.mean(S[g])
        S /= Smean
        Serr /= Smean
        imgarr = ['A','B','NA','NA']
        if lens == '0414': imgarr = ['A1','A2','B','C']
        if lens != '0712': 
            chisq_arr[img],prob_arr[img] = calc_chi_sqrd(S[g][days[g]<100]/CSOnorm[days[g]<100],Serr[g][days[g]<100]/CSOnorm[days[g]<100],calcprob=True)
        plt.errorbar(days[g]+dayoffset*(img-1),S[g]/CSOnorm,yerr=Serr[g]/CSOnorm,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label=None)
        plt.scatter(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img],lw=2,ls=ls_arr[img]))
    if lens == '0414':
        plt.legend(testlegs,('A1','A2','B','C'),loc=4)
    elif lens == '0712':
        plt.legend(testlegs,('A','B','C','D'),loc=2)
    else:
        plt.legend(testlegs,('A','B'),loc=2)
    plt.title('Normalized Lightcurve for Lens %s'%lens_dict[lens]['name'])
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    plt.xlim(1810-cr[0][0],2090-cr[0][0])
    #plt.plot(days[g],np.mean(S[g]/CSOnorm))
    #plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot.9.11.13.png'%lens)
    for img in range(0,4):
        if lens != '0712': FILE.write("%3s %7.2f %7.3f %6.4f "%(imgarr[img],chisq_arr[img],chisq_arr[img]/len(CSOnorm[days[g]<100]),prob_arr[img]))
lens = '0712'
cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
nimg = lens_dict[lens]['images']
testlegs = []
plt.figure(1)
plt.clf()
chisq_arr,prob_arr = np.zeros(4),np.zeros(4)
FILE.write("\n%4s "%lens)
for img in range(1,nimg):
    S = cr[:,img+1]
    rms = cr[:,nimg+img+1]
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if img == 1: 
        SA = cr[:,0]
        rmsA = cr[:,5]
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(SA>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(SA>0)&(CSO1S>0)&(CSO2S>0)))[0]
        S = 0.5*(S+SA)
        Serr = 0.5*np.sqrt(rms**2+(fluxratio_err*S)**2+rmsA**2+(fluxratio_err*SA)**2)
    else:
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
    #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
    CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
    Smean = np.mean(S[g])
    S /= Smean
    Serr /= Smean
    imgarr = ['A+B','C','D','NA']
    chisq_arr[img-1],prob_arr[img-1] = calc_chi_sqrd(S[g][days[g]<100]/CSOnorm[days[g]<100],Serr[g][days[g]<100]/CSOnorm[days[g]<100],calcprob=True)  
    plt.errorbar(days[g]+dayoffset*(img-1),S[g]/CSOnorm,yerr=Serr[g]/CSOnorm,color=color_arr[img-1],fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
    plt.scatter(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img-1])
    testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img-1],lw=2,ls=ls_arr[img-1]))
plt.legend(testlegs,('A+B','C','D'),loc=2)
plt.title('Normalized Lightcurve for Lens %s'%lens_dict[lens]['name'])
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.xlim(1810-cr[0][0],2090-cr[0][0])
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot_comb_A+B.9.11.13.png'%lens)
for img in range(0,4):
    FILE.write("%3s %7.2f %7.3f %6.4f "%(imgarr[img],chisq_arr[img],chisq_arr[img]/len(CSOnorm[days[g]<100]),prob_arr[img]))
FILE.close()
