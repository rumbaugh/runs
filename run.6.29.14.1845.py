import numpy as np
import matplotlib.pylab as plt

execfile("/home/rumbaugh/radmon_var_chisq_test.py")

space_inbetween = 0.2

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0088

try:
    dayoffset
except NameError:
    dayoffset = 0.2

try:
    trials
except NameError:
    trials = 10000

date = '6.29.14'

lens_dict = {'0414': {'name': 'MG0414','images': 4}, '0712': {'name': 'B0712','images': 4}, '1030': {'name': 'J1030','images': 2}, '1127': {'name': 'B1127','images': 2}, '1152': {'name': 'B1152','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']
sizes=[6,6,6,9]
symbols = ["o","s","D","h"]

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,2],CSO2cr[:,2]


g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

orig_sib = space_inbetween
for lens in lens_dict:
    if lens == '0414':
        space_inbetween = 0.08
        yticklocs,yticklabs = np.array([0.96,0.98,1.,1.02,1.04])+space_inbetween*(-1.5),np.array(['','0.98','1.00','1.02',''])
        yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1.5),np.copy(yticklabs)
        for i in range(1,4):
            yticklocs,yticklabs = np.append(yticklocs,yticklocso+space_inbetween*(i-1.5)),np.append(yticklabs,yticklabso)
    elif lens == '1030':
        space_inbetween = 0.15
        yticklocs,yticklabs = np.array([0.825,0.85,0.875,0.9,0.925,0.95,0.975,1.,1.025,1.05,1.075])+space_inbetween*(-0.5),np.array(['','0.85','','0.90','','0.95','','1.00','','1.05',''])
        yticklocs,yticklabs = np.append(yticklocs,np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075,1.1,1.125,1.15])+space_inbetween*(0.5)),np.append(yticklabs,np.array(['','0.95','','1.00','','1.05','','1.10','','']))
    elif lens == '1127':
        space_inbetween = 0.1
        yticklocs,yticklabs = np.array([0.825,0.85,0.875,0.9,0.925,0.95,0.975,1.,1.025,1.05,1.075])+space_inbetween*(-0.5),np.array(['','0.85','','0.90','','0.95','','1.00','','',''])
        yticklocs,yticklabs = np.append(yticklocs,np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075,1.1,1.125,1.15])+space_inbetween*(0.5)),np.append(yticklabs,np.array(['','','','1.00','','1.05','','1.10','','']))
    elif lens == '1152':
        space_inbetween = 0.1
        yticklocs,yticklabs = np.array([0.825,0.85,0.875,0.9,0.925,0.95,0.975,1.,1.025,1.05,1.075])+space_inbetween*(-0.5),np.array(['','0.85','','0.90','','0.95','','1.00','','',''])
        yticklocs,yticklabs = np.append(yticklocs,np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075,1.1,1.125,1.15])+space_inbetween*(0.5)),np.append(yticklabs,np.array(['','','','1.00','','1.05','','1.10','','']))
    else:
        space_inbetween = orig_sib
    FILE = open('/home/rumbaugh/EVLA/light_curves/test.%s.%s.dat'%(lens,date),'w')
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    nimg = lens_dict[lens]['images']
    days = cr[:,0]-cr[0][0]
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.axvline(x=1946-1839,lw=2,ls='dashed',color='k')
    plt.axvline(x=1976-1839,lw=2,ls='dashed',color='k')
    testlegs = []
    S_arr = np.zeros((nimg,np.shape(cr)[0]))
    for img in range(0,nimg):
        if nimg == 2:
            arb_offset = space_inbetween*(img-0.5)
        elif nimg == 4:
            arb_offset = space_inbetween*(img-1.5)
        elif nimg == 3:
            arb_offset = space_inbetween*(img-1)
        else:
            arb_offset = None
        S = cr[:,img+1]
        rms = cr[:,nimg+img+1]
        g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
        #CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=30)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=50)&(np.arange(len(S))!=56)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '0712':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=45)&(np.arange(len(S))!=48)&(np.arange(len(S))!=58)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1030':
            g = np.where(((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=30)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=58)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1127':
            g = np.where(((np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(S>0)&(CSO1S>0)&(CSO2S>0)))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        elif lens == '1152':
            g = np.where((np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=30)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(S))!=42)&(np.arange(len(S))!=59)&(np.arange(len(S))!=62)&(S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #if img == 0: 
        #    meanS0 = np.mean(S[g]*CSOnorm)
        #else:
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
        Smean = np.mean(S[g])
        S /= Smean
        Serr /= Smean
        S_arr[img] = S
        S += arb_offset
        imgarr = ['A','B','NA','NA']
        if lens == '0414': imgarr = ['A1','A2','B','C']
        plt.axhline(y=np.mean(S[g]/CSOnorm),lw=2,ls='dashed',color='k')
        plt.errorbar(days[g]+dayoffset*(img-1),S[g]/CSOnorm,yerr=Serr[g]/CSOnorm,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,marker=symbols[img],ms=sizes[img],label=None)
        plt.scatter(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img],lw=2,ls=ls_arr[img]))
    if lens != '0712': plt.yticks(yticklocs,yticklabs)
    if lens == '0414':
        plt.legend(testlegs,('A1','A2','B','C'),loc=4)
        imgsarr = ['A1','A2','B','C']
        plt.ylim(0.83,1.18)
    elif lens == '0712':
        plt.legend(testlegs,('A','B','C','D'),loc=2)
        imgsarr = ['A','B','C','D']
    elif lens == '1030':
        plt.legend(testlegs,('A','B'),loc=2)
        imgsarr = ['A','B']
        plt.ylim(0.76,1.22)
    elif lens == '1127':
        plt.legend(testlegs,('A','B'),loc=2)
        imgsarr = ['A','B']
        plt.ylim(0.88,1.14)
    elif lens == '1152':
        plt.legend(testlegs,('A','B'),loc=2)
        imgsarr = ['A','B']
        plt.ylim(0.895,1.11)
    else:
        plt.legend(testlegs,('A','B'),loc=2)
        imgsarr = ['A','B']
    plt.title('Normalized Lightcurve for Lens %s'%(lens_dict[lens]['name']))
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    #plt.xlim(1810-cr[0][0],2090-cr[0][0])
    plt.xlim(1820-cr[0][0],2105-cr[0][0])
    #plt.plot(days[g],np.mean(S[g]/CSOnorm)*np.ones(len(g)))
    if lens != '0712': plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot_offset.%s.png'%(lens,date))
    for j in range(0,np.shape(cr)[0]):
        FILE.write('%3i %5.1f'%(j,days[j]))
        for k in range(0,nimg): FILE.write(' %6.4f'%S_arr[k][j])
        FILE.write('\n')
    FILE.close()
