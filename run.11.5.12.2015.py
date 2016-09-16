import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab

try:
    skipahead
except NameError:
    skipahead = 0
try:
    init
except NameError:
    init = 0

try:
    appendflag
except NameError:
    appendflag = 0

try:
    caxisvar
except NameError:
    caxisvar = 'antenna2'

CSO_arr = np.array(['J0003+4807','J1400+6210','J1414+4554','J1545+4751','J1734+0926','J1816+3457','J1823+7938','J1826+1831','J1927+7358','J1945+7055'])

plottype = np.array(['Amp vs. Time','Amp vs. UVDist','Amp vs. Frequency'])
xaxis_arr = np.array(['time','uvdist','frequency'])

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/PartialObskey_Late.8.30.12.dat',dtype='string')


EarlyorLate_arr = obskey[:,0].copy()
SBgrouparr = obskey[:,1].copy()
SBnumarr = obskey[:,2].copy()
montharr = obskey[:,3].copy()
datearr = obskey[:,4].copy()
SBlongnum_arr = obskey[:,6] .copy()
badants_arr = obskey[:,10].copy()
fieldskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/Fieldskey.dat',dtype='string')
EorLcheck_arr = fieldskey[:,0]
SBcheck_arr = fieldskey[:,1]
numfield_arr = fieldskey[:,2]
fieldsdict = {'Early': {'1': int(numfield_arr[3]), '2': int(numfield_arr[4])}, 'Late': {'1': int(numfield_arr[0]), '2': int(numfield_arr[1]), '3': int(numfield_arr[2])}}

CSO_norm_flux_dict = {'1': {}, '2': {}, '3': {}}
for i in range(0,len(SBnumarr)): CSO_norm_flux_dict[SBgrouparr[i]][SBnumarr[i]] =  np.array([])


BPfielddict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': '9', '2': '3', '3': '3'}}

PFCdict = {'Early': {'1': '3C48', '2': '3C48'}, 'Late': {'1': '3C286', '2': '3C48', '3': '3C48'}}

CSO_fieldnums_dict = {'Early': {'1': np.array(['4','7']), '2': np.array(['1','7'])}, 'Late': {'1': np.array(['1','2','3','4','8','10']), '2': np.array(['1','2','3','4','7','8']), '3': np.array(['1','2','4','8','9','10'])}}

CSO_fieldnames_dict = {'Early': {'1': np.array(['J0427+4133','J0754+5324']), '2': np.array(['J0204+0903','J0754+5324'])}, 'Late': {'1': np.array(['J1414+4554','J1400+6210','J1545+4751','J1816+3457','J1945+7055','J1823+7938']), '2': np.array(['J0003+4807','J1823+7938','J1927+7358','J1945+7055','J1816+3457','J1826+1831']), '3': np.array(['J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'])}}

PCfieldnumdict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['5','7']), '2': np.array(['5']), '3': np.array(['5','7'])}}

PCfieldnamedict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['J2006+6424']), '2': np.array(['J2006+6424']), '3': np.array(['J2006+6424'])}}

avgchannelarr = np.array(['64','64',''])
avgtimearr = np.array(['','','30000'])
avgscanarr = np.array([False,False,True])

june10th_time = 4814380883
timeticks = june10th_time+86400+86400*10*(np.arange(11)-1)
timelabels = np.array(['6-01','6-11','6-21','7-1','7-11','7-21','7-31','8-10','8-20','8-30','9-9'])
pylab.xticks(timeticks,timelabels)
pylab.xlabel('Time')
pylab.ylabel('Normalized Flux')
i,endloop = 0,0
if skipahead == 1:
    i = init
st = time.time()
prevtime = st
for i in range(0,len(CSO_arr)):
    CSOload = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.8.17.12.dat'%CSO_arr[i],dtype='string')
    CSOload2 = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.11.5.12.dat'%CSO_arr[i],dtype='string')
    timest,fluxest,SBnums,scannums = CSOload[:,5],CSOload[:,6],CSOload[:,1],CSOload[:,2]
    times,fluxes = np.zeros(len(timest)),np.zeros(len(timest))
    for j in range(len(timest)):
        times[j],fluxes[j] = float(timest[j]),float(fluxest[j])
    if len(CSOload2.shape) > 1:
        timest2,fluxest2,SBnumst,scannumst = CSOload2[:,5],CSOload2[:,6],CSOload2[:,1],CSOload2[:,2]
        times2,fluxes2 = np.zeros(len(timest2)),np.zeros(len(timest2))
        for j in range(len(timest2)):
            times2[j],fluxes2[j] = float(timest2[j]),float(fluxest2[j])
        times,fluxes,SBnums,scannums = np.append(times,times2),np.append(fluxes,fluxes2),np.append(SBnums,SBnumst),np.append(scannums,scannumst)
    else:
        timest2,fluxest2,SBnumst,scannumst = CSOload2[5],CSOload2[6],CSOload2[1],CSOload2[2]
        times,fluxes,SBnums,scannums = np.append(times,float(timest2)),np.append(fluxes,float(fluxest2)),np.append(SBnums,SBnumst),np.append(scannums,scannumst)
    nfluxes = fluxes/np.average(fluxes)
    for j in range(0,len(fluxes)): CSO_norm_flux_dict[SBnums[j]][scannums[j]] = np.append(CSO_norm_flux_dict[SBnums[j]][scannums[j]],nfluxes[j])
    #pylab.plot(times,fluxes/np.average(fluxes))
    #pylab.scatter(times,fluxes/np.average(fluxes))
