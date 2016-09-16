import numpy as np
import matplotlib.pylab as plt

lens_dict = {'0414': {'images': 4}, '0712': {'images': 4}, '1030': {'images': 2}, '1127': {'images': 2}, '1152': {'images': 2}}
color_arr = ['blue','red','green','purple']

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,2],CSO2cr[:,2]

CSOnorm = 0.5*(CSO1S[(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34)))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]) + CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]))

print np.mean(CSOnorm)

plt.figure(1)
plt.clf()
plt.scatter(CSO1day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSOnorm)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOnorm.8.29.13.png')



plt.figure(1)
plt.clf()
plt.scatter(CSO1day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.plot(CSO1day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.title('Lightcurve for CSO 1244')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO1244.lc_norm_plot.8.29.13.png')

plt.figure(1)
plt.clf()
plt.scatter(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.plot(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.title('Lightcurve for CSO 1400')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO1400.lc_norm_plot.8.29.13.png')

plt.figure(1)
plt.clf()
plt.scatter(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]))/(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])))
plt.plot(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]))/(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])))
plt.title('Relative CSO Lightcurve')
plt.xlabel('Days')
plt.ylabel('Flux Ratio')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO_rel_flux_plot.8.29.13.png')


for lens in lens_dict:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    FILE = open('/home/rumbaugh/EVLA/light_curves/plots/test/%s_norm_output_full.8.30.13.dat'%lens,'w')
    nimg = lens_dict[lens]['images']
    norm_flux_arr = np.zeros((nimg,len(cr[:,0])))
    if nimg == 4:
        FILE.write('# flux1 flux2 flux3 flux4\n')
    else:
        FILE.write('# fluxA fluxB\n')
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for img in range(0,nimg):
        S = cr[:,img+1]
        g = np.where(((np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=56)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=58)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where((np.arange(len(S))!=34)&(np.arange(len(S))!=42)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #if img == 0: 
        #    meanS0 = np.mean(S[g]*CSOnorm)
        #else:
        g = np.where(((np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        S /= np.mean(S[g])
        plt.scatter(days[g],S[g]/CSOnorm,color=color_arr[img])
        plt.plot(days[g],S[g]/CSOnorm,color=color_arr[img])
        norm_flux_arr[img] = S/(0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g])))
    if lens == '0414':
        plt.legend(('A1','A2','B','C'),loc=2)
    elif lens == '0712':
        plt.legend(('A','B','C','D'),loc=2)
    else:
        plt.legend(('A','B'),loc=2)
    plt.title('Normalized Lightcurve for Lens %s'%lens)
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    plt.xlim(1810,2090)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/test/%s.lc_norm_plot.8.30.13.png'%lens)
    if img == nimg-1:
        for j in range(0,len(S)):
            if nimg == 4:
                FILE.write('%f %f %f %f\n'%(norm_flux_arr[0][j],norm_flux_arr[1][j],norm_flux_arr[2][j],norm_flux_arr[3][j]))
            else:
                FILE.write('%f %f\n'%(norm_flux_arr[0][j],norm_flux_arr[1][j]))
        FILE.close()
lens = '0712'
cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
nimg = lens_dict[lens]['images']
plt.figure(1)
plt.clf()
norm_flux_arr = np.zeros((nimg,len(cr[:,0])))
FILE = open('/home/rumbaugh/EVLA/light_curves/plots/test/%s_norm_output_A+B_full.8.30.13.dat'%lens,'w')
FILE.write('# fluxA+B fluxC fluxD\n')
for img in range(1,nimg):
    S = cr[:,img+1]
    if img == 1: 
        SA = cr[:,0]
        g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(SA>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(SA>0)&(CSO1S>0)&(CSO2S>0)))[0]
        S = 0.5*(S+SA)
    else:
        g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
    #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        g = np.where(((np.arange(len(S))!=34)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
    CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
    S /= np.mean(S[g])
    plt.scatter(days[g],S[g]/CSOnorm,color=color_arr[img])
    plt.plot(days[g],S[g]/CSOnorm,color=color_arr[img])
    norm_flux_arr[img] = S/(0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g])))
for j in range(0,len(S)):
    FILE.write('%f %f %f\n'%(norm_flux_arr[0][j],norm_flux_arr[1][j],norm_flux_arr[2][j]))
FILE.close()
plt.legend(('A+B','C','D'),loc=2)
plt.title('Normalized Lightcurve for Lens %s'%lens)
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
#plt.xlim(1810,2090)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/test/%s.lc_norm_plot_comb_A+B.8.30.13.png'%lens)
