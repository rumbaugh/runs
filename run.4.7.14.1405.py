import numpy as np
import matplotlib.pylab as plt

lens_dict = {'0414': {'name': 'MG0414', 'fullname': '0414+573', 'images': 4}, '0712': {'name': 'B0712', 'fullname': '0712+472', 'images': 4}, '1030': {'name': 'J1030', 'fullname': '1030+074','images': 2}, '1127': {'name': 'B1127','fullname': '1127+385','images': 2}, '1152': {'name': 'B1152','fullname': '1152+199','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']


sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_NC_4.5.14_1244+408.dat'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_NC_4.5.14_1035+564.dat')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,1],CSO2cr[:,1]

g = np.where((CSO1S>0)&(CSO2S>0))#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_3.23.14_1244+408.dat'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_3.23.14_1400+621.dat')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,1],CSO2cr[:,1]
g = np.where((CSO1S>0)&(CSO2S>0))#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO


CSOnorm2 = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

lens='1030'
img=0
cr1 = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_NC_4.5.14_%s.dat'%(lens_dict[lens]['fullname']))
S1 = cr1[:,img+1]
cr2 = np.loadtxt('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_3.23.14_%s.dat'%(lens_dict[lens]['fullname']))
S2 = cr2[:,img+1]
