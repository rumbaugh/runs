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
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOnorm.8.22.13.png')



plt.figure(1)
plt.clf()
plt.scatter(CSO1day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.plot(CSO1day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.title('Lightcurve for CSO 1244')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO1244.lc_norm_plot.8.22.13.png')

plt.figure(1)
plt.clf()
plt.scatter(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.plot(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])*CSOnorm)
plt.title('Lightcurve for CSO 1400')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO1400.lc_norm_plot.8.22.13.png')

plt.figure(1)
plt.clf()
plt.scatter(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]))/(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])))
plt.plot(CSO2day[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))],(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO1S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]))/(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))]/np.mean(CSO2S[((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=34))])))
plt.title('Relative CSO Lightcurve')
plt.xlabel('Days')
plt.ylabel('Flux Ratio')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO_rel_flux_plot.8.22.13.png')


for lens in lens_dict:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    nimg = lens_dict[lens]['images']
    plt.figure(1)
    plt.clf()
    days = cr[:,0]
    for img in range(0,nimg):
        S = cr[:,img+1]
        g = np.where(((np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((S/np.mean(S[g])>1.05)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((S/np.mean(S[g])>1.1)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((S/np.mean(S[g])>1.1)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((S/np.mean(S[g])>1.055)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where(((S/np.mean(S[g])>1.03)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        print np.mean(CSOnorm)
        plt.scatter(days[g],S[g]*CSOnorm,color=color_arr[img])
        plt.plot(days[g],S[g]*CSOnorm,color=color_arr[img])
    plt.title('Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Flux')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_plot.8.22.13.png'%lens)
    plt.clf()
    for img in range(0,nimg):
        S = cr[:,img+1]
        g = np.where(((np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((S/np.mean(S[g])>1.05)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((S/np.mean(S[g])>1.1)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((S/np.mean(S[g])>1.1)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((S/np.mean(S[g])>1.055)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where(((S/np.mean(S[g])>1.03)&(np.arange(len(S))!=34)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #if img == 0: 
        #    meanS0 = np.mean(S[g]*CSOnorm)
        #else:
        S /= np.mean(S[g])
        plt.scatter(days[g],S[g]*CSOnorm,color=color_arr[img])
        plt.plot(days[g],S[g]*CSOnorm,color=color_arr[img])
    plt.title('Normalized Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Normalized Flux')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot.8.22.13.png'%lens)
