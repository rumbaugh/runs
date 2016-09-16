set_dirs
set_plot,'PS'
device,file='/home/rumbaugh/paperstuff/CapODPlotOverPlot.7.28.11.ps',/color
loadct,13

readcol,"/home/rumbaugh/LFC/logNlogS.powlaw.fit.dat",names,k_0,k_0_err,k0kref,k0kreferr,k1,k1err,a1,a1err,k1kr,k1krerr,k2,k2err,a2,a2err,k2kr,k2krerr,k3,k3err,a3,a3err,k3kr,k3krerr,format="A,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D"

readcol,"/scratch/rumbaugh/ciaotesting/analysis/CapODplot.dat",zt,Rt,Rerrt,format="D,D,D"

cz = (0.69+0.82+0.76+0.84+0.9)/5.0
zMe = DBLARR(6)
zMe[0] = 0.69
zMe[1] = 0.82
zMe[2] = 0.76
zMe[3] = 0.84
zMe[4] = 0.9
zMe[5] = cz

zlen = n_elements(zt)-2
z = zt[0:zlen-1]
R = Rt[0:zlen-1]
Rerr = Rerrt[0:zlen-1]
CfitZ = DBLARR(2)
CfitZ[0] = zt[zlen]
CfitZ[1] = zt[zlen+1]
CfitR = DBLARR(2)
CfitR[0] = Rt[zlen]
CfitR[1] = Rt[zlen+1]

plot,[0,1],[0,1],/nodata,XRANGE=[0,1.5],YRANGE=[0.5,2.5],xstyle=1,ystyle=1,XTITLE="z",YTITLE="k/k!Dref",CHARTHICK=5,CHARSIZE=1.4,XTHICK=4,YTHICK=4
oploterror,z,R,Rerr,PSYM=4,color=30,SYMSIZE=1.2,THICK=2
oplot,CfitZ,CfitR,THICK=3
plotsym,0,FILL=1
oploterror,zMe[0:4],k0kref[0:4],k0kreferr[0:4],PSYM=6,color=250,SYMSIZE=1,THICK=2
oplot,zMe[0:4],k0kref[0:4],PSYM=6,color=250,SYMSIZE=0.8,THICK=17.7
plotsym,4,FILL=1
oploterror,zMe[5],k0kref[5],k0kreferr[5],PSYM=8,color=100,SYMSIZE=1.5,THICK=3
oplot,zMe[5:5],k0kref[5:5],PSYM=8,color=100,SYMSIZE=2.3,THICK=1

LEGEND,['Fields from C05','Our fields','5-field composite'],PSYM=[4,6,8],COLOR=[30,250,100],SYMSIZE=[1.2,0.7,1.8],THICK=[1.5,17,1],CHARTHICK=5,CHARSIZE=1.5,/right_legend,/bottom

plot,[0,1],[0,1],/nodata,XRANGE=[0,1.5],YRANGE=[0.5,2.5],xstyle=1,ystyle=1,XTITLE="z",YTITLE="k/k!Dref",TITLE="Fit on range S=5e-15 - 1e-14",CHARTHICK=2
oploterror,z,R,Rerr,PSYM=6,color=30,SYMSIZE=2,THICK=2
oplot,CfitZ,CfitR
oploterror,zMe[0:4],k1kr[0:4],k1krerr[0:4],PSYM=4,color=250,SYMSIZE=2,THICK=2
oploterror,zMe[5],k1kr[5],k1krerr[5],PSYM=5,color=180,SYMSIZE=2,THICK=2

plot,[0,1],[0,1],/nodata,XRANGE=[0,1.5],YRANGE=[0.5,2.5],xstyle=1,ystyle=1,XTITLE="z",YTITLE="k/k!Dref",TITLE="Fit on range S=1e-14 - 4e-14",CHARTHICK=2
oploterror,z,R,Rerr,PSYM=6,color=30,SYMSIZE=2,THICK=2
oplot,CfitZ,CfitR
oploterror,zMe[0:4],k2kr[0:4],k2krerr[0:4],PSYM=4,color=250,SYMSIZE=2,THICK=2
oploterror,zMe[5],k2kr[5],k2krerr[5],PSYM=5,color=180,SYMSIZE=2,THICK=2

plot,[0,1],[0,1],/nodata,XRANGE=[0,1.5],YRANGE=[0.5,2.5],xstyle=1,ystyle=1,XTITLE="z",YTITLE="k/k!Dref",TITLE="Fit on range S=5e-15 - 4e-14",CHARTHICK=2
oploterror,z,R,Rerr,PSYM=6,color=30,SYMSIZE=2,THICK=2
oplot,CfitZ,CfitR
oploterror,zMe[0:4],k3kr[0:4],k3krerr[0:4],PSYM=4,color=250,SYMSIZE=2,THICK=2
oploterror,zMe[5],k3kr[5],k3krerr[5],PSYM=5,color=180,SYMSIZE=2,THICK=2

end
