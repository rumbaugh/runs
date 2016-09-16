import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

Bcutoff = 2025-1839.

space_inbetween = 0.2
dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

days4months_dict  = {5: 28, 4: 28+30, 3: 28+30+31, 2: 28+30+31+28, 1: 28+30+31+28+31, 12: 28+30+31+28+31+31, 11: 28+30+31+28+31+31+30, 10: 28+30+31+28+31+31+30+31}

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573']#,'1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

for source in sources:
    tdates = np.array(np.copy(dates))
    gdel = np.zeros(0,dtype='int')
    if source == '0414+573':
        gdel = np.where((tdates == '4.10.01') | (tdates == '11.26.00') | (tdates == '12.03.00'))[0]
        #tdates = np.delete(tdates,gdel)
    elif source == '1030+074':
        gdel = np.where((tdates == '4.10.01') | (tdates == '3.06.01'))[0]
        #tdates = np.delete(tdates,gdel)
    elif source == '1152+199':
        gdel = np.where((tdates == '1.15.01') | (tdates == '11.20.00') | (tdates == '12.07.00') | (tdates == '4.10.01') | (tdates == '3.06.01'))[0]
        #tdates = np.delete(tdates,gdel)
    FILE = open('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_UVR_0_300_5.29.14_%s.dat'%source,'w')
    for date in tdates:
        if date[1] == '.':
            month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
        else:
            month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
        daytot = 2058-days4months_dict[month]+day
        #if date not in ['3.06.01','3.16.01','4.10.01']:
        if date not in tdates[gdel]:
            FILE.write('%f'%daytot)
            cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_5.29.14.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!',usecols=(0,1,2))
            num_img = 4
            for img in range(0,num_img):
                fluxstr = cr[img][0]
                FILE.write(' ' + fluxstr[:len(fluxstr)-1])
            FILE.write('\n')
        else:
            FILE.write('%f'%daytot)
            if source in ['0414+573','0712+472']: num_img = 4
            else: num_img = 2
            for img in range(0,num_img):
                FILE.write(' 0.')
            FILE.write('\n')
    FILE.close()

import matplotlib.pylab as plt
fluxratio_err = 0.0088

date = '5.29.14'

lens_dict = {'0414': {'name': 'MG0414', 'fullname': '0414+573', 'images': 4}, '0712': {'name': 'B0712', 'fullname': '0712+472', 'images': 4}, '1030': {'name': 'J1030', 'fullname': '1030+074','images': 2}, '1127': {'name': 'B1127','fullname': '1127+385','images': 2}, '1152': {'name': 'B1152','fullname': '1152+199','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']

#CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_1244+408.dat'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_1400+621.dat')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,1],CSO2cr[:,1]

#CSO1day -= CSO1day[0]
#CSO2day -= CSO2day[0]

g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]

CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

orig_sib = space_inbetween
for lens in ['0414']:
    if lens == '0414':
        space_inbetween = 0.08
        yticklocs,yticklabs = np.array([0.96,0.98,1.,1.02,1.04])+space_inbetween*(-1.5),np.array(['','0.98','1.00','1.02',''])
        yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1.5),np.copy(yticklabs)
        for i in range(1,4):
            yticklocs,yticklabs = np.append(yticklocs,yticklocso+space_inbetween*(i-1.5)),np.append(yticklabs,yticklabso)
    #FILE = open('/home/rumbaugh/EVLA/light_curves/test.%s.%s.dat'%(lens,date),'w')
    #cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/%s_g.edt'%(lens))
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_UVR_0_300_5.29.14_%s.dat'%(lens_dict[lens]['fullname']))
    nimg = lens_dict[lens]['images']
    days = cr[:,0]-cr[0][0]
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #plt.fill_betweenx([-999,999],[Bcutoff,Bcutoff],[999,999],edgecolor='k',facecolor='none')#,hatch='/')
    plt.bar([Bcutoff],[999],width=500,bottom=-200,edgecolor='k',facecolor='none',hatch='/')
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
        rms = np.zeros(len(S))
        #rms = cr[:,nimg+img+1]
        g = np.where((CSO1S>0)&(CSO2S>0)&(S>0))
        CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        #CSOnorm = 0.5*(CSO1S/np.mean(CSO1S[g]) + CSO2S/np.mean(CSO2S[g]))
        if lens == '0414':
            S[1],S[26],S[11],S[-18] = 0,0,0,0
            g = np.where((S>0)&(CSO1S>0)&(CSO2S>0))[0]
            CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
        Smean = np.mean(S[g])
        S /= Smean
        Serr /= Smean
        S_arr[img] = S
        S += arb_offset
        imgarr = ['A','B','NA','NA']
        if lens == '0414': imgarr = ['A1','A2','B','C']
        plt.axhline(y=np.mean(S[g]/CSOnorm),lw=2,ls='dashed',color='k')
        plt.errorbar(days[g],S[g]/CSOnorm,yerr=Serr[g]/CSOnorm,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label=None)
        plt.scatter(days[g],S[g]/CSOnorm,color=color_arr[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g],S[g]/CSOnorm,color=color_arr[img],lw=2,ls=ls_arr[img]))
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
    if lens != '0712': plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.lc_norm_plot_offset_UVR_0_300.%s.png'%(lens,date))
