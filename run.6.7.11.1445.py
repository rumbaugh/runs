import numpy as np
import math
import matplotlib.pylab as pylab
import matplotlib.axes as ax

execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/plotcircle.py")
execfile("/home/rumbaugh/angconvert.py")

degree_symbol = unichr(176)

try:
    Ilim
except NameError:
    Ilim = 23.5

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'
html_green = '#99FF00'
html_grey = '#CCCCCC'
html_yelo = '#FFFF00'

names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
path = '/home/rumbaugh/LFC'
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])
pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])
zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])

masks1324 = np.array(['1322A','1322C','1322E','1322F','1322G','1322H','1322J','1322K','1322L','1322M'])#,'LRIS'])
masks1604 = np.array(['GHF1','GHF2','FG1','FG2','16XR1','16XR2','16XR3','16CN2','16CN3','16CN4','16CN5','16CN6','16COM1','CE1','LRIS.scm1','LRIS.scm2','LRIS.scm4','LRIS.scnm2','SC1NM1','SC1NM2','SC2NM1','SC2NM2','oldLRIS','oldLRISe'])
masks5281 = np.array(['5281M1','5281M2','5281M3'])
masks1757 = np.array(['N200M1','N200M2'])#,'N200X1','N200X2'])
#masks0023 = np.array(['0023X1','0023X2','0023X3B','0023X4','
masks0023 = np.array(['00DMA','00DMB','00ND1','00ND2','00ND4'])#,'LRIS'])

colorlist = np.array(['red','blue',html_teal,html_pink,html_orng,html_brwn,html_green,'green',html_purp,html_yelo])


