import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab

execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/smoothing_1d.py")
execfile("/home/rumbaugh/chi_squared_min.py")

try:
    justone
except NameError:
    justone = False
try:
    skipahead
except NameError:
    skipahead = 0
try:
    init
except NameError:
    init = 0
try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0095

try:
    timestep
except NameError:
    timestep = 1.0
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 50*timestep
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

CSO_arr = np.array(['J0003+4807','J1400+6210','J1414+4554','J1545+4751','J1734+0926','J1816+3457','J1823+7938','J1826+1831','J1927+7358','J1945+7055'])
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
BPfielddict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': '9', '2': '3', '3': '3'}}
PFCdict = {'Early': {'1': '3C48', '2': '3C48'}, 'Late': {'1': '3C286', '2': '3C48', '3': '3C48'}}
CSO_fieldnums_dict = {'Early': {'1': np.array(['4','7']), '2': np.array(['1','7'])}, 'Late': {'1': np.array(['1','2','3','4','8','10']), '2': np.array(['1','2','3','4','7','8']), '3': np.array(['1','2','4','8','9','10'])}}
CSO_fieldnames_dict = {'Early': {'1': np.array(['J0427+4133','J0754+5324']), '2': np.array(['J0204+0903','J0754+5324'])}, 'Late': {'1': np.array(['J1414+4554','J1400+6210','J1545+4751','J1816+3457','J1945+7055','J1823+7938']), '2': np.array(['J0003+4807','J1823+7938','J1927+7358','J1945+7055','J1816+3457','J1826+1831']), '3': np.array(['J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'])}}
PCfieldnumdict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['5','7']), '2': np.array(['5']), '3': np.array(['5','7'])}}
PCfieldnamedict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['J2006+6424']), '2': np.array(['J2006+6424']), '3': np.array(['J2006+6424'])}}


avgposmod =  np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.A1_pos_compiled.8.25.12.dat',dtype='string')
A1xstr = avgposmod[:,7].copy()
A1ystr = avgposmod[:,8].copy()
A1x,A1y = np.zeros(len(A1xstr)),np.zeros(len(A1xstr))
for j in range(0,len(A1x)):
    A1x[j],A1y[j] = float(A1xstr[j]),float(A1ystr[j])
A1x_mean,A1y_mean = np.average(A1x),np.average(A1y)
#ltime = np.zeros(len(datearr)-6)
june10th_time = 4814380883.0

ltimemod = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938.LATE.obs_times.8.30.12.dat',dtype='float')
ltimet = ltimemod[:,4].copy()
infile,outfile,loc = 'concatshift.fixpos.8.29.12','/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.fluxplot.concatshift.fixpos.11.5.12',8

#rms errors
rmsload = np.loadtxt('/home/rumbaugh/rms_errors.B1938+666.12.7.12.dat',dtype='string')
rmsgrouparr,rmsnumarr,rms_arr = rmsload[:,1].copy(),rmsload[:,2].copy(),str2float(rmsload[:,3].copy())
rmsindarr = np.zeros(0,dtype='int')

CSO_norm_flux_dict = {'1': {}, '2': {}, '3': {}}
for i in range(0,len(SBnumarr)): CSO_norm_flux_dict[SBgrouparr[i]][SBnumarr[i]] =  np.array([])

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


i,endloop,i2,i3 = 0,0,0,0
#A1flux,A2flux,B1flux,B2flux,C1flux,C2flux = np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6),np.zeros(len(datearr)-6)
A1flux,A2flux,B1flux,B2flux,C1flux,C2flux,ltime = np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)

#all of this is to set up the arrays with the image fluxes
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
        if ((SBnumarr[i] != '15') & (SBnumarr[i] in rmsnumarr) & (SBgrouparr[i] in rmsgrouparr)):
            ltime = np.append(ltime,ltimet[i3])
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
        if ((SBnumarr[i] != '15') & (SBnumarr[i] in rmsnumarr) & (SBgrouparr[i] in rmsgrouparr)):
            A2flux = np.append(A2flux,fluxes[Agroupinds[Agrp_argsort[0]]])
            A1flux = np.append(A1flux,fluxes[Agroupinds[Agrp_argsort[1]]])
        if ((rads[Agroupinds[Agrp_argsort[1]]] < rads[Agroupinds[Agrp_argsort[0]]]) | (len(Agroupinds) != 2)): "Something went wrong with A1 and A2"
        group2inds = np.where(PAs < 60)
        group2inds = group2inds[0]
        grp2_argsort = np.argsort(PAs[group2inds])
        if ((SBnumarr[i] != '15') & (SBnumarr[i] in rmsnumarr) & (SBgrouparr[i] in rmsgrouparr)):
            B1flux = np.append(B1flux,fluxes[group2inds[grp2_argsort[len(group2inds)-1]]])
        group3inds = np.where(PAs < PAs[group2inds[grp2_argsort[len(group2inds)-1]]]-0.1)
        group3inds = group3inds[0]
        grp3_argsort = np.argsort(rads[group3inds])
        if ((SBnumarr[i] != '15') & (SBnumarr[i] in rmsnumarr) & (SBgrouparr[i] in rmsgrouparr)):
            C2flux = np.append(C2flux,fluxes[group3inds[grp3_argsort[0]]])
            C1flux = np.append(C1flux,fluxes[group3inds[grp3_argsort[1]]])
            B2flux = np.append(B2flux,fluxes[group3inds[grp3_argsort[2]]])
            grmsind1 = np.where(rmsgrouparr == SBgrouparr[i])
            grmsind1 = grmsind1[0]
            grmsind2 = np.where(rmsnumarr[grmsind1] == SBnumarr[i])
            grmsind2 == grmsind2[0]
            rmsindarr = np.append(rmsindarr,grmsind1[grmsind2[0]])
        if len(A2flux) > 0:
            if isnan(A2flux[len(A2flux)-1]): print 'A2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(A1flux[len(A2flux)-1]): print 'A1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(C2flux[len(A2flux)-1]): print 'C2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(C1flux[len(A2flux)-1]): print 'C1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(B2flux[len(A2flux)-1]): print 'B2flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
            if isnan(B1flux[len(A2flux)-1]): 
                print 'B1flux is NaN: LateSB%s_%s'%(SBgroupnum,SBnumarr[i])
                print medCSO_nflux
            if ((B2flux[len(A2flux)-1] > B1flux[len(A2flux)-1]) | (len(group3inds) != 3) | (len(group2inds) != 4)): sys.exit("Something went wrong with B/C images")
        i2 += 1
        i3 += 1
    conflagarr = np.loadtxt('/home/rumbaugh/Continue.txt',dtype='string')  
    if conflagarr == 'False': endloop = 1
    if endloop != 1: i += 1
