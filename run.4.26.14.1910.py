import numpy as np
import matplotlib.pylab as plt

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.00687

try:
    dayoffset
except NameError:
    dayoffset = 0.2

first_day = 1942 - 0.001
date = '4.26.14'

dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

lens_dict = {'0414': {'name': 'MG0414', 'fullname': '0414+573', 'images': 4}, '0712': {'name': 'B0712', 'fullname': '0712+472', 'images': 4}, '1030': {'name': 'J1030', 'fullname': '1030+074','images': 2}, '1127': {'name': 'B1127','fullname': '1127+385','images': 2}, '1152': {'name': 'B1152','fullname': '1152+199','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']


sources = ['0414+573']#,'1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

#CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_1244+408.dat'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_1035+564.dat')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,1],CSO2cr[:,1]
#CSO1day = np.append(CSO1day1[CSO1day1 < first_day],CSO1day2)
#CSO2day = np.append(CSO2day1[CSO2day1 < first_day],CSO2day2)
#CSO1S = np.append(CSO1S1[CSO1day1 < first_day],CSO1S2)
#CSO2S = np.append(CSO2S1[CSO2day1 < first_day],CSO2S2)

# Set bad points to zero
#CSO1S[7],CSO1S[10],CSO1S[-17] = 0,0,0

g = np.where((CSO1S>0)&(CSO2S>0))#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19))[0]
#g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g]),color=color_arr[0])
plt.plot(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g]),color=color_arr[0],lw=2,ls=ls_arr[0])
plt.scatter(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g]),color=color_arr[1])
plt.plot(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g]),color=color_arr[1],lw=2,ls=ls_arr[1])
plt.title('Normalized CSO Lightcurves')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.legend(('CSO1244','CSO1035'),loc=2)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.lc_plot.%s.png'%date)

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
plt.legend(('CSO1244','CSO1035'),loc=2)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.lc_norm_plot.%s.png'%date)

pcr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_1400+621.dat')
days,S = pcr[:,0]-CSO1cr[0][0],pcr[:,1]
#S[-17] = 0
g = np.where(S>0)[0]
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(days[g],S[g])
plt.plot(days[g],S[g],lw=2)
plt.title('1400+524 Lightcurve')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Flux',fontsize=14)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO_1400+621.lc_plot.%s.png'%date)



for lens in ['0414']:
    #cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_UVT_4.14.14_%s.dat'%(lens_dict[lens]['fullname']))
    nimg = lens_dict[lens]['images']
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    days = cr[:,0]-cr[0][0]
    #days = np.append(days1[days1 < first_day-cr[0][0]],days2)
    S2 = cr[:,1]
    for img in range(1,nimg):
        S = cr[:,img+1]
        if img == 1: S += S2
        #S = np.append(S1[days1 < first_day-cr[0][0]],S2)
        g = np.where((CSO1S>0)&(CSO2S>0)&(S>0))#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19))[0]
        #g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            S[1],S[26],S[11],S[-18] = 0,0,0,0
            g = np.where((S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            S[55],S[16] = 0,0
            g = np.where((S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            S[50],S[-3],S[-7],S[-22],S[-26],S[-39] = 0,0,0,0,0,0
            g = np.where(((S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            S[12],S[-10] = 0,0
            g = np.where(((S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            #g = np.where(((np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #elif lens == '1152':
            #g = np.where((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=42)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0))[0]
        #    CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #print np.mean(CSOnorm)
        plt.scatter(days[g],S[g]/np.mean(S[g]),color=color_arr[img])
        plt.plot(days[g],S[g]/np.mean(S[g]),color=color_arr[img])
    if lens == '0414':
        plt.legend(('A','B','C'),loc=2)
    elif lens == '0712':
        plt.legend(('A','B','C','D'),loc=2)
    else:
        plt.legend(('A','B'),loc=2)
    plt.title('Lightcurve for Lens %s'%lens)
    plt.xlabel('Days')
    plt.ylabel('Flux')
    plt.xlim(1810-cr[0][0],2090-cr[0][0])
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_rel_plot_UVT_comb.%s.png'%(lens,date))
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    testlegs = []
    for img in range(0,nimg):
        S = cr[:,img+1]
        #S2 = cr2[:,img+1]
        #S = np.append(S1[days1 < first_day-cr[0][0]],S2)
        rms = np.zeros(len(S))
        #rms = cr[:,nimg+img+1]
        g = np.where((CSO1S>0)&(CSO2S>0)&(S>0))#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19))[0]
        #g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            S[1],S[26],S[11],S[-18] = 0,0,0,0
            g = np.where((S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            S[55],S[16] = 0,0
            g = np.where((S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            S[50],S[-3],S[-7],S[-22],S[-26],S[-39] = 0,0,0,0,0,0
            g = np.where(((S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            S[12],S[-10] = 0,0
            g = np.where(((S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        #if img == 0: 
        #    meanS0 = np.mean(S[g]*CSOnorm)
        #else:
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
        Smean = np.mean(S[g])
        S /= Smean
        Serr /= Smean
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
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot_UVT_comb.%s.png'%(lens,date))