lens = '0712'
cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
nimg = lens_dict[lens]['images']
testlegs = []
plt.figure(1)
plt.clf()
FILE = open('/home/rumbaugh/EVLA/light_curves/test.%s.1.5.14.dat'%lens,'w')
S_arr = np.zeros((nimg,np.shape(cr)[0]))
for img in range(1,nimg):
    arb_offset = 0.15*(img-1.5)
    S = cr[:,img+1]
    rms = cr[:,nimg+img+1]
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.axvline(x=1946-1839,lw=2,ls='dashed',color='k')
    plt.axvline(x=1976-1839,lw=2,ls='dashed',color='k')
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
    S_arr[img-1] = S
    S += arb_offset
    imgarr = ['A+B','C','D','NA']
    if img < 3: 
        plt.axhline(y=np.mean(S[g]/CSOnorm),lw=2,ls='dashed',color='k')
        plt.errorbar(days[g]+dayoffset*(img-1),S[g]/CSOnorm,yerr=Serr[g]/CSOnorm,color=color_arr[img-1],fmt='ro',lw=1,capsize=3,mew=1,marker=symbols[img],ms=sizes[img],label='_nolegend_')
        plt.scatter(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img-1])
        testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g]/CSOnorm,color=color_arr[img-1],lw=2,ls=ls_arr[img-1]))
plt.legend(testlegs,('A+B','C'),loc=2)
plt.title('Normalized Lightcurve for Lens %s'%(lens_dict[lens]['name']))
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
yticklocs,yticklabs = np.array([0.825,0.85,0.875,0.9,0.925,0.95,0.975,1.,1.025,1.05,1.075])+0.15*(-0.5),np.array(['','0.85','','0.90','','0.95','','1.00','','1.05',''])
yticklocs,yticklabs = np.append(yticklocs,np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075,1.1,1.125,1.15])+0.15*(0.5)),np.append(yticklabs,np.array(['','0.95','','1.00','','1.05','','1.10','','']))
plt.yticks(yticklocs,yticklabs)
#plt.xlim(1810-cr[0][0],2090-cr[0][0])
plt.xlim(1820-cr[0][0],2105-cr[0][0])
plt.ylim(0.85,1.16)
#plt.plot(days[g],np.mean(S[g]/CSOnorm)*np.ones(len(g)))
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot_comb_offset.%s.png'%(lens,date))
for j in range(0,np.shape(cr)[0]):
    FILE.write('%3i %5.1f'%(j,days[j]))
    for k in range(0,3): FILE.write(' %6.4f'%S_arr[k][j])
    FILE.write('\n')
FILE.close()