A1nflux,A2nflux,B1nflux,B2nflux,C1nflux,C2nflux = A1flux/np.average(A1flux),A2flux/np.average(A2flux),B1flux/np.average(B1flux),B2flux/np.average(B2flux),C1flux/np.average(C1flux),C2flux/np.average(C2flux)

#error propagation
A1err,B1err,C1err,C2err = np.zeros(len(A1flux)),np.zeros(len(A1flux)),np.zeros(len(A1flux)),np.zeros(len(A1flux))
for i in range(0,len(A1err)):
    A1err[i],B1err[i],C1err[i],C2err[i] = m.sqrt(rms_arr[rmsindarr[i]]**2+(fluxratio_err*A1flux[i])**2),m.sqrt(rms_arr[rmsindarr[i]]**2+(fluxratio_err*B1flux[i])**2),m.sqrt(rms_arr[rmsindarr[i]]**2+(fluxratio_err*C1flux[i])**2),m.sqrt(rms_arr[rmsindarr[i]]**2+(fluxratio_err*C2flux[i])**2)
    print A1err[i],rms_arr[rmsindarr[i]]/A1err[i],fluxratio_err*A1flux[i]/A1err[i]
    print B1err[i],rms_arr[rmsindarr[i]]/B1err[i],fluxratio_err*B1flux[i]/B1err[i]
    print C1err[i],rms_arr[rmsindarr[i]]/C1err[i],fluxratio_err*C1flux[i]/C1err[i]
    print C2err[i],rms_arr[rmsindarr[i]]/C2err[i],fluxratio_err*C2flux[i]/C2err[i]
A1avgerr,B1avgerr,C1avgerr,C2avgerr = m.sqrt(np.sum(A1err*A1err))/len(A1err),m.sqrt(np.sum(B1err*B1err))/len(B1err),m.sqrt(np.sum(C1err*C1err))/len(C1err),m.sqrt(np.sum(C2err*C2err))/len(C2err)
A1nerr,B1nerr,C1nerr,C2nerr = np.zeros(len(A1flux)),np.zeros(len(A1flux)),np.zeros(len(A1flux)),np.zeros(len(A1flux))
for i in range(0,len(A1err)):
    A1nerr[i],B1nerr[i],C1nerr[i],C2nerr[i] = m.sqrt((A1err[i]/A1flux[i])**2+(A1avgerr/np.average(A1flux))**2),m.sqrt((B1err[i]/B1flux[i])**2+(B1avgerr/np.average(B1flux))**2),m.sqrt((C1err[i]/C1flux[i])**2+(C1avgerr/np.average(C1flux))**2),m.sqrt((C2err[i]/C2flux[i])**2+(C2avgerr/np.average(C2flux))**2)

ltime = (ltime-ltime[0])/86400
#find time delays
bcar_widths = np.array([5.,10.,15.])
t_grid = np.arange(int(max(ltime))+3)-1
for i in range(0,len(bcar_widths)):
    BA_delay,BAmu,BAchisq,BAneff = chi_squared_min_delays(A1nflux,B1nflux,ltime,ltime,A1nerr,B1nerr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    BC1_delay,BC1mu,BC1chisq,BC1neff = chi_squared_min_delays(C1nflux,B1nflux,ltime,ltime,C1nerr,B1nerr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    BC2_delay,BC2mu,BC2chisq,BC2neff = chi_squared_min_delays(C2nflux,B1nflux,ltime,ltime,C2nerr,B1nerr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    print "\nBoxcar Width: %i days\n B-A - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n B-C1 - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n B-C2 - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n"%(bcar_widths[i],BA_delay,BAmu,BAchisq,BAchisq/BAneff,BAneff,BC1_delay,BC1mu,BC1chisq,BC1chisq/BC1neff,BC1neff,BC2_delay,BC2mu,BC2chisq,BC2chisq/BC2neff,BC2neff)
