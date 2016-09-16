import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/angconvert.py")

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'
  

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,269.27742210,275.3801,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66.43162760,68.4651,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])

BCGfile = '/home/rumbaugh/BCGpositions.2.15.12.dat'
crBCG = read_file(BCGfile)
BCGRA = copy_colvals(crBCG,'col2')
BCGDec = copy_colvals(crBCG,'col3')

distBCG,distRGP,distgalmean = np.zeros(9),np.zeros(9),np.zeros(9)

FILE = open('paper.centers_table.2.15.12.dat','w')
for i in range(0,9):
    FILEr = open('/home/rumbaugh/paper_marks.%s.2.17.12.reg'%(names[i]),'w')
    distBCG[i] = SphDist(centerRAs[i],centerDecs[i],BCGRA[i],BCGDec[i])
    distRGP[i] = SphDist(centerRAs[i],centerDecs[i],RGalPeakRA[i],RGalPeakDec[i])
    bcgrah,bcgram,bcgras = dec2hms(BGCRA[i])
    bcgdecd,bcgdecm,bcgdecs = dec2dms(BCGDec[i])
    rgrah,rgram,rgras = dec2hms(RGalPeakRA[i])
    rgdecd,rgdecn,rgdecs = dec2dms(RGalPeakDec[i])
    bcgramstr = '%i'%(bcgram)
    if bcgram < 10: bcgramstr = '0%i'%(bcgram)
    bcgrasstr = '%4.1f'%(bcgras)
    if bcgras < 10: bcgrasstr - '0%3.1f'%(bcgras)
    rgramstr = '%i'%(rgram)
    if rgram < 10: rgramstr = '0%i'%(rgram)
    rgrasstr = '%4.1f'%(rgras)
    if rgras < 10: rgrasstr - '0%3.1f'%(rgras)
    bcgdecmstr = '%i'%(bcgdecm)
    if bcgdecm < 10: bcgdecmstr = '0%i'%(bcgdecm)
    bcgdecsstr = '%4.1f'%(bcgdecs)
    if bcgdecs < 10: bcgdecsstr - '0%3.1f'%(bcgdecs)
    rgdecmstr = '%i'%(rgdecm)
    if rgdecm < 10: rgdecmstr = '0%i'%(rgdecm)
    rgdecsstr = '%4.1f'%(rgdecs)
    if rgdecs < 10: rgdecsstr - '0%3.1f'%(rgdecs)
    FILEr.write('point(%f,%f) # point=circle color=pink\n'%(BCGRA[i],BCGDec[i]))
    FILEr.write('point(%f,%f) # point=x color=teal\n'%([i],[i]))
    FILEr.write('point(%f,%f) # point=diamond color=orange\n'%(RGalPeakRA[i],RGalPeakDec[i]))
    FILE.write('%13s & %3i %s %s & %2i %s %s & %3i & %3i %s %s & %2i %s %s & %3i & %3i %s %s & %2i %s %s & %3i'%(names[i],bcgrah,bcgramstr,bcgrasstr,bcgdecd,bcgdecmstr,bcgdecsstr,distBCG[i],rgrah,rgramstr,rgrasstr,rgdecd,rgdecmstr,rgdecsstr,rah,rgramstr,rgrasstr,rgdecd,rgdecmstr,rgdecsstr,distRGP[i],))
    if i < 8: FILE.write(' \\\\\n')
    FILEr.close()
FILE.close()