june10th_time = 4814380883.0
#pylab.xlim(4814250883,4819371930)
pylab.xlim(timeticks[0]-20000,timeticks[len(timeticks)-1]+20000)
#pylab.savefig('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1928+666.fluxplot.11.5.12.png')
#pylab.close('all')
    

avgposmod =  np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.A1_pos_compiled.8.25.12.dat',dtype='string')
A1xstr = avgposmod[:,7].copy()
A1ystr = avgposmod[:,8].copy()
A1x,A1y = np.zeros(len(A1xstr)),np.zeros(len(A1xstr))
for j in range(0,len(A1x)):
    A1x[j],A1y[j] = float(A1xstr[j]),float(A1ystr[j])
A1x_mean,A1y_mean = np.average(A1x),np.average(A1y)
ltime = np.zeros(len(datearr)-6)
june10th_time = 4814380883.0

ltimemod = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938.LATE.obs_times.8.30.12.dat',dtype='float')
ltimet = ltimemod[:,4].copy()
infile,outfile,loc = 'concatshift.fixpos.8.29.12','/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.fluxplot.concatshift.fixpos.11.5.12',8
for idummy in range(0,1):
#def make_lens_plot(infile,outfile,loc=1):
    i,endloop,i2,i3 = 0,0,0,0
    #A1flux,A2flux,B1flux,B2flux,C1flux,C2flux = np.zeros(len(datearr)-3),np.zeros(len(datearr)-3),np.zeros(len(datearr)-3),np.zeros(len(datearr)-3),np.zeros(len(datearr)-3),np.zeros(len(datearr)-3)
    A1flux,A2flux,B1flux,B2flux,C1flux,C2flux = np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6)


    while ((i < len(datearr)) & (endloop < 0.5)):
        cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
        vis = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
        curvis = vis
        EarlyorLate = EarlyorLate_arr[i]
        SBgroupnum = SBgrouparr[i]
        if ((i != 13) & (i != 6) & (i != 21) & (len(CSO_norm_flux_dict[SBgroupnum][SBnumarr[i]]) <= 1)): 
            i3 += 1
            print SBgroupnum,SBnumarr[i]
        if ((i != 13) & (i != 6) & (i != 21) & (len(CSO_norm_flux_dict[SBgroupnum][SBnumarr[i]]) > 1)): 
            ltime[i2] = ltimet[i3]
            medCSO_nflux = np.median(CSO_norm_flux_dict[SBgroupnum][SBnumarr[i]])
            ifmod = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.%sSB%s_%s.%s.mod'%(EarlyorLate,SBgroupnum,SBnumarr[i],infile),dtype='string',skiprows=4)
            fstr,rstr,PAstr = ifmod[:,0].copy(),ifmod[:,1].copy(),ifmod[:,2].copy()
            fluxes,rads,PAs = np.zeros(len(fstr)),np.zeros(len(fstr)),np.zeros(len(fstr))
            for j in range(0,len(PAs)):
                ft,rt,Pt = fstr[j],rstr[j],PAstr[j]
                fluxes[j],rads[j],PAs[j] = float(ft[0:len(ft)-1]),float(rt[0:len(rt)-1]),float(Pt[0:len(Pt)-1])
                if isnan(fluxes[j]): print 'Nan Detected: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            fluxes *= medCSO_nflux
            Agroupinds = np.where(PAs > 75)
            Agroupinds = Agroupinds[0]
            Agrp_argsort = np.argsort(PAs[Agroupinds])
            A2flux[i2] = fluxes[Agroupinds[Agrp_argsort[0]]]
            A1flux[i2] = fluxes[Agroupinds[Agrp_argsort[1]]]
            if ((rads[Agroupinds[Agrp_argsort[1]]] < rads[Agroupinds[Agrp_argsort[0]]]) | (len(Agroupinds) != 2)): "Something went wrong with A1 and A2"
            group2inds = np.where(PAs < 60)
            group2inds = group2inds[0]
            grp2_argsort = np.argsort(PAs[group2inds])
            B1flux[i2] = fluxes[group2inds[grp2_argsort[len(group2inds)-1]]]
            group3inds = np.where(PAs < PAs[group2inds[grp2_argsort[len(group2inds)-1]]]-0.1)
            group3inds = group3inds[0]
            grp3_argsort = np.argsort(rads[group3inds])
            C2flux[i2] = fluxes[group3inds[grp3_argsort[0]]]
            C1flux[i2] = fluxes[group3inds[grp3_argsort[1]]]
            B2flux[i2] = fluxes[group3inds[grp3_argsort[2]]]
            if isnan(A2flux[i2]): print 'A2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(A1flux[i2]): print 'A1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(C2flux[i2]): print 'C2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(C1flux[i2]): print 'C1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(B2flux[i2]): print 'B2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(B1flux[i2]): 
                print 'B1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
                print medCSO_nflux
            if ((B2flux[i2] > B1flux[i2]) | (len(group3inds) != 3) | (len(group2inds) != 4)): sys.exit("Something went wrong with B/C images")
            i2 += 1
            i3 += 1
        conflagarr = np.loadtxt('/home/rumbaugh/Continue.txt',dtype='string')  
        if conflagarr == 'False': endloop = 1
        if endloop != 1: i += 1
    A1nflux,A2nflux,B1nflux,B2nflux,C1nflux,C2nflux = A1flux/np.average(A1flux),A2flux/np.average(A2flux),B1flux/np.average(B1flux),B2flux/np.average(B2flux),C1flux/np.average(C1flux),C2flux/np.average(C2flux)
    timeticks = june10th_time+86400+86400*10*(np.arange(11)-1)
    timelabels = np.array(['6-01','6-11','6-21','7-1','7-11','7-21','7-31','8-10','8-20','8-30','9-9'])
    ax = pylab.axes()
    pylab.xticks(timeticks,timelabels)
    pylab.ylim(np.min(A2flux)*0.9,np.max(C1flux)*1.1)
    pylab.xlim(4814250883,4819371930)
    pylab.xlabel('Time')
    pylab.ylabel('Normalized Flux')
    pylab.plot(ltime,A1nflux,label='A1')
    pylab.plot(ltime,A2nflux,label='A2')
    pylab.plot(ltime,B1nflux,label='B1')
    pylab.plot(ltime,B2nflux,label='B2')
    pylab.plot(ltime,C1nflux,label='C1')
    pylab.plot(ltime,C2nflux,label='C2')
    handles, labels = ax.get_legend_handles_labels()
    #print handles,labels
    #pylab.figlegend(handles,labels,1)
    ax.legend(loc=loc)
     #pylab.legend()
    pylab.scatter(ltime,A1nflux)
    pylab.scatter(ltime,A2nflux)
    pylab.scatter(ltime,B1nflux)
    pylab.scatter(ltime,B2nflux)
    pylab.scatter(ltime,C1nflux)
    pylab.scatter(ltime,C2nflux)
    pylab.savefig(outfile + '.png')
    pylab.close()
    ax = pylab.axes()
    pylab.xticks(timeticks,timelabels)
    pylab.ylim(np.min(A2flux)*0.9,np.max(C1flux)*1.1)
    pylab.xlim(4814250883-0.15*(4819371930-4814250883),4819371930)
    pylab.xlabel('Time')
    pylab.ylabel('Normalized Flux (with offset)')
    pylab.plot(ltime,A1nflux+2*offset,label='A1')
    pylab.plot(ltime,B1nflux+offset,label='B1')
    pylab.plot(ltime,C1nflux,label='C1')
    pylab.plot(ltime,C2nflux-offset,label='C2')
    handles, labels = ax.get_legend_handles_labels()
    #print handles,labels
    #pylab.figlegend(handles,labels,1)
    ax.legend(loc=2)
    #pylab.legend()
    pylab.scatter(ltime,A1nflux+2*offset)
    pylab.scatter(ltime,B1nflux+offset)
    pylab.scatter(ltime,C1nflux)
    pylab.scatter(ltime,C2nflux-offset)
    pylab.plot(ltime,np.ones(len(ltime))+2*offset,color='black',linestyle='dashed')
    pylab.plot(ltime,np.ones(len(ltime))+offset,color='black',linestyle='dashed')
    pylab.plot(ltime,np.ones(len(ltime)),color='black',linestyle='dashed')
    pylab.plot(ltime,np.ones(len(ltime))-offset,color='black',linestyle='dashed')
    pylab.xlim(4814250883-0.2*(4819371930-4814250883),4819371930+(4819371930-4814250883)*4.0/7.0)
    pylab.savefig(outfile + '.offset.png')
    pylab.close()
    #return

#make_lens_plot('concatshift.fixpos.11.5.12','/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.fluxplot.concatshift.fixpos.8.30.12',loc=8)
os.system('cp /local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.fluxplot.concatshift.fixpos.11.5.12*g /home/rumbaugh/.')

if endloop < 0.4: print '\n\nAll Done!\n'
    
