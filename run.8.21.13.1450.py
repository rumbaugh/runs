import numpy as np
import matplotlib.pylab as plt

lens_dict = {'0414': {'images': 4}, '0712': {'images': 4}, '1030': {'images': 2}, '1127': {'images': 2}, '1152': {'images': 2}}
color_arr = ['blue','red','green','purple']

for lens in lens_dict:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    nimg = lens_dict[lens]['images']
    plt.figure(1)
    plt.clf()
    days = cr[:,0]
    for img in range(0,nimg):
        S = cr[:,img+1]
        plt.scatter(days[S>0],S[S>0],color=color_arr[img])
        plt.plot(days[S>0],S[S>0],color=color_arr[img])
    plt.title('Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Flux')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_plot.8.21.13.png'%lens)
    plt.clf()
    for img in range(0,nimg):
        S = cr[:,img+1]
        if img == 0: 
            meanS0 = np.average(S[S>0])
        else:
            S *= meanS0/np.average(S[S>0])
        plt.scatter(days[S>0],S[S>0],color=color_arr[img])
        plt.plot(days[S>0],S[S>0],color=color_arr[img])
    plt.title('Normalized Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Flux')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot.8.21.13.png'%lens)