for i in range(0,5):
    master = 'master'
    if i == 2: master = '7914'
    sfile = '%s/%s'%(path,files[i])
    pfile = '%s/%s'%(path,pfiles[i])
    crp = read_file(pfile)
    if i == 0:
        pRA = get_colvals(crp,'col3')
        pDec = get_colvals(crp,'col4')
        pR = get_colvals(crp,'col5')
        pI = get_colvals(crp,'col6')
        pZ = get_colvals(crp,'col7')
    else:
        pRA = get_colvals(crp,'col2')
        pDec = get_colvals(crp,'col3')
        pR = get_colvals(crp,'col4')
        pI = get_colvals(crp,'col5')
        pZ = get_colvals(crp,'col6')
    
    crs = read_file(sfile)
    smask = get_colvals(crs,'col2')
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sq = get_colvals(crs,'col11')
    sz = get_colvals(crs,'col9')
    
    gsI = np.where(sI < Ilim)
    gsq = np.where((sq > 2.3))
    gsq = gsq[0]
    gsz = np.where((sz[gsq] >= zlb[i]) & (sz[gsq] <= zub[i]))
    gsz = gsz[0]

    gt = np.where(pI <= Ilim)
    gt = gt[0]

    if i == 0:
        #Cl1324
        pylab.ylim(30.0 + 6.0/60,31 + 2.0/60)
        pylab.xlim(201.55185,200.81315)
        xlocs = np.array([201.5,201.375,201.25,201.125,201.0,200.875])
        xlabs = np.array(['26$^{m}$00$^{s}$','30$^{s}$','25$^{m}$00$^{s}$','30$^{s}$','24$^{m}$00$^{s}$','13$^{h}$23$^{m}$30$^{s}$'])
        ylocs = np.array([30 + 10.0/60,30 + 15.0/60,30 + 20.0/60,30 + 25.0/60,30 + 30.0/60,30 + 35.0/60,30 + 40.0/60,30 + 45.0/60,30 + 50.0/60,30 + 55.0/60,31.0])
        ylabels = np.array(['30' + degree_symbol + "10'","15'","20'","25'","30'","35'","40'","45'","50'","55'",'31' + degree_symbol + "00'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        pylab.scatter(pRA[gt],pDec[gt],s=0.2,label='All Phot.')
        for j in range(0,len(masks1324)):
            g = np.where(smask[gsI] == masks1324[j])
            pylab.scatter(sRA[gsI[g]],sDec[gsI[g]],s=6,color=colorlist[j],label=masks1324[j])
        #handles, labels = ax.Axes.get_legend_handles_labels()
        #leg = pylab.legend(handles,labels,loc=3,markerscale=0.8,labelspacing=0.3)
        leg = pylab.legend()
        for t in leg.get_texts():
            t.set_fontsize('small') 
    if i == 1:
        #NEP5281
        pylab.xlim(275.797,274.953)
        pylab.ylim(68+19.5/60.0,68+34.0/60)
        xlocs = np.array([275.75,275.625,275.5,275.375,275.25,275.125,275])
        xlabs = np.array(['23$^{m}$00$^{s}$','30$^{s}$','22$^{m}$00$^{s}$','30$^{s}$','21$^{m}$00$^{s}$','30$^{s}$','18$^{h}$20$^{m}$00$^{s}$'])
        ylocs = np.array([68 + 20.0/60,68 + 25.0/60,68 + 30.0/60])
        ylabels = np.array(['68' + degree_symbol + "20'","25'","30'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        pylab.scatter(pRA[gt],pDec[gt],s=0.2,label='All Phot.')
        for j in range(0,len(masks5281)):
            g = np.where(smask[gsI] == masks5281[j])
            pylab.scatter(sRA[gsI[g]],sDec[gsI[g]],s=6,color=colorlist[j],label=masks1324[j])
        #leg = pylab.legend(loc=3,markerscale=0.8,labelspacing=0.3)
	leg = pylab.legend()
        for t in leg.get_texts():
            t.set_fontsize('small') 
    if i == 2:
        #Cl0023
        pylab.xlim(6.17,5.77)
        pylab.ylim(4 + 13.6/60,4 + 32.36/60)
        xlocs = np.array([5.875,6.0,6.125])
        xlabs = np.array(['0$^{h}$23$^{m}$30$^{s}$','24$^{m}$00$^{s}$','30$^{s}$'])
        ylocs = np.array([4 + 15.0/60,4 + 20.0/60,4 + 25.0/60,4 + 30.0/60])
        ylabels = np.array(['4' + degree_symbol + "15'","20'","25'","30'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        pylab.scatter(pRA[gt],pDec[gt],s=0.2,label='All Phot.')
        for j in range(0,len(masks0023)):
            g = np.where(smask[gsI] == masks0023[j])
            pylab.scatter(sRA[gsI[g]],sDec[gsI[g]],s=6,color=colorlist[j],label=masks1324[j])
        #leg = pylab.legend(loc=3,markerscale=0.8,labelspacing=0.3)
	leg = pylab.legend()
        for t in leg.get_texts():
            t.set_fontsize('small') 
    if i == 3:
        #Cl1604
        pylab.xlim(241.4,240.68)
        pylab.ylim(43+2.0/60,43+27.0/60)
        xlocs = np.array([240.75,240.875,241,241.125,241.25,241.375])
        xlabs = np.array(['16$^{h}$03$^{m}$00$^{s}$','30$^{s}$','04$^{m}$00$^{s}$','30$^{s}$','05$^{m}$00$^{s}$','30$^{s}$'])
        ylocs = np.array([43 + 5.0/60,43 + 10.0/60,43 + 15.0/60,43 + 20.0/60,43 + 25.0/60])
        ylabels = np.array(['43' + degree_symbol + "05'","10'","15'","20'","25'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        pylab.scatter(pRA[gt],pDec[gt],s=0.2,label='All Phot.')
        #for j in range(0,len(masks1604)):
        #    g = np.where(smask[gsI] == masks1604[j])
        #    pylab.scatter(sRA[gsI[g]],sDec[gsI[g]],s=6,color=colorlist[j],label=masks1324[j])
        ##leg = pylab.legend(loc=3,markerscale=0.8,labelspacing=0.3)
	leg = pylab.legend()
        #for t in leg.get_texts():
        #    t.set_fontsize('small') 
    if i == 4:
        #RXJ1757
        pylab.xlim(269.75,269.0)
        pylab.ylim(66 + 24.0/60, 66+38.0/60)
        xlocs = np.array([269.625,269.5,269.375,269.25,269.125,269])
        xlabs = np.array(['30$^{s}$','58$^{m}$00$^{s}$','30$^{s}$','57$^{m}$00$^{s}$','30$^{s}$','17$^{h}$56$^{m}$00$^{s}$'])
        ylocs = np.array([66 + 25.0/60,66.5,66 + 35.0/60])
        ylabels = np.array(['66' + degree_symbol + "25'","30'","35'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        pylab.scatter(pRA[gt],pDec[gt],s=0.2,label='All Phot.')
        for j in range(0,len(masks1757)):
            g = np.where(smask[gsI] == masks1757[j])
            pylab.scatter(sRA[gsI[g]],sDec[gsI[g]],s=6,color=colorlist[j],label=masks1324[j])
        #leg = pylab.legend(loc=3,markerscale=0.8,labelspacing=0.3)
	leg = pylab.legend()
        for t in leg.get_texts():
            t.set_fontsize('small')
    savfile = '/home/rumbaugh/paperstuff/masks.spatmap.color.%s.6.8.11.png'%(names[i])
    pylab.savefig(savfile)
    pylab.close('all')
      
