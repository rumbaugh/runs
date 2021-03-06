import numpy as np

pdate = '2.4.15'

dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']

CSOs = ['1244+408','1400+621']


rms_dict = dict(zip(sources,np.zeros(len(sources))))

aips_dates = np.zeros(len(dates),dtype='|S8')
for i in range(0,len(dates)):
    date = dates[i]
    year,day = date[-2:],date[-5:-3]
    if year == '00':
        month = date[0:2]
    else:
        month = date[0]
    aips_dates[i] = '%02s%02i%2s'%(year,int(month),day)

for lens in sources:
    rms_dict[lens] = np.zeros(0,dtype='f8')
    FILE = open('/home/rumbaugh/VLA/AF377/difmap_results/rms_out.%s.dat'%lens,'w')
    for date,aipsdate in zip(dates,aips_dates):
        tsources,tCSOs = np.copy(sources),np.copy(CSOs)
        if date in ['1.15.01','11.20.00','12.07.00']: tsources,tCSOs = ['0414+573','1030+074','1127+385','0712+472'],['1400+621']
        if date == '4.10.01': tsources = ['1127+385','0712+472']
        if date in ['10.08.00','10.10.00','11.26.00','12.03.00']: tsources = ['1030+074','1127+385','1152+199','0712+472']
        if date == '3.06.01': tsources,tCSOs = ['0414+573','1127+385','0712+472'],['1400+621']
        if lens in tsources:
            cr = np.loadtxt('/home/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_wrms_%s.%s.fixpos.%s.mod'%(lens,pdate,date),comments='!',dtype='string',usecols=(0,))
            trms = float(cr[-1])
            rms_dict[lens] = np.append(rms_dict[lens],trms)
            FILE.write('%f\n'%trms)
    FILE.close()
    tsort = np.sort(rms_dict[lens])
    print '%s\nrms = %f - %f\n'%(lens,tsort[0],tsort[-1])
    print np.median(tsort)
